import time

from AutoControl.Utili.calculate.randNum import gen_1d_uniform, gen_1d_accident
from AutoControl.Utili.filesys.handler import Handler
from AutoControl.Detect.detect import DetectOptions
import pyautogui
import logging

# 禁用 FailSafe 机制
pyautogui.FAILSAFE = False


class MovePlayer:
    def __init__(self, move_event, move_set, turn_set):
        handler = Handler()
        self.Settings = handler.download_json("Settings")
        self.move_rate = self.Settings["move_rate"]
        self.move_range = self.Settings['move_range']
        self.turn_range = self.Settings['turn_range']
        self.logger = logging.getLogger(__name__)

        self.move_count = 0
        self.turn_count = 0

        self.move_event = move_event
        self.move_direction = move_set['direction']
        self.is_move_specified = move_set['is_specified']
        self.turn_direction = turn_set['direction']
        self.is_turn_specified = turn_set['is_specified']

        self.move_method = None
        self.turn_method = None
        self.init_move_and_turn()

    def init_move_and_turn(self):
        if self.is_turn_specified:
            self.turn_method = self.orderly_turn_specified
        else:
            self.turn_method = self.orderly_turn_default

        if self.is_move_specified:
            self.move_method = self.orderly_move_specified
        else:
            self.move_method = self.orderly_move_default

    def create_block(self):
        """
        创建人物移动阻塞
        """
        while True:
            if self.move_event.is_set():
                block_time = gen_1d_accident([0, 0], item="角色移动")
                if block_time > 0:
                    self.move_event.clear()
                    time.sleep(block_time)
                    DTOptions = DetectOptions()
                    while True:
                        if DTOptions.detect_battled():
                            self.move_event.set()
                            break
                time.sleep(1)

    def one_way_move(self, steps, direction: str) -> None:
        """
        单方向移动
        :param steps: 移动的步数，不准确，骑自行快，穿鞋走中，无鞋走慢
        :param direction: 移动的方向
        """
        pyautogui.keyDown(direction)
        # 控制按下的时间
        time.sleep(steps * self.move_rate)
        pyautogui.keyUp(direction)

    def orderly_move_default(self) -> None:
        """
        有序移动，不指定方向，每次移动距离随机
        """
        while self.move_event.is_set():
            move_len = gen_1d_uniform(self.move_range)
            self.logger.debug("移动->" + self.move_direction[self.move_count] + "移动" + str(move_len))
            self.one_way_move(move_len, self.move_direction[self.move_count])
            self.move_count = (self.move_count + 1) % 2

    def orderly_move_specified(self) -> None:
        """
        有序移动，指定起始方向,次选方向每次都比首选方向少移动
        """
        if self.move_event.is_set():
            move_len = gen_1d_uniform(self.move_range)
            move_count = 0
            while self.move_event.is_set():
                self.one_way_move(move_len, self.move_direction[move_count])
                self.logger.debug("移动->" + self.move_direction[move_count] + "移动" + str(move_len))
                move_count = (move_count + 1) % 2
                if move_count == 1:
                    move_len = gen_1d_uniform([move_len - 0.5, move_len])
                else:
                    move_len = gen_1d_uniform(self.move_range) + 1

    def orderly_turn_default(self) -> None:
        """
        有序拐弯，不指定方向，每次移动距离随机
        """
        if self.move_event.is_set():
            time.sleep(gen_1d_uniform([0.5, 1]))
            while self.move_event.is_set():
                turn_len = gen_1d_uniform(self.turn_range)
                self.logger.debug("拐弯->" + self.turn_direction[self.turn_count] + "移动" + str(turn_len))
                self.one_way_move(turn_len, self.turn_direction[self.turn_count])
                self.turn_count = (self.turn_count + 1) % 2
                time.sleep(gen_1d_uniform([0.5, 1]))

    def orderly_turn_specified(self) -> None:
        """
        有序拐弯，指定起始方向,次选方向每次都比首选方向少移动
        """
        if self.move_event.is_set():
            turn_len = gen_1d_uniform(self.turn_range)
            turn_count = 0
            time.sleep(gen_1d_uniform([0.5, 1]))
            while self.move_event.is_set():
                self.one_way_move(turn_len, self.turn_direction[turn_count])
                self.logger.debug("拐弯->" + self.turn_direction[turn_count] + "移动" + str(turn_len))
                turn_count = (turn_count + 1) % 2
                if turn_count == 1:
                    turn_len = gen_1d_uniform([turn_len - 0.05, turn_len])
                else:
                    turn_len = gen_1d_uniform(self.turn_range) + 0.1
                time.sleep(gen_1d_uniform([0.5, 1]))