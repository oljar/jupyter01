import csv
import pandas as pd
from scipy.spatial import distance
import numpy.polynomial.polynomial as poly
import matplotlib.pyplot as plt
import numpy as np
import math
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



############################################################

# examinated points

x_tag = 'M51: Pa'

y_tag ='M53: Pa'


df = pd.read_csv("data_3.csv",sep=';', decimal=',')
df = df.sort_values(by=x_tag, ascending=True)


def main_proces(df,dist_border=10000000):

    # input filters
    df = df[df[x_tag]>= 0]
    df = df[df[y_tag]>= 0]
    df[x_tag] = df[x_tag].fillna(df[x_tag].median())
    df[y_tag] = df[y_tag].fillna(df[y_tag].median())




    x_points = (df[x_tag]).tolist() # definition of columns -x

    c=41.1 # reducer constns
    x_exam_points = [(c * math.sqrt(x) )for x in x_points]

    y_exam_points = (df[y_tag]).tolist() # definition of columns -y


    deg = 2

    # trend line



    start = x_exam_points[0]
    stop = x_exam_points[(len(x_exam_points)-1)]

    #  precision of sampling
    step = 0.1
    sequence = list(np.arange (start, stop, step))
    x_trend_points = sequence


    # coefficients od polynomial 2-grade (trend)
    coefs = poly.polyfit(x_exam_points, y_exam_points, deg)


    y_trend_points = poly.polyval(x_trend_points, coefs)


    def distance_point_to_curve(x0, y0, x_curve, y_curve):
        distances = np.sqrt((x0 - x_curve)**2 + (y0 - y_curve)**2)
        #min_distance = np.min(distances)
        return distances



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







    sol_dist_pd = pd.DataFrame(main_iteration(x_trend_points,y_trend_points,x_exam_points,y_exam_points))

    # print(f'd {sol_dist_pd}')
    # print(f'X {x_exam_points}')
    # print(f'Y {y_exam_points}')

    sol_exam=pd.DataFrame()
    sol_exam['dist'] = sol_dist_pd
    sol_exam['X_Exam'] =  x_exam_points
    sol_exam['Y_Exam'] = y_exam_points

    print('examinated points with distance')
    print(sol_exam)


    sol_trend=pd.DataFrame()
    sol_trend['X_Trend'] = pd.DataFrame(x_trend_points)
    sol_trend['Y_Trend']  = pd.DataFrame(y_trend_points)


    #print(sol_trend)

    print('y trend')
    print (f'Krzywa - y = {coefs[2]}x^2 + {coefs[1]}x + {coefs[0]}' )

    # distance border
    filtred = sol_exam[sol_exam['dist'] < dist_border]

    return filtred,sol_trend




def chart(sol_exam,sol_trend):

    plt.plot(sol_exam['X_Exam'], sol_exam['Y_Exam'], "-o")

    plt.plot(sol_trend['X_Trend'], sol_trend['Y_Trend'], "-s")

    plt.show()



sol_exam,sol_trend = main_proces(df)

chart(sol_exam,sol_trend)

df = main_proces(df)[0]
df = df.rename(columns={'X_Exam': x_tag})
df = df.rename(columns={'Y_Exam': y_tag})
print (df)
sol_exam,sol_trend  = main_proces(df,10000000)


chart(sol_exam,sol_trend)

# filtrowanie


# print('filtred')
# print(filtred)
#
# plt.plot(filtred['X_Exam'], filtred['Y_Exam'],"-o")
#
# plt.plot(sol_trend['X_Trend'], sol_trend['Y_Trend'],"-s")
#
# plt.show()

