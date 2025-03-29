from AutoControl.Move.behavior import BehaviorToolBar,BehaviorReminder
from AutoControl.Detect.detect import DetectTarget,DetectReminder,DetectIcon
from AutoControl.Poke import Poke
"""彩幽刮鳞片脚本"""
class PokeSingleB09(Poke):
    def __init__(self,recode):
        super().__init__(recode)
        self.DTReminder = DetectReminder()
        self.DTTarget = DetectTarget()
        self.DTIcon = DetectIcon()
        self.BEToolBar = BehaviorToolBar()
        self.BEReminder = BehaviorReminder()
        self.catch_num = 0


    def detect(self):
        while not self.quit_event.is_set():
            self.BEToolBar.fish_rod_toolbar_move([0,0.5])
            is_hooked = self.DTReminder.detect_hooked_remind()
            self.BEReminder.remind_move([0, 0.5])
            if is_hooked:
                self.steal()

    def steal(self):
        while True:
            if self.DTReminder.detect_passive_skill_remind():
                if not self.DTTarget.detect_poke_shiny():
                    self.BEOptions.battle_skill_1_move()
                    self.BEToolBar.fish_rod_toolbar_move([0,0.2])
                    self.BEToolBar.poke_props_move([0,0.2])
                    self.catch_num+=1
                    break
                else:
                    self.detect_shiny()
            elif self.DTOptions.detect_escape():
                self.BEOptions.escape_move([0,0.2],False)
                self.detect_shiny()
                break
            else:
                pass
        self.poke_num += 1
