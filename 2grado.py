import math
def secondogrado(a,b,c):
	a,b,c = input("inserisci i tre paramentri dell'equazione:")
	delta = (b**2 - 4*a*c)
	if delta >= 0:
		x1= (-b + math.sqrt(delta))/(2*a)
		x2= (-b - math.sqrt(delta))/(2*a)
		print x1, x2
	else:
		print "Nessuna soluzione reale"
		 


secondogrado(1,4,4)
