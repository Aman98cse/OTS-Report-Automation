# import pandas as pd
#
#
# file_path = 'raw_data/PVVNL_OTS_NOV-24_REPORT.csv'
# df = pd.read_csv(file_path)
# df['PAID_SLAB']= df['TOTAL_PAID'].apply(lambda x: "Below 50K" if x < 50000 else "50K to 1Lac" if (x>=50000 and x<100000) else "above 1Lac")
#
# df.to_csv('test.csv', index=False)
#
# print(df.head())
#
# print('hello')


import pandas as pd

def create_pivot_table(data, index_cols, columns_col, values_col, aggfunc='sum'):
    """
    Creates a pivot table from the given DataFrame.

    Args:
        data: The DataFrame containing the data.
        index_cols: A list of column names to use as row labels.
        columns_col: The column name to use as column labels.
        values_col: The column name containing the values to aggregate.
        aggfunc: The aggregation function to apply (default: 'sum').

    Returns:
        The created pivot table as a DataFrame.
    """

    pivot_table = pd.pivot_table(
        data,
        index=index_cols,
        columns=columns_col,
        values=values_col,
        aggfunc=aggfunc
    )

    return pivot_table

# Example usage:
# Assuming you have a DataFrame named 'df' with columns 'Order Date', 'Product', 'Region', and 'Sales'

# Define the pivot table parameters
index_cols = 'ZONE'
columns_col = 'CATEGORY'
values_col = 'CATEGORY'

file_path = 'demo.xlsx'
df = pd.read_excel(file_path)

print('read successful')

# Create the pivot table
df.pivot(index="ZONE", columns="CATEGORY")
# pivot_table = create_pivot_table(df, index_cols, columns_col, values_col)

# Print the pivot table
# print(pivot_table)

# Save the pivot table to an Excel file (optional)
# pivot_table.to_excel('pivot_table.xlsx')
