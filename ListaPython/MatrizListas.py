import pandas as pd

dicionario1 = {'A': [[1,2,3],[4,5,6],[7,8,9]],
                'B': [[1,3,5],[3,5,6],[7,8,9]],
                }

df = pd.DataFrame(dicionario1)

print(df)

def uniao_repeticao(row):
    combinar_lista = []

    for item in row['A'] + row['B']:
        if item not in combinar_lista:
            combinar_lista.append(item)
    return combinar_lista

df['C'] = df.apply(uniao_repeticao, axis=1)

print(df)





