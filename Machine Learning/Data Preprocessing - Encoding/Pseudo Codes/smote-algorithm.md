# Synthetic Minority Over-sampling Technique (SMOTE) Algorithm

## Algorithm Steps
1. Initialize the following data structures:
   - `processed_dataset`: List to store the processed dataset
   - `over_sampled_dataset`: List to store the dataset after over-sampling
   - `raw_dataset`: List to store the raw dataset
   - `labels`: List to store the feature labels
   - `class_count`: Dictionary to store the count of each class
   - `minority_class`: List to store the minority class samples
   - `majority_class`: List to store the majority class samples
   - `min_max_values`: Dictionary to store the minimum and maximum values for each feature of the minority class

2. Read the dataset from the file and process the raw data by type casting

3. Count the samples of each class and store the counts in the `class_count` dictionary

4. Determine the majority and minority classes based on the class counts

5. Calculate the percentage value and the number of new samples to be generated:
   - Percentage value = `[(Majority class samples / Minority class samples) - 1] * 100`
   - New samples to be generated = `[(Percentage value) * |Minority class samples|] / 100`

6. Separate the minority and majority class samples into `minority_class` and `majority_class` lists

7. Define the `update_minority_min_max` function to calculate the minimum and maximum values for each feature of the minority class samples

8. Initialize the `min_max_values` dictionary by calling the `update_minority_min_max` function with the `minority_class` list

9. Define the `generate_synthetic_attribute` function:
   - Take the index of the feature
   - Generate a new synthetic attribute value using the formula:
     `new_synthetic_sample = (max_value - min_value) * random() + min_value`

10. Generate the new synthetic samples:
    - While the number of new samples to be generated is greater than 0:
      - Create a new synthetic sample by calling the `generate_synthetic_attribute` function for each feature (except the class feature)
      - Append the minority class label to the new synthetic sample
      - Add the new synthetic sample to the `minority_class` list
      - Update the `min_max_values` dictionary by calling the `update_minority_min_max` function with the updated `minority_class` list
      - Decrement the new sample count

11. Combine the `minority_class` and `majority_class` lists to create the `over_sampled_dataset`

12. Print the following outputs:
    - `minority_class` list after over-sampling
    - `over_sampled_dataset`
