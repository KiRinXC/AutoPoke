import random
import time

import pyautogui
from AutoControl.Utili.calculate.randNum import gen_1d_uniform
from AutoControl.Utili.filesys.handler import Handler

# 禁用 FailSafe 机制
pyautogui.FAILSAFE = False


class MoveKey:
    def __init__(self):
        handler = Handler()
        self.RegKey = handler.download_json("RegKey")
        self.right_key = self.RegKey["right_key"]
        self.left_key = self.RegKey["left_key"]
        self.top_key = self.RegKey["top_key"]
        self.bottom_key = self.RegKey["bottom_key"]

        self.A_key = self.RegKey["A_key"]
        self.B_key = self.RegKey["B_key"]

        self.perfume_toolbar = self.RegKey['perfume_toolbar_key']
        self.spray_toolbar = self.RegKey['spray_toolbar_key']
        self.sweet_scent_toolbar = self.RegKey['sweet_scent_toolbar_key']
        self.fish_rod_toolbar = self.RegKey['fish_rod_toolbar_key']


    @staticmethod
    def key_press(key):
        """
        模拟正常人按键的行为
        :param key: 按键
        """
        # 这是模拟人类的反应时间
        time.sleep(gen_1d_uniform([0, 0.01]))
        pyautogui.keyDown(key)
        time.sleep(gen_1d_uniform([0,0.01]))
        pyautogui.keyUp(key)

    def item_shuffle_key(self, order):
        """随机打乱按键"""
        random.shuffle(order)
        for i in range(len(order)):
            self.key_press(order[i])

    def item_orderly_key(self, order):
        """有序执行按键"""
        for i in range(len(order)):
            self.key_press(order[i])

    def confirm_key(self):
        self.key_press(self.A_key)

    def cancel_key(self):
        self.key_press(self.B_key)

class MoveKeyOptions(MoveKey):
    def __init__(self):
        super().__init__()

        self.original_key = [self.left_key, self.top_key] # 初始化位置
        self.escape_keys = [self.right_key,self.bottom_key]
        self.bag_keys = self.right_key

    def battle_key(self):
        self.key_press(self.A_key)

    def bag_key(self):
        self.key_press(self.bag_keys)
        self.key_press(self.A_key)

    def escape_key(self):
        self.item_shuffle_key(self.escape_keys)
        self.key_press(self.A_key)

    def skill_1_key(self):
        self.item_shuffle_key(self.original_key)
        self.key_press(self.A_key)

    def skill_2_key(self):
        self.item_shuffle_key(self.original_key)
        self.bag_key()


class MoveKeyToolBar(MoveKey):
    def __init__(self):
        super().__init__()

    def perfume_toolbar_key(self):
        self.key_press(self.perfume_toolbar)

    def spray_toolbar_key(self):
        self.key_press(self.spray_toolbar)

    def sweet_scent_toolbar_key(self):
        self.key_press(self.sweet_scent_toolbar)

    def fish_rod_toolbar_key(self):
        self.key_press(self.fish_rod_toolbar)



class MoveKeyReminder(MoveKey):
    def __init__(self):
        super().__init__()

    def remind_key(self):
        self.confirm_key()

    def alert_confirm_key(self):
        self.item_orderly_key([self.top_key,self.A_key])

    def alert_cancel_key(self):
        self.cancel_key()

    def pp_confirm_key(self):
        self.confirm_key()

    def individual_values_key(self):
        self.item_orderly_key([self.right_key,self.right_key,self.right_key])

    def poke_info_close_key(self):
        self.cancel_key()

class MoveKeyHatch(MoveKey):
    def __init__(self):
        super().__init__()
    def hatch_start_key(self):
        self.confirm_key()






