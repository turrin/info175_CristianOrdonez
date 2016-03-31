from Tkinter import *
import string
import sys
v = Tk()
v.title("Encriptador 2.0.4")
v.geometry("400x450")



def jaja(entrada):
	if(op.get()==1):
		resultadoEncrip.set(encrypt1(entrada,op2.get()))
	elif(op.get()==2):
		resultadoEncrip.set(encrypt2(entrada))


def encrypt1 (palabra,N):

	N=int(N)
	palabra=palabra.lower()
	s=string.ascii_lowercase
	nuevaPalabra=""
	
	for letra in palabra:
		i=0;
		for letra2 in s:
			if letra ==letra2:
				if N+i>=26:
					j=N+i-26
					nuevaPalabra=nuevaPalabra+s[j]
				else:
					nuevaPalabra=nuevaPalabra+s[i+N]
			else:
				i=i+1
	return nuevaPalabra		
def encrypt2 (frase):
	frase=frase.lower()
	cenit=["c","e","n","i","t"]
	polar=["p","o","l","a","r"]
	n=["b","d","f","g","h","j","k","m","q","s","u","v","w","x","y","z"," "]
	nuevaPalabra=""
	
	for letra in frase:
		i=0
		for letra2 in cenit:
			if letra ==letra2:
				nuevaPalabra=nuevaPalabra+polar[i]
				
			else:
				i=i+1
		j=0
		for letra2 in polar:
			if letra ==letra2:
				nuevaPalabra=nuevaPalabra+cenit[j]
				
			else:
				j=j+1
		k=0
		for letra2 in n:
			if letra ==letra2:
				nuevaPalabra=nuevaPalabra+n[k]
				
			else:
				k=k+1
		
	return nuevaPalabra			





n=StringVar()
resultadoEncrip=StringVar()

op=IntVar()
op2=IntVar()

ingresetexto=Label(v,text="Ingrese un texto a encriptar: ")
ingresetexto.place(x=20, y=20)
########################
entrada=Entry(v,textvar=n)
entrada.place(x=20, y =40)
####################
selecEncriptacion=Label(v,text="Seleccione metodo de encriptacion:")
selecEncriptacion.place(x=20,y=70)
cesar=Radiobutton(v,text="cesar",value=1,variable=op)
cesar.place(x=20, y=90)
cenitp=Radiobutton(v,text="cenit/polar",value=2,variable=op)
cenitp.place(x=100, y=90)
selecSalto=Label(v,text="Indique el salto para encriptacion cesar:")
selecSalto.place(x=20, y=130)
barra=Spinbox(v,from_=1,to=1000,textvariable=op2)
barra.place(x=100,y=160)
texResp=Label(v,text="Texto Encriptado:")
texResp.place(x=20,y=190)
respuesta=Label(v,textvariable=resultadoEncrip)
respuesta.place(x=20, y=220)


boton1=Button(v,text="Encriptar",command=lambda:jaja(n.get(),))
boton1.place(x=300,y=145)

v.mainloop()

