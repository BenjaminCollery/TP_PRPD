from random import seed

from convexhull.exhaustive import exhaustive
from convexhull.utils import create_points, scatter_plot
from convexhull import graham
from convexhull import jarvis
from convexhull import shamos
from convexhull import eddyfloid

def main():
    """
    A sample main program to test our algorithms.

    @return: None
    """
    # initialize the random generator seed to always use the same set of points
    seed(0)
    # creates some points
    pts = create_points(8)
    show = True  # to display a frame
    save = False  # to save into .png files in "figs" directory
    scatter_plot(pts, [[]], title="convex hull : initial set", show=show, save=save)
    print("Points:", pts)
    # compute the hull
    hull = eddyfloid.convexHullEddyfloid(pts)
    print("Hull:", hull)
    scatter_plot(pts, [hull], title="convex hull : final result", show=True)


if __name__ == "__main__":
    main()
