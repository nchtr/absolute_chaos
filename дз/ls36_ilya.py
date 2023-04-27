#1 tested
class TooLOngNameErr(Exception):
    def __init__(self, msg) -> None:
        super().__init__(msg)


def check_name(name):
    if len(name)>4:
        raise TooLOngNameErr('pick a shorter name')
    else:
        print(name)



#2 not tested
DefaultDeposit=300
Bin=4.5
def ordinary_rate(StartDeposit, Bin, RateInYear):
    TotalAmount = StartDeposit *(1+Bin*RateInYear)
    profit = TotalAmount - StartDeposit
    return f'Итоговая сумма {profit}'
    

def bonus_method(StartDeposit, DefaultDeposit):
    if StartDeposit>DefaultDeposit:return f'Итоговая сумма {StartDeposit+StartDeposit/((DefaultDeposit/StartDeposit)*100)}'
    else:return f'Итоговая сумма {StartDeposit}'
    
     
def capt_method(StartDeposit, RateInYear, TotalAmountYear):
    AmountMonth = 12 * TotalAmountYear
    def forMonth(StartDeposit, RateInYear, AmountMonth):
        if (AmountMonth == 0): return StartDeposit
        return forMonth(StartDeposit, RateInYear, AmountMonth-1)*(1+RateInYear/100/12)
    profit = forMonth(StartDeposit, RateInYear, AmountMonth)
    print("Полученная прибыль: ",  profit - StartDeposit)
    print("Итоговая сумма вклада: ", profit)
    
print("Programm")
choose=input("Choose methon:\n1-Fast\t2-Bonus\t3-Capital").lower()
try: #seems like it's working
    ordinary_rate(float(input('Start Deposit = ')),Bin,float(input('Period = '))) if choose=='1' or choose=='fast' else None
    bonus_method(float(input('Start Deposit = ')), DefaultDeposit) if choose=='1' or choose=='bonus' else None
    capt_method(float(input('Start Deposit = ')), float(input('Period = ')), float(input('Full period = '))) if choose=='3' or choose=='capital' else None
except ValueError: 
    print("Enter numbers instead something else")
except ZeroDivisionError:
    print("Are u poor or joking?")