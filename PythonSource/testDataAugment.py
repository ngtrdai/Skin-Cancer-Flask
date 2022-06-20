# Phần code này để tạo ra hình ảnh về xử lý dữ liệu Data Augment trong Paper.

from numpy import expand_dims
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt

image = load_img('../Paper/Images/akiec.jpg')
image = img_to_array(image)
data = expand_dims(image, 0)

dataGenerator = ImageDataGenerator( rotation_range=180,
                                    zoom_range = 0.1,
                                    width_shift_range=0.1,
                                    height_shift_range=0.1,
                                    horizontal_flip=True,
                                    vertical_flip=True,
                                    fill_mode = "nearest")
gen = dataGenerator.flow(data, batch_size=1)

for i in range(9):
	plt.subplot(330 + 1 + i)
	myBatch = gen.next()
	image = myBatch[0].astype('uint8')
	plt.imshow(image)
plt.show()