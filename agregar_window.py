from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Agregar(object):
    def setupUi(self, Agregar):
        Agregar.setObjectName("Agregar")
        Agregar.resize(317, 194)
        self.centralwidget = QtWidgets.QWidget(Agregar)
        self.centralwidget.setObjectName("centralwidget")
        Agregar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Agregar)
        self.statusbar.setObjectName("statusbar")
        Agregar.setStatusBar(self.statusbar)

        self.retranslateUi(Agregar)
        QtCore.QMetaObject.connectSlotsByName(Agregar)

    def retranslateUi(self, Agregar):
        _translate = QtCore.QCoreApplication.translate
        Agregar.setWindowTitle(_translate("Agregar", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Agregar = QtWidgets.QMainWindow()
    ui = Ui_Agregar()
    ui.setupUi(Agregar)
    Agregar.show()
    sys.exit(app.exec_())
