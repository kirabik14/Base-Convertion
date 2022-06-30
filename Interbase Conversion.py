n=(input("Enter the base- number to be converted: "))
b_n=int(input("Enter the base the number is in (<=16): "))

def revalpha(p):
    if p=='A':
        p=10
    elif p=='B':
        p=11
    elif p=='C':
        p=12
    elif p=='D':
        p=13
    elif p=='E':
        p=14
    elif p=='F':
        p=15
    elif int(p)<10:
        p=int(p)
    else:
       print("Not Possible")
       exit()
    return p

if b_n>16:
    print("Not Possible")
    exit()

else:
    L_n=len(n)-1
    i=0
    d=0
    while i<len(n):
        p=len(n)-i-1
        z=revalpha(n[i])
        if z>(b_n):
            print("No such number possible in", b_n, "- base")
            exit()
        d+=((b_n)**p)*z
        i+=1

#print("The 10 - base expansion of", n, "in base", b_n, "is", d)

#============================================================================================================

b=int(input("Enter the base to be converted into (<=16): "))

def alphabet(p):
    if p==10:
        p='A'
    elif p==11:
        p='B'
    elif p==12:
        p='C'
    elif p==13:
        p='D'
    elif p==14:
        p='E'
    elif p==15:
        p='F'
    else:
        p=p
    return p

if b>16:
    print("Not possible")
    exit()

else:
    L=['Daibik']

    u=d

    while u>=b:
        r=u%b
        u-=r
        u=int(u/b)
        r= alphabet(r)
        L.append(str(r))
        
    u= alphabet(u)
    L.append(str(u))
    
    l=len(L)-1

    b_c='0'

    while l>0:
        b_c+=(L[l])
        l-=1

    print ("The",b,"- base equivalent of", n, "in base", b_n, "is", b_c[1:])
