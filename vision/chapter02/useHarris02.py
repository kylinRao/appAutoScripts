import harris
from pylab import *
from PIL import Image
if __name__ == '__main__':
    wid = 28
    #im1 = array(Image.open('bigtu.png').convert('L'))
    im1 = array(Image.open('tanSuoZhunBeiPath.png').convert('L'))


    harrisim = harris.compute_harris_response(im1,10)
    filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
    d1 = harris.get_descriptors(im1,filtered_coords1,wid)

    im2 = array(Image.open('bigtu.png').convert('L'))


    harrisim = harris.compute_harris_response(im2,10)
    filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
    d2 = harris.get_descriptors(im2,filtered_coords1,wid)

    matches = harris.match_twosided(d1,d2)
    harris.plot_harris_points(im2, filtered_coords2)
    figure()
gray()
harris.plot_matches(im2,im1,filtered_coords2,filtered_coords1,matches)
show()