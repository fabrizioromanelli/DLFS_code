import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from numpy import ndarray
#matplotlib inline

from typing import Callable
from typing import Dict

np.set_printoptions(precision=4)

def square(x: ndarray) -> ndarray:
    '''
    Square each element in the input ndarray.
    '''
    return np.power(x, 2)

def leaky_relu(x: ndarray) -> ndarray:
    '''
    Apply "Leaky ReLU" function to each element in ndarray
    '''
    return np.maximum(0.2 * x, x)

# IMG_FOLDER_PATH = '/mnt/c/Users/Tantrizio/Documents/Work/workspace/DLFS_code/01_foundations/images/'
# PDF_IMG_FOLDER_PATH = '/mnt/c/Users/Tantrizio/Documents/Work/workspace/DLFS_code/01_foundations/pdf_images/'

# fig, ax = plt.subplots(1, 2, sharey=True, figsize=(12, 6))  # 2 Rows, 1 Col

# input_range = np.arange(-2, 2, 0.01)
# ax[0].plot(input_range, square(input_range))
# ax[0].set_title('Square function')
# ax[0].set_xlabel('input')
# ax[0].set_ylabel('output')

# ax[1].plot(input_range, leaky_relu(input_range))
# ax[1].set_title('"ReLU" function')
# ax[1].set_xlabel('input')
# ax[1].set_ylabel('output');
# plt.savefig(IMG_FOLDER_PATH + "01_two_functions.png")
# plt.savefig(PDF_IMG_FOLDER_PATH + "01_two_functions.pdf")

## Derivates example
# a = np.array([4,4.001,3.999])
# b = square(a)

# print('a   : ',a)
# print('f(a): ',b)
## print(a[1]-a[0])
# print((b[1]-b[0])/(a[1]-a[0]))

