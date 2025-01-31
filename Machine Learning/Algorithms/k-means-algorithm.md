# K-Means Clustering Algorithm

## Assumptions
- The dataset has no missing values
- The dataset consists of numeric values only

## Algorithm Steps
1. Determine the number of clusters `k` arbitrarily
2. Initialize the following data structures:
   - `processed_dataset`: List to store the processed dataset
   - `clustered_dataset`: List to store the final clustered dataset
   - `raw_dataset`: List to store the raw dataset
   - `labels`: List to store the feature labels
   - `centroids`: Dictionary to store the centroids
     - Key: Index of centroid (1 for `k1`, 2 for `k2`, etc.)
     - Value: List of mean values for each feature
   - `group_averages`: Dictionary to store the column-group based averages
     - Key: Index of centroid
     - Value: Dictionary with 'sum', 'total', and 'avg' keys for each feature
   - `group_changes`: List to track whether any group changes occurred
   - `distance_changes`: List to store the distance changes for each sample

3. Read the dataset from the file and process the raw data by type casting
4. Choose `k` random samples as initial centroids and store them in the `centroids` dictionary
5. Initialize the `group_averages` dictionary with empty values
6. Define the `calculate_euclidean_distance` function to calculate the Euclidean distance between two vectors

7. Define the `update_centroids` function:
   - Calculate the column-group based averages for each centroid
   - Update the centroids with the calculated averages

8. While there are any group changes (`group_changes.count(True) != 0`):
   - Reset the `group_changes` list
   - For each sample in the `processed_dataset`:
     - Calculate the Euclidean distances between the sample and each centroid
     - Determine the new centroid based on the minimum distance
     - If the new centroid is different from the current centroid, append it to the `distance_changes` list and set `group_changes` to `True`
     - If the new centroid is the same as the current centroid, append the current centroid to the `distance_changes` list and set `group_changes` to `False`
   - If there are any group changes, call the `update_centroids` function to update the centroids

9. Append the final cluster labels to the `clustered_dataset`
10. Print the following outputs:
    - `group_changes` list
    - `group_averages` dictionary
    - `distance_changes` list
    - Final `clustered_dataset`

