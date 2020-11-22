## pyuic5 -x gui.ui -o gui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import files
import sys
from agregar_window import Ui_Agregar



class Main:

    def setParticlesComboBox(self):
        particles = files.readParticles()
        self.ui.cbParticles1.clear()
        self.ui.cbParticles2.clear()
        self.ui.cbParticles3.clear()

        for particle in particles:
            self.ui.cbParticles1.addItem(particle["name"])
            self.ui.cbParticles2.addItem(particle["name"])
            self.ui.cbParticles3.addItem(particle["name"])

    def setActionButtons(self):
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnClean.clicked.connect(self.cleanScreen)
        self.ui.btnAddParticles.clicked.connect(self.agregarDialog)

    # funciones asociadas a botones
    def close(self):
        exit(0)

    def cleanScreen(self):
        self.ui.txtVoltaje.clear()
        try:
            self.ui.cbParticles1.setCurrentIndex(0)
            self.ui.cbParticles2.setCurrentIndex(0)
            self.ui.cbParticles3.setCurrentIndex(0)
        except:
            print()

    def agregarDialog(self):
        self.Agregar = QtWidgets.QMainWindow()
        self.ui = Ui_Agregar()
        self.ui.setupUi(self.Agregar)
        self.ui.btnAgregarP.clicked.connect(self.agregarParticula)
        self.Agregar.show()

    def agregarParticula(self):
        #try:
        nombre = self.ui.txtNombreParticula.text().strip()
        protones = float(self.ui.txtCantidadProtones.text().strip())
        neutrones = float(self.ui.txtCantidadNeutrones.text().strip())
        electrones = float(self.ui.txtCantidadElectrones.text().strip())

        if nombre != "":
            particles = files.readParticles()
            particles.append({'name':nombre, 'type':1, 'protones':protones, 'neutrones':neutrones, 'electrones':electrones})
            files.writeParticles(particles)
            self.setParticlesComboBox()
            self.ui.txtCantidadProtones.clear()
            self.ui.txtCantidadNeutrones.clear()
            self.ui.txtCantidadElectrones.clear()
            self.ui = self.main
            self.showMessageDialog('Se agrego particula con exito')

        else:
            self.showMessageDialog("Tiene campos vacios")
        #except:
            #self.showMessageDialog("Ingreso datos no numericos")
            

    def showMessageDialog(self, message: str):
        self.dialogo = QtWidgets.QMessageBox()
        self.dialogo.setWindowTitle("")
        self.dialogo.setText(message)
        self.dialogo.show()


    def setGuiFunction(self):
        self.setParticlesComboBox()
        self.setActionButtons()

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.main = Ui_MainWindow()
        self.ui = self.main
        self.ui.setupUi(MainWindow)
        self.setGuiFunction()
        MainWindow.show()
        sys.exit(app.exec_())

Main()




    