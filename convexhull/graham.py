from convexhull.utils import *


def graham_convex_hull(pts):
    min = 0
    max = 10
    points = pts
    print(points)
    anchor_point = points[0];
    for p in points:
        if p[1]< anchor_point[1]:
            anchor_point = p
        else:
            if p[1] == anchor_point[1] and p[0] < anchor_point[0]:
                anchor_point = p
    ordered_points = polar_quicksort(points, anchor_point)

    convexhull = []
    convexhull.append(ordered_points[0])
    convexhull.append(ordered_points[1])
    print(convexhull)

    for p in range(2,len(ordered_points)):
        n = len(convexhull)

        while n >= 2 and determinant(convexhull[n-2],convexhull[n-1],ordered_points[p]) <= 0:
            convexhull.pop()
            n = len(convexhull)
            print(n)

        scatter_plot(points, [convexhull], title="Graham search", show=True)
        convexhull.append(ordered_points[p])

    return convexhull


############