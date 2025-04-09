import threading
import time
import logging
from concurrent.futures import ThreadPoolExecutor

from AutoControl.Detect.createTemplate import  create_template
from AutoControl.Detect.detect import DetectOptions

from AutoControl.Move.behavior import BehaviorOptions
from AutoControl.Move.movePlayer import MovePlayer

from AutoControl.Utili.filesys.handler import Handler
from AutoControl.Utili.control.adjustWindow import adjust_window
from AutoControl.Utili.web.reminder import remind_shiny

class Poke:
    def __init__(self,recode,move_set=None,turn_set=None):
        self.logger = logging.getLogger(__name__)
        self.move_set = move_set
        self.turn_set = turn_set

        self.detect_event = threading.Event()
        self.detect_event.set()

        self.move_event = threading.Event()

        self.quit_event = threading.Event()

        self.DTOptions = DetectOptions()
        self.BEOptions = BehaviorOptions()
        
        self.handler = Handler()
        self.recode = self.handler.download_recode(recode)
        self.Settings =self.handler.download_json("Settings")
        self.slot_value = self.Settings["slot_value"]
        self.RegDetect = self.handler.download_json("RegDetect")

        # 定义线程目标函数
        self.threads = [
            self.detect,
            self.quit,
        ]

        # 激活窗口
        adjust_window()
        # 初始化位置模板
        create_template('location.png',self.RegDetect['reg_location'], ocr=True)

        # 初始化计数器
        self.poke_num,self.shiny_num = self.recode['poke_num'],self.recode['shiny_num']

        if self.move_set:
            self.move_event.set()
            self.MP = MovePlayer(self.move_event, self.move_set, self.turn_set)
            self.move_method = self.MP.move_method
            self.threads.append(self.turn)
            if self.turn_set:
                self.turn_method = self.MP.turn_method
                self.threads.append(self.move)
            self.threads.append(self.MP.create_block)

    def detect(self):
        while not self.quit_event.is_set():
            if self.detect_event.is_set() and self.DTOptions.detect_encounter():
                self.move_event.wait()
                time.sleep(1)
                # 需要二次判定
                if self.DTOptions.detect_battle():
                    self.encounter()
                else:
                    self.move_event.set()



    def encounter(self):
        self.move_event.wait()
        self.BEOptions.escape_move(True,[0, 0.2])
        self.poke_num += 1
        self.detect_shiny()

    def detect_shiny(self):
        counter = 0
        while True:
            if self.DTOptions.detect_battled():
                self.move_event.set()
                break
            else:
                counter+=1
                if counter >= self.slot_value:
                    self.logger.error("出闪瞬间")
                    self.shiny_num+=1
                    remind_shiny()
                    self.quit_event.set()
                    self.move_event.clear()
                    time.sleep(10000)
                    break

    def move(self):
        while not self.quit_event.is_set():
            self.move_method()

    def turn(self):
        while not self.quit_event.is_set():
            self.turn_method()

    def quit(self):
        if self.move_event.is_set():
            while not self.quit_event.is_set():
                time.sleep(1)
                if not self.DTOptions.detect_location():
                    self.quit_event.set()
                    self.move_event.clear()
                    break

    def run(self):
        # 使用线程池执行任务
        with ThreadPoolExecutor(max_workers=len(self.threads)) as executor:
            for target in self.threads:
                executor.submit(target)

