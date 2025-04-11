# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AutoPokeUI.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QToolButton, QVBoxLayout, QWidget)
import UIcon_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(600, 600))
        Form.setMaximumSize(QSize(700, 700))
        icon = QIcon()
        icon.addFile(u"assets/PNG/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setMinimumSize(QSize(600, 600))
        self.tabWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabWidget.setIconSize(QSize(20, 20))
        self.tabA = QWidget()
        self.tabA.setObjectName(u"tabA")
        self.verticalLayout = QVBoxLayout(self.tabA)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabAWidget = QTabWidget(self.tabA)
        self.tabAWidget.setObjectName(u"tabAWidget")
        self.tabAWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabAWidget.setIconSize(QSize(30, 40))
        self.tabA01 = QWidget()
        self.tabA01.setObjectName(u"tabA01")
        self.verticalLayout_6 = QVBoxLayout(self.tabA01)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupA_1 = QGroupBox(self.tabA01)
        self.groupA_1.setObjectName(u"groupA_1")
        self.verticalLayout_5 = QVBoxLayout(self.groupA_1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.DirectionMapA_1 = QHBoxLayout()
        self.DirectionMapA_1.setObjectName(u"DirectionMapA_1")
        self.gridLayoutA_1 = QGridLayout()
        self.gridLayoutA_1.setObjectName(u"gridLayoutA_1")
        self.gridLayoutA_1.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.Top_ButtonA_1 = QToolButton(self.groupA_1)
        self.Top_ButtonA_1.setObjectName(u"Top_ButtonA_1")
        icon1 = QIcon()
        icon1.addFile(u":/Move/PNG/top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Top_ButtonA_1.setIcon(icon1)
        self.Top_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.Top_ButtonA_1, 1, 2, 1, 1)

        self.RightTop_ButtonA_1 = QToolButton(self.groupA_1)
        self.RightTop_ButtonA_1.setObjectName(u"RightTop_ButtonA_1")
        icon2 = QIcon()
        icon2.addFile(u":/Move/PNG/right-tip.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RightTop_ButtonA_1.setIcon(icon2)
        self.RightTop_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.RightTop_ButtonA_1, 1, 3, 1, 1)

        self.LeftBottom_ButtonA_1 = QToolButton(self.groupA_1)
        self.LeftBottom_ButtonA_1.setObjectName(u"LeftBottom_ButtonA_1")
        icon3 = QIcon()
        icon3.addFile(u":/Move/PNG/left-bottom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LeftBottom_ButtonA_1.setIcon(icon3)
        self.LeftBottom_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.LeftBottom_ButtonA_1, 3, 1, 1, 1)

        self.Right_ButtonA_1 = QToolButton(self.groupA_1)
        self.Right_ButtonA_1.setObjectName(u"Right_ButtonA_1")
        icon4 = QIcon()
        icon4.addFile(u":/Move/PNG/right.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Right_ButtonA_1.setIcon(icon4)
        self.Right_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.Right_ButtonA_1, 2, 3, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutA_1.addItem(self.horizontalSpacer_28, 2, 4, 1, 1)

        self.LaunchButtonA_1 = QToolButton(self.groupA_1)
        self.LaunchButtonA_1.setObjectName(u"LaunchButtonA_1")
        icon5 = QIcon()
        icon5.addFile(u":/Move/PNG/start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LaunchButtonA_1.setIcon(icon5)
        self.LaunchButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.LaunchButtonA_1, 2, 2, 1, 1)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayoutA_1.addItem(self.horizontalSpacer_27, 2, 0, 1, 1)

        self.RightBottom_ButtonA_1 = QToolButton(self.groupA_1)
        self.RightBottom_ButtonA_1.setObjectName(u"RightBottom_ButtonA_1")
        icon6 = QIcon()
        icon6.addFile(u":/Move/PNG/right-bottom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RightBottom_ButtonA_1.setIcon(icon6)
        self.RightBottom_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.RightBottom_ButtonA_1, 3, 3, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutA_1.addItem(self.verticalSpacer_5, 0, 2, 1, 1)

        self.Bottom_ButtonA_1 = QToolButton(self.groupA_1)
        self.Bottom_ButtonA_1.setObjectName(u"Bottom_ButtonA_1")
        icon7 = QIcon()
        icon7.addFile(u":/Move/PNG/bottom.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Bottom_ButtonA_1.setIcon(icon7)
        self.Bottom_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.Bottom_ButtonA_1, 3, 2, 1, 1)

        self.LeftTop_ButtonA_1 = QToolButton(self.groupA_1)
        self.LeftTop_ButtonA_1.setObjectName(u"LeftTop_ButtonA_1")
        icon8 = QIcon()
        icon8.addFile(u":/Move/PNG/left-top.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.LeftTop_ButtonA_1.setIcon(icon8)
        self.LeftTop_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.LeftTop_ButtonA_1, 1, 1, 1, 1)

        self.Left_ButtonA_1 = QToolButton(self.groupA_1)
        self.Left_ButtonA_1.setObjectName(u"Left_ButtonA_1")
        icon9 = QIcon()
        icon9.addFile(u":/Move/PNG/left.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Left_ButtonA_1.setIcon(icon9)
        self.Left_ButtonA_1.setIconSize(QSize(40, 40))

        self.gridLayoutA_1.addWidget(self.Left_ButtonA_1, 2, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayoutA_1.addItem(self.verticalSpacer_6, 4, 2, 1, 1)

        self.gridLayoutA_1.setRowStretch(0, 1)
        self.gridLayoutA_1.setRowStretch(1, 3)
        self.gridLayoutA_1.setRowStretch(2, 3)
        self.gridLayoutA_1.setRowStretch(3, 3)
        self.gridLayoutA_1.setRowStretch(4, 1)
        self.gridLayoutA_1.setColumnStretch(0, 1)
        self.gridLayoutA_1.setColumnStretch(1, 3)
        self.gridLayoutA_1.setColumnStretch(2, 3)
        self.gridLayoutA_1.setColumnStretch(3, 3)
        self.gridLayoutA_1.setColumnStretch(4, 1)
        self.gridLayoutA_1.setColumnMinimumWidth(0, 1)
        self.gridLayoutA_1.setColumnMinimumWidth(1, 3)
        self.gridLayoutA_1.setColumnMinimumWidth(2, 3)
        self.gridLayoutA_1.setColumnMinimumWidth(3, 3)
        self.gridLayoutA_1.setColumnMinimumWidth(4, 1)
        self.gridLayoutA_1.setRowMinimumHeight(0, 1)
        self.gridLayoutA_1.setRowMinimumHeight(1, 3)
        self.gridLayoutA_1.setRowMinimumHeight(2, 3)
        self.gridLayoutA_1.setRowMinimumHeight(3, 3)
        self.gridLayoutA_1.setRowMinimumHeight(4, 1)

        self.DirectionMapA_1.addLayout(self.gridLayoutA_1)


        self.verticalLayout_5.addLayout(self.DirectionMapA_1)

        self.line_3 = QFrame(self.groupA_1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_3)

        self.MoveRange_A_1 = QHBoxLayout()
        self.MoveRange_A_1.setObjectName(u"MoveRange_A_1")
        self.move_labelA_1 = QLabel(self.groupA_1)
        self.move_labelA_1.setObjectName(u"move_labelA_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.move_labelA_1.sizePolicy().hasHeightForWidth())
        self.move_labelA_1.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        self.move_labelA_1.setFont(font)

        self.MoveRange_A_1.addWidget(self.move_labelA_1)

        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MoveRange_A_1.addItem(self.horizontalSpacer_86)

        self.minmove_doubleSpinBoxA_1 = QDoubleSpinBox(self.groupA_1)
        self.minmove_doubleSpinBoxA_1.setObjectName(u"minmove_doubleSpinBoxA_1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.minmove_doubleSpinBoxA_1.sizePolicy().hasHeightForWidth())
        self.minmove_doubleSpinBoxA_1.setSizePolicy(sizePolicy3)
        self.minmove_doubleSpinBoxA_1.setDecimals(1)
        self.minmove_doubleSpinBoxA_1.setMinimum(0.500000000000000)
        self.minmove_doubleSpinBoxA_1.setMaximum(5.000000000000000)
        self.minmove_doubleSpinBoxA_1.setSingleStep(0.100000000000000)

        self.MoveRange_A_1.addWidget(self.minmove_doubleSpinBoxA_1)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MoveRange_A_1.addItem(self.horizontalSpacer_87)

        self.maxmove_doubleSpinBoxA_1 = QDoubleSpinBox(self.groupA_1)
        self.maxmove_doubleSpinBoxA_1.setObjectName(u"maxmove_doubleSpinBoxA_1")
        sizePolicy3.setHeightForWidth(self.maxmove_doubleSpinBoxA_1.sizePolicy().hasHeightForWidth())
        self.maxmove_doubleSpinBoxA_1.setSizePolicy(sizePolicy3)
        self.maxmove_doubleSpinBoxA_1.setDecimals(1)
        self.maxmove_doubleSpinBoxA_1.setMinimum(0.100000000000000)
        self.maxmove_doubleSpinBoxA_1.setMaximum(10.000000000000000)
        self.maxmove_doubleSpinBoxA_1.setSingleStep(0.100000000000000)
        self.maxmove_doubleSpinBoxA_1.setValue(1.000000000000000)

        self.MoveRange_A_1.addWidget(self.maxmove_doubleSpinBoxA_1)

        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.MoveRange_A_1.addItem(self.horizontalSpacer_88)

        self.MoveRange_A_1.setStretch(0, 1)
        self.MoveRange_A_1.setStretch(1, 1)
        self.MoveRange_A_1.setStretch(2, 1)
        self.MoveRange_A_1.setStretch(3, 1)
        self.MoveRange_A_1.setStretch(4, 1)
        self.MoveRange_A_1.setStretch(5, 1)

        self.verticalLayout_5.addLayout(self.MoveRange_A_1)

        self.TurnRangeA_1 = QHBoxLayout()
        self.TurnRangeA_1.setObjectName(u"TurnRangeA_1")
        self.turn_labelA_1 = QLabel(self.groupA_1)
        self.turn_labelA_1.setObjectName(u"turn_labelA_1")
        sizePolicy2.setHeightForWidth(self.turn_labelA_1.sizePolicy().hasHeightForWidth())
        self.turn_labelA_1.setSizePolicy(sizePolicy2)
        self.turn_labelA_1.setFont(font)

        self.TurnRangeA_1.addWidget(self.turn_labelA_1)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TurnRangeA_1.addItem(self.horizontalSpacer_89)

        self.minturn_doubleSpinBoxA_1 = QDoubleSpinBox(self.groupA_1)
        self.minturn_doubleSpinBoxA_1.setObjectName(u"minturn_doubleSpinBoxA_1")
        sizePolicy3.setHeightForWidth(self.minturn_doubleSpinBoxA_1.sizePolicy().hasHeightForWidth())
        self.minturn_doubleSpinBoxA_1.setSizePolicy(sizePolicy3)
        self.minturn_doubleSpinBoxA_1.setDecimals(1)
        self.minturn_doubleSpinBoxA_1.setMinimum(0.500000000000000)
        self.minturn_doubleSpinBoxA_1.setMaximum(5.000000000000000)
        self.minturn_doubleSpinBoxA_1.setSingleStep(0.100000000000000)

        self.TurnRangeA_1.addWidget(self.minturn_doubleSpinBoxA_1)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TurnRangeA_1.addItem(self.horizontalSpacer_90)

        self.maxturn_doubleSpinBoxA_1 = QDoubleSpinBox(self.groupA_1)
        self.maxturn_doubleSpinBoxA_1.setObjectName(u"maxturn_doubleSpinBoxA_1")
        sizePolicy3.setHeightForWidth(self.maxturn_doubleSpinBoxA_1.sizePolicy().hasHeightForWidth())
        self.maxturn_doubleSpinBoxA_1.setSizePolicy(sizePolicy3)
        self.maxturn_doubleSpinBoxA_1.setDecimals(1)
        self.maxturn_doubleSpinBoxA_1.setMinimum(0.100000000000000)
        self.maxturn_doubleSpinBoxA_1.setMaximum(10.000000000000000)
        self.maxturn_doubleSpinBoxA_1.setSingleStep(0.100000000000000)
        self.maxturn_doubleSpinBoxA_1.setValue(1.000000000000000)

        self.TurnRangeA_1.addWidget(self.maxturn_doubleSpinBoxA_1)

        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.TurnRangeA_1.addItem(self.horizontalSpacer_91)

        self.TurnRangeA_1.setStretch(0, 1)
        self.TurnRangeA_1.setStretch(1, 1)
        self.TurnRangeA_1.setStretch(2, 1)
        self.TurnRangeA_1.setStretch(3, 1)
        self.TurnRangeA_1.setStretch(4, 1)
        self.TurnRangeA_1.setStretch(5, 1)

        self.verticalLayout_5.addLayout(self.TurnRangeA_1)

        self.line = QFrame(self.groupA_1)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.RecordA_1 = QHBoxLayout()
        self.RecordA_1.setObjectName(u"RecordA_1")
        self.encounter_labelA_1 = QLabel(self.groupA_1)
        self.encounter_labelA_1.setObjectName(u"encounter_labelA_1")
        self.encounter_labelA_1.setFont(font)

        self.RecordA_1.addWidget(self.encounter_labelA_1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RecordA_1.addItem(self.horizontalSpacer_30)

        self.encounter_lineEditA_1 = QLineEdit(self.groupA_1)
        self.encounter_lineEditA_1.setObjectName(u"encounter_lineEditA_1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.encounter_lineEditA_1.sizePolicy().hasHeightForWidth())
        self.encounter_lineEditA_1.setSizePolicy(sizePolicy4)
        self.encounter_lineEditA_1.setMinimumSize(QSize(100, 50))
        self.encounter_lineEditA_1.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.encounter_lineEditA_1.setClearButtonEnabled(False)

        self.RecordA_1.addWidget(self.encounter_lineEditA_1)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RecordA_1.addItem(self.horizontalSpacer_31)

        self.shiny_labelA_1 = QLabel(self.groupA_1)
        self.shiny_labelA_1.setObjectName(u"shiny_labelA_1")
        self.shiny_labelA_1.setFont(font)

        self.RecordA_1.addWidget(self.shiny_labelA_1)

        self.shiny_lineEditA_1 = QLineEdit(self.groupA_1)
        self.shiny_lineEditA_1.setObjectName(u"shiny_lineEditA_1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.shiny_lineEditA_1.sizePolicy().hasHeightForWidth())
        self.shiny_lineEditA_1.setSizePolicy(sizePolicy5)
        self.shiny_lineEditA_1.setMinimumSize(QSize(100, 50))
        self.shiny_lineEditA_1.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)

        self.RecordA_1.addWidget(self.shiny_lineEditA_1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.RecordA_1.addItem(self.horizontalSpacer_32)

        self.Reset_buttonA_1 = QPushButton(self.groupA_1)
        self.Reset_buttonA_1.setObjectName(u"Reset_buttonA_1")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Reset_buttonA_1.sizePolicy().hasHeightForWidth())
        self.Reset_buttonA_1.setSizePolicy(sizePolicy6)
        self.Reset_buttonA_1.setMinimumSize(QSize(50, 50))
        icon10 = QIcon()
        icon10.addFile(u":/Tips/PNG/Reset.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Reset_buttonA_1.setIcon(icon10)
        self.Reset_buttonA_1.setIconSize(QSize(25, 25))

        self.RecordA_1.addWidget(self.Reset_buttonA_1)

        self.RecordA_1.setStretch(0, 1)
        self.RecordA_1.setStretch(1, 1)
        self.RecordA_1.setStretch(2, 1)
        self.RecordA_1.setStretch(3, 1)
        self.RecordA_1.setStretch(4, 1)
        self.RecordA_1.setStretch(5, 1)
        self.RecordA_1.setStretch(6, 1)
        self.RecordA_1.setStretch(7, 1)

        self.verticalLayout_5.addLayout(self.RecordA_1)

        self.line_2 = QFrame(self.groupA_1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_5.addWidget(self.line_2)

        self.frameMainDirectionA_1 = QFrame(self.groupA_1)
        self.frameMainDirectionA_1.setObjectName(u"frameMainDirectionA_1")
        sizePolicy.setHeightForWidth(self.frameMainDirectionA_1.sizePolicy().hasHeightForWidth())
        self.frameMainDirectionA_1.setSizePolicy(sizePolicy)
        self.frameMainDirectionA_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameMainDirectionA_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frameMainDirectionA_1)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.MainDireLayoutA_1 = QHBoxLayout()
        self.MainDireLayoutA_1.setObjectName(u"MainDireLayoutA_1")
        self.mainDire_labelA_1 = QLabel(self.frameMainDirectionA_1)
        self.mainDire_labelA_1.setObjectName(u"mainDire_labelA_1")
        self.mainDire_labelA_1.setFont(font)

        self.MainDireLayoutA_1.addWidget(self.mainDire_labelA_1)

        self.lr_checkBoxA_1 = QCheckBox(self.frameMainDirectionA_1)
        self.lr_checkBoxA_1.setObjectName(u"lr_checkBoxA_1")
        self.lr_checkBoxA_1.setFont(font)
        self.lr_checkBoxA_1.setChecked(True)
        self.lr_checkBoxA_1.setAutoExclusive(True)
        self.lr_checkBoxA_1.setTristate(False)

        self.MainDireLayoutA_1.addWidget(self.lr_checkBoxA_1)

        self.tb_checkBoxA_1 = QCheckBox(self.frameMainDirectionA_1)
        self.tb_checkBoxA_1.setObjectName(u"tb_checkBoxA_1")
        self.tb_checkBoxA_1.setFont(font)
        self.tb_checkBoxA_1.setAutoExclusive(True)

        self.MainDireLayoutA_1.addWidget(self.tb_checkBoxA_1)


        self.horizontalLayout_16.addLayout(self.MainDireLayoutA_1)


        self.verticalLayout_5.addWidget(self.frameMainDirectionA_1)

        self.MoveDetailsA_1 = QHBoxLayout()
        self.MoveDetailsA_1.setObjectName(u"MoveDetailsA_1")
        self.frameBiasA_1 = QFrame(self.groupA_1)
        self.frameBiasA_1.setObjectName(u"frameBiasA_1")
        sizePolicy.setHeightForWidth(self.frameBiasA_1.sizePolicy().hasHeightForWidth())
        self.frameBiasA_1.setSizePolicy(sizePolicy)
        self.frameBiasA_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameBiasA_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_67 = QHBoxLayout(self.frameBiasA_1)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.BiasLayoutA_1 = QHBoxLayout()
        self.BiasLayoutA_1.setObjectName(u"BiasLayoutA_1")
        self.BiaslabelA_1 = QLabel(self.frameBiasA_1)
        self.BiaslabelA_1.setObjectName(u"BiaslabelA_1")
        self.BiaslabelA_1.setFont(font)

        self.BiasLayoutA_1.addWidget(self.BiaslabelA_1)

        self.BiascheckBoxA_1 = QCheckBox(self.frameBiasA_1)
        self.BiascheckBoxA_1.setObjectName(u"BiascheckBoxA_1")
        sizePolicy3.setHeightForWidth(self.BiascheckBoxA_1.sizePolicy().hasHeightForWidth())
        self.BiascheckBoxA_1.setSizePolicy(sizePolicy3)
        self.BiascheckBoxA_1.setFont(font)
        self.BiascheckBoxA_1.setCheckable(True)
        self.BiascheckBoxA_1.setChecked(True)
        self.BiascheckBoxA_1.setAutoExclusive(True)

        self.BiasLayoutA_1.addWidget(self.BiascheckBoxA_1)


        self.horizontalLayout_67.addLayout(self.BiasLayoutA_1)


        self.MoveDetailsA_1.addWidget(self.frameBiasA_1)

        self.frameTurnA_1 = QFrame(self.groupA_1)
        self.frameTurnA_1.setObjectName(u"frameTurnA_1")
        sizePolicy.setHeightForWidth(self.frameTurnA_1.sizePolicy().hasHeightForWidth())
        self.frameTurnA_1.setSizePolicy(sizePolicy)
        self.frameTurnA_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameTurnA_1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_69 = QHBoxLayout(self.frameTurnA_1)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.TurnLayoutA_1 = QHBoxLayout()
        self.TurnLayoutA_1.setObjectName(u"TurnLayoutA_1")
        self.TurnlabelA_1 = QLabel(self.frameTurnA_1)
        self.TurnlabelA_1.setObjectName(u"TurnlabelA_1")
        self.TurnlabelA_1.setFont(font)

        self.TurnLayoutA_1.addWidget(self.TurnlabelA_1)

        self.TurncheckBoxA_1 = QCheckBox(self.frameTurnA_1)
        self.TurncheckBoxA_1.setObjectName(u"TurncheckBoxA_1")
        sizePolicy3.setHeightForWidth(self.TurncheckBoxA_1.sizePolicy().hasHeightForWidth())
        self.TurncheckBoxA_1.setSizePolicy(sizePolicy3)
        self.TurncheckBoxA_1.setFont(font)
        self.TurncheckBoxA_1.setChecked(True)
        self.TurncheckBoxA_1.setAutoExclusive(True)

        self.TurnLayoutA_1.addWidget(self.TurncheckBoxA_1)


        self.horizontalLayout_69.addLayout(self.TurnLayoutA_1)


        self.MoveDetailsA_1.addWidget(self.frameTurnA_1)


        self.verticalLayout_5.addLayout(self.MoveDetailsA_1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_2 = QPushButton(self.groupA_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy7)
        icon11 = QIcon()
        icon11.addFile(u":/Tips/PNG/gotcha.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QSize(100, 60))

        self.horizontalLayout.addWidget(self.pushButton_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.verticalLayout_5.setStretch(0, 4)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.verticalLayout_5.setStretch(7, 1)
        self.verticalLayout_5.setStretch(8, 1)
        self.verticalLayout_5.setStretch(9, 1)

        self.verticalLayout_6.addWidget(self.groupA_1)

        icon12 = QIcon()
        icon12.addFile(u":/A/PNG/psyduck.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA01, icon12, "")
        self.tabA02 = QWidget()
        self.tabA02.setObjectName(u"tabA02")
        self.verticalLayout_15 = QVBoxLayout(self.tabA02)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        icon13 = QIcon()
        icon13.addFile(u":/A/PNG/mew.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA02, icon13, "")
        self.tabA03 = QWidget()
        self.tabA03.setObjectName(u"tabA03")
        self.verticalLayout_16 = QVBoxLayout(self.tabA03)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        icon14 = QIcon()
        icon14.addFile(u":/A/PNG/snorlax.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA03, icon14, "")
        self.tabA04 = QWidget()
        self.tabA04.setObjectName(u"tabA04")
        self.verticalLayout_13 = QVBoxLayout(self.tabA04)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        icon15 = QIcon()
        icon15.addFile(u":/A/PNG/pokeballs.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA04, icon15, "")
        self.tabA05 = QWidget()
        self.tabA05.setObjectName(u"tabA05")
        self.verticalLayout_14 = QVBoxLayout(self.tabA05)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        icon16 = QIcon()
        icon16.addFile(u":/A/PNG/fish.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA05, icon16, "")
        self.tabA06 = QWidget()
        self.tabA06.setObjectName(u"tabA06")
        self.verticalLayout_8 = QVBoxLayout(self.tabA06)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        icon17 = QIcon()
        icon17.addFile(u":/A/PNG/egg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabAWidget.addTab(self.tabA06, icon17, "")

        self.verticalLayout.addWidget(self.tabAWidget)

        icon18 = QIcon()
        icon18.addFile(u":/Menu/PNG/mega-ball.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabA, icon18, "")
        self.tabC = QWidget()
        self.tabC.setObjectName(u"tabC")
        self.verticalLayout_22 = QVBoxLayout(self.tabC)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.tabWidget_3 = QTabWidget(self.tabC)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget_3.setIconSize(QSize(30, 40))
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_9 = QVBoxLayout(self.tab_11)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        icon19 = QIcon()
        icon19.addFile(u":/C/PNG/pokemon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_3.addTab(self.tab_11, icon19, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.verticalLayout_18 = QVBoxLayout(self.tab_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        icon20 = QIcon()
        icon20.addFile(u":/C/PNG/weedle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_3.addTab(self.tab_13, icon20, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_20 = QVBoxLayout(self.tab_12)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        icon21 = QIcon()
        icon21.addFile(u":/C/PNG/avatar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_3.addTab(self.tab_12, icon21, "")

        self.verticalLayout_22.addWidget(self.tabWidget_3)

        icon22 = QIcon()
        icon22.addFile(u":/Menu/PNG/game.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabC, icon22, "")
        self.tabM = QWidget()
        self.tabM.setObjectName(u"tabM")
        self.verticalLayout_23 = QVBoxLayout(self.tabM)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tabWidget_4 = QTabWidget(self.tabM)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget_4.setIconSize(QSize(30, 40))
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_33 = QVBoxLayout(self.tab_15)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        icon23 = QIcon()
        icon23.addFile(u":/M/PNG/money-bag.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tab_15, icon23, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_34 = QVBoxLayout(self.tab_16)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        icon24 = QIcon()
        icon24.addFile(u":/M/PNG/meowth.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tab_16, icon24, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.horizontalLayout_59 = QHBoxLayout(self.tab_17)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        icon25 = QIcon()
        icon25.addFile(u":/M/PNG/instinct.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget_4.addTab(self.tab_17, icon25, "")

        self.verticalLayout_23.addWidget(self.tabWidget_4)

        icon26 = QIcon()
        icon26.addFile(u":/Menu/PNG/pokecoin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabM, icon26, "")
        self.tabSettings = QWidget()
        self.tabSettings.setObjectName(u"tabSettings")
        self.verticalLayout_10 = QVBoxLayout(self.tabSettings)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox = QGroupBox(self.tabSettings)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox.setSizePolicy(sizePolicy3)
        self.doubleSpinBox.setBaseSize(QSize(0, 0))
        self.doubleSpinBox.setMinimum(0.500000000000000)
        self.doubleSpinBox.setMaximum(1.000000000000000)
        self.doubleSpinBox.setSingleStep(0.010000000000000)
        self.doubleSpinBox.setValue(0.850000000000000)

        self.horizontalLayout_8.addWidget(self.doubleSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)
        self.horizontalLayout_8.setStretch(3, 1)
        self.horizontalLayout_8.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy8)

        self.horizontalLayout_9.addWidget(self.comboBox)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 1)
        self.horizontalLayout_9.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_7)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_6.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_6.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_6.setMinimum(0.000000000000000)
        self.doubleSpinBox_6.setMaximum(1.000000000000000)
        self.doubleSpinBox_6.setSingleStep(0.010000000000000)
        self.doubleSpinBox_6.setValue(0.500000000000000)

        self.horizontalLayout_10.addWidget(self.doubleSpinBox_6)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayout_10.setStretch(2, 1)
        self.horizontalLayout_10.setStretch(3, 1)
        self.horizontalLayout_10.setStretch(4, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 2)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 2)

        self.verticalLayout_10.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.tabSettings)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_18)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font)

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_19)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_7.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_7.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_7.setMinimum(0.900000000000000)
        self.doubleSpinBox_7.setMaximum(1.000000000000000)
        self.doubleSpinBox_7.setSingleStep(0.010000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_7)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_20)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")
        sizePolicy3.setHeightForWidth(self.doubleSpinBox_8.sizePolicy().hasHeightForWidth())
        self.doubleSpinBox_8.setSizePolicy(sizePolicy3)
        self.doubleSpinBox_8.setDecimals(3)
        self.doubleSpinBox_8.setMinimum(0.000000000000000)
        self.doubleSpinBox_8.setMaximum(0.010000000000000)
        self.doubleSpinBox_8.setSingleStep(0.001000000000000)
        self.doubleSpinBox_8.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)
        self.doubleSpinBox_8.setValue(0.009000000000000)

        self.horizontalLayout_6.addWidget(self.doubleSpinBox_8)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_22)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 1)
        self.horizontalLayout_6.setStretch(4, 1)
        self.horizontalLayout_6.setStretch(5, 1)
        self.horizontalLayout_6.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_12)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_23)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        self.label_9.setFont(font)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_24)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy3.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy3)
        self.lineEdit.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_7.addWidget(self.lineEdit)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_25)

        self.pushButton_10 = QPushButton(self.groupBox_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy3.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy3)

        self.horizontalLayout_7.addWidget(self.pushButton_10)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_26)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 1)
        self.horizontalLayout_7.setStretch(3, 1)
        self.horizontalLayout_7.setStretch(4, 1)
        self.horizontalLayout_7.setStretch(5, 1)
        self.horizontalLayout_7.setStretch(6, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 2)

        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.pushButton = QPushButton(self.tabSettings)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)

        self.verticalLayout_10.addWidget(self.pushButton)

        self.verticalLayout_10.setStretch(0, 3)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_10.setStretch(2, 1)
        icon27 = QIcon()
        icon27.addFile(u":/Menu/PNG/gear.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabSettings, icon27, "")
        self.tabK = QWidget()
        self.tabK.setObjectName(u"tabK")
        self.verticalLayout_7 = QVBoxLayout(self.tabK)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.KeysgroupBox = QGroupBox(self.tabK)
        self.KeysgroupBox.setObjectName(u"KeysgroupBox")
        self.verticalLayout_21 = QVBoxLayout(self.KeysgroupBox)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.KeysgroupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)
        self.label_3.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_3)

        self.ClientKeylineEdit = QLineEdit(self.KeysgroupBox)
        self.ClientKeylineEdit.setObjectName(u"ClientKeylineEdit")
        sizePolicy7.setHeightForWidth(self.ClientKeylineEdit.sizePolicy().hasHeightForWidth())
        self.ClientKeylineEdit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_12.addWidget(self.ClientKeylineEdit)

        self.GetKeyButton = QPushButton(self.KeysgroupBox)
        self.GetKeyButton.setObjectName(u"GetKeyButton")
        sizePolicy3.setHeightForWidth(self.GetKeyButton.sizePolicy().hasHeightForWidth())
        self.GetKeyButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_12.addWidget(self.GetKeyButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_20)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_4 = QLabel(self.KeysgroupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.ServerKeylineEdit = QLineEdit(self.KeysgroupBox)
        self.ServerKeylineEdit.setObjectName(u"ServerKeylineEdit")
        sizePolicy7.setHeightForWidth(self.ServerKeylineEdit.sizePolicy().hasHeightForWidth())
        self.ServerKeylineEdit.setSizePolicy(sizePolicy7)

        self.horizontalLayout_13.addWidget(self.ServerKeylineEdit)

        self.VerifyKeyButton = QPushButton(self.KeysgroupBox)
        self.VerifyKeyButton.setObjectName(u"VerifyKeyButton")
        sizePolicy3.setHeightForWidth(self.VerifyKeyButton.sizePolicy().hasHeightForWidth())
        self.VerifyKeyButton.setSizePolicy(sizePolicy3)

        self.horizontalLayout_13.addWidget(self.VerifyKeyButton)


        self.verticalLayout_21.addLayout(self.horizontalLayout_13)

        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer_21)

        self.verticalLayout_21.setStretch(0, 2)
        self.verticalLayout_21.setStretch(1, 6)
        self.verticalLayout_21.setStretch(2, 2)
        self.verticalLayout_21.setStretch(3, 6)

        self.verticalLayout_7.addWidget(self.KeysgroupBox)

        icon28 = QIcon()
        icon28.addFile(u":/Menu/PNG/crown.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabK, icon28, "")
        self.tabL = QWidget()
        self.tabL.setObjectName(u"tabL")
        self.verticalLayout_11 = QVBoxLayout(self.tabL)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.toolButton_90 = QToolButton(self.tabL)
        self.toolButton_90.setObjectName(u"toolButton_90")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.toolButton_90.sizePolicy().hasHeightForWidth())
        self.toolButton_90.setSizePolicy(sizePolicy9)
        self.toolButton_90.setMinimumSize(QSize(450, 400))
        self.toolButton_90.setMaximumSize(QSize(450, 450))
        icon29 = QIcon()
        icon29.addFile(u":/Tips/PNG/111.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_90.setIcon(icon29)
        self.toolButton_90.setIconSize(QSize(450, 450))

        self.horizontalLayout_93.addWidget(self.toolButton_90)


        self.verticalLayout_11.addLayout(self.horizontalLayout_93)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_110)

        self.checkBox_37 = QCheckBox(self.tabL)
        self.checkBox_37.setObjectName(u"checkBox_37")
        self.checkBox_37.setFont(font)

        self.horizontalLayout_96.addWidget(self.checkBox_37)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_111)


        self.verticalLayout_11.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_112)

        self.label_92 = QLabel(self.tabL)
        self.label_92.setObjectName(u"label_92")
        font2 = QFont()
        font2.setPointSize(16)
        self.label_92.setFont(font2)

        self.horizontalLayout_92.addWidget(self.label_92)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_116)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_117)

        self.label_93 = QLabel(self.tabL)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font2)

        self.horizontalLayout_92.addWidget(self.label_93)

        self.horizontalSpacer_118 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_118)


        self.verticalLayout_11.addLayout(self.horizontalLayout_92)

        self.verticalLayout_11.setStretch(0, 3)
        self.verticalLayout_11.setStretch(1, 1)
        self.verticalLayout_11.setStretch(2, 1)
        icon30 = QIcon()
        icon30.addFile(u":/Menu/PNG/nature.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.tabWidget.addTab(self.tabL, icon30, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.retranslateUi(Form)
        self.Reset_buttonA_1.clicked.connect(self.shiny_lineEditA_1.clear)
        self.Reset_buttonA_1.clicked.connect(self.encounter_lineEditA_1.clear)

        self.tabWidget.setCurrentIndex(0)
        self.tabAWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_4.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"PokeAuto", None))
        self.groupA_1.setTitle(QCoreApplication.translate("Form", u"\u5355\u9047\u5237\u95ea", None))
        self.Top_ButtonA_1.setText("")
        self.RightTop_ButtonA_1.setText("")
        self.LeftBottom_ButtonA_1.setText("")
        self.Right_ButtonA_1.setText("")
        self.LaunchButtonA_1.setText("")
        self.RightBottom_ButtonA_1.setText("")
        self.Bottom_ButtonA_1.setText("")
        self.LeftTop_ButtonA_1.setText("")
        self.Left_ButtonA_1.setText("")
        self.move_labelA_1.setText(QCoreApplication.translate("Form", u"\u79fb\u52a8\u8303\u56f4", None))
        self.turn_labelA_1.setText(QCoreApplication.translate("Form", u"\u8f6c\u5411\u8303\u56f4", None))
        self.encounter_labelA_1.setText(QCoreApplication.translate("Form", u"\u9047\u602a", None))
        self.encounter_lineEditA_1.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.shiny_labelA_1.setText(QCoreApplication.translate("Form", u"\u51fa\u95ea", None))
        self.shiny_lineEditA_1.setPlaceholderText(QCoreApplication.translate("Form", u"0", None))
        self.Reset_buttonA_1.setText("")
        self.mainDire_labelA_1.setText(QCoreApplication.translate("Form", u"\u4e3b\u65b9\u5411", None))
        self.lr_checkBoxA_1.setText(QCoreApplication.translate("Form", u"\u5de6/\u53f3", None))
        self.tb_checkBoxA_1.setText(QCoreApplication.translate("Form", u"\u4e0a/\u4e0b", None))
        self.BiaslabelA_1.setText(QCoreApplication.translate("Form", u"\u504f\u5411", None))
        self.BiascheckBoxA_1.setText("")
        self.TurnlabelA_1.setText(QCoreApplication.translate("Form", u"\u8f6c\u5411", None))
        self.TurncheckBoxA_1.setText("")
        self.pushButton_2.setText("")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA01), "")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA02), "")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA03), "")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA04), "")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA05), "")
        self.tabAWidget.setTabText(self.tabAWidget.indexOf(self.tabA06), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabA), QCoreApplication.translate("Form", u"\u5237\u95ea", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), "")
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), "")
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabC), QCoreApplication.translate("Form", u"\u6293\u7d20\u6750", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), "")
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), "")
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_17), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabM), QCoreApplication.translate("Form", u"\u8d5a\u94b1", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8c03\u6574\u9608\u503c", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf\u5339\u914d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u79fb\u52a8\u901f\u7387", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"0.1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"0.15", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"0.2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Form", u"0.25", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"\u9f20\u6807/\u952e\u76d8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u8c03\u6574\u8303\u56f4", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u6302\u673a\u6982\u7387", None))
        self.label_9.setText(QCoreApplication.translate("Form", u" \u55b5\u7801\u63d0\u9192 ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u8bf7\u8f93\u5165\u55b5\u7801", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"\u6d4b\u8bd5", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u5e76\u9a8c\u8bc1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSettings), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.KeysgroupBox.setTitle(QCoreApplication.translate("Form", u"\u9a8c\u8bc1\u5bc6\u94a5", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5ba2\u6237\u7aef\u5bc6\u94a5", None))
        self.GetKeyButton.setText(QCoreApplication.translate("Form", u"\u83b7\u53d6", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u670d\u52a1\u7aef\u5bc6\u94a5", None))
        self.VerifyKeyButton.setText(QCoreApplication.translate("Form", u"\u9a8c\u8bc1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabK), QCoreApplication.translate("Form", u"\u5bc6\u94a5", None))
        self.toolButton_90.setText("")
        self.checkBox_37.setText(QCoreApplication.translate("Form", u"\u589e\u52a0\u51fa\u95ea\u6982\u7387", None))
        self.label_92.setText(QCoreApplication.translate("Form", u"\u611f\u8c22\u597d\u8bc4", None))
        self.label_93.setText(QCoreApplication.translate("Form", u"\u652f\u6301\u6b63\u7248", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabL), QCoreApplication.translate("Form", u"\u8054\u7cfb\u4f5c\u8005", None))
    # retranslateUi

