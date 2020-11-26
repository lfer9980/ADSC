from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image
import os

V2_1 = None
v2_2 = None
V2 = None

def cerrar():
    try:
        V2_1.destroy()
    except:
        pass
    main_window.destroy()

def siguiente_v2_3():
    pass

def siguiente_v2_2():
    global V2_2

    V2_1.destroy()
    V2_2 = Frame(main_window, bg = "black")
    V2_2.grid(row = 0,column = 0)

    #elementos de la pantalla 3
    V2_lpaso1 = Label(
        V2_2,
        text = "Paso 1: Vamos a identificar los sintomas del paciente. \n Por Favor seleccione SOLO UNA opcion:",
        bg = "black",
        fg = "DarkOrange",
        font = ("Verdana regular", 40))
    V2_lpaso1.grid(
        row = 0,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20) 

    #pregunta 13
    V2_l13 = Label(
        V2_2, 
        text = "El paciente presenta peritonitis? \n(considerar aborto en condiciones no esteriles)",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l13.grid(
        row = 4,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 13
    p13_varSi = IntVar ()
    p13_varNo = IntVar ()

    #respuestas de pregunta 13
    cb_p13_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p13_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p13_Si.grid(
        row = 5,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p13_No = Checkbutton (
        V2_2,
        text = "A) NO",
        variable = p13_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p13_No.grid(
        row = 6,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #pregunta 14
    V2_l14 = Label(
        V2_2, 
        text = "El paciente presenta alguna infeccion cutanea? \n(estreptococos o estafilococos)",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l14.grid(
        row = 4,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 14
    p14_varSi = IntVar ()
    p14_varNo = IntVar ()

    #respuestas de pregunta 8
    cb_p14_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p14_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p14_Si.grid(
        row = 5,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p14_No = Checkbutton (
        V2_2,
        text = "A) NO",
        variable = p14_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p14_No.grid(
        row = 6,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    #pregunta 15
    V2_l15 = Label(
        V2_2, 
        text = "El paciente presenta una infeccion gangrenosa?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l15.grid(
        row = 7,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 15
    p15_varSi = IntVar ()
    p15_varNo = IntVar ()

    #respuestas de pregunta 15
    cb_p15_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p15_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p15_Si.grid(
        row = 8,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p15_No = Checkbutton (
        V2_2,
        text = "A) NO",
        variable = p15_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p15_No.grid(
        row = 9,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    #pregunta 16
    V2_l16 = Label(
        V2_2, 
        text = "El paciente presenta fiebre alta?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l16.grid(
        row = 7,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 16
    p16_varSi = IntVar ()
    p16_varNo = IntVar ()

    #respuestas de pregunta 16
    cb_p16_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p16_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p16_Si.grid(
        row = 8,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p16_No = Checkbutton (
        V2_2,
        text = "A) NO",
        variable = p16_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p16_No.grid(
        row = 9,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    #pregunta 17
    V2_l17 = Label(
        V2_2, 
        text = "El paciente presenta estasis sanguinea?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l17.grid(
        row = 10,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 17
    p17_varSi = IntVar ()
    p17_varNo = IntVar ()

    #respuestas de pregunta 17
    cb_p17_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p17_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p17_Si.grid(
        row = 11,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p17_No = Checkbutton (
        V2_2,
        text = "A) NO",
        variable = p17_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p17_No.grid(
        row = 12,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #buton siguiente ventana 3
    V2_b3 = Button (
        V2_2,
        text = "Siguiente", 
        command = V3,
        bg = "#C2353B",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b3.grid(
        row = 13,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)

def siguiente_v2_1():
    global V2_1

    V2.destroy()
    V2_1 = Frame(main_window, bg = "black")
    V2_1.grid(row = 0,column = 0)

    #elementos de la pantalla 2
    V2_lpaso1 = Label(
        V2_1,
        text = "Paso 1: Vamos a identificar los sintomas del paciente. \n Por Favor seleccione SOLO UNA opcion:",
        bg = "black",
        fg = "DarkOrange",
        font = ("Verdana regular", 40))
    V2_lpaso1.grid(
        row = 0,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20) 

    #pregunta 7
    V2_l7 = Label(
        V2_1, 
        text = "Presenta quemaduras graves?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l7.grid(
        row = 4,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 7
    p7_varSi = IntVar ()
    p7_varNo = IntVar ()

    #respuestas de pregunta 7
    cb_p7_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p7_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p7_Si.grid(
        row = 5,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p7_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p7_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p7_No.grid(
        row = 6,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #pregunta 8
    V2_l8 = Label(
        V2_1, 
        text = "El paciente presenta sudoracion excesiva, diarrea o vomitos?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l8.grid(
        row = 4,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 8
    p8_varSi = IntVar ()
    p8_varNo = IntVar ()

    #respuestas de pregunta 8
    cb_p8_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p8_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p8_Si.grid(
        row = 5,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p8_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p8_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p8_No.grid(
        row = 6,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    #pregunta 9
    V2_l9 = Label(
        V2_1, 
        text = "El paciente fue sometido a anestesia general o espinal?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l9.grid(
        row = 7,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 9
    p9_varSi = IntVar ()
    p9_varNo = IntVar ()

    #respuestas de pregunta 9
    cb_p9_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p9_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p9_Si.grid(
        row = 8,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p9_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p9_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p9_No.grid(
        row = 9,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    #pregunta 10
    V2_l10 = Label(
        V2_1, 
        text = "El paciente presenta alguna contusion en el craneo?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l10.grid(
        row = 7,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 10
    p10_varSi = IntVar ()
    p10_varNo = IntVar ()

    #respuestas de pregunta 10
    cb_p10_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p10_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p10_Si.grid(
        row = 8,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p10_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p10_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p10_No.grid(
        row = 9,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    #pregunta 11
    V2_l11 = Label(
        V2_1, 
        text = "El paciente es alergico a alguna sustancia?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l11.grid(
        row = 9,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 11
    p11_varSi = IntVar ()
    p11_varNo = IntVar ()

    #respuestas de pregunta 11
    cb_p11_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p11_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p11_Si.grid(
        row = 10,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p11_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p11_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p11_No.grid(
        row = 11,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #pregunta 12
    V2_l12 = Label(
        V2_1, 
        text = "El paciente fue sometido a una inyeccion de histamina?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l12.grid(
        row = 9,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 12
    p12_varSi = IntVar ()
    p12_varNo = IntVar ()

    #respuestas de pregunta 12
    cb_p12_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p12_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p12_Si.grid(
        row = 10,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p12_No = Checkbutton (
        V2_1,
        text = "A) NO",
        variable = p12_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p12_No.grid(
        row = 11,
        column = 2,
        sticky = 'NSW',
        pady = 5)


    #buton siguiente ventana 2
    V2_b2 = Button (
        V2_1,
        text = "Siguiente", 
        command = siguiente_v2_2,
        bg = "#C2353B",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b2.grid(
        row = 12,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)
  
def v2():
    global V2
    #pantalla 2
    V2 = Frame(main_window, bg = "black")
    V2.grid(row = 0,column = 0)
    main_window.grid_columnconfigure(0, weight = 1)

    #elementos de la pantalla 2
    V2_lpaso1 = Label(
        V2,
        text = "Paso 1: Vamos a identificar los sintomas del paciente. \n Por Favor seleccione SOLO UNA opcion:",
        bg = "black",
        fg = "DarkOrange",
        font = ("Verdana regular", 40))
    V2_lpaso1.grid(
        row = 0,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20)

    #pregunta 1
    V2_l1 = Label(
        V2, 
        text = "Cuanto TIEMPO ha pasado desde que ingreso a urgencias?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l1.grid(
        row = 1,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)
    #variables preguntas 1
    p1_var1 = IntVar ()
    p1_var2 = IntVar ()
    p1_var3 = IntVar ()
    p1_var4 = IntVar ()
    p1_var5 = IntVar ()
    p1_var6 = IntVar ()

    #respuestas de pregunta 1
    cb_p1_1 = Checkbutton (
        V2,
        text = "A) entre 0 y 10 minutos",
        variable = p1_var1,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_1.grid(
        row = 2,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p1_2 = Checkbutton (
        V2,
        text = "B) entre 10 y 20 minutos",
        variable = p1_var2,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_2.grid(
        row = 3,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p1_3 = Checkbutton (
        V2, text = "C) entre 20 y 30 minutos",
        variable = p1_var3,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_3.grid(
        row = 4,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p1_4 = Checkbutton (
        V2,
        text = "D) entre 30 y 40 minutos",
        variable = p1_var4,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_4.grid(
        row = 2,
        column = 1,
        sticky = 'NSW',
        pady = 5)

    cb_p1_5 = Checkbutton (
        V2,
        text = "E) entre 40 y 50 minutos",
        variable = p1_var5,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_5.grid(
        row = 3,
        column = 1,
        sticky = 'NSW',
        pady = 5)

    cb_p1_6 = Checkbutton (
        V2,
        text = "F) mas de 50 minutos",
        variable = p1_var6,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p1_6.grid(
        row = 4,
        column = 1,
        sticky = 'NSW',
        pady = 5)

    #pregunta 2
    V2_l2 = Label(
        V2, 
        text = "Cual es el gasto cardiaco? (LATIDOS POR MIN x 70)",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l2.grid(
        row = 1,
        column = 2,
        columnspan = 2,
        sticky = "NW",
        pady = 10)

    #variables preguntas 2
    p2_var1 = IntVar ()
    p2_var2 = IntVar ()
    p2_var3 = IntVar ()
    p2_var4 = IntVar ()
    p2_var5 = IntVar ()

    #checkbox pregunta 2
    cb_p2_1 = Checkbutton (
        V2,
        text = "A) arriba de 5000 ml/min",
        variable = p2_var1,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p2_1.grid(
        row = 2 ,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    cb_p2_2 = Checkbutton (
        V2,
        text = "B) entre 3750 y 5000 ml/min",
        variable = p2_var2,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p2_2.grid(
        row = 3,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    cb_p2_3 = Checkbutton (
        V2,
        text = "C) entre 2500 y 3750 ml/min",
        variable = p2_var3,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p2_3.grid(
        row = 4,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    cb_p2_4 = Checkbutton (
        V2,
        text = "D) entre 1250 y 2500 ml/min",
        variable = p2_var4,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p2_4.grid(
        row = 2,
        column = 3,
        sticky = 'NSW',
        pady = 5)

    cb_p2_5 = Checkbutton (
        V2,
        text = "E) menor a 1250 ml/min",
        variable = p2_var5,
        onvalue = 1,
        offvalue = 0,
        justify = LEFT,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p2_5.grid(
        row = 3,
        column = 3,
        sticky = 'NSW',
        pady = 5)


    #pregunta 3
    V2_l3 = Label (
        V2,
        text = "Cual es la presion ARTERIAL actual?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 18))
    V2_l3.grid(
        row = 5,
        column = 0,
        columnspan = 2,
        sticky = 'NW',
        pady = 10)

    #variables preguntas 3
    p3_var1 = IntVar ()
    p3_var2 = IntVar ()
    p3_var3 = IntVar ()
    p3_var4 = IntVar ()

    #checkbox pregunta 3
    cb_p3_1 = Checkbutton (
        V2, 
        text = "A) 120 mmHg o mas",
        variable = p3_var1,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p3_1.grid(
        row = 6,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p3_2 = Checkbutton (
        V2,
        text = "B) entre 90 y 120 mmHg",
        variable = p3_var2,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p3_2.grid(
        row = 7,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p3_3 = Checkbutton (
        V2,
        text = "C) entre 60 y 90 mmHg",
        variable = p3_var3,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p3_3.grid(
        row = 8,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    cb_p3_4 = Checkbutton (
        V2,
        text = "D) menor a 45 mmHg",
        variable = p3_var4,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p3_4.grid(
        row = 6,
        column = 1,
        sticky = 'NSW',
        pady = 5)


    #pregunta 4
    V2_l4 = Label (
        V2,
        text = "Presenta hemorragia visible?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 18))
    V2_l4.grid(
        row = 5,
        column = 2,
        sticky = 'NW',
        pady = 10)

    #variables preguntas 4
    p4_varSi = IntVar ()
    p4_varNo = IntVar ()

    #checkbox pregunta 4
    cb_p4_Si = Checkbutton (
        V2,
        text = "A) SI",
        variable = p4_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p4_Si.grid(
        row = 6,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    cb_p4_No = Checkbutton (
        V2,
        text = "A) NO",
        variable = p4_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p4_No.grid(
        row = 7,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    #pregunta 5
    V2_l5 = Label(
        V2, 
        text = "Presenta perdida de plasma?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l5.grid(
        row = 8,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 5
    p5_varSi = IntVar ()
    p5_varNo = IntVar ()

    #respuestas de pregunta 5
    cb_p5_Si = Checkbutton (
        V2,
        text = "A) SI",
        variable = p5_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p5_Si.grid(
        row = 9,
        column = 0,
        sticky = 'NSW',
        pady = 5)
    
    cb_p5_No = Checkbutton (
        V2,
        text = "A) NO",
        variable = p5_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p5_No.grid(
        row = 10,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #pregunta 6
    V2_l6 = Label(
        V2, 
        text = "Presenta alguna obstruccion intestinal?",
        bg = "black",
        fg = "#2188C2",
        justify = LEFT,
        font = ("Verdana regular", 15))
    V2_l6.grid(
        row = 8,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #variables pregunta 6
    p6_varSi = IntVar ()
    p6_varNo = IntVar ()

    #respuestas de pregunta 6
    cb_p6_Si = Checkbutton (
        V2,
        text = "A) SI",
        variable = p6_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p6_Si.grid(
        row = 9,
        column = 2,
        sticky = 'NSW',
        pady = 5)
    
    cb_p6_No = Checkbutton (
        V2,
        text = "A) NO",
        variable = p6_varNo,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        font = ("Verdana bold", 15),
        command = "")
    cb_p6_No.grid(
        row = 10,
        column = 2,
        sticky = 'NSW',
        pady = 5)

    #buton siguiente ventana 2
    V2_b1 = Button (
        V2,
        text = "Siguiente", 
        command = siguiente_v2_1,
        bg = "#C2353B",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b1.grid(
        row = 11,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)


#creando la pantalla principal
main_window = Tk()
main_window.title("ADSC")
main_window.geometry('1920x1080')
main_window.wm_protocol("WM_DELETE_WINDOW", cerrar)
main_window.config(bg = 'black')
v2()


if __name__ == "__main__":
    main_window.mainloop()
    