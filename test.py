import pandas as pd
print("Введите месяц")
month=input()
print("Введите год")
year=int(input())
n=0
s=0
dni=[31,28,31,30,31,30,31,31,30,31,30,31]
vdni=[31,29,31,30,31,30,31,31,30,31,30,31]
mes = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
for i in mes:
    if i == month:
        a=11-mes.index(i)
n=11-a
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    with open ('C:/Users/Admin/Desktop/form.txt','w') as f:
        for j in mes:
            if mes.index(j)==n:
                l=mes.index(j)
                print("\n".join(mes[l:12]),file=f)
        for k in range(n,mes.index('Декабрь')+1):
            s=vdni[k]+s
            print(s,file=f) 
else:
    with open ('C:/Users/Admin/Desktop/form.txt','w') as f:
        for j in mes:
            if mes.index(j)==n:
                l=mes.index(j)
                print("\n".join(mes[l:12]),file=f)
        for k in range(n,mes.index('Декабрь')+1):
            s=dni[k]+s
            print(s,file=f) 




#index=mes.index('Сентябрь')#получение индекса элемента списка
#print(index)
#как начать с месяца? 1)поиск количества итераций, например если апрель,
#то необзодимо провести 7 итераций, и вывести результат
