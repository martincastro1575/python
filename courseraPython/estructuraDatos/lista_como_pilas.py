#Last in first out (LIFO)

stack = [1,2,3,4,5]

#Ingresando elementos a la pila
stack.append(7) #[1,2,3,4,5,7]
stack.append(10) #[1,2,3,4,5,7,10]

#Sacando elemento de la pila
stack.pop() ##[1,2,3,4,5,7]
stack.pop() ##[1,2,3,4,5]
stack.pop() ##[1,2,3,4]

