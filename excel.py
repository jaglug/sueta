import pandas as pd
print("Введите 1 год")
ngod=int(input())
print("Введите последний год")
pgod=int(input())
a=[]
b=[]
s='Год'
c=['','','','','','','','','','','','']
mes = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
god=[2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
#df = pd.DataFrame({'Месяц': mes, 'Год':god})
#df.to_excel ('C:/Users/Admin/Desktop/xform.xlsx',sheet_name='formulyar', index=False)

for k in range (ngod,pgod+1):
    print(k)
    break
for j in mes:
    print(j)
for i in range(ngod,pgod+1):
    for j in mes:
        print(i,j,end="\t")
#a.append(k)
#df=pd.DataFrame({'Год':a})

#df.to_excel ('C:/Users/Admin/Desktop/xform.xlsx',sheet_name='formulyar', index=False)
"""
for j in god:
    a.append(j)
df=pd.DataFrame({'Год':a})
    
for i in mes:
    b.append(i)
df=pd.DataFrame({'Год':c,'Месяц':b})
df.to_excel ('C:/Users/Admin/Desktop/xform.xlsx',sheet_name='formulyar', index=False)
"""