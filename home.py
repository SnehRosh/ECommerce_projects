import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import seaborn as sns 
from matplotlib import pyplot as plt


# Config
st.set_page_config(
    layout="wide",
    page_title="E-Commerce Analysis App",
    page_icon="🛍️"
)
 
cols_to_drop=['Review Text','Title']

@st.cache_data()
def load_data(path):
    df = pd.read_csv('Sales_Transactions.csv')
   
    df.drop(columns=cols_to_drop, inplace=True)
    return df

with st.spinner('Processing E-Commerce Data'):
    df=load_data('Sales_Transaction.csv')
with st.container():
    st.title("Women Fashion Trend Data-Analysis")
    st.image("https://www.scnsoft.com/blog-pictures/ecommerce/fashion-ecommerce/guide-to-fashion-ecommerce.png",width=800,caption='Ecom Analysis')
    st.subheader("Data Summary",divider='red')
c1,c2,c3,c4=st.columns(4)

total_products=df.shape[0]
type_trend="Women Clothing"

#Main Heads
c1.metric("Total PRODUCTS",total_products)
c2.metric("Type",type_trend)
c3.image("https://www.dlf.pt/dfpng/middlepng/475-4754245_women-fashion-ecommerce-website-development-fashion-website-png.png",width=500)

st.header("Fasion Data-Visualization",divider='rainbow')

#Popular Product class  based on Ratings
st.subheader('Popular Products',divider='blue')
fig = px.histogram(df, 
                   x='Class Name',
                   y='Rating')
st.plotly_chart(fig,use_container_width=True)

#Product Trend based on age
st.subheader('Product Trend Analysis',divider='orange')
fig2 = sns.lineplot(
             data=df,
             x='Age',
             y='Department Name',
             hue='Department Name'
            )
plt.show()
fig2,ax=plt.subplots()

#Top Product based on rating
top_products = df.sort_values(by='Rating',ascending=False).head(10)
tp_list = top_products[['Clothing ID','Rating','Division Name','Class Name']]

c1,c2 = st.columns([1,2])

c1.dataframe(tp_list)
fig3 = px.bar(tp_list,x='Class Name',y='Clothing ID',
       title="Type of Clothing along with ID's Range",
       hover_data=['Class Name', 'Clothing ID'],
       width=500,
       color='Class Name')
c2.plotly_chart(fig3,use_container_width=True)

#Scatter plot visualisation based on Rating of Division Name
st.subheader('Cloths Rating based on Division',divider='rainbow')
fig4 = sns.scatterplot(data=df,x='Division Name',
                       y='Rating',
                       hue='Rating',
                       palette='hot',
                       style='Division Name')
fig4,ax=plt.subplots()

#Sunburst plotting on age and clothing analysis
c1,c2 = st.columns([1,2])
df_sun = df[['Clothing ID','Division Name','Department Name','Class Name','Rating']].head(10)
c2.dataframe(df_sun)
trans_nan = df.dropna()
fig5 = px.sunburst(
    data_frame=trans_nan,
    path=['Division Name','Department Name','Class Name'],
    values='Age',
    names=trans_nan.index,
    color='Rating',
    color_continuous_scale='RdBu'
)
c1.plotly_chart(fig5,use_container_width=True)

#Treemap ploting
st.subheader('Clothes Division based on Recommended IND',divider='rainbow')
c1,c2 = st.columns(2)
fig6= px.treemap(
    data_frame=trans_nan,
    path=['Division Name','Department Name','Class Name'],
    values='Recommended IND',
    names=trans_nan.index
)
c1.plotly_chart(fig6,use_container_width=True)
c2.image("https://raw.githubusercontent.com/wpcodevo/lc28-fashion-ecommerce-website/starter/fashion%20ecommerce%20website%20html%20css%20scss%20javascript.png",width=600)

# Rating Analysis on Departments Name
st.subheader('Rating analysis based on Departments Name ',divider='violet')
fig7 = sns.displot(data=df, x='Rating',hue='Department Name')
fig7,ax=plt.subplots()
plt.show()

st.toast('Your graph has been loaded!',icon='🫡')
