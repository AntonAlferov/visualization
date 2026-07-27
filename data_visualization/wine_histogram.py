from matplotlib import pyplot as plt

import config_test_data
import custom_dark_theme  # noqa: F401

wines = config_test_data.wines
fig, ax = plt.subplots()

ax.hist(
    wines[wines['wine_type'] == 'white']['density'],
    bins=80,
    color='#eef0c6',
    alpha=0.7,
    edgecolor='white',
    linewidth=0.8,
    label='Гистограмма плотности Белого вина',
    density=True
)
ax.hist(
    wines[wines['wine_type'] == 'red']['density'],
    bins=20,
    color='#c60c0c',
    alpha=0.7,
    edgecolor='white',
    linewidth=0.8,
    label='Гистограмма плотности Красного вина',
    density=True
)

ax.set_xlim(right=1.005)

ax.legend(loc='upper left')

ax.grid()

ax.plot(1, 0, ">", color='#90a8b9', transform=ax.transAxes, clip_on=False, markersize=7)
ax.plot(0, 1, "^", color='#90a8b9', transform=ax.transAxes, clip_on=False, markersize=7)

ax.set_xlabel('Плотность вина (г/куб.см.)')
ax.set_ylabel('Плотность вероятности')

plt.show()
