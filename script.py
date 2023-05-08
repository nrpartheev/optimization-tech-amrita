# Importing libraries
import math
import sys

# Create a function named f(x) for calculating the function value
def f(x, equation):
    try:
        variables = {'x': x}
        val = eval(equation, variables)
    except:
        val = sys.maxsize
    return val

# This function is for finding the f'(x)
def derivative_f(x, equation):
    if x > 0.01:
        difx = 0.01 * x
    else:
        difx = 0.0001
    temp = f(x + difx, equation)
    temp2 = f(x - difx, equation)
    temp3 = 2 * difx
    return (temp - temp2) / temp3

# This function is for finding the f''(x)
def double_derivative_f(x, equation):
    if x > 0.01:
        difx = 0.01 * x
    else:
        difx = 0.0001
    temp = f(x + difx, equation)
    temp2 = f(x - difx, equation)
    temp3 = difx ** 2
    temp4 = 2 * f(x)
    return (temp + temp2 - temp4) / temp3


#...................................................................................................#
#--------------------------------- ALL THE SINGLE VARIABLE TECH ------------------------------------#
#...................................................................................................#

def exhaustive_search_method():
    equation = input('Enter the equation (e.g., x**2 or (x**3)+(x**2)): ')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    x1 = a
    n = float(input("Enter n (greater than 0): "))
    delta = ((b - a) / n)
    x2 = delta + x1
    x3 = delta + x2
    print("Initially x1: {:.2f}, x2: {:.2f}, x3: {:.2f}".format(x1, x2, x3))
    print("Function values f(x1): {:.2f}, f(x2): {:.2f}, f(x3): {:.2f}".format(f(x1, equation), f(x2, equation),
                                                                               f(x3, equation)))
    while ((f(x1, equation) >= f(x2, equation) >= f(x3, equation)) or (
            f(x1, equation) <= f(x2, equation) <= f(x3, equation))):
        x1 = x2
        x2 = x3
        x3 = x3 + delta
        print("Changing x1: {:.2f}, x2: {:.2f}, x3: {:.2f}".format(x1, x2, x3))
        print("Function values f(x1): {:.2f}, f(x2): {:.2f}, f(x3): {:.2f}".format(f(x1, equation), f(x2, equation),
                                                                                   f(x3, equation)))
    print("There is a function between {:.2f} and {:.2f}".format(x1, x3))
    print("Accuracy: {:.2f}".format((2 * (b - a)) / n))


def bounding_phase_searching():
    equation = input('Enter the equation (e.g., x**2 or (x**3)+(x**2)): ')
    initial = float(input("Enter the initial guess: "))
    approx = float(input("Enter the approximation: "))
    if approx < 0:
        approx = -(approx)
    while (not (f(initial - approx, equation) <= f(initial, equation) <= f(initial + approx, equation) or
                f(initial - approx, equation) >= f(initial, equation) >= f(initial + approx, equation))):  
        initial = float(input("Invalid guess. Please enter another number: "))
    print("f(initial - approx) = {:.2f}, f(initial) = {:.2f}, f(initial + approx) = {:.2f}".format(
        f(initial - approx, equation), f(initial, equation), f(initial + approx, equation)))

    if f(initial - approx, equation) <= f(initial, equation) <= f(initial + approx, equation):
        print("f(initial - approx) <= f(initial) <= f(initial + approx)")
        approx = -(approx)

    print("approx is {:.2f}".format(approx))
    k = 0
    next_val = initial + (pow(2, k) * approx)
    print("x({}) = {:.2f}, x({}) = {:.2f}".format(k, initial, k + 1, next_val))
    print("f(x(k)) = {:.2f}, f(x(k+1)) = {:.2f}".format(f(initial, equation), f(next_val, equation)))

    while f(next_val, equation) < f(initial, equation):
        print("x({}) < x({})".format(next_val, initial))
        k += 1
        print("k = {}".format(k))
        previous = initial
        initial = next_val
        next_val = initial + (pow(2, k) * approx)
        print("x(k) = {:.2f}, x(k+1) = {:.2f}".format(initial, next_val))
        print("f(x(k)) = {:.2f}, f(x(k+1)) = {:.2f}".format(f(initial, equation), f(next_val, equation)))

    print("There exists a root between {:.2f} and {:.2f}".format(previous, next_val))



def interval_halving():
    equation = input('Enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
    a = float(input("Enter the lower bound: "))
    b = float(input("Enter the upper bound: "))
    e = float(input("Enter the approximation parameter: "))
    L = b - a
    print("L = {:.2f}".format(L))

    while (b - a) > e:
        counter = 1
        L = b - a
        print("a = {:.2f}".format(a))
        print("b = {:.2f}".format(b))
        print("L = {:.2f}".format(L))
        xm = (a + b) / 2
        print("xm = {:.2f}".format(xm))
        x1 = a + (L / 4)
        print("x1 = {:.2f}".format(x1))
        x2 = b - (L / 4)
        print("x2 = {:.2f}".format(x2))
        print("f(x1) = {:.2f}, f(x2) = {:.2f}, f(xm) = {:.2f}".format(f(x1, equation), f(x2, equation), f(xm, equation)))

        if f(x1, equation) < f(xm, equation):
            print("f(x1) < f(xm)")
            print("Changing b to xm and xm to x1")
            b = xm
            xm = x1
            counter = 0

        if counter == 1:
            if f(x2, equation) < f(xm, equation):
                print("f(x2) < f(xm)")
                print("Changing a to xm and xm to x2")
                a = xm
                xm = x2
            else:
                print("Changing b to x2 and a to x1")
                a = x1
                b = x2

    print("({:.2f}, {:.2f})".format(a, b))


def F(nth):
    n1, n2 = 0, 1
    count = 0
    while count < nth + 1:
        nther = n1 + n2
        n1 = n2
        n2 = nther
        count += 1
    return n1

def fibonacii():
    equation = input('Enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    n = float(input("Enter n: "))
    k = 2
    L = b - a

    while n + 1 != k:
        print("a = {:.2f}".format(a))
        print("b = {:.2f}".format(b))
        print("L = {:.2f}".format(L))
        print("n - k + 1 = {:.2f}".format(n - k + 1))
        print("n + 1 = {:.2f}".format(n + 1))
        Lk = (F(n - k + 1) / F(n + 1)) * L
        print("Lk = {:.2f}".format(Lk))
        x1 = a + Lk
        print("x1 = {:.2f}".format(x1))
        x2 = b - Lk
        print("x2 = {:.2f}".format(x2))
        print("f(x1) = {:.2f}, f(x2) = {:.2f}".format(f(x1, equation), f(x2, equation)))

        if f(x1, equation) > f(x2, equation):
            a = x1
        if f(x1, equation) < f(x2, equation):
            b = x2
        if f(x1, equation) == f(x2, equation):
            a = x1
            b = x2
        k += 1
        print("k = {:.2f}".format(k))

    print("({:.2f}, {:.2f})".format(a, b))


def bisection():
    equation = input('Enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
    a = float(input("Enter initial guess a: "))
    b = float(input("Enter initial guess b: "))

    if (derivative_f(a, equation) > 0 and derivative_f(b, equation) > 0) or (
            derivative_f(a, equation) < 0 and derivative_f(b, equation) < 0):
        print("Invalid input")
        secant()
    else:
        print("Valid input")

    x1 = a
    x2 = b
    print("Set x1 = a and x2 = b")
    print("derivative_f(a) = {:.2f}".format(derivative_f(a, equation)))
    print("derivative_f(b) = {:.2f}".format(derivative_f(b, equation)))
    termination = float(input("Enter termination criteria: "))
    z = (x1 + x2) / 2
    print("z = (x1 + x2) / 2 ==> z = {:.2f}".format(z))

    while abs(derivative_f(z, equation)) > termination:
        print("derivative_f(z) = {:.2f}".format(derivative_f(z, equation)))
        if derivative_f(z, equation) < 0:
            print("x1 = z")
            x1 = z
        elif derivative_f(z, equation) > 0:
            print("x2 = z")
            x2 = z
        print("x1 = {:.2f}".format(x1))
        print("x2 = {:.2f}".format(x2))
        z = (x1 + x2) / 2
        print("z = (x1 + x2) / 2 ==> z = {:.2f}".format(z))

    print("*** End of loop ***")
    print("x1 = {:.2f}".format(x1))
    print("x2 = {:.2f}".format(x2))
    z = (x1 + x2) / 2
    print("z = (x1 + x2) / 2 ==> z = {:.2f}".format(z))
    print("****** End ******")

def newton_raphson():
  equation = input('enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
  initial = float(input("enter the initial guess: "))
  termination = float(input("enter the termination: "))
  print("setting k = 1")
  k = 1
  while abs(derivative_f(initial, equation)) > termination:
    print("| x({}) = {:.2f} |".format(k, initial), end='')
    print("| f'({}({:.2f})) = {:.2f} |".format(k, initial, derivative_f(initial, equation)), end='')
    print("| f''({}({:.2f})) = {:.2f} |".format(k, initial, double_derivative_f(initial, equation)))
    print("x({}) = x({}) - (f'({}) / f''({}))".format(k+1, k, k, k))
    next_value = initial - (derivative_f(initial, equation) / double_derivative_f(initial, equation))
    k += 1
    initial = next_value

def successive_quadratic_estimation_method():
  equation = input('enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
  initial = float(input("enter the initial point: "))
  k = 1
  delta = float(input("enter the step size: "))
  print("assigning x{} = x{} + delta".format(k+1, k))
  next_value = initial + delta
  if f(initial, equation) > f(next_value, equation):
    next_next = initial + (2 * delta)
  else:
    next_next = initial - delta
  array = [f(initial, equation), f(next_value, equation), f(next_next, equation)]

def secant():
  equation = input('enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
  a = float(input("enter the first point: "))
  b = float(input("enter the second point: "))
  
  if (derivative_f(a, equation) > 0 and derivative_f(b, equation) > 0) or (derivative_f(a, equation) < 0 and derivative_f(b, equation) < 0):
    print("Invalid input. The function does not cross the x-axis between the given points.")
    secant()
  else:
    print("Valid input")
  
  termination = float(input("enter the termination: "))
  z = b - (derivative_f(b, equation) * (b - a) / (derivative_f(b, equation) - derivative_f(a, equation)))
  print("z = x2 - (f'(x2) / (f'(x2) - f'(x1)) * (x2 - x1))")
  print("z = {:.2f}".format(z))
  print("f'(z) = {:.2f}".format(derivative_f(z, equation)))

  while abs(derivative_f(z, equation)) > termination:
    if derivative_f(z, equation) > 0:
      print("We must eliminate the right part.")
      if (b - z) < ((b - a) / 2):
        print("b - z < halving")
        print("b = z")
        b = z
      else:
        print("halving < b - z")
        b = (b - a) / 2
    else:
      print("We must eliminate the left part.")
      if (z - a) < (b - a / 2):
        print("z - a < halving")
        print("a = z")
        a = z
      else:
        print("halving < z - a")
        a = (b - a) / 2
    z = b - (derivative_f(b, equation) * (b - a) / (derivative_f(b, equation) - derivative_f(a, equation)))
    print("z = b - (f'(a) / (f'(b) - f'(a)) * (b - a))")
    print("z = {:.2f}".format(z))
    print("f'(z) = {:.2f}".format(derivative_f(z, equation)))


def cube():
  equation = input('enter the equation (Ex: x**2 or (x**3)+(x**2)): ')
  a = float(input("enter the initial guess: "))
  delta = float(input("enter the step size: "))
  e0 = float(input("enter the termination: "))
  e1 = float(input("enter the termination2: "))
  
  print("f'(x0) = {:.2f}".format(derivative_f(a, equation)))
  
  if derivative_f(a, equation) > 0:
    print("f'(x0) > 0, so changing delta to -delta.")
    delta = -delta
  
  k = 0
  intial = a
  print("x1 = x0 + 2^K * delta")
  next = intial + (pow(2, k) * delta)
  print("x1 = {:.2f}".format(next))
  print("f'({}) = {:.2f}".format(k+1, derivative_f(next, equation)))
  print("f'({}) = {:.2f}".format(k, derivative_f(intial, equation)))
  
  while derivative_f(next, equation) * derivative_f(intial, equation) > 0:
    print("f'(k) * f'(k+1) > 0")
    print("Continuing with the iteration.")
    k += 1
    intial = next
    next = intial + (pow(2, k) * delta)
    print("***************")
    print("x{} = x{} + 2^{} * delta".format(k+1, k, k))
    print("x{} = {:.2f}".format(k, intial))
    print("x{} = {:.2f}".format(k+1, next))
    print("f'({}) = {:.2f}".format(k+1, derivative_f(next, equation)))
    print("f'({}) = {:.2f}".format(k, derivative_f(intial, equation)))
    print("***************")
  
  print("So finally:")
  x1 = intial
  x2 = next
  print("x1 = x({}): {:.2f}".format(k, x1))
  print("x2 = x({}): {:.2f}".format(k+1, x2))
  
  print("Now we calculate z, w, and mew")
  z = ((3 * (f(x1, equation) - f(x2, equation))) / (x2 - x1)) + derivative_f(x1, equation) + derivative_f(x2, equation)
  print("z = {:.2f}".format(z))
  w = ((x2 - x1) / abs(x2 - x1)) * (pow((pow(z, 2) - (derivative_f(x1, equation) * derivative_f(x2, equation))), 0.5))
  print("w = {:.2f}".format(w))
  mew = (derivative_f(x2, equation) + w - z) / (derivative_f(x2, equation) - derivative_f(x1, equation) + (2 * w))
  print("mew = {:.2f}".format(mew))
  
  if mew == 0:
    print("xdash = x2")
    xdash = x2
    print("xdash = {:.2f}".format(xdash))
  elif 0 <= mew and mew <= 1:
    print("xdash = x2 - (mew *    (x2 - x1)")
    xdash = x2 - (mew * (x2 - x1))
    print("xdash = {:.2f}".format(xdash))
  else:
    print("xdash = x1")
    xdash = x1
    print("xdash = {:.2f}".format(xdash))

  print("|f'(xdash)| = {:.2f}".format(abs(derivative_f(xdash, equation))))

  while f(xdash, equation) > f(x1, equation):
    print("f(xdash) > f(x1), so xdash becomes 1/2 * xdash + x1")
    xdash = 0.5 * xdash + x1
  
  if derivative_f(xdash, equation) * derivative_f(x1, equation) < 0:
    print("f'(xdash) * f'(x1) < 0, so assigning x2 = xdash")
    x2 = xdash
  else:
    print("f'(xdash) * f'(x1) > 0, so assigning x1 = xdash")
    x1 = xdash

  print("After iteration, we get:")
  print("x1 = {:.2f}".format(x1))
  print("x2 = {:.2f}".format(x2))
  print("*******************")
  print("")
  print("")

  while not (abs(derivative_f(xdash, equation)) <= e0 and abs((xdash - x1) / xdash) <= e1):
    print("Now we calculate z, w, and mew")
    print("f(x1) = {:.2f}".format(f(x1, equation)))
    print("f(x2) = {:.2f}".format(f(x2, equation)))
    print("f'(x1) = {:.2f}".format(derivative_f(x1, equation)))
    print("f'(x2) = {:.2f}".format(derivative_f(x2, equation)))

    z = ((3 * (f(x1, equation) - f(x2, equation))) / (x2 - x1)) + derivative_f(x1, equation) + derivative_f(x2, equation)
    print("z = {:.2f}".format(z))
    w = ((x2 - x1) / abs(x2 - x1)) * (pow((pow(z, 2) - (derivative_f(x1, equation) * derivative_f(x2, equation))), 0.5))
    print("w = {:.2f}".format(w))
    mew = (derivative_f(x2, equation) + w - z) / (derivative_f(x2, equation) - derivative_f(x1, equation) + (2 * w))
    print("mew = {:.2f}".format(mew))
  
    if mew == 0:
      print("xdash = x2")
      xdash = x2
      print("xdash = {:.2f}".format(xdash))
    elif 0 <= mew and mew <= 1:
      print("xdash = x2 - (mew * (x2 - x1))")
      xdash = x2 - (mew * (x2 - x1))
      print("xdash = {:.2f}".format(xdash))
    else:
      print("xdash = x1")
      xdash = x1
      print("xdash = {:.2f}".format(xdash))

    print("f(xdash) = {:.2f}".format(f    (xdash, equation)))
    print("f(x1) = {:.2f}".format(f(x1, equation)))

    while f(xdash, equation) > f(x1, equation):
      print("f(xdash) > f(x1), so xdash becomes 1/2 * xdash + x1")
      xdash = 0.5 * xdash + x1
    
    if derivative_f(xdash, equation) * derivative_f(x1, equation) < 0:
      print("f'(xdash) * f'(x1) < 0, so assigning x2 = xdash")
      x2 = xdash
    else:
      print("f'(xdash) * f'(x1) > 0, so assigning x1 = xdash")
      x1 = xdash

    print("After iteration, we get:")
    print("x1 = {:.2f}".format(x1))
    print("x2 = {:.2f}".format(x2))
    print("*******************")
    print("")
    print("")


  



print("*****************greetings******************")

print("1.Exhaustive_search_method")
print("2.Bounding_phase_searching")
print("3.Interval_halving")
print("4.Fibonacii")
print("5.Bisection")
print("6.Newton raphson")
print("7.Secant method")
print("8.Cube")
subchoice=int(input("Enter the desired choice: "))
if subchoice==1:
  exhaustive_search_method()
if subchoice==2:
  bounding_phase_searching()
if subchoice==3:
  interval_halving()
if subchoice==4:
  fibonacii()
if subchoice==5:
  bisection()
if subchoice==6:
  newton_raphson()
if subchoice==7:
  secant()
if subchoice==8:
  cube()

print('[EXECUTED SUCCESSFULLY]')