from math import pi
from sympy import symbols, Eq, simplify, solve, sympify, expand
import math
import cmath
def simultaneous():
    x, y = symbols ('x y')
    eq1_input=input("Enter first equation")
    eq2_input=input("Enter the second equation")
    lhs1, rhs1 = eq1_input.split("=")
    lhs2, rhs2 = eq2_input.split("=")
    eq1 = Eq(sympify(lhs1), sympify(rhs1))
    eq2 = Eq(sympify(lhs2), sympify(rhs2))
    solution = solve((eq1, eq2), (x, y))
    print("The solution is:", solution)

def solve_quadratic():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    disc = b**2 - 4*a*c

    if disc < 0:
        print("No real solutions")
    elif disc == 0:
        x = -b / (2*a)
        print("One solution:", x)
    else:
        x1 = (-b + math.sqrt(disc)) / (2*a)
        x2 = (-b - math.sqrt(disc)) / (2*a)
        print("Two solutions:", x1, "and", x2)
def expand_expr(expr):
    return expand(expr)
def simplify_expr(expr):
    return simplify(expr)
def expand_function():
    expr_input = input("Enter expression to expand: ")
    expr = sympify(expr_input)
    result = expand_expr(expr)
    print("Expanded:", result)


def simplify_function():
    expr_input = input("Enter expression to simplify: ")
    expr = sympify(expr_input)
    result = simplify_expr(expr)
    print("Simplified:", result)
def add():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    num=num1+num2
    print(num1,"+",num2,"=",num)

def minus():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    num=num1-num2
    print(num1,"-",num2,"=",num)

def multiply():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    num=num1*num2
    print(num1,"x",num2,"=",num)

def divide():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    if num1==0 or num2==0:
        print("You can't devide by 0!")
    else:
        num=num1/num2
        print(num1,"/",num2,"=",num)

def floor_division():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    num=num1//num2
    print(num1,"(⌊)",num2,"=",num)

def remainder():
    num1=int(input("Enter a number"))
    num2=int(input("Enter another number"))
    num=num1%num2
    print("There is a remainder of",num)

def circ_area():
    num1=int(input("What is the radius"))
    num=num1*num1
    num=num*pi
    print("The area is",num)

def binary():
    binary_string =input("Enter Binary")
    decimal_number = int(binary_string, 2)
    print(f"The decimal equivalent of binary {binary_string} is {decimal_number}.")

def profit():
    tr=int(input("Enter your total revenue"))
    tc=int(input("Enter your total costs"))
    profit=tr-tc
    print("Your profit is",profit)

def interior():
    n=int(input("Enter number of sides in your regular polygon"))
    if n <=2:
        print("Number of sides must be over 2")
    else:
        n=n-2
        n=n*180
        print("The sum of interior angles is",n)

def compl_square():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))

    choice = input("Type 'form' for completed square or 'solve' to solve for x: ").lower()

    h = -b / (2 * a)
    k = c - (b ** 2) / (4 * a)

    if choice == "form":
        print(f"Completed square form: {a}(x - ({h}))^2 + ({k})")
    elif choice == "solve":
        disc = b**2 - 4*a*c
        if disc < 0:
            print("No real solutions")
        else:
            x1 = (-b + math.sqrt(disc)) / (2*a)
            x2 = (-b - math.sqrt(disc)) / (2*a)
            print(f"x = {x1}, {x2}")
    else:
        print("Invalid choice")
def time():
    conversion=input("What would you like to convert from? in seconds minutes hours days weeks or years").lower()
    convert=input("What would you like to convert to?").lower()
    if conversion=="seconds" and convert=="minutes":
        num=float(input("Enter the number of seconds"))
        num=num/60
        print(num,"minutes")
    elif conversion=="seconds" and convert=="hours":
        num=float(input("Enter the number of seconds"))
        num=num/60
        num=num/60
        print(num,"hours")
    elif conversion=="seconds" and convert=="days":
        num=float(input("Enter the number of seconds"))
        num=num/60
        num=num/60
        num=num/24
        print(num,"days")
    elif conversion=="seconds" and convert=="weeks":
        num=float(input("Enter the number of seconds"))
        num=num/604800
        print(num,"weeks")
    elif conversion=="seconds" and convert=="years":
        num=float(input("Enter the number of seconds"))
        num=num/31536000
        print(num,"years")
    elif conversion=="minutes" and convert=="seconds":
        num=input("Enter number of minutes")
        num=num*60
        print(num,"seconds")
    elif conversion=="minutes" and convert=="hours":
        num=float(input("Enter number of minutes"))
        num=num/60
        print(num,"hours")
    elif conversion=="minutes" and convert=="days":
        num=float(input("Enter number of minutes"))
        num=num/60
        num=num/24
        print(num,"days")
    elif conversion=="minutes" and convert=="weeks":
        num=float(input("Enter number of minutes"))
        num=num/60
        num=num/24
        num=num/7
        print(num,"weeks")
    elif conversion=="minutes" and convert=="years":
       num=float(input("Enter number of minutes"))
       num=num/525600
    elif conversion=="hours" and convert=="seconds":
        num=float(input("Enter a number of hours"))
        num=num*360
        print(num,"seconds")
    elif conversion=="hours" and convert=="minutes":
        num=float(input("Enter a number of hours"))
        num=num*60
        print(num,"minutes")
    elif conversion=="hours" and convert=="days":
        num=float(input("Enter a number of hours"))
        num=num/24
        print(num,"days")
    elif conversion=="hours" and convert=="weeks":
        num=float(input("Enter a number of hours"))
        num=num/24
        num=num/7
        print(num,"weeks")
    elif conversion=="hours" and convert=="years":
         num=float(input("Enter a number of hours"))
         num=num/8760
         print(num,"years")
    elif conversion=="days" and convert=="seconds":
        num=float(input("enter a number of days"))
        num=num*24
        num=num*360
        print (num,"seconds")
    elif conversion=="days" and convert=="minutes":
        num=float(input("enter a number of days"))
        num=num*24
        num=num*60
        print (num,"minutes")
    elif conversion=="days" and convert=="hours":
        num=float(input("enter a number of days"))
        num=num*24
        print(num,"hours")
    elif conversion=="days" and convert=="weeks":
        num=float(input("enter a number of days"))
        num=num/7
        print(num,"weeks")
    elif conversion=="days" and convert=="years":
        num=float(input("enter a number of days"))
        num=num/365
        print(num,"years")
    elif conversion=="weeks" and convert=="seconds":
        num=float(input("enter a number of weeks"))
        num=num/7
        num=num/24
        num=num/360
        print(num,"seconds")
    elif conversion=="weeks" and convert=="minutes":
        num=float(input("enter a number of weeks"))
        num=num/7
        num=num/24
        num=num/60
        print(num,"minutes")
    elif conversion=="weeks" and convert=="hours":
        num=float(input("enter a number of weeks"))
        num=num/7
        num=num/24
        print(num,"hours")
    elif conversion=="weeks" and convert=="days":
        num=float(input("enter a number of weeks"))
        num=num/7
        print(num,"days")
    elif conversion=="weeks" and convert=="years":
        num=float(input("enter a number of weeks"))
        num=num/52.1428571
        print(num,"seconds")
    elif conversion=="years" and convert=="seconds":
        num=float(input("enter a number of years"))
        num=num*52.1428571
        num=num*7
        num=num*24
        num=num*60
        num=num*60
        print(num,"seconds")
    elif conversion=="years" and convert=="minutes":
        num=float(input("enter a number of weeks"))
        num=num*52.1428571
        num=num*7
        num=num*24
        num=num*60
        print(num,"minutes")
    elif conversion=="years" and convert=="hours":
        num=float(input("enter a number of years"))
        num=num*52.1428571
        num=num*7
        num=num*24
        print(num,"hours")
    elif conversion=="years" and convert=="days":
        num=float(input("enter a number of years"))
        num=num*52.1428571
        num=num*7
        print(num,"days")
    elif conversion=="years" and convert=="days":
        num=float(input("enter a number of years"))
        num=num*52.1428571
        print(num,"weeks")
    else:
        print("Invalid")
while True:

    calc = input("Do you want to add, minus, multiply, divide, floor division, remainder, circle area, binary, profit, interior, time, complete the square, solve simultaneous equations, expand, simplify, solve quadratic or stop?").lower()
    if calc=="add":
        add()
    elif calc=="minus":
        minus()
    elif calc=="multiply":
        multiply()
    elif calc=="divide":
        divide()
    elif calc=="floor division":
        floor_division()
    elif calc=="remainder":
        remainder()
    elif calc=="circle area":
        circ_area()
    elif calc=="binary":
        binary()
    elif calc=="profit":
        profit()
    elif calc=="interior":
        interior()
    elif calc=="time":
        time()
    elif calc=="complete the square":
        compl_square()
    elif calc=="solve simultaneous equations":
        simultaneous()
    elif calc == "expand":
        expand_function()
    elif calc == "simplify":
        simplify_function()
    elif calc == "solve quadratic":
        solve_quadratic()
    else:
        print("Goodbye")
        break

