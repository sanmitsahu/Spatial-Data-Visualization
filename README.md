# Spatial Data Visualization
Capture spatial data, visualize it, do queries on it, and visualize the query results.

1. You need to create (generate) latitude,longitude pairs (ie. spatial coordinates) for 9 locations. One of those will be where your home/apartment/dorm room is. The other eight would have to be spread out - at least 100 feet between adjacent locations (and at most 200 or 300 or even 400 feet between neighboring points)

2. Now that you have 9 coordinates and their label strings, you are going to create a KML file (.kml format) out of them using a text editor. Specifically, each location will be a 'placemark' in your .kml file (with a label, and coords). Here is more detail. The .kml file with the 9 placemarks is going to be your starter file, for doing visualizations and queries.

3.(a)compute the convex hull for your 9 points [a convex hull for a set of 2D points is the smallest convex polygon that contains the point set]. Use the query's result polygon's coords, to create a polygon in your .kml file (edit the .kml file, add relevant XML to specify the KML polygon's coords). Load this into Google Earth, visually verify that your 9 points are inside the convex hull. 
(b) compute the three nearest neighbors of your home/apt/dormroom location. Use the query's results, to create three line segments in your .kml file: line(home,neighbor1), line(home,neighbor2), line(home,neighbor3). Verify this looks correct using Google Earth, take a snapshot.

4. Using Tommy Trojan as the center, compute (don't use GPS!) a set (sequence) of lat-long (ie. spatial) co-ordinates that lie along a pretty Spirograph(TM) curve :) Create a new KML file with these points, visualize it on Google Earth.
