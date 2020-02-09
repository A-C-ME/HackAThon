import math
import itertools

start = [0,0, "start"]
checkout = [-45.5,16, "checkout"]

bakery = [-85,23,"bakery"]
meat = [-88,63,"meat"]
paperAndCleaning = [-73,76,"paper and cleaning"]
adultBeverages = [-63,88,"adult beverages"]
cartRoom = [-75,0,"cart room"]
baby = [-48.4,82,"baby"]
girlsClothing = [-52,60,"girl clothing"]
boysClothing = [-40,60,"boy clothing"]
shoes = [-35,82,"shoes"]
womensAcc = [-53,47,"womens accessories"]
intimateApp = [-45,47,"intimate apparel"]
mensWear = [-26.5,55,"mens wear"]
subway = [-48,24,"subway"]
womensWear = [-39,34,"womens wear"]
candy = [-29,22.5,"candy"]
jewelry = [-13,34,"jewelry"]
crafts = [-17,81,"crafts and sewing"]
waterFountain = [-30,93,"drinking fountain"]
cosmetics = [-4,34,"cosmetics"]
houseware = [0,48,"houseware"]
healthAndBeauty = [22,18,"health and beauty"]
petCare = [38,18,"pet care"]
garden = [60,18,"garden"]
hardware = [39,50,"hardware"]
toys = [27,36,"toys"]
paint = [27,53,"paint"]
autocare = [27,63,"autocare"]
celebrations = [9,31,"celebrations"]
furniture = [9,65,"furniture"]
homedecor = [9,50,"home decor and appliances"]
wireless = [5,77,"wireless"]
videogames = [12,77,"video games"]
sports = [29,80,"sports"]
fruitsAndVeggies = [-72,27,"fruits and veggies"]
frozen = [-72,42,"frozen"]
cannedFood = [-72,53,"canned food"]
snacks = [-72,65,"snacks"]
drinks = [-72,84,"drinks"]
dairy = [-90,94,"dairy"]

totDistancesForPerms = []

def calc(points):
    totDistance = 0
    for i in range(len(points))[1:]:
        totDistance+=math.sqrt( ((points[i][0]-points[i-1][0])**2)+((points[i][1]-points[i][1])**2))
    return totDistance

points = [toys, sports, dairy, cannedFood, frozen, fruitsAndVeggies, intimateApp, hardware, houseware]

perms = list(itertools.permutations(points))

for i in perms:
    i = list(i)
    i.insert(0, start)
    i.append(checkout)
    i = tuple(i)
    totDistancesForPerms.append(calc(i))
print(perms[totDistancesForPerms.index(min(totDistancesForPerms))])


