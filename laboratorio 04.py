def controlla(lista,numero):
	i=0
	while i < len(lista):
		if lista[i] == numero:
			print 1
			return 1
			
		i=i+1	
	print 0
	
#controlla([4,5,6],8)

def crescente(lista): 		#controlla se la lista e' ordinata
	i = 0
	lung = (len(lista))-1   #len parte da 0 quindi metto -1
	while i < lung:
		if not lista[i] < lista[i+1]:
			return False
		i=i+1
	return True

#crescente([1,2,5,4])


def decrescente(lista):
	i=0
	lung=(len(lista))-1
	while i < lung:
		 if not lista[i] > lista [i+1]:
			return False
		 i=i+1
	return True
	
#f([8,9,5,4])

def controllalista(lista):
	lista = input("Inserisci un vettore:")
	if crescente(lista)==True:
		return "e' crescente"
	if decrescente(lista)==True:
		return "e' decrescente"
	else:
		return "non e' ordinata"
		
print controllalista([5,4,3,2])

	




''' questa e' fatta dal professore'''
def controlla1(lista):
	crescente = 1
	decrescente = -1
	i = 0
	lung = (len(lista))-1   
	while i < lung:
		if(lista[i] < lista[i+1]):  
			decrescente = 0
		if(lista[i] > lista[i+1]):
			crescente = 0	
		i = i+1
	return crescente+decrescente
	
#print controlla1([4,3,2,1])

	




			
		

