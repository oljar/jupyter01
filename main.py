import csv
import pandas as pd
#
# fake_dataset = pd.read_csv('example1.csv',header=None, sep=';',decimal=',')
#
# print(fake_dataset)
#
#
# df = fake_dataset.fillna(fake_dataset.median(axis=0))
#
# print('####################')
# print (df)
#
# df.to_csv('example_2.csv', encoding='utf-8')4


# otwieranie pliku csv i iteracja csv
with open('example1.csv', 'r') as csvfile:
    lista_list = csv.reader(csvfile, delimiter=';')
    filtered_list = []

    for sublist in lista_list:
        filtered_sublist = []
        for element in sublist:


                element = element.replace(",", ".")

                try:
                    element = float(element)
                except:
                    continue

                filtered_sublist.append(element)

        filtered_list.append(filtered_sublist)

# konwersja csv do DataFrame
print(filtered_list)
df = pd.DataFrame(filtered_list)





print (df)

# iterracja DataFrame


for i in range((df.shape)[0]):
    for j in range((df.shape)[1]):
        print(df.iloc[i,j])

#zapis do csv
z = df.to_csv()
print(z)

# zapis do csv bez indeksu i nagłówka
x =df.to_csv( header=False, index=False)

print(x)



print (df)




# filtracja

a =df[df>1]

print (a)

# uzupełnienie zerem  NaN
b=df.fillna(0)

print(b)

# uzupełnienie średnią NaN
c=df.fillna(df.mean())
print (c)

# uzupełnienie medianą NaN
c=df.fillna(df.median())
print (c)

# zapis DataFrame do CSV
print(a.to_csv( header=False, index=False, sep= ';'))






# filtracja w określonej kolumnie
print('przewijanie po kolumnach ')
for i in range(0,2):

    d =df.loc[df[i]>1,i]

    print (d)


#filtracja

e =df[df>3]
print (e)
#usuawnie NaN w kolumnach
f=e.dropna(axis=1, how='all')
print (f)