# Data Preprocessing - Encoding Algorithm

# todo : Work on the target variable index. It should be changeable and not constraint as being at the end.

# ! Assumed that the target variable (class) is located at the last index of a list !

# Initialize a list to store the processed dataset
processed_dataset = []

# Initialize a list to store the encoded dataset
encoded_dataset = []

# Initialize a dictionary to store the continuous typed features and their indexes
# Key = index of the list where the feature resides
# Value = dictionary of that feature values (Key&Value: feature value)
continuous_typed_features = dict()

# Initialize a dictionary to store the integer typed features and their indexes
# Key = index of the list where the feature resides
# Value = dictionary of that feature values (Key&Value: feature value)
integer_typed_features = dict()

# Initialize a dictionary to store the categorical features and their indexes
# Key = index of the list where the feature resides
# Value = dictionary of that feature values (Key: feature value & Value: number of first occurrence in list (1,2,3,..))
categorical_features = dict()

# Initialize a dictionary to store the target variables (classes) of dataset
# Key = target value
# Value = number of first occurrence in list (1,2,3,..)
targets = dict()

# Define path of dataset file
# file_path = '../Datasets/iris/iris.data'
file_path = "test-data.csv"

# Read all lines of the file
with open(file_path, "r") as file:
    lines = file.readlines()


# Control whether the value is numeric
def is_numeric(value) -> bool:
    try:
        # Try to cast
        float(value)
        # The value is either float or integer
        return True
    except:
        # The values is not numeric
        return False


# Process each line in the dataset
for line in lines:
    if not line.isspace():
        # Initialize list of the instance's data
        instance = []

        # Remove newline characters and split by commas
        values = line.strip().split(",")

        for index in range(0, len(values) - 1):
            value = values[index]
            # Check whether the feature is numeric
            if is_numeric(value):
                # If the value is floating-point number
                if len(value.split(".")) > 1:
                    instance.append(float(value))

                    # Process the continuous typed feature values for future encoding
                    # Get dictionary of continuous typed features at index
                    feats = continuous_typed_features.get(index)

                    # The feature is present in the dictionary
                    if feats is not None:
                        if float(value) not in list(feats.keys()):
                            continuous_typed_features[index][float(value)] = float(
                                value
                            )
                    # The feature is not present yet
                    else:
                        # Add the feature to dictionary
                        continuous_typed_features[index] = {float(value): float(value)}
                # If the value is integer
                elif len(value.split(".")) == 1:
                    instance.append(int(value))

                    # Process the integer typed feature values for future encoding
                    # Get dictionary of integer typed features at index
                    feats = integer_typed_features.get(index)

                    # The feature is present in the dictionary
                    if feats is not None:
                        if int(value) not in list(feats.keys()):
                            integer_typed_features[index][int(value)] = int(value)
                    # The feature is not present yet
                    else:
                        # Add the feature to dictionary
                        integer_typed_features[index] = {int(value): int(value)}
            # In case of non-numeric values
            else:
                instance.append(value)

                # Process the categorical feature values for future encoding
                # Get dictionary of categorical features at index
                feats = categorical_features.get(index)

                # The feature is present in the dictionary
                if feats is not None:
                    if value not in list(feats.keys()):
                        categorical_features[index][value] = len(feats.keys()) + 1
                # The feature is not present yet
                else:
                    # Add the feature to dictionary
                    categorical_features[index] = {value: 1}

        # Process the target values for future encoding
        # Check for new target values
        if values[-1] not in list(targets.keys()):
            targets[values[-1]] = len(targets.keys()) + 1

        # Append the target value to the list
        instance.append(targets.get(values[-1]))

        # Add the instance to the processed dataset
        processed_dataset.append(instance)

# Display the processed rows
print("Processed dataset:")
for i in processed_dataset:
    print(i)
print()


# Function of encoding target variable (class) of the dataset
def encode_target_variable(targets_count, target_value) -> list:
    # Evaluating possible cases:
    # Possible results for 3 classes:       Possible results for 2 classes:
    # [1,0,0] : target_value=1              [1,0] : target_value=1
    # [0,1,0] : target_value=2              [0,1] : target_value=2
    # [0,0,1] : target_value=3

    # Initialize the list of binary logic map
    binary_logic_map = []
    # Counter for while-loop
    counter = 1

    # Fill the list by zero or one
    while counter <= targets_count:
        if target_value == counter:
            binary_logic_map.append(1)
        else:
            binary_logic_map.append(0)
        counter += 1

    return binary_logic_map


# Encode the target values according to the binary logic map
for i in range(0, len(processed_dataset)):
    processed_dataset[i] = processed_dataset[i][:-1] + encode_target_variable(
        len(targets.keys()), processed_dataset[i][-1]
    )

# Combine all variables according to their indexes
for row in range(0, len(processed_dataset)):
    # Initialize list of the instance's data
    instance = []

    # Go through all variables and find the right index
    for col in range(0, len(processed_dataset[row])):
        # Integer typed features
        if col in list(integer_typed_features.keys()):  # Index check
            for feats in list(integer_typed_features.get(col).keys()):
                if feats == processed_dataset[row][col]:
                    instance.append(integer_typed_features[col][feats])

        # Continuous typed features
        elif col in list(continuous_typed_features.keys()):  # Index check
            for feats in list(continuous_typed_features.get(col).keys()):
                if feats == processed_dataset[row][col]:
                    instance.append(continuous_typed_features[col][feats])

        # Categorical features
        elif col in list(categorical_features.keys()):  # Index check
            for feats in list(categorical_features.get(col).keys()):
                if feats == processed_dataset[row][col]:
                    instance.append(categorical_features[col][feats])

        # Target values
        else:
            instance.append(processed_dataset[row][col])

    # Add the instance to new dataset list
    encoded_dataset.append(instance)

# Display the processed rows after target encoding
print("Processed dataset after target variable encoding:")
for i in processed_dataset:
    print(i)
print()

# Display the encoded rows
print("Encoded dataset:")
for i in encoded_dataset:
    print(i)
print()
