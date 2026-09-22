print("escriba su nombre de usuario")
nombre_de_usuario = input()
combustible = 100
luna = 0
marte = 0
saturno = 0
destinos = ["luna", "marte", "saturno"]
costos = [20, 35, 50]
print("bienvenido ", nombre_de_usuario)
print("su combustible inicial es:", combustible)
print("elija destino", destinos)
a = input("elija destino ")
if a == marte:
    print("sucantida de combustible es: ",costos[0])
elif a == luna:
    print("la cantidad de combustible es: ",costos[1])
else: 
    print("su cantidad de combustible es: ",costos[-1])
