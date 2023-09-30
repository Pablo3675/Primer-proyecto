Diccionario = {"XD":"Es una forma de expresar algo gracioso", "LOL":"Basicamente lo mismo que XD", "F":"Se usa cuando sucede algo triste", "Hype":"Se usa cuando algo genera mucha intriga", "Hater":"Una persona que odia a alguien en internet sin razón alguna"}

x = input("Que palabra te gustaría conocer?:")

if x in Diccionario.keys():
    print(Diccionario[x])
    
else:
    print("Esa palabra no se encuentra en el diccionario.")
