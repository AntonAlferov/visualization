from matplotlib import pyplot as plt
from matplotlib.ticker import AutoMinorLocator

import config_test_data
import custom_dark_theme  # noqa: F401


wines = config_test_data.wines

quality_counts = wines['quality_label'].value_counts().sort_values(ascending=True)

fig, ax = plt.subplots()
fig.set_facecolor('#071826')
ax.set_facecolor('#071826')

for spine in ax.spines.values():
    spine.set_visible(False)

ax.set_xticklabels([])
ax.tick_params(axis='y', which='major', direction='inout', length=15, width=2, labelleft=False)
ax.tick_params(axis='y', which='minor', direction='inout', length=6, width=2, labelleft=False)
ax.tick_params(axis='x', which='both', length=0)

bars = ax.bar(
    quality_counts.index,
    quality_counts.values,
    color=["#309fee", "#216392", "#122a3d",],
    width=0.6,
)

x_centers = []
bar_heights = []

for bar in bars:
    x_center = bar.get_x() + bar.get_width() / 2.0
    x_centers.append(x_center)
    bar_heights.append(bar.get_height())

    ax.text(
        x=x_center,
        y=bar.get_height() + 5,
        s=f'{bar.get_height()}',
        ha='center',
        va='bottom',
        fontsize=12,
    )

x_point = [
    x_centers[0],
    (x_centers[0] + x_centers[1]) / 2,
    x_centers[1],
    x_centers[2] * 0.8
]

y_point = [
    bar_heights[0] * 5.6,
    bar_heights[1] * 1.4,
    bar_heights[1] * 1.2,
    bar_heights[2] * 1.2
]
ax.annotate(
    '',
    xy=(x_point[-1],y_point[-1]),
    xytext=(x_point[-2], y_point[-2]),
    arrowprops={'arrowstyle': '->', 'color': '#456872', 'linewidth': 4, 'mutation_scale': 30},
)

ax.plot(x_point[:-1], y_point[:-1], color='#456872', linewidth=4)

ax.xaxis.set_minor_locator(AutoMinorLocator(5))
ax.yaxis.set_minor_locator(AutoMinorLocator(5))

ax.grid(which='major', axis='both', color='#456872', linestyle='--', linewidth=0.6, alpha=0.3)
ax.grid(which='minor', axis='both', color='#456872', linestyle='-.', linewidth=0.4, alpha=0.2)

ax.set_ylim(top=max(quality_counts.values) * 1.5)

ax.legend(
    bars,
    quality_counts.index,
    bbox_to_anchor=(0.25, 0.95),
    labelcolor='#A6C0C7',
    facecolor='#071826',
    edgecolor='#071826',
    framealpha=0.4,
)

ax.text(
    0.55,
    0.97,
    'Количество вина разного качества',
    transform=ax.transAxes,
    verticalalignment='top',
    horizontalalignment='left',
    fontsize='large',
)

plt.show()
