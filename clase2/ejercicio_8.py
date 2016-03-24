import string
def encrypt (N):
	palabra= raw_input("ingrese una palabra: ")
	palabra=palabra.lower()
	s=string.ascii_lowercase
	nuevaPalabra=""
	
	for letra in palabra:
		i=0;
		for letra2 in s:
			if letra ==letra2:
				nuevaPalabra=nuevaPalabra+s[i+N]
			else:
				i=i+1
	return nuevaPalabra			


if __name__ == "__main__":
	N=raw_input("ingrese un numero:")
print (encrypt(int(N)))

