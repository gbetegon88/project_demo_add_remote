# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
crm_prepared = dataiku.Dataset("crm_prepared")
crm_prepared_df = crm_prepared.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

crm_with_python_df = crm_prepared_df # For this sample code, simply copy input to output


# Write recipe outputs
crm_with_python = dataiku.Dataset("crm_with_python")
crm_with_python.write_with_schema(crm_with_python_df)
