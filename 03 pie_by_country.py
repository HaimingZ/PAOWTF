import pandas as pd
import plotly.express as px
import os

# read data
datapath = os.path.dirname(__file__)
df = pd.read_csv(datapath + '/data/data_processed.csv')

# pie chart by publication country
df_ = df['Country'].value_counts()
print(df_)

fig = px.pie(df_, values=df_.values, names=df_.index, width=600, height=400)
fig.update_traces(textposition='inside')
fig.update_layout(template='simple_white',
                  uniformtext_minsize=13,
                  uniformtext_mode='hide',
                  font=dict(family='Times New Roman', size=20),
                  margin=dict(l=10, r=10, t=10, b=10))
fig.show()
fig.write_image(datapath + "/figures/Fig_proportion_by_country.pdf")
