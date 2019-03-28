import matplotlib.pyplot as plt
from math import pi

# Abilities data
ted_abilities = {
    'COMPUTER': 60,
    'ENGLISH': 50,
    'LONGBOARD': 40,
    'UKULELE': 16,
    'HANDWRITING': 10,
    'DRIVING': 50,
}

# number of variable
# categories=list(df)[1:]
categories = ted_abilities.keys()
N = len(categories)

# But we need to repeat the first value to close the circular graph:
values=list(ted_abilities.values())
values += values[:1]

# What will be the angle of each axis in the plot? (we divide the plot / number of variable)
angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

# Initialise the spider plot
ax = plt.subplot(111, polar=True)

# Draw one axe per variable + add labels labels yet
plt.xticks(angles[:-1], categories, color='#0047BD', size=10)

# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([0,20,40,60,80], ["0","20","40","60","80"], color="#FD4703", size=7)
plt.ylim(0,100)

# Plot data
ax.plot(angles, values, linewidth=1.5, linestyle='solid', color='#009543')

# Fill area
ax.fill(angles, values, 'b', color='#00AB38', alpha=0.6)

plt.show()
