string = "teste"
string1 = ""
string2 = ""

if len(string) % 2 != 0:
    string2 += string[len(string)//2]

# Percorrendo a string até a metade
for i in range(len(string)//2):
    string1 += string[len(string)-1-i]
    string2 += string[(len(string)//2-1)-i]

# Unir as duas partes
string_invertida = string1 + string2

print("String original: ", string)
print("String invertida: ", string_invertida)