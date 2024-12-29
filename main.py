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

file_path = 'demo.xlsx'
df = pd.read_excel(file_path)
df['PAID_SLAB']= df['TOTAL_PAID'].apply(lambda x: "Below 50K" if x < 50000 else "50K to 1Lac" if (x>=50000 and x<100000) else "above 1Lac")
df.to_excel('final.xlsx', index=False)
 
file_path = 'final.xlsx'
df = pd.read_excel(file_path)
print(df['ZONE'].shape)
print(df['ZONE'].dtype)
print(df['ZONE'].head())

# Step 2: Create a Pivot Table using pandas
pivot_table = pd.pivot_table(df, 
                             values=['TOTAL_PAID'], 
                             index=['ZONE', 'CIRCLE','DIVISION_NAME'], 
                             columns='PAID_SLAB',
                             aggfunc={'TOTAL_PAID': 'sum','ZONE': 'count'}, 
                             fill_value=0)

# Step 3: Create a new Excel workbook to write the pivot table
pivot_file_path = 'pivot_table.xlsx'
with pd.ExcelWriter(pivot_file_path, engine='openpyxl') as writer:
    pivot_table.to_excel(writer, sheet_name='Pivot Table')

print(f"Pivot table written to {pivot_file_path}")

