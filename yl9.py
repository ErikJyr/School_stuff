
a = float(input(" Külg a: "))
b = float(input(" Külg b: "))
c = float(input(" Külg c: "))

if a + b > c and a + c > b and b + c > a:
    
    if a == b == c:
        print("See kolmnurk on võrdkülgne.")
    elif a == b or b == c or a == c:
        print("See kolmnurk on võrdhaarne.")
    else:
        print("See kolmnurk on erikülgne.")
else:
    print("sellist kolmnurka ei ole olemas.")
