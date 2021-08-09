# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import pickle
import os

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Train model

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
iris_ds = dataiku.Dataset("iris_dataset")
iris_df = iris_ds.get_dataframe()

array = iris_df.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

# Fit the model on training set
model = LogisticRegression()
model.fit(X_train, Y_train)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Create pickle

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# save the model to folder
folder_path = dataiku.Folder("YJC0hRC9").get_path()
model_path = os.path.join(folder_path, "logistic_regression.pkl")
pickle.dump(model, open(model_path, 'wb'))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Load pickle

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# load the model from disk
model = pickle.load(open(model_path, "rb"))
result = model.predict(X_test)
print(result)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: MARKDOWN
# # Create lookup table

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df_to_enrich = iris_df[["pedi", "age"]]
df_to_enrich["id"] = df_to_enrich.index

# Recipe outputs
enrichment_dataset = dataiku.Dataset("enrichment_dataset")
enrichment_dataset.write_with_schema(df_to_enrich)