## pyuic5 -x gui.ui -o gui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import files
import sys



class Main:

    def setParticlesComboBox(self):
        particles = files.readParticles()
        self.ui.cbParticles1.clear()
        self.ui.cbParticles2.clear()
        self.ui.cbParticles3.clear()
        self.ui.cbParticulasEliminar.clear()

        for particle in particles:
            self.ui.cbParticles1.addItem(particle["name"])
            self.ui.cbParticles2.addItem(particle["name"])
            self.ui.cbParticles3.addItem(particle["name"])
            self.ui.cbParticulasEliminar.addItem(particle['name'])

    def setActionButtons(self):
        self.ui.btnClose.clicked.connect(self.close)
        self.ui.btnClean.clicked.connect(self.cleanScreen)
        self.ui.btnAgregarP.clicked.connect(self.agregarParticula)
        self.ui.btnCancelarEliminar.clicked.connect(self.cancelarEliminar)
        self.ui.btnEliminarParticulas.clicked.connect(self.eliminarParticulas)
        self.ui.btnCalcelarAgregar.clicked.connect(self.cancelarAgregar)
        self.ui.btnSimulate.clicked.connect(self.simular)
        self.ui.btnCalcelarAgregar.clicked.connect()

    def cleanAgregar(self):
        self.ui.txtNombreParticula.clear()
        self.ui.txtCantidadProtones.clear()
        self.ui.txtCantidadNeutrones.clear()
        self.ui.txtCantidadElectrones.clear()

    def simular(self):
        print('simular')

    # funciones asociadas a botones
    def close(self):
        exit(0)
    def cancelarEliminar(self):
        self.ui.eliminarBox.setVisible(False)
    def cancelarAgregar(self):
        self.ui.agregarBox.setVisible(False)

    def cleanScreen(self):
        self.ui.txtVoltaje.clear()
        try:
            self.ui.cbParticles1.setCurrentIndex(0)
            self.ui.cbParticles2.setCurrentIndex(0)
            self.ui.cbParticles3.setCurrentIndex(0)
        except:
            print()

  

    def agregarParticula(self):
        try:
            nombre = self.ui.txtNombreParticula.text().strip()
            protones = float(self.ui.txtCantidadProtones.text().strip())
            neutrones = float(self.ui.txtCantidadNeutrones.text().strip())
            electrones = float(self.ui.txtCantidadElectrones.text().strip())

            if nombre != "":
                particles = files.readParticles()
                exist = False

                for p in particles:
                    if p['name'] == nombre:
                        exist = True
                
                if exist == False:
                    particles.append({'name':nombre, 'type':1, 'protones':protones, 'neutrones':neutrones, 'electrones':electrones})
                    files.writeParticles(particles)
                    self.setParticlesComboBox()
                    self.ui.txtCantidadProtones.clear()
                    self.ui.txtCantidadNeutrones.clear()
                    self.ui.txtCantidadElectrones.clear()
                    self.showMessageDialog('Se agrego particula con exito')
                else:
                    self.showMessageDialog('Ya existe una particula con ese nombre')

            else:
                self.showMessageDialog("Tiene campos vacios")
        except:
            self.showMessageDialog("Ingreso datos no numericos")
            
    def eliminarParticulas(self):
        try:
            nombre = self.ui.cbParticulasEliminar.currentText()
            particles = files.readParticles()
            modified = []

            for particle in particles:
                if particle['name'] != nombre:
                    modified.append(particle)
            files.writeParticles(modified)
            self.setParticlesComboBox()
            self.showMessageDialog('Se elimino la particula con exito')
        except:
            self.showMessageDialog('No se pudo eliminar la particula')
        

    def showMessageDialog(self, message: str):
        self.dialogo = QtWidgets.QMessageBox()
        self.dialogo.setWindowTitle("Message")
        self.dialogo.setText(message)
        self.dialogo.show()


    def setGuiFunction(self):
        self.setParticlesComboBox()
        self.setActionButtons()

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.setGuiFunction()
        MainWindow.show()
        sys.exit(app.exec_())

Main()




    