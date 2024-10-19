
def pattern1(num):
    for i in range(0, num):
        for j in range(0, num - i + 1):
            print(" ", end=" ")
        
        for j in range(2 * i + 1):
            print("*", end=" ")
        
        for j in range(0, num - i + 1):
            print(" ", end=" ")
        print("\n")
    
def pattern2(num):
    for i in range(0, num):
        for j in range(0, i):
            print(" ", end=" ")
        
        for j in range(2 * (num) - (2 * i + 1)):
            print("*", end=" ")
        
        for j in range(0, i):
            print(" ", end=" ")
        print("\n")

def pattern3(num):
    for i in range(0, num):
        for j in range(0, num - i + 1):
            print(" ", end=" ")
        
        for j in range(2 * i + 1):
            print("*", end=" ")
        
        for j in range(0, num - i + 1):
            print(" ", end=" ")
        print("\n")
    
    for i in range(0, num):
        for j in range(0, i + 2):
            print(" ", end=" ")
        
        for j in range(2 * (num) - (2 * i + 1)):
            print("*", end=" ")
        
        for j in range(0, i + 1):
            print(" ", end=" ")
        print("\n")

def pattern4(num):
    for i in range(2 * num):
        star = i
        if (i > num):
            star = 2 * num - i
        for j in range(star):
            print("*", end=" ")
        print("\n")
       
def pattern5(num):
    start = 1
    for i in range(num):
        if (i % 2 == 0):
            start = 0
        else:
            start = 1
        for j in range(i):
            print(start, end=" ")
            start = 1 - start
        print("\n")
      
def pattern6(num):
    space = 2 * (num) - 4
    for i in range(1, num):
        for j in range(1, i):
            print(j, end=" ")
        
        for j in range(space):
            print(" ", end=" ")
        
        for j in range(1, i):
            print(i - j, end=" ")
        print("\n")
        space = space - 2
       
def pattern7(num):
    n = 1
    for i in range(num):
        for j in range(i):
            print(n, end=" ")
            n = n + 1      
        print("\n")

def pattern8(num):
    for j in range(num):
        for i in range(j):
            char = chr(65 + i)
            print(char, end=" ")
        
        print("\n")
        
def pattern9(num): 
    for j in range(num): 
        for i in range(num - j - 1): 
            char = chr(65 + i)
            print(char, end=" ")
        print("\n")

def pattern10(num):  
    x = 1
    for j in range(num): 
        for i in range(j): 
            char = chr(63 + x)
            print(char, end=" ")
        x = x + 1
        print("\n")
            
def pattern11(num):
    for i in range(num):
        x = 0
        for i in range(2 * num - i):
            print(" ")
        for j in range(i):
            char = chr(65 + x)
            print(char, end=" ")
        x = x + 1
        print("\n")
```

