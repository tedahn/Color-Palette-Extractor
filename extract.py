import imageio
import cv2
import glob

#html = open("index.html", "w")
text = open("index.html", "w")
for filename in glob.glob('./images/*'):
    #html.write("<div>")
    #html.write("<img width=\"150px\" src=\"" + filename + "\">")
    text.write("<div>")
    text.write("<img width=\"150px\" src=\"" + filename + "\">")
    print(filename)
    im = cv2.imread(filename, 1)
    print(im.shape)
    print(im)
    text.write("<p> {} </p>".format(im))
    text.write("</div>")
    print (type(im))
    print("done")
