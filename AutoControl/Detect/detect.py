import logging

from AutoControl.Detect.colorcCheck import is_all_black,is_all_white,is_any_black,is_any_white
from AutoControl.Detect.imageMatch import image_match
from AutoControl.Utili.filesys.handler import Handler
from AutoControl.Utili.web.reminder import remind_shiny

class Detect:
    def __init__(self):
        handler = Handler()
        self.logger = logging.getLogger(__name__)

        self.RegDetect = handler.download_json('RegDetect')
        self.reg_win = self.RegDetect["reg_win"]

        self.reg_encounter = self.RegDetect["reg_encounter"]
        self.reg_battle = self.RegDetect["reg_battle"]
        self.reg_escape = self.RegDetect['reg_escape']
        self.reg_location = self.RegDetect['reg_location']

        self.reg_health_bar = self.RegDetect["reg_health_bar"]
        self.reg_poke_info = self.RegDetect["reg_poke_info"]
        self.reg_cancel = self.RegDetect["reg_cancel"]

        self.reg_remind = self.RegDetect["reg_remind"]
        self.reg_remind_text = self.RegDetect["reg_remind_text"]
        self.reg_remind_passive_skill = self.RegDetect["reg_remind_passive_skill"]
        self.reg_alert_confirm_hatch = self.RegDetect["reg_alert_confirm_hatch"]


        self.reg_icon_walking = self.RegDetect["reg_icon_walking"]
        self.reg_icon_props = self.RegDetect["reg_icon_props"]
        self.reg_icon_pokedex = self.RegDetect["reg_icon_pokedex"]
        self.reg_icon_close_hatchbox = self.RegDetect["reg_icon_close_hatchbox"]
        self.reg_icon_close_computerbox = self.RegDetect["reg_icon_close_computerbox"]

        self.tem_location_path = handler.get_template_path('location')
        self.tem_escape_path = handler.get_template_path('escape')

        self.tem_poke_gender_path = handler.get_template_path('poke_gender')
        self.tem_poke_type_path = handler.get_template_path('poke_type')
        self.tem_poke_name_path = handler.get_template_path('poke_name')
        self.tem_poke_status_path = handler.get_template_path('poke_status')
        self.tem_poke_shiny_path = handler.get_template_path('poke_shiny')

        self.tem_alert_confirm_path = handler.get_template_path('alert_confirm')
        self.tem_remind_hooked_path = handler.get_template_path('remind_hooked')
        self.tem_remind_passive_skill_path = handler.get_template_path('remind_passive_skill')

        self.tem_icon_walking_path = handler.get_template_path('icon_walking')
        self.tem_icon_props_path = handler.get_template_path('icon_props')
        self.tem_icon_pokedex_path = handler.get_template_path('icon_pokedex')
        self.tem_icon_close_path = handler.get_template_path('icon_close')

        self.Settings = handler.download_json('Settings')
        self.match_thresh = self.Settings["match_thresh"]


class DetectOptions(Detect):
    """
    只包含遭遇、对战、位置、逃跑
    """

    def __init__(self):
        super().__init__()

    def detect_encounter(self):
        """
        通过检测角色昵称（有白色）是否存在来判断此时是否进入对战
        """
        if is_any_white(self.reg_encounter):
            return False
        else:
            self.logger.debug("进入对战状态")
            return True

    def detect_battled(self):
        """
        通过检测特定区域是否全黑来判断此时是否已经脱离对战状态    （全黑）
        """
        if is_all_black(self.reg_battle):
            return False
        else:
            self.logger.debug("脱离对战状态")
            return True

    def detect_battle(self):
        """
        通过检测特定区域是否全黑来判断此时是否已经脱离对战状态    （全黑）
        """
        if is_all_black(self.reg_battle):
            self.logger.debug("处于对战状态")
            return True
        else:
            return False

    def detect_escape(self):
        """
        检测是否有 逃 字，判断是否出现四个选项框   二值图像ocr
        """
        max_val = image_match(self.tem_escape_path, self.reg_escape, is_ocr=True)
        if max_val >= self.match_thresh:
            self.logger.debug(f"弹出四个选项框，最大匹配度为{max_val}")
            return True
        else:
            return False

    def detect_location(self):
        """
        检测左上角的位置   二值图像ocr
        """
        # 这里需要特殊的阈值
        max_val = image_match(self.tem_location_path,self.reg_location, is_ocr=True)
        if max_val >= 0.6:
            return True
        else:
            self.logger.debug(f"角色位置被挪移，最大匹配度为{max_val}")
            return False

    def detect_cancel(self):
        """
        检测是否弹出   返回 （有白色）
        :return:
        """
        if is_any_white(self.reg_cancel):
            self.logger.debug("显示取消键")
            return True
        else:
            return False


class DetectTarget(Detect):
    """
    捕捉指定名称的精灵，检测血条和精灵名称
    """

    def __init__(self):
        super().__init__()
        self.detect_target_list = []  # 初始化检测目标列表

    def detect_health_bar(self):
        """
        检测血条（有白色）
        """
        if is_any_white(self.reg_health_bar):
            self.logger.debug("精灵已亮血条")
            return True
        else:
            return False

    def detect_poke_status(self):
        """
        检测遭遇精灵的状态 （睡眠、烧伤、麻痹……）
        """
        max_val = image_match(self.tem_poke_status_path, self.reg_poke_info, is_ocr=False)
        if max_val >= self.match_thresh:
            return True
        else:
            self.logger.debug(f"精灵未进入指定状态，最大匹配度为{max_val}")
            return False

    def detect_poke_gender(self):
        """
        检测精灵性别，原图检测ori
        """
        max_val = image_match(self.tem_poke_gender_path,self.reg_poke_info, is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"确认为目标精灵性别，最大匹配度为{max_val}")
            return True
        else:
            self.logger.debug(f"非目标精灵性别，最大匹配度为{max_val}")
            return False

    def detect_poke_name(self):
        """
        检测遭遇精灵的名字    二值图像检测ocr
        """
        max_val = image_match(self.tem_poke_name_path,self.reg_poke_info, is_ocr=True)
        if max_val >= self.match_thresh:
            self.logger.debug(f"确认为目标精灵名称，最大匹配度为{max_val}")
            return True
        else:
            self.logger.debug(f"非目标精灵名称，最大匹配度为{max_val}")
            return False

    def detect_poke_type(self):
        """
        检测精灵属性   二值图像检测ocr
        """
        max_val = image_match(self.tem_poke_type_path, self.reg_poke_info, is_ocr=True)
        if max_val >= self.match_thresh:
            self.logger.debug(f"确认为目标精灵属性，最大匹配度为{max_val}")
            return True
        else:
            self.logger.debug(f"非目标精灵属性，最大匹配度为{max_val}")
            return False

    def detect_poke_shiny(self):
        """
        检测精灵是否是闪光
        """
        max_val = image_match(self.tem_poke_shiny_path, self.reg_poke_info, is_ocr=True)
        if max_val >= self.match_thresh:
            self.logger.debug(f"确认为闪光精灵，最大匹配度为{max_val}")
            remind_shiny()
            return True
        else:
            self.logger.debug(f"非闪光精灵，最大匹配度为{max_val}")
            return False

    def detect_target(self):
        """
        检测是否是目标精灵 仅依靠名字 或者是 性别和属性
        :return: 返回的是一个状态列表
        """
        status_list = []
        while True:
            if self.detect_health_bar():
                for detect_element in self.detect_target_list:
                    status_list.append(detect_element())
                return status_list


class DetectReminder(Detect):
    def __init__(self):
        super().__init__()

    def detect_remind(self):
        """
        检测提醒框
        """
        if is_all_white(self.reg_remind):
            self.logger.debug("显示提醒框")
            return True
        else:
            return False

    def detect_remind_text(self):
        """
        循环等待提醒框出现文字
        """
        while True:
            if self.detect_remind():
                if is_any_black(self.reg_remind_text):
                    self.logger.debug("提醒框显示文字")
                    return True

    def detect_hooked_remind(self):
        """
        判定是否出现 精  字 来判断是否上鱼 原图ori
        """
        if self.detect_remind_text():
            max_val = image_match(self.tem_remind_hooked_path, self.reg_remind_text, is_ocr=False)
            if max_val >= self.match_thresh:
                self.logger.debug(f"精灵上钩了！最大匹配度为{max_val}")
                return True
            else:
                self.logger.debug(f"无精灵上钩，最大匹配度为{max_val}")
                return False

    def detect_passive_skill_remind(self):
        max_val = image_match(self.tem_remind_passive_skill_path,self.reg_remind_passive_skill,is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"触发被动技能，最大匹配度为{max_val}")
            return True
        else:
            return False

    def detect_alert_confirm_hatch(self):
        max_val = image_match(self.tem_alert_confirm_path,self.reg_alert_confirm_hatch,is_ocr=True)
        if max_val >= self.match_thresh:
            self.logger.debug(f"弹出警告框，最大匹配度{max_val}")
            return True
        else:
            return False


class DetectIcon(Detect):
    """
    检测图标
    """
    def __init__(self):
        super().__init__()

    def detect_walking_icon(self):
        """
        检测游戏窗口左侧是否存在 人物移动图标  二值图像ocr
        """
        max_val = image_match(self.tem_icon_walking_path,self.reg_icon_walking, is_ocr=True)
        if max_val >= self.match_thresh:
            return True
        else:
            self.logger.debug(f"未显示步数，最大匹配度为{max_val}")
            return False

    def detect_props_icon(self):
        """
        检测首发精灵是否携带道具
        """
        max_val = image_match(self.tem_icon_props_path,self.reg_icon_props, is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"精灵携带道具，最大匹配度为{max_val}")
            return True
        else:
            self.logger.debug(f"精灵未携带道具，最大匹配度为{max_val}")
            return False

    def detect_pokedex_icon(self):
        """
        检测宝可梦图鉴图标
        """
        max_val = image_match(self.tem_icon_pokedex_path, self.reg_icon_pokedex, is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"弹出宝可梦信息页，最大匹配度为{max_val}")
            return True
        else:
            return False

    def detect_hatchbox_close_icon(self):
        """
        检测孵蛋页关闭图标
        """
        max_val = image_match(self.tem_icon_close_path, self.reg_icon_close_hatchbox, is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"弹出孵蛋页面{max_val}")
            return True
        else:
            self.logger.debug(f"未弹出孵蛋页面{max_val}")
            return False

    def detect_computerbox_close_icon(self):
        """
        检测电脑箱子页关闭图标
        """
        max_val = image_match(self.tem_icon_close_path, self.reg_icon_close_computerbox, is_ocr=False)
        if max_val >= self.match_thresh:
            self.logger.debug(f"弹出电脑箱子{max_val}")
            return True
        else:
            return False

























