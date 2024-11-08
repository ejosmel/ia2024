def separar_positivos_negativos(numeros): 
		numeros.sort()
negativos = [num for num in numeros if num < 0] 
positivos = [num for num in numeros if num >= 0] 
return negativos, positivos 
