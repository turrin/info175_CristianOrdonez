print "hola"
def compara (x,y):
	if (x>y):
		return x," mayor que ",y
	elif(x<y):
		return x," menor que ",y
	else:
		return "son iguales"


if __name__ == "__main__":
	x= input ("ingrese un numero ")
	y= input ("ingtrese un segundo numero ")

	print(compara(x,y))

