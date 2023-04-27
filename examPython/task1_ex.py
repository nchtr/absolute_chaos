#яндере код))))))))
from time import sleep
import sys


class Pizza:
    '''Пицца. Базовая и вкусная. Подойдет для новичков'''
    def __init__(self) -> None:
        self._dough=False
        self._cheese=True
        self._tasty=False
        self._ingredientsCollected=False
        self._formed=False
        self._baked=False
        self._cutted=False
        self._packed=False
    
    def prepare(self):
        print("ПИЦЦА ГОТОВИТСЯ")
        self._dough=True
        self._ingredientsCollected=True
        self._formed=True
        sleep(0.5)
        print("Пицца успешно приготовлена и отправляется на следующий этап готовки")
        
    def bake(self):
        print("ПИЦЦА ЗАПЕКАЕТСЯ")
        sleep(1.5)
        self._baked=True
        self._tasty=True
        print('Пицца испеклась без инцидентов')
    
    def cut(self):
        print('ПИЦЦА НАРЕЗАЕТСЯ')
        sleep(0.5)
        self._cutted=True
        print("Пицца нарезана. (нет, она не нашинкована)")
        
    def pack(self):
        print('ПИЦЦА УПАКОВЫВАЕТСЯ')
        sleep(0.3)
        self._packed=True
        print('Пицца упакована и ожидает вас.')
        
    
class Pepperoni(Pizza):
    '''Отличительной чертой пиццы «Пепперони» является ее остро-жгучий вкус. В этой пицце главную роль играет колбаса «Пепперони», нарезанная небольшими кусочками.'''
    unusualIngredient='Pepperoni'
    price=1600
    def __init__(self) -> None:
        super().__init__()
        
    def getPrice(self):
        return self.price
        
class BBQ(Pizza):
    '''Пицца BBQ - это сочетание пикантной итальянской колбасы Салями, нежного сыра "Моцарелла", сочной ветчины, грибов и специального пряного соуса BBQ на хрустящем тесте.'''
    unusualIngredient='Barbecue sauce'
    price=1800
    def __init__(self) -> None:
        super().__init__()
    def getPrice(self):
        return self.price
        
class SeafoodPizza(Pizza):
    '''Пицца Дары Моря. Соус бешамель,сыр моцарелла, тигровые креветки, филе лосося, шампиньоны, сладкий перец.'''
    unusualIngredient='Salmon'
    price=2200
    def __init__(self) -> None:
        super().__init__()
        
    def getPrice(self):
        return self.price
        
        
print('Меню:\n1-Пицца Пеперони\n2-Пицца BBQ\n3-Пицца Дары Моря')
taskList=[]
for userChoise in range(4):
    choose=input('Выберите желаемую пиццу:\t').lower()
    if choose=='1':taskList.append(1)
    elif choose=='пицца пеперони':taskList.append(1)
    elif choose=='2':taskList.append(2)
    elif choose=='пицца bbq':taskList.append(2)
    elif choose=='3':taskList.append(3)
    elif choose=='пицца даря моря':taskList.append(3)
    else:
        print('Здесь нет такого, поэтому вы лишаетесь одного элемента в заказе')
        
print('Подтвердите заказ:')
confirm=input('1-подтверждаю\t2-отмена').lower()
peperoni=Pepperoni()
bbq=BBQ()
sea=SeafoodPizza()
priceList=[]
for item in taskList:
    if item==1:priceList.append(peperoni.getPrice())
    elif item==2:priceList.append(bbq.getPrice())
    elif item==3:priceList.append(sea.getPrice())
price_sum=0
for price in priceList:
    price_sum+=price
if confirm=='1' or 'подтверждаю':
    print(f'ЧЕК:\nЗаказ из {len(priceList)} продуктов.\nСумма:{price_sum}')
    for item in taskList:
        if item==1:
            peperoni.prepare()
            peperoni.bake()
            peperoni.cut()
            peperoni.pack()
        elif item==2:
            bbq.prepare()
            bbq.bake()
            bbq.cut()
            bbq.pack()
        elif item==3:
            sea.prepare()
            sea.bake()
            sea.cut()
            sea.pack()
        print("Все готово")
else:
    print('Заказ отменен')
    sys.exit()

