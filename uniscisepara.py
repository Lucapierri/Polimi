'''Funzione che calcola le cifre di un numero'''
def nc(n):
	i=10			#divisore
	contatore=0 	#incrementa di 1 a ogni divisione
	while n >=1:	#divisone per 10
		n=n/i
		contatore=contatore+1
	return contatore
	


'''unisce i due numeri dati moltiplicando per dieci elevato al numero di cifre del secondo numero'''
def unisci(num1,num2):
	cifre=nc(num2)					#richiama la funzione nc
	return num1*(10**cifre)+num2	
	

'''funzione che separa un numero conoscendo le cifre del secondo'''
def separa1(numero,nc2):
	numero2=numero%(10**nc2)	#il resto della divisione  è il numero 2
	return numero2

''' funzione che separa un numero conoscendo le cifre del primo'''	
def separa2(numero,nc1):
	numero1=numero/(10**nc1)	#la parte intera della divisione è il numero 1
	return numero1


''' funzione riassuntiva che unisce e separa i due input(numeri)'''
def uniscisep(input1,input2):
	x1=unisci(input1,input2)	
	print x1
	x2=separa1(x1,nc(input2))
	x3=separa2(x1,nc(input1))
	print x2, ',',x3
	
uniscisep(13,23)	
	
	
	

