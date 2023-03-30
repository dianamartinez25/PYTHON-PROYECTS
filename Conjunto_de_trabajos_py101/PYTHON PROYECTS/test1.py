#help("keywords")
import keyword
print(keyword.kwlist)
a = keyword.kwlist
print(type(a))

a = 4.345
print(type(a))
print(isinstance(a, str))
x = 10
#print(hex(id(x)))
print(id(x))
x = 20
print(id(x))
nombres = ["Jon","María"]
print(id(nombres))
nombres.append("Pedro")
print(id(nombres))

exists = True
if exists == True:
    print("TRUE")
    print("True")
print("FIN")

x = 3
if (x > 1):
    print("mas que uno")
elif (x < 3) and (y < 3):
    print("jkaja")




