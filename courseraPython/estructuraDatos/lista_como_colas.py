from collections import deque #Libreria para implementacion de cola de forma eficiente


#Primero en entrar primero en salir (FIFO)


#lista como cola
queue = [1,2,3]

#Se puede agregar a la cola de esta forma, pero  no es la manera mas eficiente
queue.append(4) #[1,2,3,4]
queue.append(7) #[1,2,3,4,7]

#Se puede agregar a la cola de esta forma, pero  no es la manera mas eficiente
queue.pop(0) ##[2,3,4,7]
queue.pop(0) ##[3,4,7]


#Colas implementadas de manera eficiente con libreria estandar
queue = deque([1,2,3])

#Agrego elementos
queue.append(10) #[1,2,3,10]
queue.append(12) #[1,2,3,10,12]

#Elimino elementos
queue.popleft() #[2,3,10,12]
queue.popleft() #[3,10,12]

