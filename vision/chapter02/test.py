import sift
from numpy import *
from PIL import Image
from pylab import *



if __name__ == '__main__':
    imname1 = 'bigtu.png'
    #imname1 ='tansuodatu.png'
    im1 = array(Image.open(imname1).convert('L'))
    #sift.process_image(imname1,'empire.sift')
    l1,d1 = sift.read_features_from_file('empire.sift')

    imname2 = 'tansuoyemian.png'
    #imname2 = imname1

    im2 = array(Image.open(imname2).convert('L'))
    #sift.process_image(imname2,'empire2.sift')
    l2,d2 = sift.read_features_from_file('empire2.sift')


    matches = sift.match_twosided(d1,d2)
    print matches
    sift.plot_features(im1,l1,circle=True)

    show()

    sift.plot_features(im2,l2,circle=True)
    show()

    #sift.plot_matches(im2,im1,l2,l1,matches)
    #sift.plot_matches(im2,im2,l2,l2,matches)
    print l1
    print l1[1][0],l1[1][1]
    print l2
    print l2[1][0]
    sift.plot_matches(im1,im2,l1,l2,matches)
    print l2
    print l2[1][0]
    gray()
    show()




