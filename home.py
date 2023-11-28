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
    st.title('Women Fashion Trend Data-Analysis')
    st.image("https://www.nopcommerce.com/images/blog/2023-march-fashion-ecommerce-trends/__comp.jpg",caption='Ecom Analysis')
    st.subheader("Data Summary",divider='red')
c1,c2,c3,c4=st.columns(4)

total_products=df.shape[0]
type_trend="Women Clothing"

#Main Heads
c1.metric("Total PRODUCTS",total_products)
c2.metric("Type",type_trend)
c3.image("https://www.dlf.pt/dfpng/middlepng/475-4754245_women-fashion-ecommerce-website-development-fashion-website-png.png",width=500)

st.header("Fashion Data-Visualization",divider='rainbow')

#Popular Product class  based on Ratings
st.subheader('Popular Products',divider='blue')
fig = px.histogram(df, 
                   x='Class Name',
                   y='Rating')
st.plotly_chart(fig,use_container_width=True)

#Product Trend based on age
st.subheader('Analysis on Department of clothes based on ages',divider='grey')
c1,c2=st.columns(2)
fig2,ax=plt.subplots()
ax = sns.lineplot(
             data=df,
             x='Age',
             y='Department Name',
             hue='Department Name'
            )
c1.pyplot(fig2)
c2.image('https://www.iadvize.com/hubfs/FASHION%20%281%29.png')
plt.show()


#Top Product based on rating
st.subheader('Product Trend Analysis',divider='orange')
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
st.subheader('Visualisation based on Rating of Division Names',divider='orange')
c1,c2 = st.columns(2)
fig4 = sns.relplot(data=df,
                x='Division Name',
                y='Rating',
                hue="Rating",
                style="Department Name")
c1.pyplot(fig4)
c2.image('https://cdn.dribbble.com/userupload/8873876/file/original-0fd18e38f8265aa4f41b130201262944.png?resize=450x338&vertical=center',width=500)


#Sunburst plotting on age and clothing analysis
st.subheader('Clothes Rating based on Division and Departments ',divider='rainbow')
c1,c2 = st.columns(2)
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
c1,c2 = st.columns(2)
c1.subheader('Clothes Division based on Recommended IND',divider='rainbow')
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
c1,c2=st.columns(2)
c1.image('https://www.dfupublications.com/images/2022/06/08/India%E2%80%99s-fashion-e-commerce-market-to-grow-to-30-billion-in-5-years_large.jpg')
fig7 = sns.displot(data=df, x='Rating',hue='Department Name',binwidth=0.5)
c2.pyplot(fig7)


#Positive Feedback
pos_feed = df[['Positive Feedback Count','Division Name','Rating']].head(30)
st.subheader('Positive Feedback Counts Based on Division Name of Clothes',divider='blue')
c1,c2 = st.columns(2)
c2.dataframe(pos_feed)
fig8,ax=plt.subplots()
ax=sns.violinplot(data=pos_feed, 
               x='Division Name',
               y='Positive Feedback Count',
               hue='Rating',
               bw_adjust=.5, 
               cut=1, linewidth=1, palette="Set3",legend=False)
c1.pyplot(fig8)
plt.show()


# 3D
st.subheader('3-D Visualisation on Rating',divider='blue')
c1,c2 = st.columns(2)
Age_v= df[['Age','Recommended IND','Rating','Department Name']].head(30)
c2.dataframe(Age_v)
fig9 = px.scatter_3d(Age_v, 
                     x='Rating', 
                     y='Recommended IND', 
                     z='Age',
                     color='Department Name')
c1.plotly_chart(fig9,use_container_width=True)

st.toast('Your graph has been loaded!',icon='🫡')
