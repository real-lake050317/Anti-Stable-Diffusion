import cv2, random
image = cv2.imread("./images/egon.jpg")

blur_rate = 1

for _ in range(int((image.shape[0]*image.shape[1])*blur_rate)):
    x = random.randint(0, image.shape[0] - 1)
    y = random.randint(0, image.shape[1] - 1)
    image[x, y] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

cv2.imwrite("./images/egon_noise.jpg", image)