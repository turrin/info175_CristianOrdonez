import string
def encrypt (frase):
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


if __name__ == "__main__":
	p= raw_input("ingrese una fese: ")
print encrypt(p)
