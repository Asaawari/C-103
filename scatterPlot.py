import pandas as pd
import plotly.express as px

df = pd.read_csv("csv files/data.csv")

figure = px.scatter(df,x="Population",y="Per capita",size="Percentage",color="Country",size_max=60,title="Per capita income of each country")
figure.show()