from convexhull.utils import *
import operator


def convexHullShamos(pts):

    convex_hull = []
    convex_hull = partition(pts,convex_hull)

    return convex_hull



def partition(pts,convex_hull):
    convex_hull = []
    pts = sorted(sorted(pts,key = operator.itemgetter(1)), key = operator.itemgetter(0))
    p = [0,0]
    ## condition d'arrêt , lorsque notre nuage de points est de taille 3
    ## le nuage est donc le convex hull
    if len(pts)<=3:
        for i in range(0,len(pts)):
            convex_hull.append(pts[i])
        if len(pts) == 3 and determinant(convex_hull[0],convex_hull[1],convex_hull[2]):
            p = convex_hull[1]
            convex_hull.remove(p)
            convex_hull.add(p)
        return convex_hull

    list1 = []
    list2 = []

    for i in range(0,len(pts)//2):
        list1.append(pts[i])

    for i in range((len(pts)//2) , len(pts)):
        list2.append(pts[i])

    convex_hull_1 = []
    convex_hull_2 = []

    convex_hull_1 = partition(list1,convex_hull_1)
    convex_hull_2 = partition(list2,convex_hull_2)

    convex_hull_aux = fusion(convex_hull_1,convex_hull_2)

    print(convex_hull_aux)
    for i in range(0,len(convex_hull_aux)):
        convex_hull.append(convex_hull_aux[i])

    return convex_hull



def fusion(convex_hull_1,convex_hull_2):

    if convex_hull_1 == []:
        return convex_hull_2

    if convex_hull_2 == []:
        return convex_hull_1


    imax =0
    for i in range(1,len(convex_hull_1)):
        if convex_hull_1[i][0] > convex_hull_1[imax][0]:
            imax = i


    imin =0
    ip1 = imax
    ip2 = imin
    b = True

    ## on détermine le segment du haut
    while b:
        b = False
        if determinant(convex_hull_2[ip2],convex_hull_1[ip1],convex_hull_1[(ip1+1)%len(convex_hull_1)]) >  0:
            ip1 = (ip1+1)%len(convex_hull_1)
            b = True
        if  determinant(convex_hull_1[ip1],convex_hull_2[ip2],convex_hull_2[(ip2-1+len(convex_hull_2))%len(convex_hull_2)]) <  0:
            ip2 = (ip2-1+len(convex_hull_2))%len(convex_hull_2)
            b = True

    im1 = imax
    im2 = imin

    b= True
    while b:
        b = False
        if determinant(convex_hull_2[im2], convex_hull_1[im1], convex_hull_1[(im1 - 1 + len(convex_hull_1)) % len(convex_hull_1)]) < 0:
            im1 = (im1 - 1 + len(convex_hull_1)) % len(convex_hull_1)
            b = True
        if determinant(convex_hull_1[im1], convex_hull_2[im2],convex_hull_2[(im2 + 1) % len(convex_hull_2)]) > 0:
            im2 = (im2 + 1) % len(convex_hull_2)
            b = True

    convex_hull = []
    for i in range(0,im1+1):
        convex_hull.append(convex_hull_1[i])

    if ip2 ==0:
        for i in range(im2,len(convex_hull_2)):
            convex_hull.append(convex_hull_2[i])
        convex_hull.append(convex_hull_2[0])
    else:
        for i in range(im2,ip2+1):
            convex_hull.append(convex_hull_2[i])

    if ip1 != 0:
        for i in range(ip1, len(convex_hull_1)):
            convex_hull.append(convex_hull_1[i])


    return convex_hull
