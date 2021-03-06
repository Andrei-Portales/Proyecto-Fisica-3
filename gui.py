from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(967, 579)
        MainWindow.setMinimumSize(QtCore.QSize(967, 579))
        MainWindow.setMaximumSize(QtCore.QSize(967, 579))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.agregarBox = QtWidgets.QGroupBox(self.centralwidget)
        self.agregarBox.setGeometry(QtCore.QRect(520, 10, 431, 261))
        self.agregarBox.setObjectName("agregarBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.agregarBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 40, 391, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.txtNombreParticula = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtNombreParticula.setObjectName("txtNombreParticula")
        self.horizontalLayout_9.addWidget(self.txtNombreParticula)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.txtCantidadProtones = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtCantidadProtones.setObjectName("txtCantidadProtones")
        self.horizontalLayout_10.addWidget(self.txtCantidadProtones)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        self.txtCantidadNeutrones = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtCantidadNeutrones.setObjectName("txtCantidadNeutrones")
        self.horizontalLayout_13.addWidget(self.txtCantidadNeutrones)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_14.addWidget(self.label_12)
        self.txtCantidadElectrones = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.txtCantidadElectrones.setObjectName("txtCantidadElectrones")
        self.horizontalLayout_14.addWidget(self.txtCantidadElectrones)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnCalcelarAgregar = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnCalcelarAgregar.setObjectName("btnCalcelarAgregar")
        self.horizontalLayout_3.addWidget(self.btnCalcelarAgregar)
        self.btnAgregarP = QtWidgets.QPushButton(self.layoutWidget_2)
        self.btnAgregarP.setObjectName("btnAgregarP")
        self.horizontalLayout_3.addWidget(self.btnAgregarP)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.eliminarBox = QtWidgets.QGroupBox(self.centralwidget)
        self.eliminarBox.setGeometry(QtCore.QRect(520, 300, 431, 191))
        self.eliminarBox.setObjectName("eliminarBox")
        self.layoutWidget = QtWidgets.QWidget(self.eliminarBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 411, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.cbParticulasEliminar = QtWidgets.QComboBox(self.layoutWidget)
        self.cbParticulasEliminar.setObjectName("cbParticulasEliminar")
        self.horizontalLayout.addWidget(self.cbParticulasEliminar)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btnEliminarParticulas = QtWidgets.QPushButton(self.layoutWidget)
        self.btnEliminarParticulas.setObjectName("btnEliminarParticulas")
        self.horizontalLayout_2.addWidget(self.btnEliminarParticulas)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 491, 541))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 30, 471, 501))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(0, -1, -1, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.cbParticles1 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbParticles1.setObjectName("cbParticles1")
        self.horizontalLayout_4.addWidget(self.cbParticles1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.cbParticles2 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbParticles2.setObjectName("cbParticles2")
        self.horizontalLayout_5.addWidget(self.cbParticles2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.cbParticles3 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.cbParticles3.setObjectName("cbParticles3")
        self.horizontalLayout_6.addWidget(self.cbParticles3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem3)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.txtVoltaje = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.txtVoltaje.setObjectName("txtVoltaje")
        self.horizontalLayout_7.addWidget(self.txtVoltaje)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.btnClean = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClean.setFont(font)
        self.btnClean.setObjectName("btnClean")
        self.horizontalLayout_8.addWidget(self.btnClean)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.btnSimulate = QtWidgets.QPushButton(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSimulate.setFont(font)
        self.btnSimulate.setObjectName("btnSimulate")
        self.horizontalLayout_8.addWidget(self.btnSimulate)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(0, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem9)
        self.btnClose = QtWidgets.QPushButton(self.layoutWidget_3)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_11.addWidget(self.btnClose)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Espectrometro de masas"))
        self.agregarBox.setTitle(_translate("MainWindow", "Agregar Particula"))
        self.label_7.setText(_translate("MainWindow", "Nombre de particula:"))
        self.label_8.setText(_translate("MainWindow", "Cantidad de protones:"))
        self.label_11.setText(_translate("MainWindow", "Cantidad de neutrones:"))
        self.label_12.setText(_translate("MainWindow", "Cantidad de electrones:"))
        self.btnCalcelarAgregar.setText(_translate("MainWindow", "Limpiar"))
        self.btnAgregarP.setText(_translate("MainWindow", "Agregar"))
        self.eliminarBox.setTitle(_translate("MainWindow", "Eliminar Particula"))
        self.label_9.setText(_translate("MainWindow", "Particula a Eliminar:"))
        self.btnEliminarParticulas.setText(_translate("MainWindow", "Eliminar"))
        self.groupBox.setTitle(_translate("MainWindow", "Simulador"))
        self.label.setText(_translate("MainWindow", "Espectrometro de masas"))
        self.label_2.setText(_translate("MainWindow", "Particulas para simular:"))
        self.label_3.setText(_translate("MainWindow", "Particula 1:"))
        self.label_4.setText(_translate("MainWindow", "Particula 2:"))
        self.label_5.setText(_translate("MainWindow", "Particula 3:"))
        self.label_6.setText(_translate("MainWindow", "Voltaje de selector:"))
        self.btnClean.setText(_translate("MainWindow", "Limpiar"))
        self.btnSimulate.setText(_translate("MainWindow", "Simular"))
        self.btnClose.setText(_translate("MainWindow", "Salir"))