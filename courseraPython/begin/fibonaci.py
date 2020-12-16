def fib(n):
    a, b = 0,1

    for value in range(1,n):
        a, b = b, a + b 
    
    print("\nTotal", b)
    

fib(35) 