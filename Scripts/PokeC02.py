import time

from AutoVisor.detect.detect import DetectTarget
from AutoVisor.move.behavior import BehaviorA006
from AutoVisor.PokeSingle import PokeSingle

"""单遇抓公虫"""
class PokeA06(PokeSingle):
    def __init__(self,version,recode_filename,password,time_limit,move_set,turn_set):
        super().__init__(version,recode_filename,password,time_limit,move_set,turn_set)
        self.BE = BehaviorA006(self.version)
        self.catch_move = self.BE.catch_move

        self.DTTarget = DetectTarget(self.version)
        # 初始化要匹配的模板和匹配函数
        self.DTTarget.tem_poke_gender_path = self.handler.get_template_path("poke_gender_male")
        self.DTTarget.tem_poke_type_path = self.handler.get_template_path("poke_type_insect")
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_type)
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_gender)

    def detect(self):
        while not self.quit_event.is_set():
            if self.DTOptions.detect_encounter():
                self.move_event.clear()
                time.sleep(2)
                # 需要二次判定
                if self.DTOptions.detect_battle():
                    self.catch()
                    self.poke_num += 1
                    self.handler.upload_recode(self.recode_filename,self.poke_num,self.shiny_num)
                else:
                    self.move_event.set()

    def catch(self):
        if self.DTTarget.detect_target():
            self.catch_move()
            self.move_event.set()
            self.catch_num+=1
        else:
            self.BE.escape_move([0,0.2])
            self.detect_shiny()


from AutoControl.Detect.detect import DetectTarget
from AutoControl.Move.behavior import BehaviorCatch
from AutoControl.Poke import Poke
"""单遇抓公虫"""
class PokeC01(Poke):
    def __init__(self,recode,move_set,turn_set):
        super().__init__(recode,move_set,turn_set)
        self.catch_num = 0
        self.DTTarget = DetectTarget()
        self.BECatch = BehaviorCatch()
        # 初始化要匹配的模板和匹配函数
        self.DTTarget.tem_poke_gender_path = self.handler.get_template_path("poke_gender_male")
        self.DTTarget.tem_poke_type_path = self.handler.get_template_path("poke_type_insect")
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_type)
        self.DTTarget.detect_target_list.append(self.DTTarget.detect_poke_gender)

    def encounter(self):
        self.move_event.clear()
        self.catch()
        self.poke_num += 1

    def catch(self):
        status_list = self.DTTarget.detect_target()
        if status_list[0] or status_list[1]:
            self.BECatch.catch_low_level_move()
            self.move_event.set()
            self.catch_num+=1
        else:
            self.BEOptions.escape_move([0,0.1])
            self.detect_shiny()


