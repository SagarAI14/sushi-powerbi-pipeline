from extract_api import extract_data
import pandas as pd

def run_pipeline():

    print("Extracting data from API...\n")

    data = extract_data()

    # Convert API response to DataFrame
    df = pd.DataFrame(data)

    print("Initial Data Preview:\n")
    print(df.head(5).to_string())

    # =========================
    # VALIDATION CHECKS
    # =========================

    print("\n=========================")
    print("DATA VALIDATION")
    print("=========================\n")

    # Shape
    print(f"Shape: {df.shape}")

    # Columns
    print("\nColumns:")
    print(df.columns.tolist())

    # Data types
    print("\nData Types:")
    print(df.dtypes)

    # Null values
    print("\nNull Values:")
    print(df.isnull().sum())

    # Duplicate rows
    duplicate_count = df.duplicated().sum()

    print(f"\nDuplicate Rows: {duplicate_count}")

    # =========================
    # DATA CLEANING
    # =========================

    print("\n=========================")
    print("DATA CLEANING")
    print("=========================\n")

    # Remove duplicates
    if duplicate_count > 0:
        df = df.drop_duplicates()
        print(f"Removed {duplicate_count} duplicate rows")
    else:
        print("No duplicate rows found")

    # Fill null values for text columns
    text_columns = df.select_dtypes(include="object").columns

    for col in text_columns:
        df[col] = df[col].fillna("Unknown")
        df[col] = df[col].str.strip()

    print("\nText columns cleaned")

    # Convert numeric columns safely
    numeric_columns = ["userId", "id"]

    for col in numeric_columns:

        if col in df.columns:

            df[col] = pd.to_numeric(df[col], errors="coerce")

            df[col] = df[col].fillna(0)

            df[col] = df[col].astype(int)

    print("Numeric columns converted")

    # Final validation
    print("\n=========================")
    print("FINAL DATA CHECK")
    print("=========================\n")

    print(df.info())

    print("\nCleaned Data Preview:\n")
    print(df.head(5).to_string())

    # Save cleaned CSV
    output_path = "../data/processed/api_data_cleaned.csv"

    df.to_csv(output_path, index=False)

    print("\nCSV saved successfully!")

    print(f"\nOutput File: {output_path}")

    print("\nAPI pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()