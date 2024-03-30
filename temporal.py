import numpy as np
import bit_gen
import encode_decode
import mod_demod
import channels
import utils
from copy import copy

data = np.array([[1,0,1,1,0,1,0,1]])

# mod_demod.qpsk(data)

mod_demod.eight_psk(data)