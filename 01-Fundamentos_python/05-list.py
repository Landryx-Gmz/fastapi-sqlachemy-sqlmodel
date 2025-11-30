# --Lista--
list_number = [1,2,3,4,5,7,6] # ordenado
list_letters = ['a', 'b', 'c']
list_mix = [2, 'z', True, [1,2,3], 4.3]


shopping_cart = ["Laptop", "Silla Gamer", "Café"]

print(type(list_mix))
print(list_number)


# --Métodos--

# append

list_number.append(100)
print(list_number)
list_number.append(200)
print(list_number)

# remove

list_number.remove(1) # remueve el valor no el indice
print(list_number)

# count

print(list_number.count(5))

# .copy() copiar
# .sort() ordenar
list_number.sort()
print(list_number)
