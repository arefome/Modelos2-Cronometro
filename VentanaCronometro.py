import tkinter as tk
from tkinter import Tk,Label,Button,Frame
from Cronometro import Cronometro
from tkinter.constants import BOTTOM


class VentanaCronometro():
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.geometry('500x200')
        self.ventana.resizable(0, 0)
        self.ventana.title('Cronometro')
        self.ventana.config(background = '#72a922')
        self.cronometro_label = tk.Label(text="", font=('Tahoma', 44), fg='#ffffff', bg='#1f2f3f', pady=10, padx=10)
        self.cronometro_label.place(x=20, y=30)
        self.cronometro = Cronometro()
        self.activo = True
        self.frame = Frame(self.ventana)
        self.cronometro_label.configure(text = self.cronometro.mostrarTiempo())
        self.btnIniciar = Button(self.frame, fg='blue', text='Iniciar', command = self.actualizar)
        self.btnIniciar.grid(row=1, column=1)
        self.btnParar = Button(self.frame, fg='blue', text='Parar', command=self.parar)
        self.btnParar.grid(row=1, column=2)
        btnReiniciar = Button(self.frame, fg='blue', text='Reiniciar', command=self.reiniciar)
        btnReiniciar.grid(row=1, column=3)
        self.frame.pack(side = BOTTOM)
        self.ventana.mainloop()
        
    def actualizar(self):
        global proceso
        self.cronometro.iniciar()
        self.cronometro_label.configure(text = self.cronometro.mostrarTiempo())
        proceso = self.ventana.after(10, self.actualizar)
        self.btnIniciar.grid_forget()
    
    def parar(self):
        global proceso
        self.cronometro.detener()
        self.ventana.after_cancel(proceso)
        if self.activo:
            self.btnParar.configure(text = 'Reanudar')
            self.activo = False
        else:
            self.btnParar.configure(text = 'Parar')
            self.activo = True
            proceso = self.ventana.after(10, self.actualizar)
    
    def reiniciar(self):
        global proceso
        self.cronometro.reiniciar()
        self.ventana.after_cancel(proceso)
        self.cronometro_label.configure(text = self.cronometro.mostrarTiempo())
        self.btnIniciar.grid(row=1,column=1)
        self.frame.pack(side=BOTTOM)
        
main = VentanaCronometro()