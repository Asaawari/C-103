import pandas as pd
import plotly.express as px

df = pd.read_csv("csv files/data.csv")

figure = px.bar(df,x="Country",y="InternetUsers",title="Number of Internet Users in each country")
figure.show()