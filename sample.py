#OPEN CV


'''
import cv2
 
image = cv2.imread('wallp.jpg')
 
#covert the image to grayscale
gimage= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
 
#convert the image to blur
bimage = cv2.GaussianBlur(image,(15,15),0)
 
inverted_image = cv2.bitwise_not(image)
 
edges = cv2.Canny(image,100,200)
 
window_edge = 'Edges'
cv2.namedWindow(window_edge,cv2.WINDOW_NORMAL)
cv2.imshow(window_edge,edges)
 
window_original = 'Original image'
cv2.namedWindow(window_original,cv2.WINDOW_NORMAL)
cv2.imshow(window_original,image)
 
window_gray = 'Graysacle image'
cv2.namedWindow(window_gray,cv2.WINDOW_NORMAL)
cv2.imshow(window_gray,gimage)
 
window_invert = 'Inverted Image'
cv2.namedWindow(window_invert,cv2.WINDOW_NORMAL)
cv2.imshow(window_invert,inverted_image)
 
window_blur = "blur image"
cv2.namedWindow(window_blur,cv2.WINDOW_NORMAL)
cv2.imshow(window_blur,bimage)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
What is opencv?
    -> Open source Computer Vision
    -> mainly used for image processing technique with computer vision
 
if we want to install opencv
    pip install opencv-python
 
    it will install 2 packages
    1. opencv
    2. numpy
        -> is also a package
        -> which will have the implementations of advance mathematical formulas, execitions, implementations
        -> and also it will have the implementations of array executions also
 
    -> we are going to use image in our project, but directly we can't use it. that's why we need to represent
    -> that image as array representation.
    -> arrays has indexes and images will be splited into indexes execution.
for example
    -> if i have an image with height of 50cm and width of 50 cm
    -> this image will be splited into 5 X 5 matrix ot 50 X 50 matrix
 
    if 50 X 50
        -> each row will have 50 columns and each column will have images which is splited into the parts of 50 X 50
 
basic program to execute opencv in our python file.
 
1. we need to install opencv
2. create a python file and import opencv in that file
3. write a print statement as opencv_name.__version__
 
Predefined functions available:
 
1. how to read an image to our program
    -> imread()
        -> used to get the image from the specified file location.
 
    syntax:
    cv2.imread("filename","flag")
    filename -> the path to the image.
    flag -> how the image should be read(with color or without color)
 
    if you want the image in color, we need to use cv2.IMREAD_COLOR in place of flag
    if you want the image without color, we need to use cv2.IMREAD_GRAYSCALE in place of flag
 
    -> it always return the input image as value, so we need to store that input image value in a variable
 
2. How we need to display the image
    -> imshow()
        -> used to display the input image as a new window screen
 
    syntax:
    cv2.imshow("window screen name",variable_name)
 
    -> will have a disadvantage, that is it will open the window screen and closes it at the same time
    -> if it happens, then we can't able to see the output
 
3. How we need to hold the input image screen
    -> waitKey()
        -> used to hold our screen for certain seconds until user press any key.
 
    syntax:
    cv2.waitKey(0) -> starting from 0 need to wait until user press a key
 
import cv2
 
img1 = cv2.imread("image1.jpg",cv2.IMREAD_COLOR)
 
cv2.imshow("Input 1 Image Screen",img1)
 
cv2.waitKey(0)
 
4. How do get multiple and print it in multiple output screen
    -> we can use multiple variables and multiple imshow function to print the multiple image outputs
    -> if i want to close i need to click on the image, sometimes it will not close the all windows
    -> to avoid this mistakes we need to use one more function
        -> destoryAllWindows()
            -> used to close all the output screens at the same time.
        syntax:
        cv2.destroyAllWindows()
 
import cv2
 
img1 = cv2.imread("image1.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("image1.jpg",cv2.IMREAD_COLOR)
 
cv2.imshow("Input 1 Image Screen",img1)
cv2.imshow("Input 2 Image Screen ",img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 
5. How to get multiple image but need output in one screen
    -> concatenate()
        -> used to merge all the variables values as one output.
        -> this function will not be available in opencv package, it will be available only in numpy package
 
    1. import the numpy package to our program
        import numpy
    2. using the concatenate function
 
    syntax:
        numpy.concatenate((variable1,variable2,variable3,..),axis value)
 
        axis value:
            -> this axis value represents whether the multiple images needs to be in sample line or different line
            -> horizontal or vertical
            ->   axis=1   or axis=0
 
    -> this concatenate function will return the answer as one image merged with multiple images.
    -> So, we need to store that return answer in a variable
 
import cv2
import numpy
 
img1 = cv2.imread("blood cell.jpg",cv2.IMREAD_COLOR)
img2 = cv2.imread("blood cell.jpg",cv2.IMREAD_COLOR)
 
final_img  = numpy.concatenate((img1,img2),axis=0)
 
cv2.imshow("Concatenated Image Output",final_img)
 
cv2.waitKey(0)
cv2.destroyAllWindows()


--> Day 2: <--
 
if we got an image and we have changed that image as grayscale and i want to save that converted grayscale image.
6. how to save a image
    -> imwrite()
        -> used to save the image as a new image file.
 
    syntax:
    cv2.imwrite(imagename,imageSource)
 
    imagename = filename that how you want to store
    imagesource = the input image, you got.
 
import cv2
 
img1 = cv2.imread("image1.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite('grayscale_converted_image.jpg',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
   
 
import cv2
 
img1 = cv2.imread("grayscale_converted_image.jpg")
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
If we have a image that is too large to fit in a screen or we have an image that is too small for visibility.
7. How to resize the images
    -> resize()
        -> used to resize the given image to a common image.
 
    syntax:
    cv2.resize(source,size,destination,fx,fy,interpolation)
 
    source -> imread function variable
    size -> (height,width) to be changed
    destination -> if we want to store the resized image, then we will give the name for that resized image
                -> optional
    fx -> scalar factor of x axis
       -> 0 to 1 is the size
    fy -> scalat factor of y axis
       -> 0 to 1 is the size
    interpolation -> mainly used for predefiend sizes
        -> INTER_AREA -> shrink
        -> INTER_CUBIC -> large the image with slow conversion
        -> INTER_LINEAR -> zoom
        -> optional
 
    when you give an half image condition, then we need to use the following arguments
 
        source -> img
        size -> (0,0)
        when we have the size as (0,0), then it's a must, we need to give the fx and fy value.
        fx => 0 to 1
        fy => 0 to 1
for merging both resized_image and half_image
 
import cv2
import numpy as np
 
img = cv2.imread('image1.jpg')
resize_image = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
half_image = cv2.resize(img,(0,0),fx=0.5,fy=0.5)
 
concat_image = np.concatenate((resize_image,half_image),axis=1)
cv2.imshow('concat_image',concat_image)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 

--->>  Day 3:   <<---

Edge detection:
    -> if you have any shape in your image and you want to focus only on that image.
 
    -> we need to know edge detection algorithm
        -> filter, supression, gradient calculation
    -> we have predefnied function
        -> canny edge detection algorithm
        -> used for edge detection methods and it's introduced by John F.Canny
 
    -> Canny() function
    syntax:
    cv2.Canny(sourceImage,minValue,maxValue)
 
    minValue = minimum value needed for gradient
    maxValue = maximum value needed for gradient
 
import cv2
 
img = cv2.imread('blood cell.jpg')
 
edge1 = cv2.Canny(img,0,100)
edge2 = cv2.Canny(img,100,300)
edge3 = cv2.Canny(img,100,500)
cv2.imshow("Edge1 Output",edge1)
cv2.imshow("Edge2 Output",edge2)
cv2.imshow('Edge3 Output',edge3)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 
Can we do arithmetic operations in our image?
    -> Yes we can do arithmetic operations in our image
 
1. Addition
    -> adding two or more images as one final image
    syntax:
    cv2.add(img1,img2)
        -> this syntax lead to error, because the pixels are missing
 
    cv2.addWeighted(img1,wt1,img2,wt2,gammaValue)
    wt1 -> how much visibility we are going to have for img1
    wt2 -> how much visibility we are going to have for img2
    gammaValue -> Measurement of light
 
    Add must have both the images as same size
 
import cv2
 
img1 = cv2.imread('broken.jpg')
img2 = cv2.imread('galaxy1.jpg')
 
add_img1 = cv2.addWeighted(img1,0.5,img2,0.4,0)
add_img2 = cv2.addWeighted(img1,0.4,img2,0.5,0)
cv2.imshow('Added1 Output',add_img1)
cv2.imshow('Added2 Output',add_img2)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 
 
Subtraction:
    -> subtract(img1,img2)
 
'''
'''
import cv2
 
img1 = cv2.imread('broken.jpg')
img2 = cv2.imread('galaxy1.jpg')
 
sub_img1 = cv2.subtract(img1,img2)
sub_img2 = cv2.subtract(img2,img1)
cv2.imshow('Sub1 Output',sub_img1)
cv2.imshow('sub2 Output',sub_img2)
 
 
cv2.waitKey(0)
cv2.destroyAllWindows()
 



-->>  DAY 4  <<--

Skin Disease Project Part 1
1. get the image
2. resize the image to constant size
3. Normalization technique
    -> to have a common implementation of the image we will be going for normalization
    -> 255
4. include the dimensions of the images
    -> will not be available in cv2, it will be available in numpy
    -> expand_dims(image,axis=)
 
manual
1. convert the image from color to grayscale
    -> cvtColor(image,cv2.COLOR_BGR2GRAY)
2. increase the smoothness of the image
    -> blur the image
    -> GaussianBlur(image,(SigmaX,sigmaY),kernelSize)
3. threshold calculation
    -> used to change the blured image with black and white and also with only the edges
    -> threshold(image,thresholdValue,maxValue,thresholdType)
4. find the contour
    -> find the dimensions of an image which has a curved edges
    -> findContours(image,contourType,contourValue)
    contourType:
    RETR_LINK -> singleinheritance, parents and child
    RETR_EXTERNAL -> only parent
    RETR_TREE -> hierarical inhertiance, grandparents, parents, child
 
    contourValue
    CHAIN_APPROX_SIMPLE
    CHAIN_APPROX_NONE


import cv2
import numpy as np
 
img = cv2.imread('image1.jpg')
img_resize = cv2.resize(img,(250,250))
cv2.imshow('without nor',img_resize)
img_nor = img_resize/255.0
cv2.imshow('with nor',img_nor)
img_dim = np.expand_dims(img_nor,axis=0)
print(img_dim)

# gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray',gray)
# blur = cv2.GaussianBlur(gray,(3,3),0)
# cv2.imshow('Blur',blur)
# val1,threshold = cv2.threshold(blur,120,255,cv2.THRESH_BINARY)
# cv2.imshow('Threshold',threshold)
# contour,val2 = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
# print(contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
 
'''


#DAY2

# import cv2
# import numpy

# img1 = cv2.imread("image1.jpg",cv2.IMREAD_GRAYSCALE)
# # resize = cv2.resize(img1,(600,600))
# half_size = cv2.resize(img1, (0,0), fx=0.5, fy=0.5)
# cv2.imshow("Original Image", img1)
# cv2.imshow("Resizxed Image", half_size)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#DAY3

# import cv2

# img1 = cv2.imread('cells.jpg')
# img1_s = cv2.resize(img1,(500,500))

# img2 = cv2.imread('image1.jpg')
# img2_s = cv2.resize(img2,(500,500))

# add_img = cv2.addWeighted(img1_s,0.5,img2_s,0.5,0)

# cv2.imshow("Added Images", add_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


#DAY4

import cv2
import numpy as np

img = cv2.imread('image1.jpg')
img_resize = cv2.resize(img,(500,500))
cv2.imshow("Resized Image", img_resize)

# img_norm = img_resize/255.0
# cv2.imshow("Normalized Image", img_norm)

# img_dim = np.expand_dims(img_norm,axis=0)
# print(img_dim)

gray = cv2.cvtColor(img_resize,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray)

blur = cv2.GaussianBlur(gray,(5,5),0)
cv2.imshow("Blur Image", blur)

val,threshold = cv2.threshold(blur,150,255,cv2.THRESH_BINARY)
cv2.imshow('Threshold', threshold)
print(val)

contour,val2 = cv2.findContours(threshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(contour)

cv2.waitKey(0)
cv2.destroyAllWindows()