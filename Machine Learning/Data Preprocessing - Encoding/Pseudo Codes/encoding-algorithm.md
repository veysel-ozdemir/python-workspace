# Data Preprocessing and Encoding Algorithm

## Initialize Data Structures
1. Create empty list `processed_dataset`
2. Create empty list `encoded_dataset`
3. Create dictionary `continuous_typed_features` to store continuous features
   - Key: feature index
   - Value: dictionary mapping feature values to themselves
4. Create dictionary `integer_typed_features` to store integer features
   - Key: feature index
   - Value: dictionary mapping feature values to themselves
5. Create dictionary `categorical_features` to store categorical features
   - Key: feature index
   - Value: dictionary mapping feature values to enumerated values (1,2,3...)
6. Create dictionary `targets` to store target classes
   - Key: target value
   - Value: enumerated value (1,2,3...)
7. Create dictionary `encoding_values` to store encoded values

## Helper Functions
```
Function is_numeric(value):
    Try:
        Convert value to float
        Return True
    Catch:
        Return False

Function encode_target_variable(targets_count, target_value):
    Initialize empty list binary_logic_map
    For i from 1 to targets_count:
        If i equals target_value:
            Append 1 to binary_logic_map
        Else:
            Append 0 to binary_logic_map
    Return binary_logic_map

Function get_key_by_value(dictionary, search_value):
    For each key, value in dictionary:
        If value equals search_value:
            Return key
    Return None
```

## Main Algorithm
1. Read dataset from file

2. For each line in dataset:
    - Skip if line is empty
    - Split line by commas
    - Initialize empty instance list
    
    For each value except last (features):
        If value is numeric:
            If value contains decimal point:
                Convert to float
                Update continuous_typed_features dictionary
            Else:
                Convert to integer
                Update integer_typed_features dictionary
        Else:
            Keep as string
            Update categorical_features dictionary
        Add processed value to instance list
    
    Process target value:
        If target not in targets dictionary:
            Add new target with next enumeration value
        Add encoded target to instance
    
    Add instance to processed_dataset

3. Encode categorical features:
    For each column in processed_dataset:
        For each row:
            If value is categorical and not encoded:
                Add to encoding_values with next enumeration value

4. Encode target variables:
    For each instance in processed_dataset:
        Replace target value with binary logic map

5. Create final encoded dataset:
    For each row in processed_dataset:
        Initialize new instance list
        
        For each column value:
            If column is integer feature:
                Add mapped integer value
            Else if column is continuous feature:
                Add mapped continuous value
            Else if column is categorical feature:
                Add encoded categorical value
            Else:
                Add target value (already encoded)
                
        Add encoded instance to encoded_dataset

## Output
- Return encoded_dataset containing all processed and encoded features
