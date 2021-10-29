import time
a = input("first: ")
b = input("seccond: ")
c = int(a) + int(b)
d = int(a) - int(b)
e = int(a) * int(b)
f = int(a) / int(b)

g = input("+,-,,/,?: ")
if g == "+":
    print("yo number is: " + str(c))
    time.sleep(10)
elif g == "-":
    print("yo number is: " + str(d))
    time.sleep(10)
elif g == "":
    print("yo number is: " + str(e))
    time.sleep(10)
elif g == "/":
    print("yo number is: " + str(f))
    time.sleep(10)
time.sleep(10)
