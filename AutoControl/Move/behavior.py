import random
import logging
import time

from AutoControl.Move.moveKey import MoveKeyOptions,MoveKeyToolBar,MoveKeyReminder
from AutoControl.Move.moveMouse import MoveMouseOptions,MoveMouseToolBar,MoveMouseReminder
from AutoControl.Detect.detect import DetectOptions, DetectReminder, DetectTarget, DetectIcon
from AutoControl.Utili.calculate.randNum import gen_1d_accident
from AutoControl.Utili.filesys.handler import Handler


class Behavior:
    def __init__(self):
        handler = Handler()
        self.Settings = handler.download_json("Settings")
        # 使用键盘的概率
        self.pro = self.Settings["behavior_pro"]
        self.logger = logging.getLogger(__name__)

    def confirm_method_list(self, key_list, mouse_list, item):
        if random.random() < self.pro:
            self.logger.debug(f"键盘-->{item}")
            return key_list
        else:
            self.logger.debug(f"鼠标-->{item}")
            return mouse_list

    def confirm_method(self, key, mouse, item):
        if random.random() < self.pro:
            self.logger.debug(f"键盘-->{item}")
            return key
        else:
            self.logger.debug(f"鼠标-->{item}")
            return mouse


    @staticmethod
    def item_move_with_before_check(detect, action, item, wait_scope):
        """ 主要用在提醒框的确认
        有检查条件的随机键盘或鼠标响应，响应之后会再次判定
        :param detect: 触发开始执行移动的条件函数
        :param action: 响应函数
        :param item:移动项目的名称
        :param wait_scope:阻塞时间
        """
        time.sleep(gen_1d_accident(wait_scope, item=item))
        action()
        while detect():
            # 在执行action()之后再次检测
            action()


    @staticmethod
    def item_move_with_after_check(detect, action, item, wait_scope):
        """
        有检查条件的随机键盘或鼠标响应，响应之后不会再次判定
        :param detect: 触发开始执行移动的条件函数
        :param action: 响应函数
        :param item:移动项目的名称
        :param wait_scope:阻塞时间范围
        """
        while True:
            if detect():
                time.sleep(gen_1d_accident(wait_scope, item=item))
                action()
                break


    @staticmethod
    def item_move_multiple_check_with_event(detect_start, detect_exit, action, item, event, wait_scope):
        """
        有检查条件的随机键盘或鼠标响应，响应之后不会再次判定，新增了事件参数
        :param detect_start: 触发开始事件移动的条件函数
        :param detect_exit: 触发结束事件移动的条件函数
        :param action: 响应函数
        :param item:移动项目的名称
        :param event :事件的线程
        :param wait_scope:阻塞时间
        """
        while True:
            if detect_start():
                time.sleep(gen_1d_accident(wait_scope, item=item))
                action()
                if not detect_start():
                    event.clear()
                    break
            elif detect_exit():
                event.clear()
                break
            else:
                pass

    @staticmethod
    def item_move_without_check(action, item,wait_scope):
        """
        无检查条件的随机键盘或鼠标响应
        :param action: 键盘响应函数
        :param item:移动项目的名称
        :param wait_scope:阻塞时间
        """
        time.sleep(gen_1d_accident(wait_scope, item=item))
        action()



class BehaviorOptions(Behavior):
    def __init__(self):
        super().__init__()
        self.MKOptions = MoveKeyOptions()
        self.MMOptions = MoveMouseOptions()
        self.DTOptions = DetectOptions()

    def battle_skill_1_move(self,wait_1,wait_2) ->None:
        key_list = [self.MKOptions.battle_key,self.MKOptions.skill_1_key]
        mouse_list = [self.MMOptions.battle_mouse,self.MMOptions.skill_1_mouse]
        battle_action,skill_1_action = self.confirm_method_list(key_list,mouse_list,item = "一技能")
        self.item_move_with_after_check(self.DTOptions.detect_escape, battle_action, "对战", wait_1)
        self.item_move_with_after_check(self.DTOptions.detect_cancel, skill_1_action, "一技能", wait_2)

    def battle_skill_2_move(self,check,wait_1,wait_2) ->None:
        key_list = [self.MKOptions.battle_key,self.MKOptions.skill_2_key]
        mouse_list = [self.MMOptions.battle_mouse,self.MMOptions.skill_2_mouse]
        battle_action,skill_2_action = self.confirm_method_list(key_list,mouse_list,item = "二技能")
        if check:
            self.item_move_with_after_check(self.DTOptions.detect_escape, battle_action, "对战", wait_1)
        else:
            self.item_move_without_check(battle_action,"对战",wait_1)
        self.item_move_with_after_check(self.DTOptions.detect_cancel, skill_2_action, "二技能", wait_2)


    def bag_pokeball_move(self,check,wait_1,wait_2) ->None:
        key_list = [self.MKOptions.bag_key,self.MKOptions.confirm_key]
        mouse_list = [self.MMOptions.bag_mouse,self.MMOptions.confirm_mouse]
        bag_action, confirm_action = self.confirm_method_list(key_list, mouse_list, item="丢精灵球")
        if check:
            self.item_move_with_after_check(self.DTOptions.detect_escape, bag_action, "背包", wait_1)
        else:
            self.item_move_without_check(bag_action, "背包", wait_1)
        self.item_move_with_after_check(self.DTOptions.detect_cancel, confirm_action, "确认键", wait_2)

    def escape_move(self,check,wait_scope) ->None:
        escape_action = self.confirm_method(self.MKOptions.escape_key, self.MMOptions.escape_mouse,item="逃跑")
        if check:
            self.item_move_with_after_check(self.DTOptions.detect_escape, escape_action, "逃跑", wait_scope)
        else:
            self.item_move_without_check(escape_action, "逃跑", wait_scope)


class BehaviorToolBar(Behavior):
    def __init__(self):
        super().__init__()
        self.MKToolBar = MoveKeyToolBar()
        self.MMToolBar = MoveMouseToolBar()
        self.DTOptions = DetectOptions()

    def perfume_toolbar_move(self, wait_scope):
        perfume_toolbar_action= self.confirm_method(self.MKToolBar.perfume_toolbar_key,self.MMToolBar.perfume_toolbar_mouse,item="工具栏香水")
        self.item_move_without_check(perfume_toolbar_action,"工具栏香水",wait_scope)

    def spray_toolbar_move(self,wait_scope):
        spray_toolbar_action = self.confirm_method(self.MKToolBar.spray_toolbar_key,self.MMToolBar.spray_toolbar_mouse,"工具栏喷雾")
        self.item_move_without_check(spray_toolbar_action,"工具栏喷雾",wait_scope)

    def sweet_scent_toolbar_move(self,wait_scope):
        """脱战之后使用"""
        sweet_scent_toolbar_action = self.confirm_method(self.MKToolBar.sweet_scent_toolbar_key, self.MMToolBar.sweet_scent_toolbar_mouse, "工具栏甜甜香气")
        self.item_move_with_after_check(self.DTOptions.detect_battled, sweet_scent_toolbar_action, "工具栏甜甜香气", wait_scope)

    def fish_rod_toolbar_move(self,wait_scope):
        """脱战之后使用"""
        fish_rod_toolbar_action =self.confirm_method(self.MKToolBar.fish_rod_toolbar_key, self.MMToolBar.fish_rod_toolbar_mouse,"工具栏鱼竿")
        self.item_move_with_after_check(self.DTOptions.detect_battled, fish_rod_toolbar_action, "工具栏鱼竿", wait_scope)

    def first_pokebar_move(self,check,wait_scope) ->None:
        self.logger.debug("鼠标-->首发精灵")
        first_pokebar_action = self.MMToolBar.first_pokebar_mouse
        if check:
            self.item_move_with_after_check(self.DTOptions.detect_battled,first_pokebar_action, "首发精灵", wait_scope)
        else:
            self.item_move_without_check(first_pokebar_action, "首发精灵", wait_scope)

    def poke_props_move(self,wait_scope):
        self.logger.debug("鼠标-->取下道具")
        poke_props_action = self.MMToolBar.poke_props_mouse
        self.item_move_without_check(poke_props_action,"取下道具",wait_scope)


class BehaviorReminder(Behavior):
    def __init__(self):
        super().__init__()
        self.MKReminder = MoveKeyReminder()
        self.MMReminder = MoveMouseReminder()
        self.DTReminder = DetectReminder()
        self.DTIcon = DetectIcon()

    def remind_move(self, wait_scope):
        remind_action = self.confirm_method(self.MKReminder.remind_key,self.MMReminder.remind_mouse,"提醒框")
        self.item_move_with_before_check(self.DTReminder.detect_remind, remind_action, "提醒框", wait_scope)

    def alert_confirm_move(self,wait_scope):
        alert_confirm_action = self.confirm_method(self.MKReminder.alert_confirm_key,self.MMReminder.alert_confirm_mouse, "警告框")
        self.item_move_with_before_check(self.DTReminder.detect_remind, alert_confirm_action, "警告框", wait_scope)


    def alert_cancel_move(self,wait_scope):
        self.logger.debug("键盘-->取消警告框")
        alert_cancel_action = self.MKReminder.cancel_key
        self.item_move_without_check(alert_cancel_action,"取消警告框",wait_scope)

    def pp_confirm_move(self,wait_scope):
        pp_confirm_action = self.confirm_method(self.MKReminder.pp_confirm_key,self.MMReminder.pp_confirm_mouse,"使用pp果")
        self.item_move_with_before_check(self.DTReminder.detect_remind, pp_confirm_action, "使用pp果", wait_scope)

    def individual_values_move(self,wait_scope):
        if random.random() < 0.5:
            key_list = [self.MKReminder.individual_values_key, self.MKReminder.poke_info_close_key]
            mouse_list = [self.MMReminder.individual_values_mouse,self.MMReminder.poke_info_close_mouse]
            individual_values_action, poke_info_close_action = self.confirm_method_list(key_list, mouse_list, item="检查个体值")
            self.item_move_with_after_check(self.DTIcon.detect_pokedex_icon, individual_values_action, "检查个体值", wait_scope)
            self.item_move_without_check(poke_info_close_action,"关闭宝可梦信息框",wait_scope)
        else:
            poke_info_close_action = self.confirm_method(self.MKReminder.poke_info_close_key,self.MMReminder.poke_info_close_mouse,"关闭宝可梦信息框")
            self.item_move_with_after_check(self.DTIcon.detect_pokedex_icon, poke_info_close_action, "关闭宝可梦信息框", wait_scope)


class BehaviorCatch(Behavior):
    def __init__(self):
        super().__init__()
        self.handler = Handler()
        self.DTTarget = DetectTarget()
        self.DTTarget.tem_poke_status_path = self.handler.get_template_path('poke_status_sleep')
        self.BEOptions = BehaviorOptions()
        self.BEReminder = BehaviorReminder()

    def catch_low_level_move(self):
        """只使用一技能"""
        self.BEOptions.battle_skill_1_move([0,0.1],[0,0.1])
        self.BEOptions.bag_pokeball_move(True,[0, 0.1], [0, 0.1])
        while True:
            if self.BEOptions.DTOptions.detect_battled():
                # 判断是否脱离对战
                break
            elif self.BEOptions.DTOptions.detect_escape():
                # 未脱离对战 则看有没有弹出选项框
                self.BEOptions.bag_pokeball_move(False,[0, 0.1], [0, 0.1])
            else:
                # 未脱离对战，也没有弹出选项框 则正在捕捉
                pass
        # 捕捉成功后会弹出信息框
        self.BEReminder.individual_values_move([0,0.1])

    def catch_middle_level_move(self):
        """不主动睡精灵"""
        self.BEOptions.battle_skill_1_move([0,0.1],[0,0.1])
        self.BEOptions.bag_pokeball_move(True,[0, 0.1], [0, 0.1])
        while True:
            if self.BEOptions.DTOptions.detect_battled():
                # 判断是否脱离对战
                break
            elif self.BEOptions.DTOptions.detect_escape():
                # 未脱离对战 则看有没有弹出选项框
                if not self.DTTarget.detect_poke_status():
                    self.BEOptions.battle_skill_2_move(False,[0,0.1],[0,0.1])
                    self.BEOptions.bag_pokeball_move(True, [0, 0.1], [0, 0.1])
                else:
                    self.BEOptions.bag_pokeball_move(False,[0, 0.1], [0, 0.1])
            else:
                # 未脱离对战，也没有弹出选项框 则正在捕捉
                pass
        # 捕捉成功后会弹出信息框
        self.BEReminder.individual_values_move([0,0.1])


    def catch_high_level_move(self):
        """主动睡精灵"""
        self.BEOptions.battle_skill_1_move([0, 0.1], [0, 0.1])
        self.BEOptions.battle_skill_2_move(True,[0, 0.1], [0, 0.1])
        self.BEOptions.bag_pokeball_move(True, [0, 0.1], [0, 0.1])
        while True:
            if self.BEOptions.DTOptions.detect_battled():
                # 判断是否脱离对战
                break
            elif self.BEOptions.DTOptions.detect_escape():
                # 未脱离对战 则看有没有弹出选项框
                if not self.DTTarget.detect_poke_status():
                    self.BEOptions.battle_skill_2_move(False, [0, 0.1], [0, 0.1])
                    self.BEOptions.bag_pokeball_move(True, [0, 0.1], [0, 0.1])
                else:
                    self.BEOptions.bag_pokeball_move(False, [0, 0.1], [0, 0.1])
            else:
                # 未脱离对战，也没有弹出选项框 则正在捕捉
                pass
        # 捕捉成功后会弹出信息框
        self.BEReminder.individual_values_move([0, 0.1])
