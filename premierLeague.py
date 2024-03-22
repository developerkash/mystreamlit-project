import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide',
                   page_title='Premier League Dashboard',
                   page_icon=":soccer:")
                   

@st.cache_data
def load():
    return pd.read_csv('premierLeague.csv')

#main code starts here
df = load()

st.image('banner.jpg', use_column_width=True, )
st.title("Premier League Dashboard")
with st.expander("View raw premier league data"):
    st.dataframe(df.sample(1000))   # display 1000 random rows

rows, cols = df.shape
c1, c2 = st.columns(2)
c1.markdown(f"### Number of rows: {rows}")
c2.markdown(f"### Number of columns: {cols}")

numeric_df = df.select_dtypes(include='number')
cat_df = df.select_dtypes(exclude='number')

with st.expander("column names"):
    st.markdown(f'columns with numbers: {" , ".join(numeric_df)}')
    st.markdown(f'columns with categories: {" , ".join(cat_df)}')

# visualize the data

c1, c2 = st.columns([1,4])
xcol = c1.selectbox('choose a column for x-axis', numeric_df.columns)
ycol = c1.selectbox('choose a column for y-axis', numeric_df.columns)
zcol = c1.selectbox('choose a column for z-axis', numeric_df.columns) 
color = c1.selectbox('choose a column for color', cat_df.columns)
fig = px.scatter_3d(df, x=xcol, y=ycol, z=zcol, color = color, height=600)

c2.plotly_chart(fig, use_container_width=True)

st.title("What is premier league?")
c1, c2 = st.columns(2)
c1.video('https://www.youtube.com/watch?v=9mucjcrhFcM')
c2.markdown(''' #english premier league is the top level of the english football league system.
            It is contested by 20 clubs, operating a system of promotion and relegation with the english football league (EFL).
            The premier league is a corporation in which the member clubs act as shareholders. Seasons run from August to May, with teams playing 38 matches each, totalling 380 matches in the season.
            Most games are played on saturdays and sundays, with a few games played during weekdays.''')

st.title("premier league clubs")
clubs = df['HomeTeam'].unique() + df['AwayTeam'].unique()
clubs = sorted(set(clubs))
st.info(" , ".join(clubs))

