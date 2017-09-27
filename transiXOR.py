
from skimage.transform import resize
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

label_size = 10
mpl.rcParams['xtick.labelsize'] = label_size 
mpl.rcParams['ytick.labelsize'] = label_size 
mpl.rcParams['figure.figsize'] = 13, 12

def sqResize(image, outwidth):
    ny, nx = image.shape
    # print("width: %i, and length: %i" %(ny, nx))
    tmp_min = np.min(image)
    tmp_max = np.max(image)
    image = 2*(image - tmp_min)/(tmp_max - tmp_min + 1e-16)-1  
    outimage = resize(image, [outwidth, outwidth])
    outimage = (outimage + 1)/2*(tmp_max - tmp_min) + tmp_min
    ny, nx = outimage.shape
    # print("width: %i, and length: %i" %(ny, nx))
    return outimage  

# data = np.float32(np.load('vds_vbg_vtg_id_D2.npy'))
data = np.load('vds_vbg_vtg_id_D2.npy')
numVds, numVbg, numVtg = data.shape
nRow = 3; nCol = 3; figsize = 6
# vds as z

## test plot
# idx = 40
# I = sqResize(data[idx, :, :], 41)
# fig, ax = plt.subplots(figsize=(6,6))
# # idx/40 scale for Vds (see genData)
# ax.imshow(I, vmin=0, vmax=255*(idx/40), origin='lower', interpolation = 'gaussian')
# plt.show()


##
# ax = plt.subplot(nRow, nCol, 1)
# img = sqResize(data[, :, :], 41)
# plt.imshow(img, vmin = 0, vmax = 255*(i/90.), origin='lower', interpolation = 'gaussian')
# plt.title('Vds = {0:.2f} V'.format(vds), fontsize = label_size)
# plt.ylabel('Vbg (V)', fontsize = label_size)
# plt.xlabel('Vtg (V)', fontsize = label_size)
# plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
# ax.set_xticklabels([0.0, 0.0, 0.2, 0.4])
# ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])

for i, vds in enumerate(np.linspace(0.24, 0.4, 9)):
    ax = plt.subplot(nRow, nCol, i + 1)
    i = 2 * i + 24
    img = sqResize(data[i, :, :], 41)
    plt.imshow(img, vmin = 0, vmax = 255*(i/41.), origin='lower', interpolation = 'gaussian')
    plt.title(r'$V_{DS}$' + ' = {0:.2f} V'.format(vds), fontsize = label_size)
    plt.ylabel(r'$V_{BG}$ (V)', fontsize = label_size)
    plt.xlabel(r'$V_{TG}$ (V)', fontsize = label_size)
    plt.subplots_adjust(wspace = 0.0, hspace = 0.35)
    ax.set_xticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])
    ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])

plt.savefig('figure1.pdf')
plt.show()

# for i, vds in enumerate(np.linspace(0, 0.4, numVds)):
#   ax = plt.subplot(nRow, nCol, i + 1)
#   img = sqResize(data[:, i, :], 41)
#   plt.imshow(img, vmin = 0, vmax = 255, origin='lower',interpolation = 'gaussian')
#   plt.title('Vbg = {0:.2f} V'.format(vds), fontsize = label_size)
#   plt.ylabel('Vds (V)', fontsize = label_size)
#   plt.xlabel('Vtg (V)', fontsize = label_size)
#   plt.subplots_adjust(wspace = 0.5, hspace = 0.5)
#   ax.set_xticklabels([0.0, 0.0, 0.2, 0.4])
#   ax.set_yticklabels([0.0, 0.0, 0.1, 0.2, 0.3, 0.4])

# plt.savefig('figure2.pdf')
