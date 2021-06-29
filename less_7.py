# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 06:11:46 2021

@author: Islom.Xorazov
"""

fruits=['olma','gilos','banan','behi','shaftoli','olcha']
costs=[10000,12000,30000,15000]
sonlar=['bir''ikki','uch',4,5,6]
names=[]#empty list
fruits=['olma','gilos','banan','behi','shaftoli','olcha']
print("birinchi meva :",fruits[0].upper())
print('ikkinchi meva: ',fruits[1].title())
print(costs[3]+costs[0])
car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
print(car_models[-1]) 
costs[0]=11500
costs[3]=18600
print(costs)
#.append('qiymat') method
fruits.append('nok')
fruits.append('qulupnay')
print(fruits)
#odatda bosh listlarni toldiramiz append yordamida 
my_fri=[]
my_fri.append('Eltin')
my_fri.append('Shurik')
my_fri.append('Islom')
my_fri.append('Bek')
print(my_fri)
#insert (indeks,'qiymat')method
car_models.insert(0,'audi')
car_models.insert(3,'lambo')
car_models.insert(5,'bugatti')
print(car_models)
del car_models[4]
del car_models[-2]
del car_models[-3]
print(car_models)
#listimizda element kop bolib ,qiymatni indeksini bilmasak,qiymatni nomidan foydalanamiz.
#REMOVE('qiymat')
car_models.remove('GM')
car_models.remove('Toyota')
car_models.remove('Hyundai')
print(car_models) 
#POP(indeks)
car_models =['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
expen_cars=car_models.pop(3)
print(expen_cars)
#SOL_EXERCISE.
choyxona=[]
choyxona.append('alish')
choyxona.append('ali')
choyxona.append('vali')
print('salom '+choyxona[1]+', bugun yig\'ilamizmi?')
print(choyxona[0]+', qandaysan?')
nums=[123,32,17,45,1,-53,]
nums[1]=nums[1]/8
nums[4]=nums[4]-10.1
print(nums)
t_peop=['alisher navoiy','beruniy','ibn sino']
z_peop=['laziz adhamov','ali','vali',]
my=t_peop.pop(2)
my1=z_peop.pop(0)
print('men tarixiy shaxslardan '+my+' ni ,zamonaviy shaxslardan esa  '+ my1+' ni hurmat qilaman')