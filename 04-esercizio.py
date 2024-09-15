#Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore

dizionario = {"a": 1, "b": 2, "c": 3}

chiavi = list(dizionario.keys())        #trasformo in liste i dati forniti dalle funzioni keys e values
valori = list(dizionario.values())      #in questo modo vado ad avere una copia statica dei dati

# print(chiavi)
# print(valori)

dizionario.clear()

# print(dizionario)

for oldKey in chiavi:
    dizionario[valori[chiavi.index(oldKey)]] = oldKey

print(dizionario)
