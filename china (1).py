# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chinesestock (1).ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(230, 230, 230)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 10, 171, 41))
        self.label.setObjectName("label")
        self.averagestockstock1 = QtWidgets.QComboBox(self.centralwidget)
        self.averagestockstock1.setGeometry(QtCore.QRect(30, 100, 131, 31))
        self.averagestockstock1.setObjectName("averagestockstock1")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockstock1.addItem("")
        self.averagestockvalue = QtWidgets.QTextEdit(self.centralwidget)
        self.averagestockvalue.setGeometry(QtCore.QRect(90, 190, 131, 31))
        self.averagestockvalue.setObjectName("averagestockvalue")
        self.averagestockyear1 = QtWidgets.QComboBox(self.centralwidget)
        self.averagestockyear1.setGeometry(QtCore.QRect(170, 70, 131, 31))
        self.averagestockyear1.setObjectName("averagestockyear1")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.averagestockyear1.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 50, 51, 16))
        self.label_3.setObjectName("label_3")
        self.averagestockyear2 = QtWidgets.QComboBox(self.centralwidget)
        self.averagestockyear2.setGeometry(QtCore.QRect(170, 130, 131, 31))
        self.averagestockyear2.setObjectName("averagestockyear2")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.averagestockyear2.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 110, 47, 13))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 170, 101, 16))
        self.label_5.setObjectName("label_5")
        self.averagestockpricecalculate = QtWidgets.QPushButton(self.centralwidget)
        self.averagestockpricecalculate.setGeometry(QtCore.QRect(120, 230, 75, 23))
        self.averagestockpricecalculate.setObjectName("averagestockpricecalculate")
        self.corralationyear1 = QtWidgets.QComboBox(self.centralwidget)
        self.corralationyear1.setGeometry(QtCore.QRect(480, 70, 131, 31))
        self.corralationyear1.setObjectName("corralationyear1")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.corralationyear1.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(340, 110, 101, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(340, 50, 47, 13))
        self.label_7.setObjectName("label_7")
        self.corralationstock1 = QtWidgets.QComboBox(self.centralwidget)
        self.corralationstock1.setGeometry(QtCore.QRect(340, 70, 131, 31))
        self.corralationstock1.setObjectName("corralationstock1")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.corralationstock1.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(480, 110, 47, 13))
        self.label_8.setObjectName("label_8")
        self.corralationyear2 = QtWidgets.QComboBox(self.centralwidget)
        self.corralationyear2.setGeometry(QtCore.QRect(480, 130, 131, 31))
        self.corralationyear2.setObjectName("corralationyear2")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.corralationyear2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(480, 50, 51, 16))
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 230, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 10, 171, 41))
        self.label_10.setObjectName("label_10")
        self.corralationstock2 = QtWidgets.QComboBox(self.centralwidget)
        self.corralationstock2.setGeometry(QtCore.QRect(340, 130, 131, 31))
        self.corralationstock2.setObjectName("corralationstock2")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.corralationstock2.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 230, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(550, 230, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(180, 400, 47, 13))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(70, 300, 171, 41))
        self.label_12.setObjectName("label_12")
        self.graphdatayear2 = QtWidgets.QComboBox(self.centralwidget)
        self.graphdatayear2.setGeometry(QtCore.QRect(180, 420, 131, 31))
        self.graphdatayear2.setObjectName("graphdatayear2")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatayear2.addItem("")
        self.graphdatagraphdata = QtWidgets.QPushButton(self.centralwidget)
        self.graphdatagraphdata.setGeometry(QtCore.QRect(130, 520, 75, 23))
        self.graphdatagraphdata.setObjectName("graphdatagraphdata")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(40, 370, 47, 13))
        self.label_13.setObjectName("label_13")
        self.graphdatayear1 = QtWidgets.QComboBox(self.centralwidget)
        self.graphdatayear1.setGeometry(QtCore.QRect(180, 360, 131, 31))
        self.graphdatayear1.setObjectName("graphdatayear1")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatayear1.addItem("")
        self.graphdatastock1 = QtWidgets.QComboBox(self.centralwidget)
        self.graphdatastock1.setGeometry(QtCore.QRect(40, 390, 131, 31))
        self.graphdatastock1.setObjectName("graphdatastock1")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.graphdatastock1.addItem("")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(180, 340, 51, 16))
        self.label_15.setObjectName("label_15")
        self.predictstock1 = QtWidgets.QComboBox(self.centralwidget)
        self.predictstock1.setGeometry(QtCore.QRect(350, 390, 131, 31))
        self.predictstock1.setObjectName("predictstock1")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.predictstock1.addItem("")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(490, 340, 51, 16))
        self.label_14.setObjectName("label_14")
        self.predictcalculate = QtWidgets.QPushButton(self.centralwidget)
        self.predictcalculate.setGeometry(QtCore.QRect(480, 520, 111, 23))
        self.predictcalculate.setObjectName("predictcalculate")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(400, 300, 191, 41))
        self.label_16.setObjectName("label_16")
        self.predictyear2 = QtWidgets.QComboBox(self.centralwidget)
        self.predictyear2.setGeometry(QtCore.QRect(490, 420, 131, 31))
        self.predictyear2.setObjectName("predictyear2")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.addItem("")
        self.predictyear2.setItemText(13, "")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(490, 400, 47, 13))
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(350, 370, 47, 13))
        self.label_19.setObjectName("label_19")
        self.predictgraph = QtWidgets.QPushButton(self.centralwidget)
        self.predictgraph.setGeometry(QtCore.QRect(360, 520, 111, 23))
        self.predictgraph.setObjectName("predictgraph")
        self.predictyear1 = QtWidgets.QComboBox(self.centralwidget)
        self.predictyear1.setGeometry(QtCore.QRect(490, 360, 131, 31))
        self.predictyear1.setObjectName("predictyear1")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.predictyear1.addItem("")
        self.corralationvalue = QtWidgets.QTextEdit(self.centralwidget)
        self.corralationvalue.setGeometry(QtCore.QRect(410, 190, 131, 31))
        self.corralationvalue.setObjectName("corralationvalue")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(410, 170, 101, 16))
        self.label_20.setObjectName("label_20")
        self.predictvalue = QtWidgets.QTextEdit(self.centralwidget)
        self.predictvalue.setGeometry(QtCore.QRect(420, 480, 131, 31))
        self.predictvalue.setObjectName("predictvalue")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(420, 460, 101, 16))
        self.label_21.setObjectName("label_21")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 280, 661, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(320, 0, 20, 531))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuChinese_Stock_Price = QtWidgets.QMenu(self.menubar)
        self.menuChinese_Stock_Price.setObjectName("menuChinese_Stock_Price")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuChinese_Stock_Price.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Average Stock Price</span></p></body></html>"))
        self.averagestockstock1.setItemText(0, _translate("MainWindow", "Fiyta Holdings Ltd"))
        self.averagestockstock1.setItemText(1, _translate("MainWindow", "Dongxu Optoelectronic Technology Co Ltd"))
        self.averagestockstock1.setItemText(2, _translate("MainWindow", "Changhong Meiling Co Ltd"))
        self.averagestockstock1.setItemText(3, _translate("MainWindow", "CSG Holding Co Ltd"))
        self.averagestockstock1.setItemText(4, _translate("MainWindow", "Dalian Refrigeration Co Ltd"))
        self.averagestockstock1.setItemText(5, _translate("MainWindow", "Shenzhen Wongtee International Enterprise Co Ltd"))
        self.averagestockstock1.setItemText(6, _translate("MainWindow", "Guangdong Electriv Power Development"))
        self.averagestockstock1.setItemText(7, _translate("MainWindow", "Shandong Chenming Paper Holding Ltd"))
        self.averagestockstock1.setItemText(8, _translate("MainWindow", "Foshan Electrical And Lighting Co Ltd"))
        self.averagestockyear1.setItemText(0, _translate("MainWindow", "2008"))
        self.averagestockyear1.setItemText(1, _translate("MainWindow", "2009"))
        self.averagestockyear1.setItemText(2, _translate("MainWindow", "2010"))
        self.averagestockyear1.setItemText(3, _translate("MainWindow", "2011"))
        self.averagestockyear1.setItemText(4, _translate("MainWindow", "2012"))
        self.averagestockyear1.setItemText(5, _translate("MainWindow", "2013"))
        self.averagestockyear1.setItemText(6, _translate("MainWindow", "2014"))
        self.averagestockyear1.setItemText(7, _translate("MainWindow", "2015"))
        self.averagestockyear1.setItemText(8, _translate("MainWindow", "2016"))
        self.averagestockyear1.setItemText(9, _translate("MainWindow", "2017"))
        self.averagestockyear1.setItemText(10, _translate("MainWindow", "2018"))
        self.label_2.setText(_translate("MainWindow", "Stock"))
        self.label_3.setText(_translate("MainWindow", "Start Year"))
        self.averagestockyear2.setItemText(0, _translate("MainWindow", "2008"))
        self.averagestockyear2.setItemText(1, _translate("MainWindow", "2009"))
        self.averagestockyear2.setItemText(2, _translate("MainWindow", "2010"))
        self.averagestockyear2.setItemText(3, _translate("MainWindow", "2011"))
        self.averagestockyear2.setItemText(4, _translate("MainWindow", "2012"))
        self.averagestockyear2.setItemText(5, _translate("MainWindow", "2013"))
        self.averagestockyear2.setItemText(6, _translate("MainWindow", "2014"))
        self.averagestockyear2.setItemText(7, _translate("MainWindow", "2015"))
        self.averagestockyear2.setItemText(8, _translate("MainWindow", "2016"))
        self.averagestockyear2.setItemText(9, _translate("MainWindow", "2017"))
        self.averagestockyear2.setItemText(10, _translate("MainWindow", "2018"))
        self.label_4.setText(_translate("MainWindow", "End Year"))
        self.label_5.setText(_translate("MainWindow", "Value"))
        self.averagestockpricecalculate.setText(_translate("MainWindow", "Calculate"))
        self.corralationyear1.setItemText(0, _translate("MainWindow", "2008"))
        self.corralationyear1.setItemText(1, _translate("MainWindow", "2009"))
        self.corralationyear1.setItemText(2, _translate("MainWindow", "2010"))
        self.corralationyear1.setItemText(3, _translate("MainWindow", "2011"))
        self.corralationyear1.setItemText(4, _translate("MainWindow", "2012"))
        self.corralationyear1.setItemText(5, _translate("MainWindow", "2013"))
        self.corralationyear1.setItemText(6, _translate("MainWindow", "2014"))
        self.corralationyear1.setItemText(7, _translate("MainWindow", "2015"))
        self.corralationyear1.setItemText(8, _translate("MainWindow", "2016"))
        self.corralationyear1.setItemText(9, _translate("MainWindow", "2017"))
        self.corralationyear1.setItemText(10, _translate("MainWindow", "2018"))
        self.label_6.setText(_translate("MainWindow", "Stock 2"))
        self.label_7.setText(_translate("MainWindow", "Stock 1"))
        self.corralationstock1.setItemText(0, _translate("MainWindow", "Fiyta Holdings Ltd"))
        self.corralationstock1.setItemText(1, _translate("MainWindow", "Dongxu Optoelectronic Technology Co Ltd"))
        self.corralationstock1.setItemText(2, _translate("MainWindow", "Changhong Meiling Co Ltd"))
        self.corralationstock1.setItemText(3, _translate("MainWindow", "CSG Holding Co Ltd"))
        self.corralationstock1.setItemText(4, _translate("MainWindow", "Dalian Refrigeration Co Ltd"))
        self.corralationstock1.setItemText(5, _translate("MainWindow", "Shenzhen Wongtee International Enterprise Co Ltd"))
        self.corralationstock1.setItemText(6, _translate("MainWindow", "Guangdong Electriv Power Development"))
        self.corralationstock1.setItemText(7, _translate("MainWindow", "Shandong Chenming Paper Holding Ltd"))
        self.corralationstock1.setItemText(8, _translate("MainWindow", "Foshan Electrical And Lighting Co Ltd"))
        self.label_8.setText(_translate("MainWindow", "End Year"))
        self.corralationyear2.setItemText(0, _translate("MainWindow", "2008"))
        self.corralationyear2.setItemText(1, _translate("MainWindow", "2009"))
        self.corralationyear2.setItemText(2, _translate("MainWindow", "2010"))
        self.corralationyear2.setItemText(3, _translate("MainWindow", "2011"))
        self.corralationyear2.setItemText(4, _translate("MainWindow", "2012"))
        self.corralationyear2.setItemText(5, _translate("MainWindow", "2013"))
        self.corralationyear2.setItemText(6, _translate("MainWindow", "2014"))
        self.corralationyear2.setItemText(7, _translate("MainWindow", "2015"))
        self.corralationyear2.setItemText(8, _translate("MainWindow", "2016"))
        self.corralationyear2.setItemText(9, _translate("MainWindow", "2017"))
        self.corralationyear2.setItemText(10, _translate("MainWindow", "2018"))
        self.label_9.setText(_translate("MainWindow", "Start Year"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Corralation"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Corralation</span></p></body></html>"))
        self.corralationstock2.setItemText(0, _translate("MainWindow", "Fiyta Holdings Ltd"))
        self.corralationstock2.setItemText(1, _translate("MainWindow", "Dongxu Optoelectronic Technology Co Ltd"))
        self.corralationstock2.setItemText(2, _translate("MainWindow", "Changhong Meiling Co Ltd"))
        self.corralationstock2.setItemText(3, _translate("MainWindow", "CSG Holding Co Ltd"))
        self.corralationstock2.setItemText(4, _translate("MainWindow", "Dalian Refrigeration Co Ltd"))
        self.corralationstock2.setItemText(5, _translate("MainWindow", "Shenzhen Wongtee International Enterprise Co Ltd"))
        self.corralationstock2.setItemText(6, _translate("MainWindow", "Guangdong Electriv Power Development"))
        self.corralationstock2.setItemText(7, _translate("MainWindow", "Shandong Chenming Paper Holding Ltd"))
        self.corralationstock2.setItemText(8, _translate("MainWindow", "Foshan Electrical And Lighting Co Ltd"))
        self.pushButton_3.setText(_translate("MainWindow", "Graph Data"))
        self.pushButton_4.setText(_translate("MainWindow", "Graph Related Data"))
        self.label_11.setText(_translate("MainWindow", "End Year"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Graph Data</span></p></body></html>"))
        self.graphdatayear2.setItemText(0, _translate("MainWindow", "2008"))
        self.graphdatayear2.setItemText(1, _translate("MainWindow", "2009"))
        self.graphdatayear2.setItemText(2, _translate("MainWindow", "2010"))
        self.graphdatayear2.setItemText(3, _translate("MainWindow", "2011"))
        self.graphdatayear2.setItemText(4, _translate("MainWindow", "2012"))
        self.graphdatayear2.setItemText(5, _translate("MainWindow", "2013"))
        self.graphdatayear2.setItemText(6, _translate("MainWindow", "2014"))
        self.graphdatayear2.setItemText(7, _translate("MainWindow", "2015"))
        self.graphdatayear2.setItemText(8, _translate("MainWindow", "2016"))
        self.graphdatayear2.setItemText(9, _translate("MainWindow", "2017"))
        self.graphdatayear2.setItemText(10, _translate("MainWindow", "2018"))
        self.graphdatagraphdata.setText(_translate("MainWindow", "Graph Data"))
        self.label_13.setText(_translate("MainWindow", "Stock"))
        self.graphdatayear1.setItemText(0, _translate("MainWindow", "2008"))
        self.graphdatayear1.setItemText(1, _translate("MainWindow", "2009"))
        self.graphdatayear1.setItemText(2, _translate("MainWindow", "2010"))
        self.graphdatayear1.setItemText(3, _translate("MainWindow", "2011"))
        self.graphdatayear1.setItemText(4, _translate("MainWindow", "2012"))
        self.graphdatayear1.setItemText(5, _translate("MainWindow", "2013"))
        self.graphdatayear1.setItemText(6, _translate("MainWindow", "2014"))
        self.graphdatayear1.setItemText(7, _translate("MainWindow", "2015"))
        self.graphdatayear1.setItemText(8, _translate("MainWindow", "2016"))
        self.graphdatayear1.setItemText(9, _translate("MainWindow", "2017"))
        self.graphdatayear1.setItemText(10, _translate("MainWindow", "2018"))
        self.graphdatastock1.setItemText(0, _translate("MainWindow", "Fiyta Holdings Ltd"))
        self.graphdatastock1.setItemText(1, _translate("MainWindow", "Dongxu Optoelectronic Technology Co Ltd"))
        self.graphdatastock1.setItemText(2, _translate("MainWindow", "Changhong Meiling Co Ltd"))
        self.graphdatastock1.setItemText(3, _translate("MainWindow", "CSG Holding Co Ltd"))
        self.graphdatastock1.setItemText(4, _translate("MainWindow", "Dalian Refrigeration Co Ltd"))
        self.graphdatastock1.setItemText(5, _translate("MainWindow", "Shenzhen Wongtee International Enterprise Co Ltd"))
        self.graphdatastock1.setItemText(6, _translate("MainWindow", "Guangdong Electriv Power Development"))
        self.graphdatastock1.setItemText(7, _translate("MainWindow", "Shandong Chenming Paper Holding Ltd"))
        self.graphdatastock1.setItemText(8, _translate("MainWindow", "Foshan Electrical And Lighting Co Ltd"))
        self.label_15.setText(_translate("MainWindow", "Start Year"))
        self.predictstock1.setItemText(0, _translate("MainWindow", "Fiyta Holdings Ltd"))
        self.predictstock1.setItemText(1, _translate("MainWindow", "Dongxu Optoelectronic Technology Co Ltd"))
        self.predictstock1.setItemText(2, _translate("MainWindow", "Changhong Meiling Co Ltd"))
        self.predictstock1.setItemText(3, _translate("MainWindow", "CSG Holding Co Ltd"))
        self.predictstock1.setItemText(4, _translate("MainWindow", "Dalian Refrigeration Co Ltd"))
        self.predictstock1.setItemText(5, _translate("MainWindow", "Shenzhen Wongtee International Enterprise Co Ltd"))
        self.predictstock1.setItemText(6, _translate("MainWindow", "Guangdong Electriv Power Development"))
        self.predictstock1.setItemText(7, _translate("MainWindow", "Shandong Chenming Paper Holding Ltd"))
        self.predictstock1.setItemText(8, _translate("MainWindow", "Foshan Electrical And Lighting Co Ltd"))
        self.label_14.setText(_translate("MainWindow", "Start Year"))
        self.predictcalculate.setText(_translate("MainWindow", "Calculate"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Predict Future Average Stock Price</span></p></body></html>"))
        self.predictyear2.setItemText(0, _translate("MainWindow", "2008"))
        self.predictyear2.setItemText(1, _translate("MainWindow", "2009"))
        self.predictyear2.setItemText(2, _translate("MainWindow", "2010"))
        self.predictyear2.setItemText(3, _translate("MainWindow", "2011"))
        self.predictyear2.setItemText(4, _translate("MainWindow", "2012"))
        self.predictyear2.setItemText(5, _translate("MainWindow", "2013"))
        self.predictyear2.setItemText(6, _translate("MainWindow", "2014"))
        self.predictyear2.setItemText(7, _translate("MainWindow", "2015"))
        self.predictyear2.setItemText(8, _translate("MainWindow", "2016"))
        self.predictyear2.setItemText(9, _translate("MainWindow", "2017"))
        self.predictyear2.setItemText(10, _translate("MainWindow", "2018"))
        self.predictyear2.setItemText(11, _translate("MainWindow", "2019"))
        self.predictyear2.setItemText(12, _translate("MainWindow", "2020"))
        self.label_17.setText(_translate("MainWindow", "End Year"))
        self.label_19.setText(_translate("MainWindow", "Stock 1"))
        self.predictgraph.setText(_translate("MainWindow", "Graph"))
        self.predictyear1.setItemText(0, _translate("MainWindow", "2008"))
        self.predictyear1.setItemText(1, _translate("MainWindow", "2009"))
        self.predictyear1.setItemText(2, _translate("MainWindow", "2010"))
        self.predictyear1.setItemText(3, _translate("MainWindow", "2011"))
        self.predictyear1.setItemText(4, _translate("MainWindow", "2012"))
        self.predictyear1.setItemText(5, _translate("MainWindow", "2013"))
        self.predictyear1.setItemText(6, _translate("MainWindow", "2014"))
        self.predictyear1.setItemText(7, _translate("MainWindow", "2015"))
        self.predictyear1.setItemText(8, _translate("MainWindow", "2016"))
        self.predictyear1.setItemText(9, _translate("MainWindow", "2017"))
        self.predictyear1.setItemText(10, _translate("MainWindow", "2018"))
        self.corralationvalue.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "Value"))
        self.label_21.setText(_translate("MainWindow", "Value"))
        self.menuChinese_Stock_Price.setTitle(_translate("MainWindow", "Chinese Stock Price"))

