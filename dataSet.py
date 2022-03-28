from ctypes import sizeof
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor

data_file_path = "archive/Melbourne_housing_FULL.csv"
data_set = pd.read_csv(data_file_path)
data_set = data_set.dropna(axis=0)

y = data_set.Price # y - prediction target

melbourne_features = ['Rooms', 'Bathroom', 'BuildingArea'] # list of features
X = data_set[melbourne_features]


melbourne_model = DecisionTreeRegressor(random_state = 1) # define model
melbourne_model.fit(X, y) # fit model

print('Making predictions for the following 5 houses: ')
print(X.head())
print("The predictions are: ")
print(melbourne_model.predict(X.head()))


 





# print(data_set.columns)
# print(payment_data.loc[:, 'Submitting_Applicable_Manufacturer_or_Applicable_GPO_Name'])
# print(payment_data.loc[:, 'Total_Amount_of_Payment_USDollars'])

