import time
from itertools import count

from AutoControl.Poke import Poke
from AutoControl.Detect.detect import DetectReminder, DetectIcon
from AutoControl.Move.behavior import BehaviorReminder, BehaviorHatch

"""孵蛋"""
class PokeA06(Poke):
    def __init__(self,recode):
        super().__init__(recode)
        self.DTReminder = DetectReminder()
        self.DTIcon = DetectIcon()
        self.BEReminder = BehaviorReminder()
        self.BEHatch = BehaviorHatch()
        self.coordinate = [0,1]
        self.poke_counter = 0

    def detect(self):
        while self.poke_counter < 30:
            self.BEOptions.MKOptions.confirm_key()
            while True:
                if self.DTReminder.detect_remind():
                    self.BEReminder.remind_move_only_key([0,0.2])
                elif self.DTIcon.detect_hatchbox_close_icon():
                    self.hatch()
                    break
                else:
                    self.BEOptions.MKOptions.confirm_key()

    def hatch(self):
        self.BEHatch.hatch_start_move([0,0.4])
        self.BEHatch.select_poke_move(self.coordinate,[0,0.1])
        print(f"/n{self.coordinate}/n")
        self.update_coordinate()
        print(f"/n{self.coordinate}/n")
        self.BEHatch.hatch_move([0,0.1])
        self.BEReminder.hatch_alert_confirm_move([0,0.1])

    def update_coordinate(self):
        self.poke_counter += 1
        if self.poke_counter <30:
            if self.coordinate[1] != 9:
                self.coordinate[1] = self.coordinate[1] + 1
            else:
                self.coordinate[0] = self.coordinate[0] + 1
                self.coordinate[1] = 0
        else:
            pass

