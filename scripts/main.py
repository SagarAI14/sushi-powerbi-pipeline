from extract import extract_data
from transform import transform_data

def run_pipeline():

    print("Extracting data...")
    raw_data = extract_data()

    print("Transforming data...")
    df = transform_data(raw_data)

    print("Saving CSV...")

    output_path = "../data/processed/sushi_usage.csv"

    df.to_csv(output_path, index=False)

    print("Pipeline completed successfully!")
    print(df)

if __name__ == "__main__":
    run_pipeline()