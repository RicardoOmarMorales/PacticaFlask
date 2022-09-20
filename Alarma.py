from email.policy import strict
from sqlite3 import Row
from struct import pack
from tkinter import *
from tkinter.tix import COLUMN

def agregar_Sensor():
    print ("Hola")

def elimina_Sensor():
    print("Chau")

#Dibuja la ventana
ventana = Tk()
ventana.title("Alarma Monitoriada")
ventana.geometry("400x400")

#Coloca títulos




tiposensor = Label(ventana,text="Tipo de sensor: ")
ubsensor = Label(ventana,text="Ubicación: ")

#Coloca caja de texto
tipo = Entry(ventana)
ubicacion = Entry(ventana)


#ubica títulos, cajas de textos y botones
tiposensor.grid(row=0,column=0, padx=6,pady=6)
ubsensor.grid(row=1,column=0, padx=6,pady=6)
tipo.grid(row=0,column=1, padx=6,pady=6)
ubicacion.grid(row=1,column=1)
#Coloca los botones de Sensores
Add_Sensor = Button(ventana, text="Agregar Sensor",bg="green", command=agregar_Sensor)
Add_Sensor.grid(row=3,column=0)
#
Del_Sendor = Button(ventana, text="Eliminar Sensor", bg="red",command=elimina_Sensor)
Del_Sendor.grid(row=3, column=1)


ventana.mainloop()