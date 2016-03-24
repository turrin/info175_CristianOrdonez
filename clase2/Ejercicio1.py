def los_multiplos (size):
	lis=[]
	for x in range(1, size+1):
		if (x%3==0 and x%7==0):
			lis.append(x)

	return lis

if __name__ == "__main__":
	s=raw_input("ingrese un numero:")

	print (los_multiplos(int(s)))