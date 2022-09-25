limite = 30
num = 5
e=0
fact=1
for i in range(1, num+1):
    fact*=i
print("factorial es: ",fact)


while num < limite:
	e =e+ 1/fact# se llama a la función factorial creada por ti
	num = num + 1
print("num",num)
print("e",e)


