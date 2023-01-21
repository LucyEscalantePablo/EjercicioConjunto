# union de 3 conjuntos
print('***********************')
print('La union de 3 conjuntos')
print('***********************\n')

conjuntoA = {1,2,3,4,5,6,7}
conjuntoB = {4,5,6,8,9,11,0}
conjuntoC = {4,5,1,6,13,15}

print(f'conjunto A {conjuntoA}')
print(f'conjunto B {conjuntoB}')
print(f'conjunto C {conjuntoC}')

unionABC = conjuntoA | conjuntoB | conjuntoC
print(f'\nLa unión de los 3 conjuntos A, B, C es : {unionABC}')

# interseccion de 3 conjuntos

print('\n***********************')
print('La interseccion de 3 conjuntos')
print('***********************\n')

intresecionABC = conjuntoA & conjuntoB & conjuntoC
print(f'La intercción de los 3 conjuntos A, B, C es: {intresecionABC}')

# Diferencia de 3 conjuntos

print('\n***********************')
print('La diferencia de 3 conjuntos')
print('***********************\n')

diferenciaABC = conjuntoA - conjuntoB and conjuntoA - conjuntoC
print(f'La diferencia de A, es decir solo el conjunto A menos B, C {diferenciaABC}')
