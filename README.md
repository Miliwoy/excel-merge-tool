# Excel Merge Tool

This project merges multiple Excel files into one cleaned spreadsheet using Python and Pandas.

## Features

- Reads all `.xlsx` files from the `input_files` folder
- Combines them into one dataset
- Adds a `Source File` column
- Removes duplicate records by `Customer ID`
- Exports the result to `merged_output.xlsx`

## How to Run

Install dependencies:

```bash
pip install pandas openpyxl
```

Run the script:

```bash
python merge_excel.py
```

## Technologies

- Python
- Pandas
- OpenPyXL
