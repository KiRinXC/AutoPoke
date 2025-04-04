import time

from AutoControl.Poke import Poke
from AutoControl.Detect.detect import DetectReminder
from AutoControl.Move.behavior import BehaviorReminder,BehaviorToolBar
"""群怪刷闪"""
class PokeA04(Poke):
    def __init__(self,recode):
        super().__init__(recode)
        self.threads.append(self.use_pp)
        self.DTReminder = DetectReminder()
        self.BEReminder = BehaviorReminder()
        self.BEToolBar = BehaviorToolBar()

    def detect(self):
        while not self.quit_event.is_set():
            self.BEToolBar.sweet_scent_toolbar_move([0,0.2])
            self.BEOptions.escape_move([0,0.5])
            self.poke_num+=5
            self.detect_shiny()

    def use_pp(self):
        while not self.quit_event.is_set():
            if self.DTReminder.detect_remind():
                self.BEReminder.pp_confirm_move([0,0.3])
                # 等到下一次点击相差大于 80s
                time.sleep(80)


