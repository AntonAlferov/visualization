from matplotlib import patches
from matplotlib import pyplot as plt
import pandas as pd

import config_test_data
import custom_dark_theme  # noqa: F401


wines = config_test_data.wines
fig, ax = plt.subplots(figsize=(24, 18))

radius_sugar = pd.qcut(wines['residual sugar'], q=6, labels=[100, 200, 400, 800, 1600, 3200])
label_sugar = pd.qcut(wines['residual sugar'], q=6)

scatter = ax.scatter(
    x=wines['fixed acidity'],
    y=wines['alcohol'],
    s=radius_sugar,
    c=wines['wine_type'].map({'white': "#acad9988", 'red': "#c60c0c9e"}),
    edgecolors='white',
    linewidths=1.5
)

red_patch = patches.Patch(color='#c60c0c', label='Красное вино')
white_patch = patches.Patch(color='#eef0c6', label='Белое вино')

legend_1 = ax.legend(
    handles=[white_patch, red_patch],
    labels=['Белое вино', 'Красное вино'],
    loc='upper center',
    ncol=2,
    fontsize='xx-large'
)
ax.add_artist(legend_1)

handles, _ = scatter.legend_elements(prop='sizes', alpha=0.6, color='#90a8b9')

ax.legend(handles,
          label_sugar.cat.categories,
          title='Остаточный сахар',
          fontsize='xx-large',
          title_fontsize='xx-large',
          labelspacing=2.0,
          loc='right',
          bbox_to_anchor=(1, 0.72)
          )

ax.plot(1, 0, ">", transform=ax.transAxes, clip_on=False, color='#90a8b9', markersize=7)
ax.plot(0, 1, "^", transform=ax.transAxes, clip_on=False, color='#90a8b9', markersize=7)

ax.grid()

ax.tick_params(labelsize='xx-large')

ax.set_xlabel('Уровень кислотности', fontsize='xx-large')
ax.set_ylabel('Содержание алкоголя', fontsize='xx-large')
ax.set_title('Показатели кислотности, крепости и уровня остаточного сахара в разрезе типов вина', color='#90a8b9', size='xx-large', pad=15, weight='bold')

plt.show()
