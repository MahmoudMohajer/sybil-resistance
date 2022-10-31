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

days = st.slider(
    'select range of days',
    1,
    16,
    (1,16)
)

tokens = st.slider(
    'select range of tokens',
    1,
    18,
    (1,18)
)

votes = st.slider(
    'select range of votes',
    1,
    3500,
    (1,3500),
    step=100
)

con_1= f'Variety_of_days >= {days[0]} & Variety_of_days <= {days[1]}'
con_2 = f'Variety_of_tokens >= {tokens[0]} & Variety_of_tokens <={tokens[1]}'
con_3 = f'Votes >= {votes[0]} & Votes <= {votes[1]}'

st.dataframe(
    data.query(f'{con_1} & {con_2} & {con_3}'),
    width=5000,
    height=500
    )