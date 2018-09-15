import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('westbrook.jpg')//2
plt.imshow(img)
plt.show()
plt.imsave('Q2.jpg', img)