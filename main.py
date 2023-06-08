import csv
import pandas as pd
from scipy.spatial import distance

import numpy as np

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








def distance_point_to_curve(x0, y0, x_curve, y_curve):
    distances = np.sqrt((x0 - x_curve)**2 + (y0 - y_curve)**2)
    #min_distance = np.min(distances)
    return distances





#współrzędne krzywej trendu
x_trend_points=[1,2,3.656,4,5,6,7,8,9,1]
y_trend_points=[1,20,30,40,50,60,70,80,90,1]


#badane punkty

x_exam_points=[1,20,30,40.765,50,60,70,80,90,100]
y_exam_points=[1,20,30,40,50,60,70,80,90,100]


def main_iteration(x1,y1,x,y):
    dist_all=[]
    for i in range(len(x)):
        dist_sum = []
        x0=x[i]
        y0=y[i]
        for j in range (len(x1)):
            a = (distance_point_to_curve(x0,y0,x1[j],y1[j]))
            dist_sum.append(a)
        min_distance = min(dist_sum)
        dist_all.append(min_distance)
    return dist_all



print(main_iteration(x_trend_points,y_trend_points,x_exam_points,y_exam_points))


