import numpy as np
from skimage import io

image = [0] * 10
#  a)
image[0] = np.load('../images/car_0.npy')
image[1] = np.load('../images/car_1.npy')
image[2] = np.load('../images/car_2.npy')
image[3] = np.load('../images/car_3.npy')
image[4] = np.load('../images/car_4.npy')
image[5] = np.load('../images/car_5.npy')
image[6] = np.load('../images/car_6.npy')
image[7] = np.load('../images/car_7.npy')
image[8] = np.load('../images/car_8.npy')
image[9] = np.load('../images/car_8.npy')


sum = np.sum(image)  # b)
print('Suma pixelilor tuturor imagiinilor este:  ', sum)


sumi = np.zeros(10, np.int)   # c)
for i in range(10):
    sumi[i] = np.sum(image[i])
    print('Suma pixelilor imaginii ', i, ' este: ', sumi[i])

for i in range(10):  # c)
    sumi[i] = np.sum(image[i])
    print('Suma pixelilor imaginii ', i, ' este: ', sumi[i])

maxim = 0  # d)
for i in range(10):
    if sumi[i] > maxim:
        maxim = sumi[i]


print('Maximul este: ', maxim)


for i in range(10):
    if maxim == sumi[i]:
        print('Indexul imaginii cu suma maxima este: ', i)

# e)
mean = np.mean(image, axis=0)
io.imshow(mean.astype(np.uint8))
io.show()


# f)
devstd = np.std(image)
print('Deviatia standard este: ', devstd)


#  g)

image = (image - mean)/devstd


#  h

for i in range(10):
    resizedimg = image[i][200:300, 280:400]
    io.imshow(resizedimg)
    io.show()