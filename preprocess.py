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
    final_data = pd.merge(create_features(merged_data['TotalSales']), merged_data, left_index=True, right_index=True)
    final_data = final_data.reset_index()
    final_data.columns = ["date"] + list(final_data.columns[1:-1]) + ["OT"]

    final_data = final_data.set_index("date")

    return final_data

# statistics by group_idx
def create_features(total_sales):
    group = pd.DataFrame(index=total_sales.index)
    # 1st and 7th lag
    group['lag_1'] = total_sales.shift(1).fillna(0)
    group['lag_7'] = total_sales.shift(7).fillna(0)
    
    # rolling mean and sd
    for window in [3, 7, 14, 30]:
        group[f'rolling_mean_{window}'] = total_sales.rolling(window).mean().bfill()
        group[f'rolling_std_{window}'] = total_sales.rolling(window).std().bfill()
    
    # exponential moving average
    group['ema_7'] = total_sales.ewm(span=7, adjust=False).mean()
    
    # first order difference
    group['daily_diff'] = total_sales.diff(1)
    
    return group.fillna(0)

if __name__ == "__main__":
    file_names = [f'raw_data/cluster_{i}.csv' for i in [1, 5, 7]]

    for file_name in file_names:
        raw_data = pd.read_csv(file_name)
        preprocess(raw_data).to_csv("dataset/retail/" + file_name[9:])
