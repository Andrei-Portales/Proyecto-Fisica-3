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
            chargeMagOne = abs(p1['charge'])
            chargeMagTwo = abs(p2['charge'])
            chargeMagThree = abs(p3['charge'])
            
            # Se calcula la velocidad de cada particula
            velocityOne = math.sqrt((2*chargeMagOne*voltaje)/p1['mass'])
            velocityTwo = math.sqrt((2*chargeMagTwo*voltaje)/p2['mass'])
            velocityThree = math.sqrt((2*chargeMagThree*voltaje)/p3['mass'])
            
            
            # Valores de campos magnetico y electrico 
            magneticField = 2000
            electricField = 1000
            
            # Se calcula la velocidad angular
            velAngular1 = (chargeMagOne*magneticField) / p1['mass']
            velAngular2 = (chargeMagTwo*magneticField) / p2['mass']
            velAngular3 = (chargeMagThree*magneticField) / p3['mass']
            
            # Se inicializan los radios
            radiusOne = velocityOne/velAngular1
            radiusTwo = velocityTwo/velAngular2
            radiusThree = velocityThree/velAngular3
            
            # Si la carga es distinta de 0 el radio se puede calcular...
            if chargeMagOne > 0:
                radiusOne = (p1['mass']*velocityOne)/(chargeMagOne*magneticField)
            if chargeMagTwo > 0:
                radiusTwo = (p2['mass']*velocityTwo)/(chargeMagTwo*magneticField)
            if chargeMagThree > 0:
                radiusThree = (p3['mass']*velocityThree)/(chargeMagThree*magneticField)
                
             
            #Coordenadas de la primera particula
            p1ZPos = []
            p1XPos = []
            
            #Coordenadas de la segunda particula
            p2ZPos = []
            p2XPos = []
            
            #Coordenadas de la tercera particula
            p3ZPos = []
            p3XPos = []
            
            
            # Se calcula la trayectoria de la particula 1
            medioPeriodo = (2*math.pi)/(velAngular1*2)
            medioPeriodo = round(medioPeriodo)
            
            for i in range(10):
                x = radiusOne*math.sin(velAngular1*(i/1000))
                y = radiusOne*math.cos(velAngular1*(i/1000))
                
                p1ZPos.append(x)
                p1XPos.append(y)
            
            # Se calcula la trayectoria de la particula 2
            medioPeriodo = (2*math.pi)/(velAngular2*2)
            medioPeriodo = round(medioPeriodo)
            
            for i in range(10):
                x = radiusTwo*math.sin(velAngular2*(i/1000))
                y = radiusTwo*math.cos(velAngular2*(i/1000))
                
                p2ZPos.append(x)
                p2XPos.append(y)
                
            # Se calcula la trayectoria de la particula 3
            medioPeriodo = (2*math.pi)/(velAngular3*2)
            medioPeriodo = round(medioPeriodo)
            
            for i in range(10):
                x = radiusThree*math.sin(velAngular3*(i/1000))
                y = radiusThree*math.cos(velAngular3*(i/1000))
                
                p3ZPos.append(x)
                p3XPos.append(y)
            
            
            
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
                    mass = (protones * 1.6725e-27) + (neutrones * 1.6750e-27) + (electrones * 9.1091e-31)
                    charge = (protones * 1.602e-19) + (neutrones * 0) + (electrones * -1602e-19)
                    particles.append({'name':nombre, 'mass': mass, 'charge':charge})
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




    