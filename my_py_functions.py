
'''======palindrome or not========'''
def palindrome(a):
    length=len(a)
    iterator=0
    while iterator <= length/2:
        if a[iterator]==a[length-iterator-1]:
            iterator+=1
        else:
            return False

    return True

def palindrome_fast(a):
    return a==a[::-1]

'''=======GCD of two numbers======'''

def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b

    return gcd(b, a % b) 



'''====GCD of Two Numbers -Aliter======='''
def gcda(a,b):
    while(b!=0):
        c=a%b
        a=b
        b=c
    return a


'''========CONVERT INT TO A STRING IN ANY BASE==========='''

def toStr(number,base):
    convertString="0123456789ABCDEF" #for base 16, change for others
    if number<base:
        return convertString[number]
    else:
        return toStr(number//base,base) + convertString[number%base]



'''======ANAGRAM TESTER==========='''
def anagram(s1,s2):

    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    if s1!=s2:
        return False
    return True



'''====ANAGRAM LEXICOGRAPHICALLY ARRANGED===='''
def anagramlex(s1,s2,value=0):
        '''value:Lexicographically smallest or biggest
        value: max=1 or min=0 (default=0)'''
        if len(s1)!=len(s2):
            return False
        s1=sorted(s1)
        s2=sorted(s2)
        if s1!=s2:
            return False
        if value==0:
            return s1
        else:
            return s1[::-1]


'''======check for pair in array with sum equal to some value======'''
def checkpair(arr,size,add):
    arr=sorted(arr)
    l=0
    r=size-1
    while l<r:
        if(arr[l]+arr[r]==add):
            return 1
        elif (arr[l]+arr[r]<add):
            l+=1
        else:
            r-=1
    return 0


'''=======LCM (LCM OF A RANGE ALSO) AND GCD========'''
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

#print lcmm(*range(1,502))



'''====Sum of Divisors==='''
'''Sum and list of divisors'''
def sumofdiv(number):
    add=0
    temp=[]
    a=int(number**0.5)+1
    for i in range(1,a):
        if number%i==0:
            add=add+i
            if int(number/i)!=i:
                add=add+(number/i)
            temp.append(number/i)
            temp.append(i)
    del temp[0]
    add=add-number
    return add,temp


'''====Prime Tester==='''
def prime(number):
    j=2
    if number<=1:
        return False
    q=int(number**0.5)+1
    while j<q:
        if number%j==0:
            return False
        j=j+1
    return True


'''====Prime factors===='''
def primef(n):
    art=[]
    while n%2==0:
        art.append(2)
        n=n/2
    for i in range(3,int(n**0.5)+1,2):
        while n%i==0:
            art.append(i)
            n=n/i
    if n>2:
        art.append(n)
    return art

'''====Nth non-fibonacci number==='''
for i in xrange(n):
    a,b,c = 1,2,3
    size  = input()
    while size >0:
        a,b = b,c
        c = a+b
        size -= c-b-1
    size += c-b-1 # adding the redundant subtraction
    print b + size
