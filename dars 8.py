#sort() methodi
cars=['bmw','benz','audi','lambo','ferrari','bugatti','aston martin','bentley','porsche']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#asl listni tartibini buzmagan holda tartiblash un ##sorted() metodidan foydalanamiz
cars=['bmw','benz','audi','lambo','ferrari','bugatti','aston martin','bentley','porsche']
print(sorted(cars))
print(sorted(cars,reverse=True))
numbers=[123,12,34,12,333,23,4456,76,4,-43,-52]
numbers.sort()
print(numbers)
print(sorted(numbers,reverse=True))
#reverse orqali royxatni boshini oxiriga oxirini boshiga aylantirish
#LEN royxatni uzunligini aniqlash
cars=['bmw','benz','audi','lambo','ferrari','bugatti','aston martin','bentley','porsche']
print(len(cars))
#RANGE() funksiyasi
sonlar=list(range(0,10))
print(sonlar)
#range yordamida qadamlarni berish mumkin
juft=list(range(0,20,2))
toq=list(range(1,20,2))
print(juft)
print(toq)
narhlar = [13000, 14500, 1325672, 10800, 2100, 13454, 18000]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
#royxatni kesish
cars=['bmw','benz','audi','lambo','ferrari','bugatti','aston martin','bentley','porsche']
my_cars=cars[1:4]
print(my_cars)
print(cars[:6])
print(cars[3:])
cars1=cars[:]
tomonlar=(20,25,30,35)
print(tomonlar)#tuple type -ozgarmas 
#bunga ozgartirish kiritish un typeini listga ozgartiramiz
countries=['uzb','russia','france','italy','germany']
print(countries)
print(len(countries))
print(sorted(countries))
print(sorted(countries,reverse=True))
print(countries)
countries.reverse()
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
juft_sonlar=list(range(120,1200,2))
print(juft_sonlar)
print(sum(juft_sonlar))
print(max(juft_sonlar)-min(juft_sonlar))
print(len(juft_sonlar))
print(juft_sonlar[:20])
print(juft_sonlar[:-20])
print(juft_sonlar[540:560])
taomlar=['manti','honim','osh','jiz','beshbarmak','bilinshik','kasha']
nonushta=taomlar[:]
nonushta.remove('manti')
nonushta.remove('osh')
nonushta.remove('honim')
nonushta.remove('jiz')
nonushta.remove('beshbarmak')
print(nonushta)
nonushta.append('sut')
nonushta.insert(1,'saryog\'')
nonushta.insert(3,'issiq non')
print(nonushta)
print(taomlar)
nonushta=tuple(nonushta)
