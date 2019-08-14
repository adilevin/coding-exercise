"""
THIS PROBLEM SHOULD BE DONE AFTER YOU HAVE SOLVED fit_circle.py PROBLEM.

Problem:

Given set of (x,y) points in the plane, sampled in the vicinity of a circular arc,
estimate the circle's radius and center point.

We will check how good your estimated circle approximate points which are not on the arc necessarily.

How to get started:

Run this script. It will read the input points and plot them. Then, add your
code below (see comments).

"""

from utils import read_pnts, plot_points, save_answer

pnts = read_pnts('./training_data_partial.npy')
plot_points(pnts)
#
# Here you should complete an algorithm to estimate the circle radius and center
#
estimated_radius, estimated_center = 1.0, (2.0, 3.0)
#
# In the end, save the estimates circle coordinates to a file
#
save_answer('./estimated_circle_coordinates_partial.json', estimated_radius, estimated_center)