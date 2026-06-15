import numpy as np
import matplotlib.pyplot as plt

time = []
rmsd = []

with open(".../file_location", "r") as file:

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
plt.figure(figsize=(8,5))

plt.plot(time, rmsd)

plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("RMSD Analysis")

plt.tight_layout()

plt.savefig(".../figures", dpi=300)

plt.show()