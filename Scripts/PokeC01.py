import threading
import time

from AutoControl.Detect.detect import DetectTarget
from AutoControl.Move.behavior import BehaviorCatch
from AutoControl.Poke import Poke
"""单遇抓蘑蘑菇"""
class PokeC01(Poke):
    def __init__(self,recode,move_set,turn_set):
        super().__init__(recode,move_set,turn_set)
        self.catch_num = 0
        self.catch_event = threading.Event()
        self.DTTarget = DetectTarget()
        self.BECatch = BehaviorCatch()
        # 初始化要匹配的模板和匹配函数
        self.DTTarget.tem_poke_name_path = self.handler.get_template_path("poke_name_shroomish")
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_shiny)
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_name)

        self.threads.append(self.catch)

    def encounter(self):
        self.move_event.wait()
        status_list = self.DTTarget.detect_target()
        if status_list[0] or not status_list[1]:
            self.catch_event.set()
        else:
            self.BEOptions.escape_move(True, [0, 0.1])
            self.detect_shiny()
        self.detect_event.wait()
        self.poke_num += 1

    def catch(self):
        while True:
            if self.catch_event.is_set():
                self.BECatch.catch_low_level_move()
                self.catch_event.clear()
                self.move_event.set()
                self.detect_event.set()
                self.catch_num += 1
            time.sleep(1)




