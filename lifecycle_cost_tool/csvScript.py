import pandas as pd

# Define the key columns
key_columns = [
    'award_base_action_date_fiscal_year',
    'total_obligated_amount',
    'recipient_name',
    'period_of_performance_start_date',
    'period_of_performance_current_end_date'
]

# Replace with the path to your CSV file
csv_file_path = '/Users/owenlin/Desktop/Product Lifecycle App/lifecycle_cost_tool/uploads/Contracts_PrimeAwardSummaries_2024-08-17_H00M19S15_1.csv'

# Read the CSV file using only the key columns
try:
    df = pd.read_csv(csv_file_path, usecols=key_columns)
    
    # Clean the data (e.g., remove rows with missing data)
    df_clean = df.dropna()

    # Save the cleaned DataFrame to a new CSV file
    output_csv_path = r'/Users/owenlin/Desktop/Product Lifecycle App/lifecycle_cost_tool/exports/cleaned_contracts.csv'  # Replace with your desired output CSV file path
    df_clean.to_csv(output_csv_path, index=False)

    print(f"Cleaned data has been exported to {output_csv_path}")

except ValueError as e:
    print(f"Error processing the CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
