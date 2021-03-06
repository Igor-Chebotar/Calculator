from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(710, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_Q = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Q.setGeometry(QtCore.QRect(150, 160, 61, 61))
        self.btn_Q.setObjectName("btn_Q")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.btn_Q)
        self.btn_P = QtWidgets.QPushButton(self.centralwidget)
        self.btn_P.setGeometry(QtCore.QRect(80, 160, 61, 61))
        self.btn_P.setObjectName("btn_P")
        self.buttonGroup.addButton(self.btn_P)
        self.btn_H = QtWidgets.QPushButton(self.centralwidget)
        self.btn_H.setGeometry(QtCore.QRect(80, 230, 61, 61))
        self.btn_H.setObjectName("btn_H")
        self.buttonGroup.addButton(self.btn_H)
        self.btn_I = QtWidgets.QPushButton(self.centralwidget)
        self.btn_I.setGeometry(QtCore.QRect(150, 230, 61, 61))
        self.btn_I.setObjectName("btn_I")
        self.buttonGroup.addButton(self.btn_I)
        self.btn_A = QtWidgets.QPushButton(self.centralwidget)
        self.btn_A.setGeometry(QtCore.QRect(150, 300, 61, 61))
        self.btn_A.setObjectName("btn_A")
        self.buttonGroup.addButton(self.btn_A)
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(80, 300, 61, 61))
        self.btn_9.setObjectName("btn_9")
        self.buttonGroup.addButton(self.btn_9)
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(80, 370, 61, 61))
        self.btn_1.setObjectName("btn_1")
        self.buttonGroup.addButton(self.btn_1)
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(150, 370, 61, 61))
        self.btn_2.setObjectName("btn_2")
        self.buttonGroup.addButton(self.btn_2)
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(220, 370, 61, 61))
        self.btn_3.setObjectName("btn_3")
        self.buttonGroup.addButton(self.btn_3)
        self.btn_R = QtWidgets.QPushButton(self.centralwidget)
        self.btn_R.setGeometry(QtCore.QRect(220, 160, 61, 61))
        self.btn_R.setObjectName("btn_R")
        self.buttonGroup.addButton(self.btn_R)
        self.btn_J = QtWidgets.QPushButton(self.centralwidget)
        self.btn_J.setGeometry(QtCore.QRect(220, 230, 61, 61))
        self.btn_J.setObjectName("btn_J")
        self.buttonGroup.addButton(self.btn_J)
        self.btn_B = QtWidgets.QPushButton(self.centralwidget)
        self.btn_B.setGeometry(QtCore.QRect(220, 300, 61, 61))
        self.btn_B.setObjectName("btn_B")
        self.buttonGroup.addButton(self.btn_B)
        self.btn_G = QtWidgets.QPushButton(self.centralwidget)
        self.btn_G.setGeometry(QtCore.QRect(10, 230, 61, 61))
        self.btn_G.setObjectName("btn_G")
        self.buttonGroup.addButton(self.btn_G)
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(10, 300, 61, 61))
        self.btn_8.setObjectName("btn_8")
        self.buttonGroup.addButton(self.btn_8)
        self.btn_O = QtWidgets.QPushButton(self.centralwidget)
        self.btn_O.setGeometry(QtCore.QRect(10, 160, 61, 61))
        self.btn_O.setObjectName("btn_O")
        self.buttonGroup.addButton(self.btn_O)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(570, 370, 61, 61))
        self.add.setObjectName("add")
        self.mult = QtWidgets.QPushButton(self.centralwidget)
        self.mult.setGeometry(QtCore.QRect(570, 230, 61, 61))
        self.mult.setObjectName("mult")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(10, 370, 61, 61))
        self.btn_0.setObjectName("btn_0")
        self.buttonGroup.addButton(self.btn_0)
        self.ded = QtWidgets.QPushButton(self.centralwidget)
        self.ded.setGeometry(QtCore.QRect(570, 300, 61, 61))
        self.ded.setObjectName("ded")
        self.deg = QtWidgets.QPushButton(self.centralwidget)
        self.deg.setGeometry(QtCore.QRect(570, 160, 61, 61))
        self.deg.setObjectName("deg")
        self.eq = QtWidgets.QPushButton(self.centralwidget)
        self.eq.setGeometry(QtCore.QRect(360, 440, 341, 61))
        self.eq.setObjectName("eq")
        self.point = QtWidgets.QPushButton(self.centralwidget)
        self.point.setGeometry(QtCore.QRect(10, 440, 61, 61))
        self.point.setObjectName("point")
        self.btn_c = QtWidgets.QPushButton(self.centralwidget)
        self.btn_c.setGeometry(QtCore.QRect(80, 440, 61, 61))
        self.btn_c.setObjectName("btn_c")
        self.ce = QtWidgets.QPushButton(self.centralwidget)
        self.ce.setGeometry(QtCore.QRect(150, 440, 61, 61))
        self.ce.setObjectName("ce")
        self.big_label = QtWidgets.QLabel(self.centralwidget)
        self.big_label.setGeometry(QtCore.QRect(10, 90, 691, 61))
        self.big_label.setObjectName("big_label")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 691, 31))
        self.label.setText("")
        self.label.setObjectName("label")
        self.change_notation = QtWidgets.QPushButton(self.centralwidget)
        self.change_notation.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.change_notation.setObjectName("change_notation")
        self.label_base = QtWidgets.QLabel(self.centralwidget)
        self.label_base.setGeometry(QtCore.QRect(670, 10, 31, 31))
        self.label_base.setObjectName("label_base")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(120, 10, 71, 21))
        self.comboBox.setObjectName("comboBox")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(640, 370, 61, 61))
        self.change.setObjectName("change")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(360, 370, 61, 61))
        self.btn_5.setObjectName("btn_5")
        self.btn_N = QtWidgets.QPushButton(self.centralwidget)
        self.btn_N.setGeometry(QtCore.QRect(500, 230, 61, 61))
        self.btn_N.setObjectName("btn_N")
        self.btn_C = QtWidgets.QPushButton(self.centralwidget)
        self.btn_C.setGeometry(QtCore.QRect(290, 300, 61, 61))
        self.btn_C.setObjectName("btn_C")
        self.btn_D = QtWidgets.QPushButton(self.centralwidget)
        self.btn_D.setGeometry(QtCore.QRect(360, 300, 61, 61))
        self.btn_D.setObjectName("btn_D")
        self.btn_E = QtWidgets.QPushButton(self.centralwidget)
        self.btn_E.setGeometry(QtCore.QRect(430, 300, 61, 61))
        self.btn_E.setObjectName("btn_E")
        self.btn_S = QtWidgets.QPushButton(self.centralwidget)
        self.btn_S.setGeometry(QtCore.QRect(290, 160, 61, 61))
        self.btn_S.setObjectName("btn_S")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(500, 370, 61, 61))
        self.btn_7.setObjectName("btn_7")
        self.btn_K = QtWidgets.QPushButton(self.centralwidget)
        self.btn_K.setGeometry(QtCore.QRect(290, 230, 61, 61))
        self.btn_K.setObjectName("btn_K")
        self.btn_T = QtWidgets.QPushButton(self.centralwidget)
        self.btn_T.setGeometry(QtCore.QRect(360, 160, 61, 61))
        self.btn_T.setObjectName("btn_T")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(430, 370, 61, 61))
        self.btn_6.setObjectName("btn_6")
        self.btn_U = QtWidgets.QPushButton(self.centralwidget)
        self.btn_U.setGeometry(QtCore.QRect(430, 160, 61, 61))
        self.btn_U.setObjectName("btn_U")
        self.btn_L = QtWidgets.QPushButton(self.centralwidget)
        self.btn_L.setGeometry(QtCore.QRect(360, 230, 61, 61))
        self.btn_L.setObjectName("btn_L")
        self.btn_F = QtWidgets.QPushButton(self.centralwidget)
        self.btn_F.setGeometry(QtCore.QRect(500, 300, 61, 61))
        self.btn_F.setObjectName("btn_F")
        self.btn_M = QtWidgets.QPushButton(self.centralwidget)
        self.btn_M.setGeometry(QtCore.QRect(430, 230, 61, 61))
        self.btn_M.setObjectName("btn_M")
        self.btn_V = QtWidgets.QPushButton(self.centralwidget)
        self.btn_V.setGeometry(QtCore.QRect(500, 160, 61, 61))
        self.btn_V.setObjectName("btn_V")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(290, 370, 61, 61))
        self.btn_4.setObjectName("btn_4")
        self.left_bkt = QtWidgets.QPushButton(self.centralwidget)
        self.left_bkt.setGeometry(QtCore.QRect(220, 440, 61, 61))
        self.left_bkt.setObjectName("left_bkt")
        self.right_bkt = QtWidgets.QPushButton(self.centralwidget)
        self.right_bkt.setGeometry(QtCore.QRect(290, 440, 61, 61))
        self.right_bkt.setObjectName("right_bkt")
        self.deg_2 = QtWidgets.QPushButton(self.centralwidget)
        self.deg_2.setGeometry(QtCore.QRect(640, 160, 61, 61))
        self.deg_2.setObjectName("deg_2")
        self.perc = QtWidgets.QPushButton(self.centralwidget)
        self.perc.setGeometry(QtCore.QRect(640, 300, 61, 61))
        self.perc.setObjectName("perc")
        self.mult_2 = QtWidgets.QPushButton(self.centralwidget)
        self.mult_2.setGeometry(QtCore.QRect(640, 230, 61, 61))
        self.mult_2.setObjectName("mult_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator_NS"))
        self.btn_Q.setText(_translate("MainWindow", "Q"))
        self.btn_P.setText(_translate("MainWindow", "P"))
        self.btn_H.setText(_translate("MainWindow", "H"))
        self.btn_I.setText(_translate("MainWindow", "I"))
        self.btn_A.setText(_translate("MainWindow", "A"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_R.setText(_translate("MainWindow", "R"))
        self.btn_J.setText(_translate("MainWindow", "J"))
        self.btn_B.setText(_translate("MainWindow", "B"))
        self.btn_G.setText(_translate("MainWindow", "G"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_O.setText(_translate("MainWindow", "O"))
        self.add.setText(_translate("MainWindow", "+"))
        self.mult.setText(_translate("MainWindow", "*"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.ded.setText(_translate("MainWindow", "-"))
        self.deg.setText(_translate("MainWindow", "/"))
        self.eq.setText(_translate("MainWindow", "="))
        self.point.setText(_translate("MainWindow", "."))
        self.btn_c.setText(_translate("MainWindow", "C"))
        self.ce.setText(_translate("MainWindow", "CE"))
        self.big_label.setText(_translate("MainWindow", "0"))
        self.change_notation.setText(_translate("MainWindow", "?????????????? ????"))
        self.label_base.setText(_translate("MainWindow", "10"))
        self.change.setText(_translate("MainWindow", "+-"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_N.setText(_translate("MainWindow", "N"))
        self.btn_C.setText(_translate("MainWindow", "C"))
        self.btn_D.setText(_translate("MainWindow", "D"))
        self.btn_E.setText(_translate("MainWindow", "E"))
        self.btn_S.setText(_translate("MainWindow", "S"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_K.setText(_translate("MainWindow", "K"))
        self.btn_T.setText(_translate("MainWindow", "T"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_U.setText(_translate("MainWindow", "U"))
        self.btn_L.setText(_translate("MainWindow", "L"))
        self.btn_F.setText(_translate("MainWindow", "F"))
        self.btn_M.setText(_translate("MainWindow", "M"))
        self.btn_V.setText(_translate("MainWindow", "V"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.left_bkt.setText(_translate("MainWindow", "("))
        self.right_bkt.setText(_translate("MainWindow", ")"))
        self.deg_2.setText(_translate("MainWindow", "//"))
        self.perc.setText(_translate("MainWindow", "%"))
        self.mult_2.setText(_translate("MainWindow", "**"))
