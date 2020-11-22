## pyuic5 -x gui.ui -o gui.py
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
import files
import sys
import math
import matplotlib.pyplot as plt
import numpy as np



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
        self.ui.btnEliminarParticulas.clicked.connect(self.eliminarParticulas)
        self.ui.btnSimulate.clicked.connect(self.simular)
        self.ui.btnCalcelarAgregar.clicked.connect(self.cleanAgregar)


    def cleanAgregar(self):
        self.ui.txtNombreParticula.clear()
        self.ui.txtCantidadProtones.clear()
        self.ui.txtCantidadNeutrones.clear()
        self.ui.txtCantidadElectrones.clear()

    ## FUncion de simulacions
    def simular(self):
        try:
            particulas = files.readParticles()
            
            p1 = self.ui.cbParticles1.currentText()
            p2 = self.ui.cbParticles2.currentText()
            p3 = self.ui.cbParticles3.currentText()
            voltaje = float(self.ui.txtVoltaje.text().strip())

            for n in particulas:
                if n['name'] == p1:
                    p1 = n
                if n['name'] == p2:
                    p2 = n
                if n['name'] == p3:
                    p3 = n
                    
            # Se calcula la magnitud de las cargas
            chargeMagOne = abs(float(p1['charge']))
            chargeMagTwo = abs(float(p2['charge']))
            chargeMagThree = abs(float(p3['charge']))
            
            # Se calcula la velocidad de cada particula
            velocityOne = math.sqrt((2*chargeMagOne*voltaje)/float(p1['mass']))
            velocityTwo = math.sqrt((2*chargeMagTwo*voltaje)/float(p2['mass']))
            velocityThree = math.sqrt((2*chargeMagThree*voltaje)/float(p3['mass']))
            
            # Valores de campos magnetico y electrico 
            magneticField = 0.8
            electricField = 1.2
            
            # Se inicializan los radios
            radiusOne = 0
            radiusTwo = 0
            radiusThree = 0
            
            # Si la carga es distinta de 0 el radio se puede calcular...
            if chargeMagOne > 0:
                radiusOne = (float(p1['mass'])*velocityOne)/(chargeMagOne*magneticField)
            if chargeMagTwo > 0:
                radiusTwo = (float(p2['mass'])*velocityTwo)/(chargeMagTwo*magneticField)
            if chargeMagThree > 0:
                radiusThree = (float(p3['mass'])*velocityThree)/(chargeMagThree*magneticField)
            
            #Coordenadas de la primera particula
            p1ZPos = []
            p1XPos = []
            
            #Coordenadas de la segunda particula
            p2ZPos = []
            p2XPos = []
            
            #Coordenadas de la tercera particula
            p3ZPos = []
            p3XPos = []
            
            
            # Esto se usa para graficar
            with plt.style.context('dark_background'):
                plt.plot(p1ZPos,p1XPos, 'r-o')
                plt.plot(p2ZPos,p2XPos, 'b-o')
                plt.plot(p3ZPos,p3XPos, 'y-o')
            
            # Se pone nombre a los ejes
            plt.xlabel('Z Axis (m)')
            plt.ylabel('X Axis (m)')
            plt.title("Particle's Trajectory")
            
            plt.show()
            
            
            
        except:
            self.showMessageDialog('Ha ingresado datos invalidos')
            
            

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
                    self.ui.txtNombreParticula.clear()
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




    