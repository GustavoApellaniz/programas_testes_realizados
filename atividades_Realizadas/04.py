def aum(a):
    if a>4000:
        return a*1.10
    else:
        return a*1.15
    


if __name__=='__main__':
    x=float(input("sario atual? "))
    print(f"seu novo salário é {aum(x)}")