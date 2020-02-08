import math

start = [0,0]
milk = [-87,95, "milk"]
chair =  [2,70, "chair"]
panties = [-40,42, "panties"]
legos = [17,45, "legos"]
soil = [65, 20, "soil"]

points = [milk, chair, panties, legos, soil]
def shortestPath(start, points):
    tmpIndex = 0
    index = 0
    item = points[0][2]
    distance = math.sqrt( ((points[0][0]-start[0])**2)+((points[0][1]-start[1])**2))
    for i in points[1:]:
        tmpIndex += 1
        if (math.sqrt( ((i[0]-start[0])**2)+((i[1]-start[1])**2)) < distance):
            distance = math.sqrt( ((i[0]-start[0])**2)+((i[1]-start[1])**2))
            index = tmpIndex
            item = points[index][2]
    print(item)
    newStart = [points[index][0],points[index][1]]
    del points[index]
    if len(points)>0:
        shortestPath(newStart, points)



shortestPath(start, points)