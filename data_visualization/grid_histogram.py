import seaborn as sns
from matplotlib import patches
from matplotlib import pyplot as plt

import config_test_data
import custom_dark_theme  # noqa: F401

feature_to_hist = [
    'fixed acidity',
    'volatile acidity',
    'citric acid',
    'residual sugar'
    ]
label_x = [
    'Уровень кислотности',
    'Уровень летучей кислотности',
    'Количество лимонной кислоты',
    'Уровень остаточного сахара'
    ]
title = [
    'График распределения вин по уровню постоянной кислотности',
    'График распределения вин по уровню летучей кислотности',
    'График распределения вин по содержанию лимонной кислоты',
    'График распределения вин по уровню остаточного сахара'
    ]

wines = config_test_data.wines
fig, ax = plt.subplots(2, 2, figsize=(16, 10))

for i, ax_single in enumerate(ax.flatten()):
    current_feature = feature_to_hist[i]
    sns.histplot(
        data=wines,
        x=current_feature,
        hue='wine_type',
        multiple='dodge',
        stat='density',
        common_norm=False,
        shrink=0.7,
        bins=21,
        palette=['#eef0c6', '#c60c0c'],
        ax=ax_single,
    )

    ax_single.plot(1, 0, ">", transform=ax_single.transAxes, clip_on=False, color='#90a8b9', markersize=7)
    ax_single.plot(0, 1, "^", transform=ax_single.transAxes, clip_on=False, color='#90a8b9', markersize=7)

    ax_single.set_xlim(wines[current_feature].quantile(0), wines[current_feature].quantile(0.99))

    ax_single.grid()

    red_patch = patches.Patch(color='#c60c0c', label='Красное вино')
    white_patch = patches.Patch(color='#eef0c6', label='Белое вино')
    ax_single.legend(
        handles=[white_patch, red_patch],
        labels=['Белое вино', 'Красное вино'],
        loc='best',
    )

    ax_single.set_xlabel(label_x[i], labelpad=1)
    ax_single.set_ylabel('Распространненость')
    ax_single.set_title(title[i], color='#90a8b9', size='large', pad=15, weight='bold')

fig.subplots_adjust(hspace=0.4)

plt.show()
