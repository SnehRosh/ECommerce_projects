from cgi import print_exception
from turtle import *
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


# Config
st.set_page_config(
    layout="wide",
    page_title="E-Commerce Analysis App",
    page_icon="🛍️"
)
 
price_llimit = 50
price_ulimit = 100
@st.cache_data()
def load_data(path):
    df = pd.read_csv('Sales_Transaction.csv')   
    df['Total_Price'] = df['Quantity']*df['Price']
    df.set_index('ProductNo', inplace=True)
    return df

with st.spinner('Processing E-Commerce Data'):
    df=load_data('Sales_Transaction.csv')
with st.container():
    st.image("https://sarasanalytics.com/wp-content/uploads/2022/07/Why-Customer-Analytics-is-Important-for-Ecommerce.jpg",width=500)
    st.title("ECommerce Analysis app")
    st.subheader("Data Summary")
c1,c2,c3,c4,c5,c6=st.columns(6)

total_products=df.shape[0]
duration="2018-2019"

c1.metric("Total PRODUCTS",total_products)
c2.metric("Year",duration)

st.header("E-Commerce Visualization")
fig=px.line(df,x='ProductName',y='Total_Price')
st.plotly_chart(fig,use_container_width=True)

top_products=df.sort_values(by='Total_Price',ascending=False).head(25)

c1, c2=st.columns([1,3])

limit=c2.slider("Select Number of Products",1,25, value=5)
products = top_products.index.tolist()[:limit]
trans_limited = df[(df.Price > 5) & (df.Price <= 6)] 
fig2 = px.area(trans_limited,x='ProductName',y='Price')

c1.dataframe(top_products)
c2.plotly_chart(fig2 ,use_container_width=True)

st.subheader("Trend Comparison")
c1,c2=st.columns([1,3])
product_list=df.index.tolist()
products=c2.multiselect("Select products",product_list)

if products:
    products_df=df[(df.Price > 50) & (df.Price <= 60)] 
    fig3=px.line(
        products_df,
        x=products_df.index,
        y=products_df.columns
        )
    for product in products:
        c1.info(f'{product}:{df.loc[product,"Total"]} E-Commerce')
    c2.plotly_chart(fig3,use_container_width=True)
    st.toast('Your graph has been loaded!',icon='🫡')
