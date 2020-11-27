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
            
            # Se calcula la trayectoria de las particulas (un semicirculo o una linea recta)
            counter = 0
            
            while counter < 180:
                
                #Se calculan las coordenadas de la primera particula
                if velocityOne == electricField/magneticField or radiusOne == 0:
                    xcoord = counter
                    ycoord = 0
                    p1ZPos.append(xcoord)
                    p1XPos.append(ycoord)
                else:
                    xcoord = abs(radiusOne * math.cos(math.radians(counter-90)))
                    ycoord = radiusOne * math.sin(math.radians(counter-90)) + radiusOne
                    if p1['charge'] < 0 and magneticField > 0:
                        ycoord = -ycoord
                    elif p1['charge'] > 0 and magneticField < 0:
                        ycoord = -ycoord
                    p1ZPos.append(xcoord)
                    p1XPos.append(ycoord)
                
                #Coordenadas de la segunda particula
                if velocityTwo == electricField/magneticField or radiusTwo == 0:
                    xcoord = counter
                    ycoord = 0
                    p2ZPos.append(xcoord)
                    p2XPos.append(ycoord)
                else:
                    xcoord = abs(radiusTwo * math.cos(math.radians(counter-90)))
                    ycoord = radiusTwo * math.sin(math.radians(counter-90)) + radiusTwo
                    if p2['charge'] < 0 and magneticField > 0:
                        ycoord = -ycoord
                    elif p2['charge'] > 0 and magneticField < 0:
                        ycoord = -ycoord
                    p2ZPos.append(xcoord)
                    p2XPos.append(ycoord)
                
                #Coordenadas de la tercera particual
                if velocityThree == electricField/magneticField or radiusThree == 0:
                    xcoord = counter
                    ycoord = 0
                    p3ZPos.append(xcoord)
                    p3XPos.append(ycoord)
                else:
                    xcoord = abs(radiusThree * math.cos(math.radians(counter-90)))
                    ycoord = radiusThree * math.sin(math.radians(counter-90)) + radiusThree
                    if p3['charge'] < 0 and magneticField > 0:
                        ycoord = -ycoord
                    elif p3['charge'] > 0 and magneticField < 0:
                        ycoord = -ycoord
                    p3ZPos.append(xcoord)
                    p3XPos.append(ycoord)
                    
                # Se asigna el offset (que tan separados estan los datos)
                counter += 5
            
            # Se crea una figura (ventana) que contendra una fila y tres columnas
            fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
            fig.suptitle('Particles\' Trajectory', color='white')
            fig.patch.set_facecolor('#012168')
            
            # Se personaliza el gráfico 1
            ax1.plot(p1ZPos,p1XPos, 'r-o', label=p1['name'])
            ax1.legend(loc='upper right')
            ax1.set_xlabel('X Axis (m)')
            ax1.set_ylabel('Z Axis (m)')
            ax1.set_facecolor('black')
            ax1.spines['top'].set_color('red')
            ax1.spines['bottom'].set_color('red')
            ax1.spines['right'].set_color('red')
            ax1.spines['left'].set_color('red')
            ax1.xaxis.label.set_color('white')
            ax1.yaxis.label.set_color('white')
            ax1.tick_params(axis='x', colors='white')
            ax1.tick_params(axis='y', colors='white')

            # Se personaliza el gráfico 2
            ax2.plot(p2ZPos,p2XPos, 'b-o', label=p2['name'])
            ax2.legend(loc='upper right')
            ax2.set_xlabel('X Axis (m)')
            ax2.set_ylabel('Z Axis (m)')
            ax2.set_facecolor('black')
            ax2.spines['top'].set_color('blue')
            ax2.spines['bottom'].set_color('blue')
            ax2.spines['right'].set_color('blue')
            ax2.spines['left'].set_color('blue')
            ax2.xaxis.label.set_color('white')
            ax2.yaxis.label.set_color('white')
            ax2.tick_params(axis='x', colors='white')
            ax2.tick_params(axis='y', colors='white')
            
            # Se personaliza el gráfico 3
            ax3.plot(p3ZPos,p3XPos, 'y-o', label=p3['name'])
            ax3.legend(loc='upper right')
            ax3.set_xlabel('X Axis (m)')
            ax3.set_ylabel('Z Axis (m)')
            ax3.set_facecolor('black')
            ax3.spines['top'].set_color('yellow')
            ax3.spines['bottom'].set_color('yellow')
            ax3.spines['right'].set_color('yellow')
            ax3.spines['left'].set_color('yellow')
            ax3.xaxis.label.set_color('white')
            ax3.yaxis.label.set_color('white')
            ax3.tick_params(axis='x', colors='white')
            ax3.tick_params(axis='y', colors='white')
            
            # Se muestra la figura
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




    