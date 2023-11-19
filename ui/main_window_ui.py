# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1075, 648)
        MainWindow.setStyleSheet("#menu_widget, #toolBox {\n"
"    background-color: #3333FF;\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(0)
        self.splitter.setObjectName("splitter")
        self.menu_widget = QtWidgets.QWidget(self.splitter)
        self.menu_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.menu_widget.setStyleSheet("background-color: #06162d;\n"
"color: #fff;\n"
"border: none;")
        self.menu_widget.setObjectName("menu_widget")
        self.gridLayout = QtWidgets.QGridLayout(self.menu_widget)
        self.gridLayout.setContentsMargins(4, 4, 4, 15)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.menu_widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("#toolBox {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#toolBox::tab {\n"
"    padding-left:5px;\n"
"    text-align:left;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"#toolBox::tab:selected {\n"
"    background-color: #2d9cdb;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#toolBox QPushButton {\n"
"    padding:5px 0px 5px 20px;\n"
"    text-align:left;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#toolBox QPushButton:hover {\n"
"    background-color: #85C1E9;\n"
"}\n"
"\n"
"#toolBox QPushButton:checked {\n"
"    background-color: #3498DB;\n"
"}\n"
"\n"
"")
        self.toolBox.setObjectName("toolBox")
        self.general_page = QtWidgets.QWidget()
        self.general_page.setGeometry(QtCore.QRect(0, 0, 142, 592))
        self.general_page.setObjectName("general_page")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.general_page)
        self.verticalLayout.setContentsMargins(5, 0, 5, 5)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton.setStyleSheet("")
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.general_page)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_4.setCheckable(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon/home-4-48 (2).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.general_page, icon, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_widget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.search_widget = QtWidgets.QWidget(self.main_widget)
        self.search_widget.setStyleSheet("#search_widget {background-color: #ABB2B9;}")
        self.search_widget.setObjectName("search_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_8 = QtWidgets.QPushButton(self.search_widget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_8.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-96-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/icon/arrow-31-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setIconSize(QtCore.QSize(15, 15))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.search_frame = QtWidgets.QFrame(self.search_widget)
        self.search_frame.setMinimumSize(QtCore.QSize(300, 30))
        self.search_frame.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.search_frame.setFont(font)
        self.search_frame.setStyleSheet("#search_frame {\n"
"    border:  1px solid #aa7e6f;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#search_btn {\n"
"    padding:5px 5px;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#search_btn:pressed {\n"
"    padding-left: 10px;\n"
"}")
        self.search_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.search_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.search_frame)
        self.horizontalLayout_10.setContentsMargins(15, 0, 5, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.search_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setClearButtonEnabled(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_10.addWidget(self.lineEdit_5)
        self.search_btn = QtWidgets.QPushButton(self.search_frame)
        self.search_btn.setStyleSheet("")
        self.search_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icon/search-3-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon2)
        self.search_btn.setIconSize(QtCore.QSize(20, 20))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_10.addWidget(self.search_btn)
        self.horizontalLayout.addWidget(self.search_frame)
        spacerItem2 = QtWidgets.QSpacerItem(209, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.user_label = QtWidgets.QLabel(self.search_widget)
        self.user_label.setMinimumSize(QtCore.QSize(30, 30))
        self.user_label.setMaximumSize(QtCore.QSize(30, 30))
        self.user_label.setStyleSheet("#user_label {\n"
"    background-color: #fff;\n"
"    border: 1px solid #F2F4F4;\n"
"    padding: 5px 5px;\n"
"    border-radius: 15%;\n"
"}")
        self.user_label.setText("")
        self.user_label.setPixmap(QtGui.QPixmap(":/icon/icon/user-48.ico"))
        self.user_label.setScaledContents(True)
        self.user_label.setObjectName("user_label")
        self.horizontalLayout.addWidget(self.user_label)
        self.gridLayout_4.addWidget(self.search_widget, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("#tabWidget {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::close-button {\n"
"    margin-left: 3px;\n"
"    image: url(:/icon/icon/x-mark-4-32.ico)\n"
"}\n"
"\n"
"QTabBar::close-button:hover {\n"
"    \n"
"    image: url(:/icon/icon/x-mark-4-48.ico);\n"
"}")
        self.tabWidget.setIconSize(QtCore.QSize(10, 10))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout_4.addWidget(self.tabWidget, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(10)
        self.tabWidget.setCurrentIndex(-1)
        self.pushButton_8.toggled['bool'].connect(self.menu_widget.setHidden) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "create playlist"))
        self.pushButton_2.setText(_translate("MainWindow", "edit playlist"))
        self.pushButton_3.setText(_translate("MainWindow", "youtube to m3u"))
        self.pushButton_4.setText(_translate("MainWindow", "youtube mp3 "))
        self.toolBox.setItemText(self.toolBox.indexOf(self.general_page), _translate("MainWindow", "General"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Search Something..."))
from . import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())