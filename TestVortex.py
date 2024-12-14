# from SonicSurface import SonicSurface
# import time

# dist = 0.20 # focal point
# l = 5 # topological charge

# array = SonicSurface()
# array.connect( -1 )

# for _ in range(3):
#     array.vortexAt(0,dist,0, l)
#     time.sleep(1)
#     array.vortexAt(0,dist,0, -l)
#     time.sleep(1)


# array.switchOnOrOff( False )
# array.disconnect()

from SonicSurface import SonicSurface
import time

# User-defined parameters
dist = 0.195  # Focal point distance
l = 9  # Topological charge

array = SonicSurface()
array.connect(-1)

try:
    while True:  # Infinite loop
        array.vortexAt(0, dist, 0, l)
        # time.sleep(1)
        # array.vortexAt(0, dist, 0, -l)
        # time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    array.switchOnOrOff(False)
    array.disconnect()
