import pandas as pd

def clean_data(input_path, output_path):
    # 1. Read the Excel file
    df = pd.read_excel(input_path, engine='openpyxl')
    
    # 2. Remove completely empty rows (all cells null)
    df = df.dropna(how='all')
    print(f"Removed {len(df[df.isnull().all(axis=1)])} fully empty rows")
    
    # 3. Fix swapped Age (Column B) and Gender (Column C)
    swap_count = 0
    for index, row in df.iterrows():
        # Check if Column B contains gender words and Column C is numeric
        if (isinstance(row.iloc[1], str) and 
            any(gender in row.iloc[1] for gender in ['Male', 'Female', 'Non-binary']) and
            pd.to_numeric(row.iloc[2], errors='coerce') is not None):
            
            # Swap the values
            df.at[index, df.columns[1]], df.at[index, df.columns[2]] = row.iloc[2], row.iloc[1]
            swap_count += 1
    
    print(f"Fixed {swap_count} swapped Age/Gender values")


    # Step 1: Calculate the length of all columns
    expected_cols = len(df.columns)-1
    print("Length of expected columns:")
    print(expected_cols)
    bad_rows = []
    for idx, row in df.iterrows():
        # Count actual non-empty values in the row
        actual_values = sum(not pd.isna(value) for value in row)
        
        # Check if the actual values match the expected column count
        if actual_values != expected_cols:
            bad_rows.append((idx, row.astype(str).tolist()))  # Store index and row data as strings

    # Step 4: Print results
    if bad_rows:
        print("\nRows with incorrect column counts:")
        for idx, row_data in bad_rows:
            print(f"Row {idx} data: {row_data}")
        print(f"\nTotal: {len(bad_rows)} rows")
    else:
        print("\nAll rows have the correct number of values.")

    df.to_excel(output_path, index=False)
    print(f"\nSaved cleaned data to: {output_path}")

# Usage
# input_file = r"C:\Users\USER\OneDrive\Desktop\PS2\Social_Media_Usage_Sleep_Cleaned.xlsx"
input_file = r"C:\Users\USER\OneDrive\Desktop\PS2\Social Media Usage - Val.xlsm"
output_file = r"C:\Users\USER\OneDrive\Desktop\PS2\Social_Media_Usage_Val_Cleaned.xlsx"

clean_data(input_file, output_file)

