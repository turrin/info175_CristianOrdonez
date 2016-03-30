import string
def encrypt (palabra,N):

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


if __name__ == "__main__":
	N=raw_input("ingrese un numero:")
	p= raw_input("ingrese una palabra: ")
print (encrypt(p, int(N)))

