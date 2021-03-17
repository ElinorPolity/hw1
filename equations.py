
def exponent(x:float) -> float:
    n=0
    i=1.0
    sumExponent=1.0
    previousX=1.0
    counter = 2.0
    while n<110:
        num= x/i
        sumExponent=sumExponent+num
        i=i*counter
        counter=counter+1.0
        NextX=x*(x/previousX)
        previousX=x
        x=NextX
        n+=1
    return sumExponent

def ln(x:float) -> float:
    if x>0:
        i=0
        Yn=1.0
        while i<110:
            LnY=Yn+2*((x-exponent(Yn))/(x+exponent(Yn)))
            Yn=LnY
            i+=1
        return LnY
    else :
        return 0

def XtimesY(x:float,y:float) -> float:
    if x>0 :
        power=y*ln(x)
        fff=exponent(power)
        return fff
    else :
        return 0

def sqrt(x:float,y:float) -> float:
    if  x<0 and x%2!=0:
        xy= XtimesY(-y,1/x)
        return xy
    else:
        xy= XtimesY(y,1/x)
        return xy
print(sqrt(-2.3,-2.3))

def calculate(x:float) -> float:
    x=float(x)
    if x==0: 
        return 0
    elif x<0 and x%2==0:
        return 0    
    else:
        Ex=exponent(x)
        SevenX= XtimesY(7,x)
        Xminus1=1/x
        XsqrtX=sqrt(x,x)
        equation=Ex*SevenX*Xminus1*XsqrtX
        equation=float('%0.6f' % equation)
        return equation
print(calculate(2.35))
