import numpy as np
import matplotlib.pyplot as plt

time = []
rmsd = []

with open("/home/fatemeh/simulation/charmm/box/isom-complete/drug-cosolv1_nope/result/rmsd.xvg", "r") as file:

    for line in file:

        if line.startswith("#"):
            continue

        if line.startswith("@"):
            continue

        values = line.split()

        time.append(float(values[0]))
        rmsd.append(float(values[1]))

time = np.array(time)
rmsd = np.array(rmsd)

print("Average RMSD =", np.mean(rmsd))
print("Maximum RMSD =", np.max(rmsd))
print("Minimum RMSD =", np.min(rmsd))
print("Standard deviation =", np.std(rmsd))