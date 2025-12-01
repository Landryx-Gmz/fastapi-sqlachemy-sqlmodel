
user = {
    "name": "Andy",
    "age": 36,
    "email": "andy@mail.com",
    "active": True,
    (18.23, -46.55): "Sevilla, España"
}
# Cambiar valores
user["name"] = "Andres"
user["age"] = "36"
print(user)
print(user["email"])
print(user[(18.23, -46.55)])

print("------------")
# values, items, keys

print(user.items())
print(user.keys())
print(user.values())

# Agregar claves y valores

user["country"] = "Sevilla"
print(user["country"])