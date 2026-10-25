"""
Practical 6: Python Plotting
Plotting the seaborn 'penguins' dataset with matplotlib, plotly, seaborn and plotnine.

Run from the repo root with the bio511py environment active:
    python practical_6/plotting_nad.py
All plots are saved next to this script, in practical_6/.
"""

# ---------------------------------------------------------------
# Imports (good practice: all imports at the top of the script)
# ---------------------------------------------------------------
import os

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from plotnine import ggplot, aes, geom_point, labs, theme_bw, ggsave

# Save all output files in the same folder as this script,
# no matter which folder you run it from.
OUT_DIR = os.path.dirname(os.path.abspath(__file__))


def out(filename):
    """Return the full path for an output file in OUT_DIR."""
    return os.path.join(OUT_DIR, filename)


# ---------------------------------------------------------------
# a) Load the penguins dataset and remove rows with missing values
# ---------------------------------------------------------------
penguins = sns.load_dataset("penguins")
print(f"Rows before dropna: {len(penguins)}")

penguins = penguins.dropna()   # drops every row that has at least one NaN
print(f"Rows after dropna:  {len(penguins)}")
print(penguins.head())

# ---------------------------------------------------------------
# b) Scatterplot with matplotlib: flipper length (x) vs body mass (y)
# ---------------------------------------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(penguins["flipper_length_mm"], penguins["body_mass_g"], alpha=0.7)
plt.title("Penguin flipper length vs body mass")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig(out("b_scatter_matplotlib.png"), dpi=300, bbox_inches="tight")
plt.close()   # close the figure so the next plot starts fresh

# ---------------------------------------------------------------
# c) Same plot with plotly, saved as an interactive HTML file
# ---------------------------------------------------------------
fig = px.scatter(
    penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hover_data=["species", "island", "sex"],   # extra info shown on hover
    title="Penguin flipper length vs body mass",
    labels={"flipper_length_mm": "Flipper length (mm)",
            "body_mass_g": "Body mass (g)"},
)
fig.write_html(out("c_scatter_plotly.html"))

# ---------------------------------------------------------------
# d) Same plot with seaborn, coloured by species
# ---------------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.scatterplot(data=penguins, x="flipper_length_mm", y="body_mass_g",
                hue="species")          # hue = colour by a column
plt.title("Penguin flipper length vs body mass by species")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig(out("d_scatter_seaborn.png"), dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------
# e) Same plot with plotnine (ggplot2 style), saved with ggsave
# ---------------------------------------------------------------
p = (
    ggplot(penguins, aes(x="flipper_length_mm", y="body_mass_g", color="species"))
    + geom_point()
    + labs(title="Penguin flipper length vs body mass",
           x="Flipper length (mm)", y="Body mass (g)")
    + theme_bw()
)
ggsave(p, filename=out("e_scatter_plotnine.png"), dpi=300, width=8, height=6,
       verbose=False)

# ---------------------------------------------------------------
# Histogram: distribution of bill length (seaborn)
# ---------------------------------------------------------------
plt.figure(figsize=(8, 6))
sns.histplot(data=penguins, x="bill_length_mm", bins=30, kde=True)
plt.title("Distribution of penguin bill length")
plt.xlabel("Bill length (mm)")
plt.ylabel("Count")
plt.savefig(out("histogram_bill_length.png"), dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------
# Group by island and calculate mean body mass, then bar plot
# ---------------------------------------------------------------
mean_mass_per_island = penguins.groupby("island")["body_mass_g"].mean()
print("\nMean body mass per island (g):")
print(mean_mass_per_island.round(1))

plt.figure(figsize=(8, 6))
plt.bar(mean_mass_per_island.index, mean_mass_per_island.values,
        color=["#4C72B0", "#55A868", "#C44E52"])
plt.title("Average penguin body mass per island")
plt.xlabel("Island")
plt.ylabel("Mean body mass (g)")
plt.savefig(out("barplot_mean_mass_island.png"), dpi=300, bbox_inches="tight")
plt.close()

# ---------------------------------------------------------------
# Optional: two seaborn plots as subplots, with a palette
# ---------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))   # 1 row, 2 columns

# Left: boxplot of body mass per species, split by sex
sns.boxplot(data=penguins, x="species", y="body_mass_g", hue="sex",
            palette="Set2", ax=axes[0])
axes[0].set_title("Body mass by species and sex")
axes[0].set_xlabel("Species")
axes[0].set_ylabel("Body mass (g)")

# Right: bill length vs bill depth, coloured by island
sns.scatterplot(data=penguins, x="bill_length_mm", y="bill_depth_mm",
                hue="island", palette="viridis", ax=axes[1])
axes[1].set_title("Bill length vs bill depth by island")
axes[1].set_xlabel("Bill length (mm)")
axes[1].set_ylabel("Bill depth (mm)")

fig.suptitle("Palmer penguins overview")
fig.tight_layout()
fig.savefig(out("optional_subplots.png"), dpi=300, bbox_inches="tight")
plt.close(fig)

print("\nAll plots saved in:", OUT_DIR)