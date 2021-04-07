# with own code

heights = [189, 170, 189, 163, 183, 171, 185, 168, 173, 183, 173, 173, 175, 178, 183, 193, 178, 173, 174, 183, 183, 180, 168, 180, 170, 178, 182, 180, 183, 178, 182, 188, 175, 179, 183, 193, 182, 183, 177, 185, 188, 188, 182, 185, 191]

count = 0
for height in heights:
    if height > 170:
        count += 1

print(len(heights), count)

# with numpy

import numpy as np

print(np.array(heights).size, (np.array(heights) > 170).sum())

print("dimension:", np.array(heights).shape)
