def suma(b, n ):
    return b + n

def resta(n, m ):
    return n - m 
def multiplica (x, n):
    return x * n
def division (f , j):
    return f / j
n1 = float(input("Teclea el primer número"))
n2 = float(input("Teclea el segundo número"))
if __name__ == "__main__":
    x = suma (n1,n2)
    print(x)
    y = resta ( n1, n2)
    print(y)
    z = multiplica (n1, n2)
    print(z)
    print(division(n1, n2))