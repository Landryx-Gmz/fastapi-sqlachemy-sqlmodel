
#and

age = 15
licensed = True

if age >= 18 and license:
    print("Puedes conducir")
else:
    print("No puedes conducir")

# or

is_studients = False
membership = False

if is_studients or membership:
    print("Obtiene precio especial")
else:
    print("Precio normal")

# not

is_admin = True
if not is_admin:
    print("Acceso denegado")
else:
    print("Acceso permitido")

# Short Circuiting
name = False
print(name and name.upper())