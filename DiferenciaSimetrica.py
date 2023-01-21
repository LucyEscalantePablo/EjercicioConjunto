# Calcular la diferencia simétrica entre 2 conjuntos
print('*****************************************************')
print('Calculamos la diferencia simetrica de dos conjuntos: ')
print('*****************************************************\n')


conjuntoA = {'a','b','c','d'}
conjuntoB = {'a','c','e','f'}
print(f'conjunto A {conjuntoA}')
print(f'conjunto B {conjuntoB}')

diferenciSimetrica = conjuntoA ^ conjuntoB
print(f'\nLa diferencia simetrica entre el conjunto A y B es: {diferenciSimetrica}\n')