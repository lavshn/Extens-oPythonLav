cont = 1

while(cont <= 10):
  print(cont)
  contador = cont+1 

#------------------------

frutas = ["uva", "morango", "laranja"]
print(frutas[2])

#quantas frutas tem (length = tamanho)
print(len(frutas)) 

#add fruta
frutas.append("limao")

#ex while (i = index)
i=0
while(i<len(frutas)):
  print(frutas[i])
  i = i + 1

#ex for
print("Exemplo das frutas com FOR")
for fruta in frutas:
  print(fruta)

