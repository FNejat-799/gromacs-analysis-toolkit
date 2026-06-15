import numpy as np 
import matplotlib.pyplot as plt 

def read_xvg(filename):
    time = []
    rmsd = []

    with open(filename, "r") as f:
        for line in f:
            if line.startwith(("#","@")):
                continue
                cols = line.split()
                if len(cols) >= 2:
                  time.append(float(cols[0]))
                  rmsd.append(float(cols[1]))

           return np.array(time), np.array(rmsd) 


file = "rmsd.xvg"
time, rmsd = read_xvg(file)

plt.figure(figsize=(8, 5))
plt.plot(time, rmsd)

plt.xlabel("Time (ns)")
plt.ylabel("RMSD (nm)")
plt.title("RMSD Analysis")

plt.tight_layout()
plt.savefig("../figures/rmsd_plot.png", dpi=300)
plt.show() 