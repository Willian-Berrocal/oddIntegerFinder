# Este programa identifica el entero que aparece un numero impar de veces en una lista
# Solo habra un entero que aparece un numero impar de veces, los demas apareceran un numero par de veces
# El programa recorre la lista una sola vez, e incluso ignora los valores que ya revisó, gracias a la lista revised
# El tiempo de ejecucion es O(ñ), siendo ñ no el size de la lista sino el numero de enteros diferentes dentro de ella

seq = [1, 0, 1, 0, 0]
# seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
# seq = [1,1,2,-2,5,2,4,4,-1,-2,5]

revised = []
for elem in seq:
    if elem not in revised:
        if seq.count(elem) % 2 == 1:
            print(elem)
            break
        else:
            revised.append(elem)
