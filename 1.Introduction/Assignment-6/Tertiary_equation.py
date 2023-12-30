import cmath  

def solve_cubic():
    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    d = int(input("d: "))

    delta_0 = b**2 - 3*a*c
    delta_1 = 2*b**3 - 9*a*b*c + 27*a**2*d
    C = ((delta_1 + cmath.sqrt(delta_1**2 - 4*delta_0**3)) / 2)**(1/3)
    
    root_1 = -1/(3*a) * (b + C + delta_0/C)
    root_2 = -1/(3*a) * (b + cmath.exp(2j * cmath.pi/3) * C + delta_0/(cmath.exp(2j * cmath.pi/3) * C))
    root_3 = -1/(3*a) * (b + cmath.exp(4j * cmath.pi/3) * C + delta_0/(cmath.exp(4j * cmath.pi/3) * C))
    
    return root_1, root_2, root_3

roots = solve_cubic()
print(f"The roots of the cubic equation are: {roots}")
