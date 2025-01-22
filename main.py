import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fetch data from csv file
data1 = pd.read_csv('datasets/dataset1.csv')
data2 = pd.read_csv('datasets/dataset2.csv')

data = pd.concat([data1, data2], ignore_index=True)

# create column cluster color for
data['cluster color'] = 'black'

# clusters_means = {
#     'red': (-40, +40, -40),
#     'green': (+39, -39, -39),
#     'blue': (-38, -38, -38),
# }

clusters_means = {
    'red': (40, 40, 40),
    'green': (-39, -39, -39),
    'blue': (-38, -38, -38),
}



# Function to calculate Euclidean distance
def euclidean_distance(point, centroid):
    return np.sqrt((point[0] - centroid[0]) ** 2 + (point[1] - centroid[1]) ** 2 + (point[2] - centroid[2]) ** 2)





# Create a 3D plot


for _ in range(10):

    # plotting

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    # ax.clear()

    # Plot each cluster mean (centroid) as a different color
    for color, (x, y, z) in clusters_means.items():
        ax.scatter(x, y, z, color=color, marker='x', label=f'{color.capitalize()} Centroid', s=200)

    # Plot the points
    ax.scatter(data['x'], data['y'], data['z'], c=data['cluster color'].map({
        'red': 'red', 'green': 'green', 'blue': 'blue', 'black': 'black'}), marker='o', alpha=.5, )

    # Set labels
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')

    # Show the plot for the current iteration
    plt.title(f'3D Scatter Plot of Merged Dataset - {_} iterate')
    plt.legend()

    plt.draw()  # Redraw the plot
    plt.pause(0.1)  # Pause to allow the plot to update visually






    # For each point in the data, find the nearest centroid
    for i in range(len(data)):
        point = (data['x'][i], data['y'][i], data['z'][i])
        min_distance = float('inf')
        nearest_cluster_color = None
        for color, centroid in clusters_means.items():
            distance = euclidean_distance(point, centroid)
            if distance < min_distance:
                min_distance = distance
                nearest_cluster_color = color
        data.loc[i, 'cluster color'] = nearest_cluster_color

    # Iterate through each cluster color
    for cluster_color, centroid in clusters_means.items():
        # Filter rows for the current cluster color
        cluster_rows = data[data['cluster color'] == cluster_color]

        # Calculate the average of the rows for this cluster
        average = cluster_rows[['x', 'y', 'z']].mean()
        clusters_means[cluster_color] = (average['x'], average['y'], average['z'])

    # Clear the previous plot and plot new centroids and data points for this iteration
    print(clusters_means)


# To keep the final plot displayed after all iterations
plt.show()
