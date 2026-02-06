import pandas as pd

df_transcation = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_transaction.csv')
df_product = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/tbl_product.csv')

df_merged = pd.merge(df_transcation, df_product, on='product_id', how='left')

df_merged = df_merged[['trx_id','trx_date','product_id','product_name','product_category','product_cost','product_price','units']]

print(df_merged.head())