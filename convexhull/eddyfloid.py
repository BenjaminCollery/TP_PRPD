from convexhull.utils import *

def convexHullEddyfloid(pts):
    convex_hull = []

    ## on recupère les deux points d'abcisses extrémales et on les ajoute à convex hull
    minXPoint = pts[0]
    maxXPpoint = pts[0]
    for p in pts:
        if p[0] < minXPoint[0]:
            minXPoint = p
        if p[0] > maxXPpoint[0]:
            maxXPpoint = p
    convex_hull.append(minXPoint)
    convex_hull.append(maxXPpoint)

    listeBas =[]
    listeHaut = []

    for p in pts:
        if determinant(minXPoint,maxXPpoint,p) < 0:
            listeBas.append(p)
        else:
            listeHaut.append(p)

    convex_hull_1 = findHull(listeBas,minXPoint,maxXPpoint)
    convex_hull_2 = findHull(listeHaut,maxXPpoint,minXPoint)
    for p in convex_hull_1:
        convex_hull.append(p)
    for p in convex_hull_2:
        convex_hull.append(p)

    return convex_hull



def findHull(pts,p1,p2):
    if pts == []:
        return

    farthestPoint= p1
    line = []
    convex_hull = []
    line.append(p1)
    line.append(p2)

    for p in pts:
        if(distance_from_point_to_line(p,line) > distance_from_point_to_line(farthestPoint,line)):
            farthestPoint = p

    convex_hull.append(p1)
    convex_hull.append(p2)
    convex_hull.append(farthestPoint)

    pointsInsideTriangle = []
    pointsOnRightSide = []
    pointsOnLeftSide = []

    for p in pts:
        if determinant(p1,farthestPoint,p) <0:
            pointsOnLeftSide.append(p)
        if determinant(p2,farthestPoint,p) <0:
            pointsOnRightSide.append(p)

    findHull(pointsOnLeftSide,p1,farthestPoint)
    findHull(pointsOnRightSide,farthestPoint,p2)

    return convex_hull

