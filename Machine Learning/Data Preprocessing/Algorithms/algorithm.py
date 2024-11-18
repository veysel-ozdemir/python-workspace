# Data Preprocessing - Encoding Algorithm

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

# Initialize a dictionary to store encode values
encoding_values = dict()

# Initialize a dictionary to store the missing values
# Key = index of the value where it resides (column index)
# Value = dictionary (Key: index of instance (row index) & Value: number of first occurrence in list (1,2,3,..))
missing_values = dict()

# Initialize a dictionary to store the sum and total count of present values
# Key = index of the feature values (column index)
# Value = dictionary with 'sum' and 'total' keys
sums = dict()

# Initilize line counter
line_count = 0

# Initialize a list to store the labels
labels = []

# Define the target variable
target_variable = "os"

# Define path of dataset file
file_path = "../Custom Datasets/missing-value-test.csv"

# Read all lines of the file
with open(file_path, "r") as file:
    lines = file.readlines()

# Get the line where the labels reside
for line_number in range(0, len(lines)):
    if not lines[line_number].isspace():
        labels_line = lines.pop(line_number).strip().split(",")
        break

# Store the labels
for label in labels_line:
    labels.append(label)


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

        # If the target variable exists, perform the encoding process
        if values[labels.index(target_variable)] != "?":
            for index in range(0, len(values)):
                value = values[index]
                # Check whether the variable is not the target
                if index != labels.index(target_variable):
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
                                    continuous_typed_features[index][float(value)] = (
                                        float(value)
                                    )
                            # The feature is not present yet
                            else:
                                # Add the feature to dictionary
                                continuous_typed_features[index] = {
                                    float(value): float(value)
                                }
                        # If the value is integer
                        elif len(value.split(".")) == 1:
                            instance.append(int(value))

                            # Process the integer typed feature values for future encoding
                            # Get dictionary of integer typed features at index
                            feats = integer_typed_features.get(index)

                            # The feature is present in the dictionary
                            if feats is not None:
                                if int(value) not in list(feats.keys()):
                                    integer_typed_features[index][int(value)] = int(
                                        value
                                    )
                            # The feature is not present yet
                            else:
                                # Add the feature to dictionary
                                integer_typed_features[index] = {int(value): int(value)}
                    # In case of non-numeric values
                    else:
                        instance.append(value)

                        # If the value is missing
                        if value == "?":
                            if index in list(missing_values.keys()):
                                missing_values[index][line_count] = (
                                    len(missing_values[index]) + 1
                                )
                            else:
                                missing_values[index] = {line_count: 1}
                        else:
                            # Process the categorical feature values for future encoding
                            # Get dictionary of categorical features at index
                            feats = categorical_features.get(index)

                            # The feature is present in the dictionary
                            if feats is not None:
                                if value not in list(feats.keys()):
                                    categorical_features[index][value] = (
                                        len(feats.keys()) + 1
                                    )
                            # The feature is not present yet
                            else:
                                # Add the feature to dictionary
                                categorical_features[index] = {value: 1}
                # If it is the target variable
                else:
                    # Process the target values for future encoding
                    # Check for new target values
                    if value not in list(targets.keys()):
                        # Store it to the dictionary
                        targets[value] = len(targets.keys()) + 1

                    # Append the target value to the list
                    instance.append(targets.get(value))

            # Add the instance to the processed dataset
            processed_dataset.append(instance)

            # Increment line count
            line_count += 1

# Display the processed rows
print("Processed dataset:")
for i in processed_dataset:
    print(i)
print()

print("Categorical features:")
for i in categorical_features.items():
    print(i)
print()

print("Integer typed features:")
for i in integer_typed_features.items():
    print(i)
print()

print("Continuous typed features:")
for i in continuous_typed_features.items():
    print(i)
print()

print("Target variables:")
for i in targets.items():
    print(i)
print()

print("Missing values:")
for i in missing_values.items():
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


# Go through all columns of each row and store the encoding values
for col in range(0, len(processed_dataset[0])):
    for row in range(0, len(processed_dataset)):
        # Get the value
        value = processed_dataset[row][col]
        # If the value is categorical value and not already stored in dictionary
        if (
            (not is_numeric(value))
            and (not value in list(encoding_values.values()))
            and (value != "?")
        ):
            # Assign the value to the incremented key value
            encoding_values[len(encoding_values) + 1] = value

print("Encoding map of categorical features:")
for i in encoding_values.items():
    print(i)
print()


# Get the key of specified unique value of the dictionary
def get_key_by_value(dict, value):
    for key, val in dict.items():
        if val == value:
            return key
    return None


# Calculate the average values
for col in range(0, (len(processed_dataset[0]))):
    # Go through all variables and find the right index
    for row in range(0, len(processed_dataset)):
        if col in list(missing_values.keys()):
            # Get the value
            value = processed_dataset[row][col]
            # Sum the encoding values of that feature variables
            if value != "?":
                # The value is categorical
                if not is_numeric(value):
                    # The feature is present in the dictionary
                    if sums.get(col) is not None:
                        sums[col]["sum"] += get_key_by_value(
                            encoding_values, processed_dataset[row][col]
                        )
                        sums[col]["total"] += 1
                    # The feature is not present in the dictionary
                    else:
                        sums[col] = {
                            "sum": get_key_by_value(
                                encoding_values, processed_dataset[row][col]
                            ),
                            "total": 1,
                        }
                # The value is floating-point number
                elif len(str(value).split(".")) > 1:
                    # The feature is present in the dictionary
                    if sums.get(col) is not None:
                        sums[col]["sum"] += continuous_typed_features[col][value]
                        sums[col]["total"] += 1
                    # The feature is not present in the dictionary
                    else:
                        sums[col] = {
                            "sum": continuous_typed_features[col][value],
                            "total": 1,
                        }
                # The value is integer
                elif len(str(value).split(".")) == 1:
                    # The feature is present in the dictionary
                    if sums.get(col) is not None:
                        sums[col]["sum"] += integer_typed_features[col][value]
                        sums[col]["total"] += 1
                    # The feature is not present in the dictionary
                    else:
                        sums[col] = {
                            "sum": integer_typed_features[col][value],
                            "total": 1,
                        }


# Display the encoded rows
print("Averages for replacement of each feature indexes containing missing values:")
for i, j in sums.items():
    print(f"Index: {i}\t{j} \tavg: {j['sum']/j['total']}")
print()

# Combine all variables according to their indexes
for row in range(0, len(processed_dataset)):
    # Initialize list of the instance's data
    instance = []

    # Go through all variables and find the right index
    for col in range(0, len(processed_dataset[row])):
        # The variable value is missing
        if (col in list(missing_values.keys())) and (
            row in list(missing_values[col].keys())
        ):
            # Append the average value to the instance list
            avg = sums[col]["sum"] / sums[col]["total"]
            instance.append(avg)
        # The variable value is present
        else:
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
                        instance.append(get_key_by_value(encoding_values, feats))

            # Target values
            else:
                instance.append(processed_dataset[row][col])

    # Add the instance to new dataset list
    encoded_dataset.append(instance)

# Display the encoded rows
print("Encoded dataset before target variable encoding:")
for i in encoded_dataset:
    print(i)
print()

# Copy the encoded dataset
tmp = encoded_dataset.copy()
# Encode the target values according to the binary logic map
for i in range(0, len(tmp)):
    # Initialize list of the edited row
    edited_row = []
    for j in range(0, len(tmp[0])):
        # If the value is not target variable
        if j != labels.index(target_variable):
            edited_row.append(tmp[i][j])
    # Append at the end the target variable as binary logic map
    edited_row += encode_target_variable(
        len(targets.keys()), tmp[i][labels.index(target_variable)]
    )
    # Update the processed_dataset
    encoded_dataset[i] = edited_row

print("Encoded dataset:")
for i in encoded_dataset:
    print(i)
print()
