# Form implementation generated from reading ui file 'c:\design.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Stalin(object):
    def setupUi(self, Stalin):
        Stalin.setObjectName("Stalin")
        Stalin.setEnabled(True)
        Stalin.resize(274, 130)
        Stalin.setMinimumSize(QtCore.QSize(274, 130))
        Stalin.setMaximumSize(QtCore.QSize(274, 130))
        self.centralwidget = QtWidgets.QWidget(Stalin)
        self.centralwidget.setMinimumSize(QtCore.QSize(274, 130))
        self.centralwidget.setMaximumSize(QtCore.QSize(274, 130))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnBrowse = QtWidgets.QPushButton(self.centralwidget)
        self.btnBrowse.setObjectName("btnBrowse")
        self.verticalLayout.addWidget(self.btnBrowse)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Bad Script")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse)
        self.label.setObjectName("label")
        self.label.hide()
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        Stalin.setCentralWidget(self.centralwidget)

        self.retranslateUi(Stalin)
        QtCore.QMetaObject.connectSlotsByName(Stalin)

    def retranslateUi(self, Stalin):
        _translate = QtCore.QCoreApplication.translate
        Stalin.setWindowTitle(_translate("Stalin", "СТАЛИН-3000"))
        self.label_2.setText(_translate("Stalin", "Программа для бесконтактного пребывания на рабочем месте."))
        self.btnBrowse.setText(_translate("Stalin", "Старт"))
        self.label.setText(_translate("Stalin", "Сталинатор запущен"))
