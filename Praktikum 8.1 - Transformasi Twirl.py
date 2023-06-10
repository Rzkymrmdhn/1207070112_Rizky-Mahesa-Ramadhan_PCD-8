import matplotlib.pyplot as plt
from skimage.transform import swirl
from matplotlib import image as mpimg

# Path ke file gambar
image_path = "E:/PicsArt_09-12-09.03.11.jpg"

# Memuat gambar dari file
image = mpimg.imread(image_path)

# Melakukan transformasi swirl
swirled = swirl(image, rotation=0, strength=10, radius=120)

# Menampilkan gambar asli dan gambar yang telah di-swirl
fig, (ax0, ax1) = plt.subplots(nrows=1, ncols=2, figsize=(8, 3), sharex=True, sharey=True)

ax0.imshow(image, cmap=plt.cm.gray)
ax0.axis('off')

ax1.imshow(swirled, cmap=plt.cm.gray)
ax1.axis('off')

plt.show()