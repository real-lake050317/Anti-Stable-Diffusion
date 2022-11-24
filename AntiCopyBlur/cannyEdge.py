import cv2, os

path = os.getcwd()

def canny(imgname):
    img = cv2.imread("{p}/images/original_image/{ing}.png".format(p=path, ing=imgname), cv2.IMREAD_GRAYSCALE)

    min_threshold = 255/3
    max_threshold = 255
    
    edge1 = cv2.Canny(img, min_threshold, max_threshold)

    cv2.imwrite("{p}/images/canny_image/{ing}_canny.png".format(p=path, ing=imgname), edge1)
