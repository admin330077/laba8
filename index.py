contry = ['Германия',"США","Россия","Франция"]
town_germany = ['Лейпциг',"Нюрнберг","Берлин","Гамбург","Мюнхен"]
towm_usa = ["Нью-Йорк","Сан-Франциско","Чикаго","Лос-Анджелес","Вашингтон"]
town_russia = ["Москва","Санкт-Петербург","Екатеринбург","Нижний Новгород","Казань"]
towns_franch = ["Париж","Страсбург","Лион","Марсель","Ницца"]
for i in contry:
    print(i)

print('выберите страну')

user = input()

if user == 'Германия':
    for t in town_germany:
        print(t)
if user == 'США':
    for t in towm_usa:
        print(t)
        
if user == 'Россия':
    for t in town_russia:
        print(t)
if user == 'Франция':
    for t in towns_franch:
        print(t)
        
