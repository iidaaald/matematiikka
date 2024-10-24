'''
Toteuta tehtävä 1 (jossa kolme tehtävää) pythonilla
'''

#Tehtävä1.1
# a)
import numpy as np
rad1 = 2.493
print(f"{rad1} radiaania on {np.degrees(rad1)} astetta")

#b)
rad2 = 0.911
print(f"{rad1} radiaania on {np.degrees(rad2)} astetta")
#Tehtävä1.2
#a)
deg1 = 137.7
print(f"{deg1} astetta on {np.radians(deg1)} radiaania")

#b)
deg2 = 62.3
print(f"{deg1} astetta on {np.radians(deg2)} radiaania\n")

#Tehtävä1.3
degs = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])
for i in degs:
    print(np.radians(i))
