# Data Preprocessing Algorithm with Missing Value Handling

## Initialize Data Structures
1. Create empty list `processed_dataset`
2. Create empty list `encoded_dataset`
3. Create dictionary `continuous_typed_features`
   - Key: feature index
   - Value: dictionary mapping feature values to themselves
4. Create dictionary `integer_typed_features`
   - Key: feature index
   - Value: dictionary mapping feature values to themselves
5. Create dictionary `categorical_features`
   - Key: feature index
   - Value: dictionary mapping feature values to enumerated values (1,2,3...)
6. Create dictionary `targets`
   - Key: target value
   - Value: enumerated value (1,2,3...)
7. Create dictionary `encoding_values`
8. Create dictionary `missing_values`
   - Key: column index
   - Value: dictionary mapping row index to enumerated value
9. Create dictionary `sums`
   - Key: column index
   - Value: dictionary with 'sum' and 'total' keys
10. Initialize `line_count = 0`

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

2. Process each line in dataset:
    If line is not empty AND target value is not missing ('?'):
        Initialize empty instance list
        
        For each value except last (features):
            If value is numeric:
                If value contains decimal point:
                    Process as continuous feature
                Else:
                    Process as integer feature
            Else:
                If value is '?':
                    Record in missing_values dictionary
                Else:
                    Process as categorical feature
            Add processed value to instance
        
        Process target value:
            If new target, add to targets dictionary
            Add encoded target to instance
        
        Add instance to processed_dataset
        Increment line_count

3. Encode categorical features:
    For each column and row in processed_dataset:
        If value is categorical AND not '?' AND not already encoded:
            Add to encoding_values with next enumeration value

4. Encode target variables using binary logic mapping

5. Calculate averages for missing value replacement:
    For each column with missing values:
        For each row:
            If value is not missing:
                Add to running sum based on value type:
                    - Categorical: use encoded value
                    - Continuous: use feature value
                    - Integer: use feature value
                Increment total count
                Store in sums dictionary

6. Create final encoded dataset:
    For each row in processed_dataset:
        Initialize new instance list
        
        For each column value:
            If value is missing:
                Add calculated average from sums
            Else:
                Add appropriate encoded/processed value based on type
                
        Add encoded instance to encoded_dataset

## Outputs
- Processed dataset with encoded values
- Missing value locations and their replacements
- Feature type mappings
- Target variable encodings
