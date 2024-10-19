
def pattern7(num):
    for i in range(0,num):
        for j in range(0,num-i+1):
            print(" ",end=" ")
        
        for j in range(2*i+1):
            print("*",end=" ")
        
        for j in range(0,num-i+1):
            print(" ",end=" ")
        print("\n")
    
def pattern8(num8):
    for i in range(0,num8):
        for j in range(0,i):
            print(" ",end=" ")
        
        for j in range(2*(num8)-(2*i+1)):
            print("*",end=" ")
        
        for j in range(0,i):
            print(" ",end=" ")
        print("\n")
    

def pattern9(num):
    for i in range(0,num):
        for j in range(0,num-i+1):
            print(" ",end=" ")
        
        for j in range(2*i+1):
            print("*",end=" ")
        
        for j in range(0,num-i+1):
            print(" ",end=" ")
        print("\n")
    
    for i in range(0,num):
        for j in range(0,i+2):
            print(" ",end=" ")
        
        for j in range(2*(num)-(2*i+1)):
            print("*",end=" ")
        
        for j in range(0,i+1):
            print(" ",end=" ")
        print("\n")

def pattern10(num10):
    for i in range(2*num10):
        star=i
        if (i>num10):
            star=2*num10-i
        for j in range(star):
            print("*",end=" ")
        print("\n")
       
def pattern11(num11):
    start=1
    for i in range(num11):
        if (i%2==0):
            start=0
        else:
            start=1
        for j in range(i):
            print(start,end=" ")
            start=1-start
        print("\n")
      
def pattern12(num12):
    space=2*(num12)-4
    for i in range(1,num12):
        for j in range(1,i):
            print(j,end=" ")
        
        for j in range(space):
            print(" ",end=" ")
        
        for j in range(1,i):
            print(i-j,end=" ")
        print("\n")
        space=space-2
       
def pattern13(num13):
    n=1
    for i in range(num13):
        for j in range(i):
            print(n,end=" ")
            n=n+1      
        print("\n")
def pattern14(num14):
       for j in range(num14):
           for i in range(j):
               char=chr(65+i)
               print(char,end=" ")
            
           print("\n")
        
def pattern15(num15): 
    for j in range(num15): 
       for i in range(num15-j-1): 
           char=chr(65+i)
           print(char,end=" ")
       print("\n")

   
    
   
    
def pattern16(num16) :  
    x=1
    for j in range(num16): 
       for i in range(j): 
           char=chr(63+x)
           print(char,end=" ")
       x=x+1
       print("\n")
            
     
def pattern17(num17):
    for i in range(num17):
        x=0
        for i in range(2*num17-i):
            print(" ")
        for j in range(i):
            char=chr(65+ x)
            print(char,end=" ")
        x=x+1
        print("\n")
            
        
       
