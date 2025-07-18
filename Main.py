
from Events import event_list
import random
#Values=(multiplier,start_value)
#Types; Oil, Military, Civillian, Agriculture, Technology, Industry, Transport, Gold
types=["oil","mil","civ","agr","tec","ind","trn","gol"]
portf=[0,0,0,0,0,0,0,0]
money=1000
year=1900
values_list=[0,0,0,0,0,0,0,0]
event_years=[]
event_order=[]

def event_occur(event,values):
    global types
    print(event["name"])
    print(event["desc"])
    for i in types:
        effect=(event[i])
        edit=(values[i])
        edit[0]+=effect[0]
        edit[1]+=effect[1]
        values[i]=edit

def random_change(values):
    for i in types:
        edit=(values[i])
        edit[0]+=random.randint(-5,5)
        edit[1]+=random.randint(-10,10)
        values[i]=edit

def clamp(value,minvalue,maxvalue):
    value=max(minvalue, min(value, maxvalue))
    return value

def buy(type,amount):
    global portf,money,values
    price=values[type]
    price=price[1]
    cost=price*amount
    if cost>money:
        return "Can't afford"
    else:
        money-=cost
        position=types.index(type)
        portf[position]+=amount
        return ("bought "+str(amount)+" stocks of "+type+" for "+str(cost)+"$")

def sell(type,amount):
    global portf,money,values
    position=types.index(type)
    price=values[type]
    price=price[1]
    cost=price*amount
    if amount>portf[position]:
        return "Not enough stocks"
    else:
        money+=cost
        portf[position]-=amount
        return ("sold "+str(amount)+" stocks of "+type+" for "+str(cost)+"$")
    
def get_values(values):
    values_list=[0,0,0,0,0,0,0,0]
    x=0
    for i in types:
        edit=(values[i])
        data=edit[1]
        values_list[x]=data
        x+=1
    return values_list

values={
    "oil":[25,300],
    "mil":[-5,125],
    "civ":[15,200],
    "agr":[5,250],
    "tec":[10,100],
    "ind":[20,350],
    "trn":[5,250],
    "gol":[2,125]
    }


for x in event_list:
    range=x["years"]
    event_years.append(range)
    event_order.append(x)
#RUNNING LOOP ---------------------------------------------------------------------------------

while True:
    choice=input("buy/sell")
    type=input("type")
    amount=input()
    try:
        amount=int(amount)
    except:
        print("invalid amount")
    if choice=="buy":
        message=buy(type,amount)
        print(message)
    elif choice=="sell":
        message=sell(type,amount)
        print(message)
    random_change(values)
    print(portf)
    print(money)
    year+=1
    try:
        event_number=event_years.index(year)
        event=event_order[event_number]
        event_occur(event,values)
    except:
        pass
    print(get_values(values))
    print(year)