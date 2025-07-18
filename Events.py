import random

'''
FORMAT:
name={
    "name":"name of event",
    "years":(minyear,maxyear),
    "desc":"description of event",
    "oil":(...),
    "mil":(...),
    "civ":(...),
    "agr":(...),
    "tec":(...),
    "ind":(...),
    "trn":(...),
    "gol":(...)
    }
...=(multiplier effect, immediate effect)
'''
event_list = [
    {
        "name":"US Steel founded",
        "years":(random.randint(1901,1905)),
        "desc":"US Steel has been founded by JP Morgan",
        "oil":(5,0),
        "mil":(0,5),
        "civ":(5,0),
        "agr":(-10,-15),
        "tec":(5,0),
        "ind":(15,50),
        "trn":(5,0),
        "gol":(5,0)
        },

    {
        "name":"First flight and car",
        "years":(random.randint(1905,1910)),
        "desc":"The first heavier than air flight, and the ford t enters production",
        "oil":(10,5),
        "mil":(5,0),
        "civ":(15,20),
        "agr":(5,0),
        "tec":(20,10),
        "ind":(10,5),
        "trn":(20,15),
        "gol":(0,0)
        },

    {
        "name":"Standard Oil Dissolved",
        "years":(random.randint(1908,1912)),
        "desc":"The monopoly standard oil has been split by the supreme court",
        "oil":(-30,-100),
        "mil":(-5,0),
        "civ":(-5,-5),
        "agr":(5,10),
        "tec":(-5,0),
        "ind":(-10,-20),
        "trn":(-10,-15),
        "gol":(5,0)
        },

    {
        "name":"Titanic sinks",
        "years":(random.randint(1908,1912)),
        "desc":"The RMS Titanic has sunk overnight in the North Atlantic",
        "oil":(0,0),
        "mil":(0,0),
        "civ":(-5,0),
        "agr":(0,0),
        "tec":(-5,0),
        "ind":(-10,-5),
        "trn":(-20,-30),
        "gol":(0,0)
        },

    {
        "name":"Coal mine explosion",
        "years":(random.randint(1908,1912)),
        "desc":"Catastrophic coal mine explosion kills dozens",
        "oil":(5,0),
        "mil":(0,0),
        "civ":(-5,-5),
        "agr":(5,0),
        "tec":(-5,0),
        "ind":(-20,-30),
        "trn":(-10,-5),
        "gol":(-5,0)
        },

    {
        "name":"War in Europe",
        "years":(random.randint(1912)),
        "desc":"Germany at war with France and Britain",
        "oil":(15,5),
        "mil":(20,30),
        "civ":(-15,-20),
        "agr":(-5,0),
        "tec":(10,5),
        "ind":(10,15),
        "trn":(10,10),
        "gol":(0,0)
        },

    {
        "name":"US Declares neutrality",
        "years":(1913),
        "desc":"The US chooses not to intervene in the Great War",
        "oil":(-10,-10),
        "mil":(-35,-40),
        "civ":(10,25),
        "agr":(10,0),
        "tec":(-5,0),
        "ind":(-10,0),
        "trn":(-5,0),
        "gol":(-2,0)
        },

    {
        "name":"Russian civil war",
        "years":(1913),
        "desc":"The Bolshviks have gained power in Russia",
        "oil":(-5,0),
        "mil":(15,20),
        "civ":(-5,0),
        "agr":(5,0),
        "tec":(5,0),
        "ind":(10,0),
        "trn":(0,0),
        "gol":(-2,0)
        },

    {
        "name":"US joins the war",
        "years":(1913),
        "desc":"The US is now siding with the allies",
        "oil":(-10,-10),
        "mil":(-35,-40),
        "civ":(10,25),
        "agr":(10,0),
        "tec":(-5,0),
        "ind":(-10,0),
        "trn":(-5,0),
        "gol":(-2,0)
        },
    ]




'''
1900
us steel
first flight and ford t
panama canal
standard oil
titanic sunk
coal mine explosion
ww1
us join war
russian revolution
war ends
steel strikes
league of nations
culture expands
1929
wallstreet crash
empire state building
japanese expand in pacific
'''