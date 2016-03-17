if __name__ == '__main__':
	lineas= ""
	actual= raw_input("ingrese una frase ")
	while actual:
		lineas+=actual.upper()
		lineas+= "\n"
		actual= raw_input("ingrese una frase ")

	print lineas