# -*- coding: utf-8 -*-
# !/usr/local/bin/python
#
# Created by: Alpaslan GOKCEN
#
# WARNING! All changes made in this file will be lost!
import subprocess
import ConfigParser
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

# .config parser
config = ConfigParser.RawConfigParser()
config.read('eyup.conf')

# Button1 Configs


class ButtonParams(object):
    def __init__(self, Text, Icon, Tooltip, Komut, Parametre):
        self.text = Text
        self.Icon = Icon
        self.Tooltip = Tooltip
        self.cmd = Komut
        self.param = Parametre
# Button 1
btn1 = ButtonParams(config.get('buton1', 'Text'), config.get('buton1', 'Icon'), config.get('buton1', 'Tooltip'),
                    config.get('buton1', 'Komut'),  config.get('buton1', 'Parametre'))
# Button 2
btn2 = ButtonParams(config.get('buton2', 'Text'), config.get('buton2', 'Icon'), config.get('buton2', 'Tooltip'),
                    config.get('buton2', 'Komut'),  config.get('buton2', 'Parametre'))
# Button 3
btn3 = ButtonParams(config.get('buton3', 'Text'), config.get('buton3', 'Icon'), config.get('buton3', 'Tooltip'),
                    config.get('buton3', 'Komut'),  config.get('buton3', 'Parametre'))
# Button 4
btn4 = ButtonParams(config.get('buton4', 'Text'), config.get('buton4', 'Icon'), config.get('buton4', 'Tooltip'),
                    config.get('buton4', 'Komut'),  config.get('buton4', 'Parametre'))
# Button 5
btn5 = ButtonParams(config.get('buton5', 'Text'), config.get('buton5', 'Icon'), config.get('buton5', 'Tooltip'),
                    config.get('buton5', 'Komut'),  config.get('buton5', 'Parametre'))
# Button 6
btn6 = ButtonParams(config.get('buton6', 'Text'), config.get('buton6', 'Icon'), config.get('buton6', 'Tooltip'),
                    config.get('buton6', 'Komut'),  config.get('buton6', 'Parametre'))
# Button 7
btn7 = ButtonParams(config.get('buton7', 'Text'), config.get('buton7', 'Icon'), config.get('buton7', 'Tooltip'),
                    config.get('buton7', 'Komut'),  config.get('buton7', 'Parametre'))
# Button 8
btn8 = ButtonParams(config.get('buton8', 'Text'), config.get('buton8', 'Icon'), config.get('buton8', 'Tooltip'),
                    config.get('buton8', 'Komut'),  config.get('buton8', 'Parametre'))


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(680, 320)
        Dialog.setMinimumSize(QtCore.QSize(680, 320))
        Dialog.setMaximumSize(QtCore.QSize(680, 320))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8('resources/logo.png')), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(75)
        font = QtGui.QFont()
        font.setWeight(75)

        # BTN1
        self.btn1 = QtGui.QPushButton(Dialog)
        self.btn1.setText(_fromUtf8(btn1.text))
        rect = QtCore.QRect(10, 120, 150, 60)
        self.btn1.setGeometry(QtCore.QRect(rect))
        self.btn1.setFont(font)
        self.btn1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn1.setToolTip(_fromUtf8(btn1.Tooltip))
        self.btn1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn1.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(btn1.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn1.setIcon(icon1)
        self.btn1.setIconSize(QtCore.QSize(35, 35))

        # BTN2
        self.btn2 = QtGui.QPushButton(Dialog)
        self.btn2.setText(_fromUtf8(btn2.text))  # Text
        rect = QtCore.QRect(180, 120, 150, 60)   # Position
        self.btn2.setGeometry(QtCore.QRect(rect))
        self.btn2.setFont(font)
        self.btn2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn2.setToolTip(_fromUtf8(btn2.Tooltip))  # Tooltip
        self.btn2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn2.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()  # Icon
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(btn2.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn2.setIcon(icon2)  # Icon
        self.btn2.setIconSize(QtCore.QSize(35, 35))  # Icon

        # BTN3
        self.btn3 = QtGui.QPushButton(Dialog)
        self.btn3.setText(_fromUtf8(btn3.text))  # Text
        rect = QtCore.QRect(350, 120, 150, 60)   # Position
        self.btn3.setGeometry(QtCore.QRect(rect))
        self.btn3.setFont(font)
        self.btn3.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn3.setToolTip(_fromUtf8(btn3.Tooltip))  # Tooltip
        self.btn3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn3.setAutoFillBackground(False)
        icon3 = QtGui.QIcon()  # Icon
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(btn3.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn3.setIcon(icon3)  # Icon
        self.btn3.setIconSize(QtCore.QSize(35, 35))  # Icon


        # BTN4
        self.btn4 = QtGui.QPushButton(Dialog)
        self.btn4.setText(_fromUtf8(btn4.text))  # Text
        rect = QtCore.QRect(520, 120, 150, 60)   # Position
        self.btn4.setGeometry(QtCore.QRect(rect))
        self.btn4.setFont(font)
        self.btn4.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn4.setToolTip(_fromUtf8(btn4.Tooltip))  # Tooltip
        self.btn4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn4.setAutoFillBackground(False)
        icon4 = QtGui.QIcon()  # Icon
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(btn4.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn4.setIcon(icon4)  # Icon
        self.btn4.setIconSize(QtCore.QSize(35, 35))  # Icon

        # BTN5
        self.btn5 = QtGui.QPushButton(Dialog)
        self.btn5.setText(_fromUtf8(btn5.text))  # Text
        rect = QtCore.QRect(10, 210, 150, 60)   # Position
        self.btn5.setGeometry(QtCore.QRect(rect))
        self.btn5.setFont(font)
        self.btn5.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn5.setToolTip(_fromUtf8(btn5.Tooltip))  # Tooltip
        self.btn5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn5.setAutoFillBackground(False)
        icon5 = QtGui.QIcon()  # Icon
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(btn5.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn5.setIcon(icon5)  # Icon
        self.btn5.setIconSize(QtCore.QSize(35, 35))  # Icon

        # BTN6
        self.btn6 = QtGui.QPushButton(Dialog)
        self.btn6.setText(_fromUtf8(btn6.text))  # Text
        rect = QtCore.QRect(180, 210, 150, 60)   # Position
        self.btn6.setGeometry(QtCore.QRect(rect))
        self.btn6.setFont(font)
        self.btn6.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn6.setToolTip(_fromUtf8(btn6.Tooltip))  # Tooltip
        self.btn6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn6.setAutoFillBackground(False)
        icon6 = QtGui.QIcon()  # Icon
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(btn6.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn6.setIcon(icon6)  # Icon
        self.btn6.setIconSize(QtCore.QSize(35, 35))  # Icon

        # BTN7
        self.btn7 = QtGui.QPushButton(Dialog)
        self.btn7.setText(_fromUtf8(btn7.text))  # Text
        rect = QtCore.QRect(350, 210, 150, 60)   # Position
        self.btn7.setGeometry(QtCore.QRect(rect))
        self.btn7.setFont(font)
        self.btn7.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn7.setToolTip(_fromUtf8(btn7.Tooltip))  # Tooltip
        self.btn7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn7.setAutoFillBackground(False)
        icon7 = QtGui.QIcon()  # Icon
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(btn7.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn7.setIcon(icon7)  # Icon
        self.btn7.setIconSize(QtCore.QSize(35, 35))  # Icon

        # BTN8
        self.btn8 = QtGui.QPushButton(Dialog)
        self.btn8.setText(_fromUtf8(btn8.text))  # Text
        rect = QtCore.QRect(520, 210, 150, 60)   # Position
        self.btn8.setGeometry(QtCore.QRect(rect))
        self.btn8.setFont(font)
        self.btn8.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.btn8.setToolTip(_fromUtf8(btn8.Tooltip))  # Tooltip
        self.btn8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn8.setAutoFillBackground(False)
        icon8 = QtGui.QIcon()  # Icon
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(btn8.Icon)), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # Icon
        self.btn8.setIcon(icon8)  # Icon
        self.btn8.setIconSize(QtCore.QSize(35, 35))  # Icon

        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, -10, 111, 121))
        self.label.setText(_fromUtf8(""))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("resources/logo.png")))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.label1 = QtGui.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(200, 0, 250, 150))
        self.label1.setText(_fromUtf8("Kısayollarınız"))
        fontLabel = QtGui.QFont()
        fontLabel.setPixelSize(150)
        fontLabel.setPixelSize(40)
        self.label1.setFont(fontLabel)
        self.label1.setTextFormat(QtCore.Qt.AutoText)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName(_fromUtf8("label"))

        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setWindowTitle(_translate("Dialog", "Hotkey Programı", None))


# Click Events


def btn1_click():
    subprocess.Popen([btn1.cmd, btn1.param])


def btn2_click():
    subprocess.Popen([btn2.cmd, btn2.param])


def btn3_click():
    subprocess.Popen([btn3.cmd, btn3.param])


def btn4_click():
    subprocess.Popen([btn4.cmd, btn4.param])


def btn5_click():
    subprocess.Popen([btn5.cmd, btn5.param])


def btn6_click():
    subprocess.Popen([btn6.cmd, btn6.param])


def btn7_click():
    subprocess.Popen([btn7.cmd, btn7.param])


def btn8_click():
    subprocess.Popen([btn8.cmd, btn8.param])

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
# Button Signals
    Dialog.connect(ui.btn1, SIGNAL('pressed()'), btn1_click)
    Dialog.connect(ui.btn2, SIGNAL('pressed()'), btn2_click)
    Dialog.connect(ui.btn3, SIGNAL('pressed()'), btn3_click)
    Dialog.connect(ui.btn4, SIGNAL('pressed()'), btn4_click)
    Dialog.connect(ui.btn5, SIGNAL('pressed()'), btn5_click)
    Dialog.connect(ui.btn6, SIGNAL('pressed()'), btn6_click)
    Dialog.connect(ui.btn7, SIGNAL('pressed()'), btn7_click)
    Dialog.connect(ui.btn8, SIGNAL('pressed()'), btn8_click)
    Dialog.show()
    sys.exit(app.exec_())

