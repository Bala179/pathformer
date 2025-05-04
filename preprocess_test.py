import pandas as pd

def preprocess(cluster_data):

    # Convert InvoiceDate to datetime format
    cluster_data['InvoiceDate'] = pd.to_datetime(cluster_data['InvoiceDate'])

    # Extract the date part
    cluster_data['Date'] = cluster_data['InvoiceDate'].dt.date

    # Aggregate total sales by date and product code
    grouped_sales = cluster_data.groupby(['Date', 'StockCode'])['TotalSales'].sum()

    # Aggregate total sales by date
    total_sales_by_date = cluster_data.groupby('Date')['TotalSales'].sum()

    # Unstack the product code and fill all NaN's (which represent no sales) with 0
    productwise_sales = grouped_sales.unstack().fillna(0)

    merged_data = pd.merge(productwise_sales, total_sales_by_date, left_index=True, right_index=True)
    merged_data = merged_data.reset_index()
    merged_data.columns = ["date"] + list(merged_data.columns[1:-1]) + ["OT"]

    merged_data = merged_data.set_index("date")

    return merged_data

if __name__ == "__main__":
    file_names = [f'raw_data/cluster_{i}.csv' for i in [1, 5, 7]]

    for file_name in file_names:
        raw_data = pd.read_csv(file_name)
        preprocess(raw_data).to_csv("dataset/retail/" + file_name[9:])
