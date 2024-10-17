try:
    tex= "eu nao sei"
    s = tex - 4

except TypeError:
    print("Texto e numero nao se soma")
try:
    print(inexistente)
except NameError:
    print("em tratamento")
try:
    b = [0]*1
    for x in range(2):
        print(b[x])
except IndexError:
    print("socorro")
"""try:"""
dirct = {"meu nome": }
print(dirct)