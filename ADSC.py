from Tkinter import *
import tkMessageBox
from PIL import ImageTk, Image
import os

global V1,V2,V2_1, v2_2, V3, V4, V5, V5_l1, V5_l2, EV5_l1, EV5_l2, EV5_l3, EV5_l4

v_etapa = "etapa progresiva"
v_shock = "hemorragico"
main_window = None


def capturar_datos():
    global V1, V4, V5, EV5_l1, EV5_l2, EV5_l3, EV5_l4

    dato1 = EV5_l1.get()
    dato2 = EV5_l2.get()
    dato3 = EV5_l3.get()
    dato4 = EV5_l4.get()

    reporte = open("Reporte.txt", "w")

    reporte.write("INFORME MEDICO A. D. S. C.\n\n")
    reporte.write("Datos del paciente:\n\n")
    reporte.write("Edad: "+dato1+"\n")
    reporte.write("Sexo: "+dato2+"\n")
    reporte.write("Alergias: "+dato3+"\n")
    reporte.write("Antecedentes cardiovasculares: "+dato4)

    reporte.close()
    
    V5.destroy()


def v5():
    global V5, EV5_l1, EV5_l2, EV5_l3, EV5_l4
    
    #ventana5()
    V4.destroy()
    V5=Tk()
    V5.title("A.D.S.C.")
    V5.geometry("1920x1080")
    V5.config(bg="black", padx = 20)
    
    #texto titulo
    V5_lpaso4=Label(V5,text="Paso 4: Datos del paciente.", font=("Verdana regular",50),bg="black",fg="DarkOrange")
    V5_lpaso4.place(x=400, y=30)

    #texto instrucciones
    V5_lin=Label(V5,text="Ingresa los datos que se solicitan para el registro.",font=("Verdana regular",40),bg="black",fg="white")
    V5_lin.place(x=100, y=120)

    #Dato 1 texto.
    V5_l1=Label(V5,text="Edad:",font=("Verdana regular",20),bg="black",fg = "dodger blue")
    V5_l1.place(x=250, y=250)
    EV5_l1=Entry(V5,font=("Verdana regular",20))
    EV5_l1.place(x=250,y=310)
    EV5_l1.focus_set()

    #Dato 2 texto.
    V5_l2=Label(V5,text="Sexo:",font=("Verdana regular",20),bg="black",fg = "dodger blue")
    V5_l2.place(x=250, y=470)
    EV5_l2=Entry(V5,font=("Verdana regular",20))
    EV5_l2.place(x=250,y=530)
    EV5_l2.focus_set()

    #Dato 3 texto.
    V5_l3=Label(V5,text="Alergias:",font=("Verdana regular",20),bg="black",fg = "dodger blue")
    V5_l3.place(x=900, y=250)
    EV5_l3=Entry(V5,font=("Verdana regular",20))
    EV5_l3.place(x=900,y=310)
    EV5_l3.focus_set()

    #Dato 4 texto.
    V5_l4=Label(V5,text="Antecedentes \nvasculares:",font=("Verdana regular",20),bg="black",fg = "dodger blue")
    V5_l4.place(x=900, y=430)
    EV5_l4=Entry(V5,font=("Verdana regular",20))
    EV5_l4.place(x=900,y=530)
    EV5_l4.focus_set()

    #botton Terminado.
    V5_b1 =Button(V5, text="Terminado",font=("Verdana regular",25), bg="red3", fg="white", command = capturar_datos)
    V5_b1 .place(x=700, y=700)

    V5.mainloop()


def v4():
    global V4, v_etapa, v_shock

    v_in1 = None
    v_in2 = None
    v_in3 = None
    v_in4 = None
    
    V3.destroy() 
    V4=Tk()
    V4.title("A.D.S.C.")
    V4.geometry("1920x1080")
    V4.config(bg="black")


    V4_lpaso3 = Label(V4, text = 'Paso 3: DIAGNOSTICO', font = ("Verdana regular",40), bg = "black", fg = "DarkOrange").place(x = 400, y = 30) #texto paso 3

    V4_l5 = Label(V4, text = 'Esperamos haberte sido de ayuda.', font = ("Verdana regular", 20, 'bold'), bg = "black", fg = "white").place(x = 450, y = 620) #texto Esperamos haberte sido de ayuda

    V4_b1 = Button(V4, text = 'Finalizar', command = v5, font = ("Verdana regular",18), bg = "red3", fg = "white").place(x = 700, y = 700) #Boton Finalizar

    if (v_etapa == 'etapa progresiva'):

        V4_lin = Label(V4, text = 'Por favor sigue las instrucciones:', font = ("Verdana regular",20), bg = "black", fg = "white").place(x = 100, y = 120) #texto Sigue las instrucciones

        if (v_shock == 'hemorragico'):

            v_in1 = 'Transfusion sanguinea.'
            v_in2 = 'Elevar los pies del paciente 30 cm por encima de su cabeza.'
            v_in3 = 'Administrar oxigeno al paciente.'
            v_in4 = 'Aplicar una dosis de glucocorticoides al paciente.'

            V4_l1 = Label(V4, text = '1. ' + v_in1, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 220) #texto Instruccion 1
            V4_l2 = Label(V4, text = '2. ' + v_in2, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 320) #texto Instruccion 2
            V4_l3 = Label(V4, text = '3. ' + v_in3, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 420) #texto Instruccion 3
            V4_l4 = Label(V4, text = '4. ' + v_in4, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 520) #texto Instruccion 4

        elif (v_shock == 'hipovolemico'):

            v_in1 = 'Transfucion de plasma.'
            v_in2 = 'Sustitutos de plasma (Dextrano).'
            v_in3 = 'Aplicar una dosis de glucocorticoides al paciente.'

            V4_l1 = Label(V4, text = '1. ' + v_in1, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 220) #texto Instruccion 1
            V4_l2 = Label(V4, text = '2. ' + v_in2, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 320) #texto Instruccion 2
            V4_l3 = Label(V4, text = '3. ' + v_in3, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 420) #texto Instruccion 3

        elif (v_shock == 'neurogeno' or v_shock == 'anafilactico'):

            v_in1 = 'Administrar farmacos simpaticomimeticos \ncomo Noradrenalina y adrenalina.'

            V4_l1 = Label(V4, text = '1. ' + v_in1, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 220) #texto Instruccion 1

        elif (v_shock == 'septico'):

            v_in1 = 'Administrar oxigeno al paciente.'
            v_in2 = 'Aplicar una dosis de glucocorticoides al paciente.'

            V4_l1 = Label(V4, text = '1. ' + v_in1, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 220) #texto Instruccion 1
            V4_l2 = Label(V4, text = '2. ' + v_in2, font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 320) #texto Instruccion 2

        else:

            V4_l2 = Label(V4, text = 'Lo sentimos, no tenemos informacion de tal shock', font = ("Verdana regular",18), bg = "black",fg = "dodger blue").place(x = 250, y = 320) #texto Instruccion 2

    elif (v_etapa == 'etapa irreversible'):

        V4_lin = Label(V4, text = 'El paciente no cumple con los requerimentos \npara ser salvado', font = ("Verdana regular",30), bg = "black", fg = "red3").place(x = 250, y = 300) #texto shock irreversible 
                 

def v3():
    global V3, v_etapa, v_shock
    
    main_window.destroy()
    V3=Tk()
    V3.title("A.D.S.C.")
    V3.geometry('1920x1080')
    V3.config(bg='black', padx = 40)


    #elementos de la pantalla 4
    V3_lpaso1 = Label(
        V3,
        text = "Paso 2: Identifiquemos la etapa del shock\nen la que se encuentra el paciente",
        bg = "black",
        fg = "DarkOrange",
        justify = CENTER,
        font = ("Verdana regular", 50))
    V3_lpaso1.grid(
        row = 0,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20) 
    
    V3_l1 = Label(
        V3,
        text ="El paciente se encuentra en:",
        font = ("Verdana regular",20),
        bg = "black",
        fg = "white")
    V3_l1.grid(
        row = 1,
        column = 0,
        sticky = 'NSW',
        pady = 20)

    V3_l2 = Label(
        V3,
        text = "ETAPA PROGRESIVA",
        font = ("Verdana regular",40),
        bg = "black",
        fg = "#46F881")
    V3_l2.grid(
        row = 2,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20)     

    V3_l3 = Label(
        V3,
        text = "El tipo de shock que presenta es:",
        font = ("Verdana regular",20),
        bg = "black",
        fg = "#FE2543")
    V3_l3.grid(
        row = 3,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20)    
    
    V3_l4 = Label(
        V3,
        text = "SHOCK HEMORRAGICO",
        font = ("Verdana regular",40),
        bg = "black",
        fg = "#FE2543")
    V3_l4.grid(
        row = 4,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20) 
    
    V3_l5 = Label(
        V3,
        text = "porfavor da clic en siguiente para conocer el diagnostico.",
        font = ("Verdana regular",20),
        bg = "black",
        fg = "white")
    V3_l5.grid(
        row = 5,
        column = 0,
        columnspan = 4,
        sticky = 'NESW',
        pady = 20) 


    #buton siguiente ventana 4
    V3_b1 = Button (
        V3,
        text = "Siguiente", 
        command = v4,
        bg = "red3",
        fg = "white",
        font = ("Verdana bold", 18))
    V3_b1.grid(
        row = 6,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)


def siguiente_v2_2():
    global V2_2

    V2_1.destroy()
    V2_2 = Frame(main_window, bg = "black")
    V2_2.grid(row = 0,column = 0)

    #variables pregunta 13
    p13_varSi = IntVar ()
    p13_varNo = IntVar ()
    #variables pregunta 14
    p14_varSi = IntVar ()
    p14_varNo = IntVar ()
    #variables pregunta 15
    p15_varSi = IntVar ()
    p15_varNo = IntVar ()
    #variables pregunta 16
    p16_varSi = IntVar ()
    p16_varNo = IntVar ()
    #variables pregunta 17
    p17_varSi = IntVar ()
    p17_varNo = IntVar ()

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
        padx = 10,
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

    #respuestas de pregunta 13
    cb_p13_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p13_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 8
    cb_p14_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p14_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 15
    cb_p15_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p15_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 16
    cb_p16_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p16_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 17
    cb_p17_Si = Checkbutton (
        V2_2,
        text = "A) SI",
        variable = p17_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
    cb_p17_No.grid(
        row = 12,
        column = 0,
        sticky = 'NSW',
        pady = 5)

    #buton siguiente ventana 3
    V2_b3 = Button (
        V2_2,
        text = "Siguiente", 
        command = v3,
        bg = "red3",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b3.grid(
        row = 14,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)


def siguiente_v2_1():
    global V2, V2_1

    V2.destroy()
    V2_1 = Frame(main_window, bg = "black")
    V2_1.grid(row = 0,column = 0)

    #variables pregunta 7
    p7_varSi = IntVar ()
    p7_varNo = IntVar ()
    #variables pregunta 8
    p8_varSi = IntVar ()
    p8_varNo = IntVar ()
    #variables pregunta 9
    p9_varSi = IntVar ()
    p9_varNo = IntVar ()
    #variables pregunta 10
    p10_varSi = IntVar ()
    p10_varNo = IntVar ()
    #variables pregunta 11
    p11_varSi = IntVar ()
    p11_varNo = IntVar ()
    #variables pregunta 12
    p12_varSi = IntVar ()
    p12_varNo = IntVar ()

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

    #respuestas de pregunta 7
    cb_p7_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p7_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 8
    cb_p8_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p8_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 9
    cb_p9_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p9_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 10
    cb_p10_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p10_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        row = 10,
        column = 0,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #respuestas de pregunta 11
    cb_p11_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p11_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
    cb_p11_Si.grid(
        row = 11,
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
    cb_p11_No.grid(
        row = 12,
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
        row = 10,
        column = 2,
        columnspan = 2,
        sticky = 'NSW',
        pady = 10)

    #respuestas de pregunta 12
    cb_p12_Si = Checkbutton (
        V2_1,
        text = "A) SI",
        variable = p12_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
    cb_p12_Si.grid(
        row = 11,
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
    cb_p12_No.grid(
        row = 12,
        column = 2,
        sticky = 'NSW',
        pady = 5)


    #buton siguiente ventana 2
    V2_b2 = Button (
        V2_1,
        text = "Siguiente", 
        command = siguiente_v2_2,
        bg = "red3",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b2.grid(
        row = 13,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)


def v2():
    global V2, v_etapa, v_shock, main_window
    #pantalla 2

    V1.destroy()
    main_window=Tk()
    main_window.title("A.D.S.C.")
    main_window.geometry('1920x1080')
    main_window.config(bg='black', padx = 40)

    V2= Frame(main_window, bg = "black")
    V2.grid(row = 0,column = 0)

    #variables preguntas 1
    p1_var1 = IntVar()
    p1_var2 = IntVar ()
    p1_var3 = IntVar ()
    p1_var4 = IntVar ()
    p1_var5 = IntVar ()
    p1_var6 = IntVar ()
    #variables preguntas 2
    p2_var1 = IntVar ()
    p2_var2 = IntVar ()
    p2_var3 = IntVar ()
    p2_var4 = IntVar ()
    p2_var5 = IntVar ()
    #variables preguntas 3
    p3_var1 = IntVar ()
    p3_var2 = IntVar ()
    p3_var3 = IntVar ()
    p3_var4 = IntVar ()
    #variables preguntas 4
    p4_varSi = IntVar ()
    p4_varNo = IntVar ()
    #variables pregunta 5
    p5_varSi = IntVar ()
    p5_varNo = IntVar ()
    #variables pregunta 6
    p6_varSi = IntVar ()
    p6_varNo = IntVar ()


    def etapa_shock():
        global v_etapa
        if (p1_var1.get() == 1) or (p1_var2.get() == 1) or (p1_var3.get() == 1) or (p1_var4.get() == 0) or (p1_var5.get() == 0) or (p1_var.get() == 0):
            if (p3_var1.get() == 1) or (p3_var2.get() == 1) or (p3_var3.get() == 1) or (p3_var4.get() == 0):
                v_etapa = "etapa progresiva"
            elif (p3_var1.get() == 0) or (p3_var2.get() == 0) or (p3_var3.get() == 0) or (p3_var4.get() == 1):
                v_etapa = "etapa irreversible"
        elif (p1_var1.get() == 0) or (p1_var2.get() == 0) or (p1_var3.get() == 0) or (p1_var4.get() == 1) or (p1_var5.get() == 1) or (p1_var.get() == 1):
                v_etapa = "etapa irreversible"


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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #checkbox pregunta 3
    cb_p3_1 = Checkbutton (
        V2, 
        text = "A) 120 mmHg o mas",
        variable = p3_var1,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #checkbox pregunta 4
    cb_p4_Si = Checkbutton (
        V2,
        text = "A) SI",
        variable = p4_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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

    #respuestas de pregunta 5
    cb_p5_Si = Checkbutton (
        V2,
        text = "A) SI",
        variable = p5_varSi,
        onvalue = 1,
        offvalue = 0,
        bg = "black",
        fg = "white",
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        selectcolor = "black",
        font = ("Verdana bold", 15))
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
        bg = "red3",
        fg = "white",
        font = ("Verdana bold", 18))
    V2_b1.grid(
        row = 11,
        column = 3,
        sticky = 'NESW',
        padx = 20,
        pady = 5)


def v1():
    global V1

    V1=Tk()
    V1.title('A. D. S. C.')
    V1.geometry('1920x1080')
    V1.config(bg='black')
    
    V1_l1 = Label (V1, text = 'Analisis Diagnostico de Shock Circulatorio', font = ('Verdana regular', 50, 'bold'), bg = 'black', fg = 'white').place(x = 70, y = 20) #texto titulo

    imgLogo = Image.open('logo.png')
    imgLogo = imgLogo.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(imgLogo)
    
    imgFon = Label (V1, image = img).place(x = 540, y = 90, width=440, height = 450)

    V1_l2 = Label (V1, text = 'Un proyecto para asistir a los medicos en el diagnostico y', font = ("Verdana regular", 25), bg = "black", fg = "white").place(x = 370, y = 540) #texto definicion
    V1_l2_2 = Label (V1, text = 'tratamiento del shock circulatorio.', font = ("Verdana regular", 25), bg = "black", fg = "white").place(x = 520, y = 580)
  
    V1_b1 = Button (V1, text = 'Empezar', command = v2, font = ("Verdana regular", 25), bg = "red3", fg = "white").place(x = 700, y = 650) #Boton empezar

    V2_l3 = Label (V1, text = 'Copyright 2020 A.D.S.C.', font = ('Verdana regular', 14, 'italic'), bg = 'black', fg = 'white').place(x = 670, y = 720) #texto copyright
    V2_l3_2 = Label (V1, text = 'Version 0.0.1 Build 55', font = ('Verdana regular', 14, 'italic'), bg = 'black', fg = 'white').place(x = 670, y = 750)

    V1.mainloop()


if __name__ == "__main__":
    v1()
    