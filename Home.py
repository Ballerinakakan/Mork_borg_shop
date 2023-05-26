import streamlit as st
import pandas as pd
import numpy as np
import Listor as lis
import random as rng

st.title('Welcome to the shop!')

storeDF = pd.read_csv("General shop csv - GeneralShopList.csv")
#st.write(storeDF)

rolledDF = pd.DataFrame(columns=['Vara', 'Pris', 'Antal', 'Regler'])

for index, row in storeDF.iterrows():
    if(rng.randrange(100) < row[3]):
        newRow = {'Vara' : row[0], 'Pris' : row[1] + (rng.randint(0, round((row[1]/5) + 0.5)) - round((row[1]/10) + 0.5)), 'Antal' : rng.randrange(row[4]) + 1, 'Regler' : row[2] }
        if newRow['Pris'] <= 0:
            newRow['Pris'] = 1
        if newRow['Regler'] == "UPergRoll":
            newRow['Regler'] = rng.choice(lis.uPerg)
        elif newRow['Regler'] == "CPergRoll":
            newRow['Regler'] = rng.choice(lis.cPerg)
        elif newRow['Regler'] == "LightRoll":
            newRow['Regler'] = rng.choice(lis.light)
        elif newRow['Regler'] == "MedRoll":
            newRow['Regler'] = rng.choice(lis.med)
        elif newRow['Regler'] == "HeavyRoll":
            newRow['Regler'] = rng.choice(lis.heavy)

        rolledDF.loc[len(rolledDF)] = newRow

st.dataframe(rolledDF, width=900)