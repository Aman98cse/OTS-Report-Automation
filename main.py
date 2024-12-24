import pandas as pd

def create_pivot_table(data, index_cols, columns_col, values_col, aggfunc='sum'):
    pivot_table = pd.pivot_table(
        data,
        index=index_cols,
        columns=columns_col,
        values=values_col,
        aggfunc=aggfunc
    )

    return pivot_table

file_path = 'raw_data/PVVNL_OTS_NOV-24_REPORT.csv'
df = pd.read_csv(file_path)
df['PAID_SLAB']= df['TOTAL_PAID'].apply(lambda x: "Below 50K" if x < 50000 else "50K to 1Lac" if (x>=50000 and x<100000) else "above 1Lac")
df.to_csv('final.csv', index=False)

print(df.head())







