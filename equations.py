
def exponent(x:float) -> float:
    if x!=0:
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
    if x==0:
        return 1

def Ln(x:float) -> float:
    if x>0 and x!=1:
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
        power=y*Ln(x)
        fff=exponent(power)
        return fff
    else :
        return 0

def sqrt(x:float,y:float) -> float:
        xy= XtimesY(y,1.0/x)
        return xy

def calculate(x:float) -> float:
    x=float(x)
    if x>0:
        Ex=exponent(x)
        SevenX= XtimesY(7,x)
        Xminus1=1/x
        XsqrtX=sqrt(x,x)
        equation=Ex*SevenX*Xminus1*XsqrtX
        equation=float('%0.6f' % equation)
        return equation
    else: 
        return 0
