
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_JarvisOverlayGUI(object):
    def setupUi(self, JarvisOverlayGUI):
        JarvisOverlayGUI.setObjectName("JarvisOverlayGUI")
        JarvisOverlayGUI.setWindowFlag(QtCore.Qt.FramelessWindowHint)                   # line edit by me
        JarvisOverlayGUI.setWindowFlag(QtCore.Qt.WindowType.WindowStaysOnTopHint)       # line edit by me
        JarvisOverlayGUI.move(0,0)                                                      # line edit by me
        JarvisOverlayGUI.resize(402, 351)
        JarvisOverlayGUI.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame = QtWidgets.QFrame(JarvisOverlayGUI)
        self.frame.setGeometry(QtCore.QRect(150, 4, 251, 151))
        self.frame.setStyleSheet("background-color: rgb(0,0,0);\n"
                                 "border-color: rgb(255,255,255);\n"
                                 "border-width: 1px;\n"
                                 "border-style: solid;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.kartidlabel = QtWidgets.QLabel(self.frame)
        self.kartidlabel.setGeometry(QtCore.QRect(10, 10, 201, 21))
        self.kartidlabel.setStyleSheet("background-color: transparent;\n"
                                       "border-width: 0px;\n"
                                       "")
        self.kartidlabel.setText("")
        self.kartidlabel.setPixmap(QtGui.QPixmap("E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_AIVA.jpg"))
        self.kartidlabel.setScaledContents(True)
        self.kartidlabel.setObjectName("kartidlabel")
        self.minButton = QtWidgets.QPushButton(self.frame)
        self.minButton.setGeometry(QtCore.QRect(220, 0, 31, 16))
        self.minButton.setStyleSheet("color: rgb(255,255,255);\n"
                                     "background-color: transparent;\n"
                                     "border-width: 0px;\n"
                                     "font: 28pt \"Segoe UI\";\n"
                                     "font: 700 26pt \"Tahoma\";\n"
                                     "")
        self.minButton.setObjectName("minButton")
        self.SettingsFrame = QtWidgets.QFrame(self.frame)
        self.SettingsFrame.setGeometry(QtCore.QRect(0, 30, 251, 121))
        self.SettingsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SettingsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SettingsFrame.setObjectName("SettingsFrame")
        self.textBrowser = QtWidgets.QTextBrowser(self.SettingsFrame)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 81, 31))
        self.textBrowser.setStyleSheet("color: rgb(255,255,255);\n"
                                       "background-color: transparent;\n"
                                       "border-width: 0px;")
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setObjectName("textBrowser")
        self.ShowIconCB = QtWidgets.QCheckBox(self.SettingsFrame)
        self.ShowIconCB.setGeometry(QtCore.QRect(10, 30, 141, 21))
        self.ShowIconCB.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                      "color: rgb(255,255,255);\n"
                                      "background-color: transparent;\n"
                                      "border-width: 0pt;")
        self.ShowIconCB.setObjectName("ShowIconCB")
        self.ShowIconCB.setChecked(True) #line edit by me 
        self.muteCB = QtWidgets.QCheckBox(self.SettingsFrame)
        self.muteCB.setGeometry(QtCore.QRect(10, 50, 141, 21))
        self.muteCB.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                  "color: rgb(255,255,255);\n"
                                  "background-color: transparent;\n"
                                  "border-width: 0pt;")
        self.muteCB.setObjectName("muteCB")
        self.showHIconCB = QtWidgets.QCheckBox(self.SettingsFrame)
        self.showHIconCB.setGeometry(QtCore.QRect(10, 70, 141, 21))
        self.showHIconCB.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                       "color: rgb(255,255,255);\n"
                                       "background-color: transparent;\n"
                                       "border-width: 0pt;")
        self.showHIconCB.setObjectName("showHIconCB")
        self.showTerminalCB = QtWidgets.QCheckBox(self.SettingsFrame)
        self.showTerminalCB.setGeometry(QtCore.QRect(10, 90, 121, 21))
        self.showTerminalCB.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                          "color: rgb(255,255,255);\n"
                                          "background-color: transparent;\n"
                                          "border-width: 0pt;")
        self.showTerminalCB.setObjectName("showTerminalCB")
        self.customSearchCB = QtWidgets.QCheckBox(self.SettingsFrame)
        self.customSearchCB.setGeometry(QtCore.QRect(110, 50, 121, 21))
        self.customSearchCB.setStyleSheet("font: 700 7pt \"Tahoma\";\n"
                                          "color: rgb(255,255,255);\n"
                                          "background-color: transparent;\n"
                                          "border-width: 0pt;")
        self.customSearchCB.setObjectName("customSearchCB")
        self.closeButton = QtWidgets.QPushButton(self.SettingsFrame)
        self.closeButton.setGeometry(QtCore.QRect(220, 90, 31, 21))
        self.closeButton.setStyleSheet("color: rgb(255,255,255);\n"
                                       "background-color: transparent;\n"
                                       "border-width: 0px;\n"
                                       "\n"
                                       "font: 700 15pt \"Tahoma\";\n"
                                       "")
        self.closeButton.setObjectName("closeButton")
        self.jarvisMainButton = QtWidgets.QPushButton(JarvisOverlayGUI)
        self.jarvisMainButton.setGeometry(QtCore.QRect(0, 10, 141, 41))
        self.jarvisMainButton.setStyleSheet("background-color: transparent; border-image: url(""E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_logo.png)")
        self.jarvisMainButton.setText("")
        self.jarvisMainButton.setObjectName("jarvisMainButton")


        self.listeningLabel = QtWidgets.QLabel(JarvisOverlayGUI)
        self.listeningLabel.setGeometry(QtCore.QRect(0, 50, 141, 101))
        self.listeningLabel.setText("")
        self.listeningLabel.setPixmap(QtGui.QPixmap("E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_lis_mic.gif"))
        self.listeningLabel.setScaledContents(True)
        self.listeningLabel.setObjectName("listeningLabel")
        self.loadingLabel = QtWidgets.QLabel(JarvisOverlayGUI)
        self.loadingLabel.setGeometry(QtCore.QRect(0, 50, 141, 101))
        self.loadingLabel.setText("")
        self.loadingLabel.setPixmap(QtGui.QPixmap("E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_loading.gif"))
        self.loadingLabel.setScaledContents(True)
        self.loadingLabel.setObjectName("loadingLabel")
        self.speakingLabel = QtWidgets.QLabel(JarvisOverlayGUI)
        self.speakingLabel.setGeometry(QtCore.QRect(0, 50, 141, 121))
        self.speakingLabel.setText("")
        self.speakingLabel.setPixmap(QtGui.QPixmap("E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_speaking.gif"))
        self.speakingLabel.setScaledContents(True)
        self.speakingLabel.setObjectName("speakingLabel")
        self.sleepingLabel = QtWidgets.QLabel(JarvisOverlayGUI)
        self.sleepingLabel.setGeometry(QtCore.QRect(20, 60, 121, 111))
        self.sleepingLabel.setText("")
        self.sleepingLabel.setPixmap(QtGui.QPixmap("E:/AI project/jarvis_gui_mark5/gui_tools/images/jarvis_lis2.gif"))
        self.sleepingLabel.setScaledContents(True)
        self.sleepingLabel.setObjectName("sleepingLabel")
        self.searchFram = QtWidgets.QFrame(JarvisOverlayGUI)
        self.searchFram.setGeometry(QtCore.QRect(150, 150, 251, 41))
        self.searchFram.setStyleSheet("background-color: rgb(0,0,0);\n"
                                      "border-color: rgb(255,255,255);\n"
                                      "border-width: 1px;\n"
                                      "border-style: solid;\n"
                                      "")
        self.searchFram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.searchFram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searchFram.setObjectName("searchFram")
        self.sendButton = QtWidgets.QPushButton(self.searchFram)
        self.sendButton.setGeometry(QtCore.QRect(220, 10, 21, 21))
        self.sendButton.setStyleSheet("border-image: url(E:/AI project/jarvis_gui_mark5/gui_tools/images/send_botton.png);")
        self.sendButton.setText("")
        self.sendButton.setObjectName("sendButton")
        self.searchTextInput = QtWidgets.QLineEdit(self.searchFram)
        self.searchTextInput.setGeometry(QtCore.QRect(0, 0, 211, 41))
        self.searchTextInput.setStyleSheet("border-width: 1px;\n"
                                    "color: rgb(255,255,255);\n"
                                    "font:9pt \"Tahoma\";")
        self.searchTextInput.setObjectName("lineEdit")
        self.terminalFrame = QtWidgets.QFrame(JarvisOverlayGUI)
        self.terminalFrame.setGeometry(QtCore.QRect(0, 190, 401, 161))
        self.terminalFrame.setStyleSheet("border-color: rgb(255,255,255);")
        self.terminalFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.terminalFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.terminalFrame.setObjectName("terminalFrame")
        self.textEdit = QtWidgets.QTextEdit(self.terminalFrame)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")

        self.textEdit.setReadOnly(True)         # line edit by me

        self.textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit.setObjectName("textEdit")
        self.terminalText = QtWidgets.QPlainTextEdit(self.terminalFrame)
        self.terminalText.setGeometry(QtCore.QRect(0, 30, 401, 131))

        self.terminalText.setReadOnly(True)   # line edit by me

        self.terminalText.setStyleSheet("background-color: rgb(0,0,0);\n"
                                         "border-width: 1px;\n"
                                         "border-style: solid;\n"
                                         "border-color: rgb(255,255,255);\n"
                                         "font: 8pt \"Tahoma\";\n"
                                         "color: rgb(255,255,255);")
        self.terminalText.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.terminalText.setObjectName("terminalText")

        self.retranslateUi(JarvisOverlayGUI)
        QtCore.QMetaObject.connectSlotsByName(JarvisOverlayGUI)

    def retranslateUi(self, JarvisOverlayGUI):
        _translate = QtCore.QCoreApplication.translate
        JarvisOverlayGUI.setWindowTitle(_translate("JarvisOverlayGUI", "JarvisOverlayGUI"))
        self.minButton.setText(_translate("JarvisOverlayGUI", "-"))
        self.textBrowser.setHtml(_translate("JarvisOverlayGUI",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "hr { height: 1px; border-width: 0; }\n"
                                            "li.unchecked::marker { content: \"\\2610\"; }\n"
                                            "li.checked::marker { content: \"\\2612\"; }\n"
                                            "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:700;\">Settings</span></p></body></html>"))
        self.ShowIconCB.setText(_translate("JarvisOverlayGUI", "Show Status Icons"))
        self.muteCB.setText(_translate("JarvisOverlayGUI", "Mute Jarvis"))
        self.showHIconCB.setText(_translate("JarvisOverlayGUI", "Show Home Icon"))
        self.showTerminalCB.setText(_translate("JarvisOverlayGUI", "Show Terminal"))
        self.customSearchCB.setText(_translate("JarvisOverlayGUI", "Custom Search"))
        self.closeButton.setText(_translate("JarvisOverlayGUI", "x"))
        self.searchTextInput.setPlaceholderText(_translate("JarvisOverlayGUI", "Enter Query to Search"))
        self.textEdit.setHtml(_translate("JarvisOverlayGUI",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "hr { height: 1px; border-width: 0; }\n"
                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                         "</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\">Jarvis Terminal</span></p></body></html>"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    JarvisOverlayGUI = QtWidgets.QWidget()
    ui = Ui_JarvisOverlayGUI()
    ui.setupUi(JarvisOverlayGUI)
    JarvisOverlayGUI.show()
    sys.exit(app.exec_())
