from ctypes import sizeof
import pandas as pd
import numpy as np

data_file_path = "archive/Melbourne_housing_FULL.csv"
data_set = pd.read_csv(data_file_path)
data_set = data_set.dropna(axis=0)

y = data_set.Price
print(y)
print(data_set.columns)

# print(payment_data.loc[:, 'Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name'])
# print(payment_data.loc[:, 'Total_Amount_of_Payment_USDollars'])

