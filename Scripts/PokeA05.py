from AutoControl.Poke import Poke
from AutoControl.Detect.detect import DetectReminder
from AutoControl.Move.behavior import BehaviorReminder,BehaviorToolBar
"""钓鱼刷闪"""
class PokeA05(Poke):
    def __init__(self,recode):
        super().__init__(recode)
        self.DTReminder = DetectReminder()
        self.BEReminder = BehaviorReminder()
        self.BEToolBar = BehaviorToolBar()

    def detect(self):
        while not self.quit_event.is_set():
            self.BEToolBar.fish_rod_toolbar_move([0,0.5])
            is_hooked = self.DTReminder.detect_hooked_remind()
            self.BEReminder.remind_move([0, 0.5])
            if is_hooked:
                self.BEOptions.escape_move([4,6])
                self.poke_num+=1
                self.detect_shiny()