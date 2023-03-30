with open ("datos.txt", "r") as f:
    s = f.read()
    

s= s.upper()

with open ("datos.txt", "w") as f:
   f.write(s)