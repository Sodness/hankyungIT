import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# img = np.array([[30,0,255],
#                 [200,127,50]])
# plt.imshow(img, cmap='gray')
# # plt.show()
#
# img = np.array([[[0,0,0],[255,255,255],[127,127,127]],
#                 [[255,0,0],[0,255,0],[0,0,255]],
#                 [[255,255,0],[255,0,255],[255,255,255]],
#                 [[0,255,255],[127,16,3],[30,127,250]]], dtype='uint8')
# plt.imshow(img)
# # plt.show()

# --------------------------------------------------------------------
img = Image.open('./img/pen.png')
img = np.array(img)
# print(type(img))
# print(img)
# print(np.shape(img))
# print(img[100:700, 500:600])
# plt.imshow(img[100:700, 500:600])
# plt.show()
# plt.imshow(img)
# plt.show()


# --------------------------------------------------------------------
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# img = Image.open('./img/pen.jpg')
# # print(np.shape(img))
# img = img.resize((8,6))
# img = np.array((img))
# print(np.shape(img))
# plt.imshow(img)
# plt.show()
# --------------------------------------------------------------------
from PIL import Image
# img = Image.open('./img/sudoku.jpg')
# print(np.shape(img))
# plt.imshow(img)
# plt.show()
# img = np.array(img)
# print(img)

# --------------------------------------------------------------------
from PIL import Image
import numpy as np
# img = Image.open('./img/고등어.png')


# --------------------------------------------------------------------
# npy와 같은 배열자료로 갖고 다닐수 있음
# imgs = []
# img = Image.open('./img/pen.png').resize((8,8))
# img = np.array(img)
# imgs.append(img)
#
# img = Image.open('./img/고등어.png').resize((8,8))
# img = np.array(img)
# imgs.append(img)
#
# print(np.shape(imgs))
# plt.imshow(imgs[1])
# plt.show()
#
# img = Image.open('./img/pen.jpg').resize((8,8))
# img = np.array(img)
# print(np.shape(img))
# imgs.append(img)

# --------------------------------------------------------------------
from PIL import Image
from glob import glob
import matplotlib.pyplot as plt
import numpy as np

# file_list = glob('./img/*.jpg')
# # print(file_list)
#
# result = []
# for x in file_list:
#     img = Image.open(x).resize((100,100))
#     img = np.array(img)
#     if np.shape(img)[2] == 3:
#         result.append(img)
#
# print(result)
# print(np.shape(result))
# # print(np.array(result[0].shape))

# --------------------------------------------------------------------
with open('./img/lenna.jpg', 'rb') as f:
    data = f.read(16)
print(data.hex())

with open('./img/poker.jpg', 'rb') as f:
    data = f.read(16)
print(data.hex())

with open('./img/pen.jpg', 'rb') as f:
    data = f.read(16)
print(data.hex())

with open('./img/cells.png', 'rb') as f:
    data = f.read(16)
print(data.hex())

with open('./img/rice.png', 'rb') as f:
    data = f.read(16)
print(data.hex())

# --------------------------------------------------------------------


# --------------------------------------------------------------------


# --------------------------------------------------------------------


# --------------------------------------------------------------------