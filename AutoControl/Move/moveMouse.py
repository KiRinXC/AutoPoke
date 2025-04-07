import random
import time

import numpy as np
import pyautogui
from AutoControl.Utili.filesys.handler import Handler
from AutoControl.Utili.calculate.randNum import gen_2d_uniform, gen_1d_uniform

# 禁用 FailSafe 机制
pyautogui.FAILSAFE = False


class MoveMouse:
    def __init__(self):
        handler = Handler()
        self.RegMouse = handler.download_json('RegMouse')
        self.reg_win = self.RegMouse['reg_win']

        self.reg_escape = self.RegMouse['reg_escape']
        self.reg_battle = self.RegMouse['reg_battle']
        self.reg_bag = self.RegMouse['reg_bag']

        self.reg_confirm = self.RegMouse['reg_confirm']
        self.reg_cancel = self.RegMouse['reg_cancel']

        self.reg_perfume_toolbar = self.RegMouse['reg_perfume_toolbar']
        self.reg_spray_toolbar = self.RegMouse['reg_spray_toolbar']
        self.reg_sweet_scent_toolbar = self.RegMouse['reg_sweet_scent_toolbar']
        self.reg_fish_rod_toolbar = self.RegMouse['reg_fish_rod_toolbar']

        self.reg_remind = self.RegMouse['reg_remind']
        self.reg_alert_confirm = self.RegMouse['reg_alert_confirm']
        self.reg_pp_confirm = self.RegMouse['reg_pp_confirm']
        self.reg_hatch_alert_confirm = self.RegMouse['reg_hatch_alert_confirm']

        self.reg_individual_values = self.RegMouse['reg_individual_values']
        self.reg_poke_info_close = self.RegMouse['reg_poke_info_close']

        self.reg_first_pokebar = self.RegMouse['reg_first_pokebar']
        self.reg_poke_props = self.RegMouse['reg_poke_props']

        self.reg_hatch_start = self.RegMouse['reg_hatch_start']
        self.reg_select_poke_base = self.RegMouse['reg_select_poke_base']
        self.reg_hatch = self.RegMouse['reg_hatch']

    @staticmethod
    def loc_add(p1, p2):
        """
        通过原点和偏移合成真实地址
        :param p1: 偏移量
        :param p2: 起始地址
        :return: 相对于屏幕的地址
        """
        x, y = np.array(p1) + np.array(p2)
        return x, y

    @staticmethod
    def bezier_curve(p0, p1, p2, p3, t):
        """
        计算三阶贝塞尔曲线上的点
        :param p0: 起始点 (x, y)
        :param p1: 控制点1 (x, y)
        :param p2: 控制点2 (x, y)
        :param p3: 结束点 (x, y)
        :param t: 参数 t，范围 [0, 1]
        :return: 曲线上的点 (x, y)
        """
        x = (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0]
        y = (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
        return x, y

    def generate_bezier_points_random(self, p1, p2):
        """
        在两点之间生成贝塞尔曲线，并每隔一定距离采样点
        :param p1: 起始点 (x1, y1)
        :param p2: 结束点 (x2, y2)
        :return: 采样点的列表 [(x, y), (x, y), ...]
        """
        random_randint = random.randint(-1000, 1000)
        # 定义控制点（随机生成，确保曲线自然）
        control1_x = p1[0] + random_randint
        control1_y = p1[1] + random_randint
        control2_x = p2[0] + random_randint
        control2_y = p2[1] + random_randint

        # 固定采样六个点
        t_values = [0, 0.2, 0.4, 0.6, 0.8, 1]
        points = []
        for t in t_values:
            x, y = self.bezier_curve(p1, (control1_x, control1_y), (control2_x, control2_y), p2, t)
            points.append((x, y))
        return points

    def generate_bezier_points(self, p1, p2):
        """
        在两点之间生成贝塞尔曲线，并每隔一定距离采样点
        :param p1: 起始点 (x1, y1)
        :param p2: 结束点 (x2, y2)
        :return: 采样点的列表 [(x, y), (x, y), ...]
        """
        max_offset = max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))
        random_range = int(max_offset / 25 + 1) * 25
        random_randint = random.randint(-random_range, random_range)
        # 定义控制点（随机生成，确保曲线自然）
        control1_x = p1[0] + random_randint
        control1_y = p1[1] + random_randint
        control2_x = p2[0] + random_randint
        control2_y = p2[1] + random_randint

        points = []
        points_num = max(int(max_offset / 100), 2)
        t_values = np.linspace(0, 1, points_num)
        for t in t_values:
            x, y = self.bezier_curve(p1, (control1_x, control1_y), (control2_x, control2_y), p2, t)
            points.append((x, y))
        return points

    def mouse_move(self, x, y):
        # 示例坐标
        p1 = pyautogui.position()  # 起始点
        p2 = (x, y)  # 结束点
        # 生成贝塞尔曲线上的采样点
        sampled_points = self.generate_bezier_points(p1, p2)
        for i in range(len(sampled_points)):
            pyautogui.moveTo(sampled_points[i][0], sampled_points[i][1])

    @staticmethod
    def mouse_click():
        pyautogui.mouseDown()
        time.sleep(gen_1d_uniform([0, 0.001]))
        pyautogui.mouseUp()

    def random_mouse(self, pro):
        """
        随机的鼠标移动
        :param pro: 点击后鼠标随机移动的概率
        """
        # 随机在窗口随机移动
        if random.random() <= pro:
            x, y = gen_2d_uniform(self.reg_win)
            # 示例坐标
            p1 = pyautogui.position()  # 起始点
            p2 = (x, y)  # 结束点
            # 生成贝塞尔曲线上的采样点
            sampled_points = self.generate_bezier_points_random(p1, p2)
            for i in range(len(sampled_points)):
                pyautogui.moveTo(sampled_points[i][0], sampled_points[i][1])

    def item_mouse(self, region, pro=0.6):
        """
        移动到指定的范围并点击
        :param region: 指定的范围
        :param pro: 鼠标随机移动的可能性
        """
        # 范围框相对于游戏窗口的位置
        temp_x, temp_y = gen_2d_uniform(region)
        # 范围框的真实位置
        x, y = self.loc_add([temp_x, temp_y], [self.reg_win[0], self.reg_win[1]])
        self.mouse_move(x, y)
        self.mouse_click()
        # 点击后随机移动
        self.random_mouse(pro)

    def confirm_mouse(self):
        """
        确认框的移动点击
        """
        self.item_mouse(self.reg_confirm)

    def cancel_mouse(self):
        """
        取消框的移动点击
        """
        self.item_mouse(self.reg_cancel)


class MoveMouseOptions(MoveMouse):
    """
    四个选项框的移动
    """

    def __init__(self):
        super().__init__()

    def battle_mouse(self) -> None:
        self.item_mouse(self.reg_battle, pro=0.01)

    def bag_mouse(self) -> None:
        self.item_mouse(self.reg_bag,pro=0.01)

    def escape_mouse(self) -> None:
        self.item_mouse(self.reg_escape)

    def skill_1_mouse(self) -> None:
        self.battle_mouse()

    def skill_2_mouse(self) -> None:
        self.bag_mouse()


class MoveMouseToolBar(MoveMouse):
    def __init__(self):
        super().__init__()

    def perfume_toolbar_mouse(self):
        self.item_mouse(self.reg_perfume_toolbar)

    def spray_toolbar_mouse(self):
        self.item_mouse(self.reg_spray_toolbar)

    def sweet_scent_toolbar_mouse(self):
        self.item_mouse(self.reg_sweet_scent_toolbar)

    def fish_rod_toolbar_mouse(self):
        self.item_mouse(self.reg_fish_rod_toolbar)

    def first_pokebar_mouse(self):
        self.item_mouse(self.reg_first_pokebar, pro=0.01)

    def poke_props_mouse(self):
        self.item_mouse(self.reg_poke_props)


class MoveMouseReminder(MoveMouse):
    def __init__(self):
        super().__init__()

    def remind_mouse(self):
        self.item_mouse(self.reg_remind)

    def alert_confirm_mouse(self):
        """仅适用于香水、喷雾"""
        self.item_mouse(self.reg_alert_confirm)

    def pp_confirm_mouse(self):
        self.item_mouse(self.reg_pp_confirm)

    def individual_values_mouse(self):
        self.item_mouse(self.reg_individual_values,pro=0.01)

    def poke_info_close_mouse(self):
        self.item_mouse(self.reg_poke_info_close)

    def hatch_alert_confirm_mouse(self):
        self.item_mouse(self.reg_hatch_alert_confirm)

class MoveMouseHatch(MoveMouse):
    def __init__(self):
        super().__init__()
        self.colum_spacing = 63
        self.row_spacing = 53

    def hatch_start_mouse(self):
        self.item_mouse(self.reg_hatch_start)

    def select_poke_male_mouse(self, coordinate):
        reg_select_poke_male = [0,0,0,0]
        reg_select_poke_male[0] = self.reg_select_poke_base[0] + coordinate[1] * self.colum_spacing
        reg_select_poke_male[1] = self.reg_select_poke_base[1] + coordinate[0] * self.row_spacing
        reg_select_poke_male[2] = self.reg_select_poke_base[2]
        reg_select_poke_male[3] = self.reg_select_poke_base[3]
        pyautogui.keyDown('ctrl')
        self.item_mouse(reg_select_poke_male,pro=0.01)
        pyautogui.keyUp('ctrl')



    def select_poke_female_mouse(self, coordinate):
        reg_select_poke_female = [0,0,0,0]
        reg_select_poke_female[0] = self.reg_select_poke_base[0] + coordinate[1] * self.colum_spacing
        reg_select_poke_female[1] = self.reg_select_poke_base[1] + coordinate[0] * self.row_spacing + 3*self.row_spacing
        reg_select_poke_female[2] = self.reg_select_poke_base[2]
        reg_select_poke_female[3] = self.reg_select_poke_base[3]

        pyautogui.keyDown('ctrl')
        self.item_mouse(reg_select_poke_female,pro=0.01)
        pyautogui.keyUp('ctrl')


    def hatch_mouse(self):
        self.item_mouse(self.reg_hatch,pro=0.01)



