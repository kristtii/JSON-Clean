# JSON Clean Script

The JSON Clean Script is a utility that takes a JSON file as input and performs the following transformations to make the data more suitable for code consumption:

1. Removes symbols and special characters from the JSON file.
2. Replaces spaces in the JSON keys with underscores (`_`).
3. Converts all letters in the keys to lowercase.

## Why Use JSON Clean Script?

When working with JSON data in code, it's often helpful to have clean and consistent keys to avoid potential issues. By using this script, you ensure that your JSON data is in a more developer-friendly format, making it easier to access and manipulate the data programmatically.

## Usage

1. Make sure you have Python installed on your system.
2. Download the `json_clean.py` script.
3. Run the script using the following command:

```
python json_clean.py
```

Make sure to input the file location at the end of the code. Also specify the location for the new file to be saved.

**Note**: The original JSON file will not be modified. The script will create a new JSON file with the cleaned data. The new file will have a new name specified by you.

## Example

Suppose you have a JSON file named `data.json` with the following content:

```json
{
  "First Name": "Kristi",
  "Last Name": "Kristi",
  "Age": 21,
  "$Address": "Tirane"
}
```

Running the script on `data.json` will generate a new JSON file named `data_cleaned.json` with the following content:

```json
{
  "first_name": "Kristi",
  "last_name": "Kristi",
  "age": 21,
  "address": "Tirane"
}
```

Now you have a cleaned version of your JSON data, ready to be used in your code!
