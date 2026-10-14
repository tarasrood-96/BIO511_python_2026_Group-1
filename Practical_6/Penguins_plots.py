import seaborn as sns
import matplotlib.pyplot as plt
penguins=sns.load_dataset("penguins")
penguins=penguins.dropna()

#Check the cleaned data
print(penguins.head())

#Create the Matplotlib scatterplot
plt.scatter(penguins["flipper_length_mm"], penguins["body_mass_g"])
plt.xlabel("flipper_length (mm)")
plt.ylabel("body_mass (g)")
plt.title("Penguin Flipper Length vs Body Mass")

# Save and display the plot
plt.savefig("penguins_matplotlib.png")
plt.show()