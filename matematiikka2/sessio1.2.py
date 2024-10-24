'''
Laske tehtävän 2 suorakulmaisen kolmion hypotenuusan pituus käyttäen sopivaa numpyn funktiota.
'''
#Tehtävä2.1
import numpy as np
import math
kateetti1 = 1.6
kateetti2 = 2.3
kaava= math.sqrt(kateetti1**2 + kateetti2**2)
print(f"Hypotenuusa on {kaava} metriä")

print(f"Hypotenuusa numpy-kaavaa käyttäen on {np.hypot(kateetti1, kateetti2)} metriä")

