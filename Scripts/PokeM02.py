from AutoControl.Move.behavior import BehaviorToolBar,BehaviorReminder
from AutoControl.Detect.detect import DetectTarget,DetectReminder,DetectIcon
from AutoControl.Poke import Poke
"""喵喵刮鳞聚宝"""
class PokeM02(Poke):
    def __init__(self,recode):
        super().__init__(recode)
        self.DTReminder = DetectReminder()
        self.DTTarget = DetectTarget()
        self.DTIcon = DetectIcon()
        self.BEToolBar = BehaviorToolBar()
        self.BEReminder = BehaviorReminder()
        self.DTTarget.tem_poke_name_path = self.handler.get_template_path("poke_name_luvdisc")
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_shiny)
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_name)
        self.catch_num = 0
        self.skill_1_count =0
        self.skill_2_count =0

    def detect(self):
        while not self.quit_event.is_set():
            self.BEToolBar.fish_rod_toolbar_move([0,0.5])
            is_hooked = self.DTReminder.detect_hooked_remind()
            self.BEReminder.remind_move([0, 0.5])
            if is_hooked:
                self.steal()


    def steal(self):
        while True:
            if self.DTOptions.detect_battle():
                break
        status_list = self.DTTarget.detect_target()
        if status_list[0]:
            self.detect_shiny()
        elif status_list[1]:
            self.BEOptions.battle_skill_2_move(True,[0, 0.2], [0, 0.2])
            while True:
                if self.DTOptions.detect_battled():
                    if self.DTIcon.detect_props_icon():
                        self.BEToolBar.first_pokebar_move([0, 0.2])
                        self.BEToolBar.poke_props_move([0, 0.2])
                        self.catch_num += 1
                    break
                elif self.DTOptions.detect_escape():
                    self.BEOptions.battle_skill_1_move([0, 0.2], [0, 0.2])
        else:
            self.BEOptions.battle_skill_1_move([0, 0.2], [0, 0.2])
            while True:
                if self.DTOptions.detect_battled():
                    break
                elif self.DTOptions.detect_escape():
                    self.BEOptions.battle_skill_1_move([0, 0.2], [0, 0.2])
        self.poke_num += 1


