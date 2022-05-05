import random
import pprint

mt1 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]
mt2 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]
mt3 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]
mt4 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]
mt5 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]
mt6 = ["a_phero", "b_saolo", "c_herode", "d_giakeu", "e_nathan", "f_abra",None]

team1=[]
team2=[]
team3=[]
team4=[]
team5=[]
team6=[]

for i in range(6):
    check1 = False
    check2 = False
    check3 = False
    while True:
        r1 = random.choice(mt1)
        r2 = random.choice(mt2)
        if r1 == r2:
            continue
        r3 = random.choice(mt3)
        if r1 == r3 or r2 == r3:
            continue
        r4 = random.choice(mt4)
        if r1 == r4:
            continue
        r5 = random.choice(mt5)
        if r1 == r5:
            continue
        r6 = random.choice(mt6)
        if r1 == r6:
            continue

        if r1 == None or r2 == None:
            continue
        if r3 == None or r4 == None:
            continue
        if r5 == None or r6 == None:
            continue
        if r2 == r4:
            continue
        if r2 == r5:
            continue
        if r2 == r6:
            continue
        if r3 == r4:
            continue
        if r3 == r5:
            continue
        if r3 == r6:
            continue
        if r4 == r6:
            continue
        if r4 == r5:
            continue
        if r5 == r6:
            continue
        if r1 not in team1 and r2 not in team2:
            check1 = True
        if  r3 not in team3 and r4 not in team4:
            check2 = True
        if r5 not in team5 and r6 not in team6:
            check3 =True

        if check1 and check2 and check3:
            team1.append(r1)
            team2.append(r2)
            team3.append(r3)
            team4.append(r4)
            team5.append(r5)
            team6.append(r6)
            mt1.remove(r1)
            mt2.remove(r2)
            mt3.remove(r3)
            mt4.remove(r4)
            mt5.remove(r5)
            mt6.remove(r6)
            break

teams_road =[]
teams_road.append(team1)
teams_road.append(team2)
teams_road.append(team3)
teams_road.append(team4)
teams_road.append(team5)
teams_road.append(team6)

son = []
phero = []
saolo = []
herode = []
giakeu = []
nathan = []
abra = []

pprint.pprint(teams_road)




"yesss"

"nooo"
"sdasdasdasdasdasd"