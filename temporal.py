import numpy as np
import bit_gen
import encode_decode
import mod_demod
import channels
import utils
from copy import copy

data_length = 20

data = bit_gen.bitgen_light(data_length)

# data = bit_gen.bitgen_heavy(data_length)

mod_demod.qpsk(data)

# mod_demod.eight_psk(data)