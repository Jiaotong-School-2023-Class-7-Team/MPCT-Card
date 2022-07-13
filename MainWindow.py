# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import settings
import music

bgMusic = music.getPlayBgMusicThread()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/img/icon.ico"))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-image: url(:/image/img/bg.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(150, 0, 720, 171))
        self.title.setStyleSheet("background-image: url(:/image/img/null.png);\n"
                                 "font: 50pt \"交通标志专用字体\";\n"
                                 "text-align: center;\n"
                                 "color: rgb(0, 255, 255);")
        self.title.setObjectName("title")
        self.zhishi_go = QtWidgets.QPushButton(self.centralwidget)
        self.zhishi_go.setGeometry(QtCore.QRect(120, 180, 100, 160))
        self.zhishi_go.setStyleSheet("border-image: url(:/image/img/zhishi.png);\n"
                                     "border-radius: 15px")
        self.zhishi_go.setText("")
        self.zhishi_go.setObjectName("zhishi_go")
        self.duizhan_go = QtWidgets.QPushButton(self.centralwidget)
        self.duizhan_go.setGeometry(QtCore.QRect(350, 180, 100, 160))
        self.duizhan_go.setStyleSheet("border-image: url(:/image/img/duizhan.png);\n"
                                      "border-radius: 15px")
        self.duizhan_go.setText("")
        self.duizhan_go.setObjectName("duizhan_go")
        self.shiyanshi_go = QtWidgets.QPushButton(self.centralwidget)
        self.shiyanshi_go.setGeometry(QtCore.QRect(570, 180, 100, 160))
        self.shiyanshi_go.setStyleSheet("border-image: url(:/image/img/shiyanshi_disabled.png);\n"
                                        "border-radius: 15px")
        self.shiyanshi_go.setText("")
        self.shiyanshi_go.setObjectName("shiyanshi_go")
        self.shangcheng_go = QtWidgets.QPushButton(self.centralwidget)
        self.shangcheng_go.setGeometry(QtCore.QRect(120, 400, 231, 100))
        self.shangcheng_go.setStyleSheet("border-image: url(:/image/img/shangcheng.png);\n"
                                         "border-radius: 15px")
        self.shangcheng_go.setText("")
        self.shangcheng_go.setObjectName("shangcheng_go")
        self.beibao_go = QtWidgets.QPushButton(self.centralwidget)
        self.beibao_go.setGeometry(QtCore.QRect(449, 400, 221, 100))
        self.beibao_go.setStyleSheet("border-image: url(:/image/img/beibao.png);\n"
                                     "border-radius: 15px")
        self.beibao_go.setText("")
        self.beibao_go.setObjectName("beibao_go")
        self.zhishi_go.raise_()
        self.shiyanshi_go.raise_()
        self.shangcheng_go.raise_()
        self.beibao_go.raise_()
        self.title.raise_()
        self.duizhan_go.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.user_menu = QtWidgets.QMenu(self.menubar)
        self.user_menu.setObjectName("user_menu")
        self.files_menu = QtWidgets.QMenu(self.menubar)
        self.files_menu.setObjectName("files_menu")
        self.help_menu = QtWidgets.QMenu(self.menubar)
        self.help_menu.setObjectName("help_menu")
        MainWindow.setMenuBar(self.menubar)
        self.login = QtWidgets.QAction(MainWindow)
        self.login.setObjectName("login")
        self.retisger = QtWidgets.QAction(MainWindow)
        self.retisger.setObjectName("retisger")
        self.settings = QtWidgets.QAction(MainWindow)
        self.settings.setObjectName("settings")
        self.action1 = QtWidgets.QAction(MainWindow)
        self.action1.setObjectName("action1")
        self.read_file = QtWidgets.QAction(MainWindow)
        self.read_file.setObjectName("read_file")
        self.write_file = QtWidgets.QAction(MainWindow)
        self.write_file.setObjectName("write_file")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.about_ext = QtWidgets.QAction(MainWindow)
        self.about_ext.setObjectName("about_ext")
        self.user_menu.addAction(self.login)
        self.user_menu.addSeparator()
        self.user_menu.addAction(self.settings)
        self.files_menu.addAction(self.read_file)
        self.files_menu.addAction(self.write_file)
        self.help_menu.addAction(self.help)
        self.help_menu.addSeparator()
        self.help_menu.addAction(self.about_ext)
        self.menubar.addAction(self.user_menu.menuAction())
        self.menubar.addAction(self.files_menu.menuAction())
        self.menubar.addAction(self.help_menu.menuAction())

        self.settings.triggered.connect(self.openSettingsDialog)
        MainWindow.close = self.close

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MPCT Cards"))
        self.title.setText(_translate("MainWindow", "M P C T   Cards"))
        self.menubar.setStyleSheet(_translate("MainWindow", "background-image: url(:/image/img/null.png);"))
        self.user_menu.setTitle(_translate("MainWindow", "用户"))
        self.files_menu.setTitle(_translate("MainWindow", "存档"))
        self.help_menu.setTitle(_translate("MainWindow", "帮助"))
        self.login.setText(_translate("MainWindow", "登录"))
        self.login.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.retisger.setText(_translate("MainWindow", "注册"))
        self.settings.setText(_translate("MainWindow", "设置"))
        self.settings.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.action1.setText(_translate("MainWindow", "1"))
        self.read_file.setText(_translate("MainWindow", "读档"))
        self.read_file.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.write_file.setText(_translate("MainWindow", "存档"))
        self.write_file.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.help.setText(_translate("MainWindow", "帮助"))
        self.help.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.about_ext.setText(_translate("MainWindow", "关于插件"))

    @staticmethod
    def openSettingsDialog():
        Dialog = QtWidgets.QDialog()
        ui = settings.Ui_settingsDialog()
        ui.setupUi(Dialog)
        Dialog.exec()

    def close(self):
        bgMusic.wait()
        bgMusic.quit()
        self.MainWindow.close()
