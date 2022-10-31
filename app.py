import streamlit as st
import pandas as pd
import numpy as np



data = pd.read_csv('grant_profile.csv')













st.title("Sybil behavior Detection dashboard")
"in this dashboard we are presenting data and visualizations that help to Identify the general pattern"
"of how grants in gitcoin Grant rounds is happening. in this dashboard I wanted to stress highly on "
"importance of **Variability**. the more diverse a grant (in all dimensinos), the more relieble it is. "
"the table below shows the diffrent levels of 'Variability' accross all grants who participated in Gitcoin"
"Grant round 15."

st.write(data.head(20))