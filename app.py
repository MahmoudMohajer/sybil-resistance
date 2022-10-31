import streamlit as st
import pandas as pd
import numpy as np
from plotly import express as px

@st.cache
def read_data(dir):

    data = pd.read_csv(dir)
    return data

data_1 = read_data('grant_profile.csv')
data_2 = read_data('grant_info.csv')


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
    35000,
    (1,35000),
    step=99
)
money = st.slider(
    'select range of raised amount',
    1,
    85000,
    (1,85000),
    step=50
)

con_1= f'Variety_of_days >= {days[0]} & Variety_of_days <= {days[1]}'
con_2 = f'Variety_of_tokens >= {tokens[0]} & Variety_of_tokens <={tokens[1]}'
con_3 = f'Votes >= {votes[0]} & Votes <= {votes[1]}'
con_4 = f'Total_raised >={money[0]} & Total_raised <= {money[1]}'

st.dataframe(
    data_1.query(f'{con_1} & {con_2} & {con_3} & {con_4}'),
    width=5000,
    height=500
    )

"you also can get details of Grant by inserting 'grant_id'"

grant = st.text_input('enter the grant_id', 'grant_id')

st.dataframe(
    data_2.query(f'grant_id == {grant}'),
    width=5000,
    height=50
)

"I looked at the distribution of amounts of donations in USDT and out of 432k, 300k of them were in"
"range of **1-2** Dollars."
st.image('donation_dist.jpg', 'distribution of amount in USDT donation by each donor')

"as you can see we have very skewed distribution(right skewed), and it is economically optimized for"
"sybils to donate 1 USDT with each fake user and have maximium influence. but if we also consider"
"diverisity of donations as in table above by standard deviation of donations, the weight of "
"performing a sybil attack will get heavier and hard to lift."

st.image('clusters.jpeg', 'Categorizing groups of grants by Machine learning')

"the clusters show majority of grants don't get much out of matching pool. because of"
"outliers(Monopolists) there's small room for 'Poor' cluster to get a meaningful share out of the matching"
"pool, but middle class is better. it is 50-50 for middle class. and Monopolists control majority of matching pool."

st.subheader('Tree Map of Grants based on count of their Votes')

fig = px.treemap(data_frame=data_1, path=['Title'], values='Votes')

st.plotly_chart(fig, use_container_width=True)