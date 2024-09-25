# Function of encoding target variable (class) of the dataset
def encode_target_variable(class_count, target_value) -> list:
    # Evaluating possible cases:
    # Possible results for 3 classes:       Possible results for 2 classes:
    # [1,0,0] : target_value=1              [1,0] : target_value=1
    # [0,1,0] : target_value=2              [0,1] : target_value=2
    # [0,0,1] : target_value=3

    # Initialize the list of binary logic map
    binary_logic_map = []
    # Counter for while-loop
    counter = 0

    # Fill the list by zero
    while counter < class_count:
        if target_value == (counter + 1):
            binary_logic_map.append(1)
        else:
            binary_logic_map.append(0)
        counter += 1

    return binary_logic_map


# Initialize a list to store the processed dataset
processed_dataset = []

# Initialize a set to store the classes of dataset
dataset_classes = dict()

# Counter for different classes of dataset
diff_class_count = 0

# Define path of dataset file
file_path = "../Datasets/iris/iris.data"

# Read all lines of the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Process each line in the dataset
for line in lines:
    if not line.isspace():
        # Initialize list of numerical features
        numerical_values = []

        # ! handle the string typed values (nominal/categorical variables)

        # Remove newline characters and split by commas
        features = line.strip().split(",")

        # Convert features from string to numerical types
        for feature in features[:-1]:
            # If the value is floating-point number
            if len(feature.split(".")) > 1:
                numerical_values.append(float(feature))
            # If the value is integer
            elif len(feature.split(".")) == 1:
                numerical_values.append(int(feature))

        # Check for new class values
        if features[-1] not in list(dataset_classes.keys()):
            diff_class_count += 1
            dataset_classes[features[-1]] = diff_class_count

        # Append the class value
        numerical_values.append(dataset_classes.get(features[-1]))

        # Combine the numerical features and the encoded classes
        processed_dataset.append(numerical_values)

# Encode the class values according to the binary logic map
for i in range(0, len(processed_dataset)):
    processed_dataset[i] = processed_dataset[i][:-1] + encode_target_variable(
        diff_class_count, processed_dataset[i][-1]
    )

# Display the processed rows
processed_dataset[:]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Function of encoding target variable (class) of the dataset
def encode_target_variable(class_count, target_value) -> list:
    # Evaluating possible cases:
    # Possible results for 3 classes:       Possible results for 2 classes:
    # [1,0,0] : target_value=1              [1,0] : target_value=1
    # [0,1,0] : target_value=2              [0,1] : target_value=2
    # [0,0,1] : target_value=3

    # Initialize the list of binary logic map
    binary_logic_map = []
    # Counter for while-loop
    counter = 1

    # Fill the list by zero
    while counter <= class_count:
        if target_value == counter:
            binary_logic_map.append(1)
        else:
            binary_logic_map.append(0)
        counter += 1

    return binary_logic_map


# Initialize a list to store the processed dataset
processed_dataset = []

# Initialize a set to store the classes of dataset
dataset_classes = dict()

# Counter for different classes of dataset
diff_class_count = 0

# Define path of dataset file
file_path = "../Datasets/iris/iris.data"

# Read all lines of the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Process each line in the dataset
for line in lines:
    if not line.isspace():
        # Initialize list of numerical features
        numerical_values = []

        # ! handle the string typed values (nominal/categorical variables)

        # Remove newline characters and split by commas
        features = line.strip().split(",")

        # Convert features from string to numerical types
        for feature in features[:-1]:
            # If the value is floating-point number
            if len(feature.split(".")) > 1:
                numerical_values.append(float(feature))
            # If the value is integer
            elif len(feature.split(".")) == 1:
                numerical_values.append(int(feature))

        # Check for new class values
        if features[-1] not in list(dataset_classes.keys()):
            dataset_classes[features[-1]] = len(dataset_classes.keys()) + 1

        # Append the class value
        numerical_values.append(dataset_classes.get(features[-1]))

        # Combine the numerical features and the encoded classes
        processed_dataset.append(numerical_values)

# Encode the class values according to the binary logic map
for i in range(0, len(processed_dataset)):
    processed_dataset[i] = processed_dataset[i][:-1] + encode_target_variable(
        len(dataset_classes.keys()), processed_dataset[i][-1]
    )

# Display the processed rows
processed_dataset[:]
