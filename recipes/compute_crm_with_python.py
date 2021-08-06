# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
crm_prepared = dataiku.Dataset("crm_prepared")
df = crm_prepared.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
df['dif_revenue'] = df['revenue'] - df.groupby(['gender']).transform('mean')['revenue']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
crm_with_python = dataiku.Dataset("crm_with_python")
crm_with_python.write_with_schema(df)