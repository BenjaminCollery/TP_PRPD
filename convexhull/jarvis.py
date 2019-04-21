from convexhull.utils import *

def jarvis(pts):

    ## point le plus à gauche
    copy_pts = list(pts)
    anchor_point = pts[0]
    for p in pts:
        if p[0] < anchor_point[0]:
            anchor_point = p

    ## point de même abscisse que anchor, pour trouver le second point
    init_point = []
    init_point.append(anchor_point[0])
    init_point.append(anchor_point[1]-1)
    print(anchor_point)
    print(init_point)
    convex_hull= [anchor_point]

    ## calcul du second point de convex hull
    convex_point = copy_pts[0]
    for p in copy_pts:

        n = len(convex_hull)
        if p!=convex_point and p!= convex_hull[n-1] and  determinant(init_point, convex_hull[n - 1], p) < determinant(init_point, convex_hull[n - 1] ,
                                                                                convex_point):
            convex_point = p
    convex_hull.append(convex_point)
    del copy_pts[copy_pts.index(convex_point)]
    scatter_plot(pts, [convex_hull], title="convex hull : final result", show=True)

    n = len(convex_hull)

    print("deuxième boucle")
    print(copy_pts)

    fin = False

    while convex_point != convex_hull[0]:
        print('hull entrée')
        print(convex_hull)
        print('ok')
        convex_point = copy_pts[0]
        for p in copy_pts:
          n = len(convex_hull)
          if determinant(convex_hull[n-1],convex_point,p) > 0 or(determinant(convex_hull[n-1],convex_point,p) == 0 and distance(convex_hull[n-1],p) > distance(convex_hull[n-1],convex_point)):
            convex_point = p

        convex_hull.append(convex_point)
        del copy_pts[copy_pts.index(convex_point)]
        print('copy')
        print(copy_pts)
        print('hull')
        print(convex_hull)

        scatter_plot(pts, [convex_hull], title="convex hull : final result", show=True)



    return convex_hull