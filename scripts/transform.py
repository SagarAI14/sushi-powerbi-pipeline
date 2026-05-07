import pandas as pd

def transform_data(data):

    rows = []

    report_items = data.get("Report_Items", [])

    for item in report_items:

        title = item.get("Title")
        publisher = item.get("Publisher")
        platform = item.get("Platform")

        performances = item.get("Performance", [])

        for perf in performances:

            begin_date = perf["Period"]["Begin_Date"]
            end_date = perf["Period"]["End_Date"]

            instances = perf.get("Instance", [])

            for inst in instances:

                metric_type = inst.get("Metric_Type")
                count = inst.get("Count")

                rows.append({
                    "Title": title,
                    "Publisher": publisher,
                    "Platform": platform,
                    "Begin_Date": begin_date,
                    "End_Date": end_date,
                    "Metric_Type": metric_type,
                    "Count": count
                })

    df = pd.DataFrame(rows)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing text values
    df["Publisher"] = df["Publisher"].fillna("Unknown")
    df["Title"] = df["Title"].fillna("Unknown")
    df["Platform"] = df["Platform"].fillna("Unknown")

    # Handle missing numeric values
    df["Count"] = df["Count"].fillna(0)

    # Clean text columns
    df["Publisher"] = df["Publisher"].str.strip()
    df["Title"] = df["Title"].str.strip()

    # Convert Count to integer
    df["Count"] = df["Count"].astype(int)

    return df