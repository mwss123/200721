
#2

print('Kim Minji')



#3
def Base() :
    a = input('BASE :')
    if a == 'A' : return 'Adenine'
    if a == 'T' : return 'Tymine'
    if a == 'G' : return 'Guanine'
    if a == 'C' : return 'Cytosine'
    if a == 'U' : return 'Uracil'
    else : print('error')

print(Base())


#4
n = int(input('Number :'))

def Num(n) :
    a = 10/n
    try :
        return a
        
    except ZeroDivisionError :
        print('Re-try')

print(Num(n))

#5 

def factorial(n) :
    if n > 0 :
        gop = n*factorial(n-1)
   
    return gop
print(factorial(5)) 
