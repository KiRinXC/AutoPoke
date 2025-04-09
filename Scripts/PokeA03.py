from AutoControl.Detect.detect import DetectReminder,DetectIcon
from AutoControl.Move.behavior import BehaviorReminder,BehaviorToolBar
from AutoControl.Poke import Poke
"""喷雾刷闪"""
class PokeA03(Poke):
    def __init__(self, recode, move_set, turn_set):
        super().__init__(recode, move_set, turn_set)
        self.DTReminder = DetectReminder()
        self.BEReminder = BehaviorReminder()
        self.BEToolBar = BehaviorToolBar()
        self.DTIcon = DetectIcon()
        self.threads.append(self.use_spray)

    def use_spray(self):
        while not self.quit_event.is_set():
            if self.DTReminder.detect_remind():
                self.move_event.wait()
                self.BEReminder.alert_confirm_move([0,0.1])
                while True:
                    if self.DTOptions.detect_battled():
                        self.move_event.set()
                        break
            elif self.move_event.is_set() and not self.DTIcon.detect_walking_icon():
                self.BEToolBar.spray_toolbar_move([0,0.1])
            else:
                pass