import harris
from pylab import *
from PIL import Image
wid = 20
im1 = array(Image.open('bigtu.png').convert('L'))
im2 = array(Image.open('tanSuoZhunBeiPath.png').convert('L'))


harrisim = harris.compute_harris_response(im1,6)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)

harrisim = harris.compute_harris_response(im2,6)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print 'starting matching'
matches = harris.match_twosided(d1,d2)

figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches)
show()