# installing some libraries streamlit used during project
#        .\.venv\Scripts\Activate.ps1
import streamlit as st
import pandas as pd
import preprocessor,helper
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff
import streamlit.components.v1 as components


df = pd.read_csv('athlete_events.csv')
region_df=pd.read_csv('noc_regions.csv')
medal_df =df.drop_duplicates(subset=['Team','NOC','Games','Year','City','Sport','Event','Medal'])

df = preprocessor.preprocess(df, region_df)
st.sidebar.image('https://img.olympics.com/images/image/private/t_social_share_thumb/f_auto/v1538355600/primary/onpsxnx7v5atmhxvdipc')
st.sidebar.title('Summer Olympic Analysis')

#____________________________________________ Creating sidebars__________________________________________________________________________
user_menu = st.sidebar.selectbox(
    'Select type of Analysis',
    ['Home', 'Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete wise Analysis','Year-wise Analysis'])

#___________________________________Sidebar_correction_text_______________________________________________________________________________
# 1. Page Configuration (Must remain first)
st.set_page_config(
    page_title="Summer Olympic Analysis",
    page_icon="🏅",
    layout="wide"
)
# Force bright white text and labels across the entire sidebar everywhere

st.markdown(
    """
<style>
/* 1. Sidebar Background */
[data-testid="stSidebar"] {
    background-color: #0b0f19 !important;
}

/* 2. Target Every Text Element Inside Sidebar with Highest Priority */
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] h4,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] div,
[data-testid="stSidebar"] .stMarkdown {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}

/* 3. Dropdown Box Styling */
[data-testid="stSidebar"] div[data-baseweb="select"] {
    background-color: #1e293b !important;
    border-radius: 8px;
}
[data-testid="stSidebar"] div[data-baseweb="select"] span {
    color: #ffffff !important;
    -webkit-text-fill-color: #ffffff !important;
}
[data-testid="stSidebar"] svg {
    fill: #ffffff !important;
}
</style>
""",
    unsafe_allow_html=True,
)
#_____________________________________________Datasets Loading and call to preprocessor.py__________________________________________________________________________
# 2. Data Loading & Preprocessing
df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
df = preprocessor.preprocess(df, region_df)
#______________________________________________________________________Home page Frontend________________________________________________________

# 4. Route Styling & Pages
if user_menu == "Home":

# Full Background Theme for Landing Page Only
    st.markdown(
        """
        <style>
        
        /* Top header strip */
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
            border-bottom: 1px solid #e2e8f0;
        }

        /* Sidebar dark theme */
        section[data-testid="stSidebar"] {
            background-color: #0b0f19 !important;
        }
        section[data-testid="stSidebar"] * {
            color: #ffffff !important;
        }
        section[data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #1e293b !important;
            border-radius: 8px;
        }

        /* Olympic track & sky background */
        .stApp {
            background-color: #70c4f4;
            background-image: 
                linear-gradient(180deg, rgba(220, 250, 244, 0.72) 0%, rgba(224, 242, 254, 0.82) 40%, rgba(185, 28, 28, 0.45) 100%),
                url("https://static.stacker.com/s3fs-public/styles/sar_screen_maximum_large/s3/UsainBolt1FB7X_3.png");
            background-repeat: no-repeat;
            background-size: cover;
            background-position: center bottom;
            background-attachment: fixed;
        }

        /* Black Text for main page */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label, [data-testid="stMetricValue"] {
            color: #000000 !important;
        }

        /* Fullscreen Hero Container without dark box */
        .hero-fullscreen {
            text-align: center;
            padding-top: rem; 
            padding-bottom: 3rem;
            width: 100%;
        }

        .badge {
            display: inline-block;
            padding: 0.35rem 1rem;
            border-radius: 70px;
            background-color: rgba(11, 15, 25, 0.8);
            color: #f8fafc!important;
            font-weight: 800;
            font-size: 1.5rem;
            letter-spacing: 1px;
            border: 1px solid rgba(253, 224, 71, 0.5);
            margin-bottom: 0rem;
        }

        /* Typewriter Animation */
        .typewriter-text {
            font-size: 3.5rem;
            font-weight: 15data-testid="stMetricValue"00;
            letter-spacing: 2px;
            color: #0b0f19 !important;
            display: inline-block;
            overflow: hidden;
            white-space: nowrap;
            border-right: 4px solid #0b0f19;
            animation: typing 3s steps(30, end), blink-caret 0.75s step-end infinite;
            margin-bottom: 1rem;
        }

        .hero-sub-clean {
            font-size:1.5rem;
            font-weight: 600;
            color: #0b0f19!important;
            margin-bottom: 2rem;
        }

        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: #0b0f19; }
        }

        /* Feature Cards */
        .card-box {
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.6);
            border-radius: 14px;
            padding: 16px;
            min-height: 120px;
            color: #000000 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.07);
        }
        .card-box b {
            color: #000000 !important;
            font-size: 1.5rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Hero Section_________________Hero section______________________________________________________________________________________
    st.markdown(
        """
        <div class="hero-fullscreen">
            <div class="badge">OLYMPICS ARCHIVE</div><br>
            <img src="https://pngimg.com/uploads/olympic_rings/olympic_rings_PNG15.png" 
                 style="width: 150px; margin-bottom: 30px;" /><br>
            <div style="display:flex; justify-content: center;">
                <span class="typewriter-text">OLYMPIC RECORDS AND ANALYSIS....</span>
            </div>
            <div class="hero-sub-clean">
                120 Years of Athletic Excellence & World Records (1896 – 2016)
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
#___________________________metric values ,font and weight__________________________________________________________________________________________________
    st.markdown(
        """
        <style>
        /* Metric Values (e.g. 28, 23, 52, 115,525) */
        div[data-testid="stMetricValue"] > div {
            font-size: 3rem !important;
            font-weight: 600 !important;
            color: #0b0f19 !important;
        }

        /* Metric Labels (e.g. Olympic Editions, Host Cities) */
        div[data-testid="stMetricLabel"] p,
        div[data-testid="stMetricLabel"] label {
            font-size: 20rem !important;
            font-weight: 900 !important;
            color: #1e293b !important;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )
    # Metrics
    editions = df["Year"].nunique()
    cities = df["City"].nunique()
    sports = df["Sport"].nunique()
    # athletes = len(np.unique(df["Name"]))
    st.markdown(
        """
    <style>
    /* Target all possible nested elements inside the metric label */
    [data-testid="stMetricLabel"],
    [data-testid="stMetricLabel"] *,
    [data-testid="stMetricLabel"] > div,
    [data-testid="stMetricLabel"] p,
    [data-testid="stMetricLabel"] span,
    [data-testid="stMetricLabel"] strong {
        font-size: 2rem !important;
        font-weight: 500 !important;
        color:#0b0f19  !important;
    }

    /* Metric value size */
    [data-testid="stMetricValue"],
    [data-testid="stMetricValue"] * {
        font-size: 3rem !important;
        font-weight: 900 !important;
        color: #0b0f19 !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Olympic Editions", value=f"{editions}")
    with col2:
        st.metric(label="Host Cities", value=f"{cities}")
    with col3:
        st.metric(label="Sports Disciplines", value=f"{sports}")
    with col4:
        st.metric(label="Total Athletes", value='110k+')
 #__________________________________________________selection_analysis_bar_show__________________________________________________________

    st.markdown("---")
    st.markdown(
        """
    <div style="
        background: rgba(15, 23, 42, 0.85); 
        border-left: 5px solid #38bdf8; 
        padding: 12px 16px; 
        border-radius: 8px; 
        color: #ffffff; 
        font-weight: 900; 
        margin: 15px 0;">
        👈 Select an analysis mode from the sidebar to view detailed breakdowns
    </div>
    """,
        unsafe_allow_html=True,
    )
#_____________________________________________Cardboxes_______________________________________________________________________
    st.markdown("### 📊 What You Can Explore")



    c1, c2, c3, c4,c5= st.columns(5)
    with c1:
        st.markdown(
            '<div class="card-box"><b>🥇 Medal Tally</b><br>Filter overall and historical podium counts by year and nation.</div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="card-box"><b>📈 Overall Analysis</b><br>Macro trends across participating nations, events, and gender ratios.</div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="card-box"><b>🌍 Country-wise Analysis</b><br>Deep-dive into country performance, top sports, and heatmaps.</div>',
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            '<div class="card-box"><b>🏃 Athlete-wise Analysis</b><br>Age distributions, height vs. weight trends, and all-time legends.</div>',
            unsafe_allow_html=True,
        )
  #___________________________________analysis_views_backgroun__________________________________________________________________


# All Other Analysis Views (Shiny White Background)
else:
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"] {
            background-color: #ffffff !important;
            border-bottom: 1px solid #e2e8f0;
        }
        section[data-testid="stSidebar"] {
            background-color: #0b0f19 !important;
        }
        section[data-testid="stSidebar"] * {
            color: #rrrrrr !important;
        }
        section[data-testid="stSidebar"] div[data-baseweb="select"] {
            background-color: #1e293b !important;
            border-radius: 8px;
        }
        .stApp {
            background: linear-gradient(200deg, #ffffff 0%, #f8fafc 40%, #e2e8f0 100%) !important;
        }
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp p, .stApp span, .stApp label, [data-testid="stMetricValue"] {
            color: #000000 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
#________________________________________________________________________________________________________________________________



 #_________________________________________#Front view completed_____________________________________________________________

#___________________________________________ backend on sidebar selectbox ,Medal_tally________________________________________________________
if user_menu=='Medal Tally':
    # st.header('Medal tally') - will look like a heading for the medal tally table
    st.sidebar.header('Medal tally')
    years,country=helper.country_year_list(df)
    selected_year = st.sidebar.selectbox('Select Year', years)
    selected_country=st.sidebar.selectbox('Select Country',country)
    medal_tally=helper.fetch_medal_tally(df,selected_year,selected_country)
    if selected_year=='Overall' and selected_country=='Overall':
        st.title('Olympics results (1896-2016)') #fetched
    if selected_year!='Overall' and selected_country=='Overall':
        st.title('Medal Tally in '+str(selected_year)+" Summer Olympics")
    if selected_year=='Overall' and selected_country!='Overall':
        st.title('Overall Performance of ' + selected_country+' in Summer Olympics')
    if selected_year!='Overall' and selected_country!='Overall':
        st.title(selected_country+' in '+ medal_df['City'][medal_df['Year'] == selected_year].unique()[0] +' Olympics '+ str(selected_year))

    st.dataframe(medal_tally)

    # selected_year = st.session_state.get('selected_year', None)
    # selected_country = st.session_state.get('selected_country', None)


#______________________________'Overall_Analysis___________________________________________________________________________________
if user_menu=='Overall Analysis':

#______________________________________cardboxes and title view__________________________________________________________________
    if user_menu == 'Overall Analysis':

        st.markdown("""
        <div style="
            padding: 15px 20px;
            border-radius: 15px;
            background: linear-gradient(90deg, rgba(255,255,255,0.10), rgba(255,255,255,0.03));
            border: 1px solid rgba(255,255,255,0.15);
            text-align: center;
            margin-bottom: 25px;
        ">
            <h1 style="
                font-size: 45px;
                margin: 0;
                font-weight: 700;
            ">
                🏅 Overall Olympic Analysis
            </h1>
            <p style="
                font-size: 24px;
                margin: 8px 0 0 0;
                opacity: 0.7;
            ">
                A Journey Through the Olympic Games • 1896 – 2016
            </p>
        </div>
        """, unsafe_allow_html=True)
        Editions = int(df['Year'].drop_duplicates().count())
        Cities = int(df['City'].drop_duplicates().count())
        Sports = int(df['Sport'].drop_duplicates().count())
        Events = int(df['Event'].drop_duplicates().count())
        Athletes = '110K+'
        # Nations = int(df['region'].drop_duplicates().shape[0]) ###206
        Nations='200+'
#____________________________CSS for cards_____________________________________________________________________
        st.markdown("""
        <style>
        .card {
            padding: 20px;
            border-radius: 15px;
            border: 1px solid rgba(50,50,50,0.4);
            background-color: rgba(1,1,1,.8);
            text-align: center;
            margin-bottom: 20px;
        }

        .card-title {
            font-size: 22px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .card-value {
            font-size: 38px;
            font-weight: 700;
        }
        </style>
        """, unsafe_allow_html=True)

        # First row
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Editions</div>
                <div class="card-value">{Editions}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Hosts</div>
                <div class="card-value">{Cities}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Sports</div>
                <div class="card-value">{Sports}</div>
            </div>
            """, unsafe_allow_html=True)

        # Second row
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Events</div>
                <div class="card-value">{Events}</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Nations</div>
                <div class="card-value">{Nations}</div>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="card">
                <div class="card-title">Athletes</div>
                <div class="card-value">{Athletes}</div>
            </div>
            """, unsafe_allow_html=True)

                   ### make it into dataframe
 #_________________ Backend of Overall analysis______________________________________________________________________________

    nations_over_time=helper.data_over_time(df)
    fig = px.line(nations_over_time, x='Year', y='No. of countries participated')
    fig.update_xaxes(dtick=8)
    fig.update_yaxes(dtick=25)
    st.title('No.of Nations Participating Over the Years')
    st.plotly_chart(fig)


    events_over_time=helper.events_over_time(df)
    fig = px.line(events_over_time, x='Year', y='No. of events')
    fig.update_xaxes(dtick=8)
    fig.update_yaxes(dtick=25)
    st.title('No. of Events Over the years')
    st.plotly_chart(fig)


    athletes_over_time=helper.athletes_over_time(df)
    fig=px.line(athletes_over_time, x='Year', y='No. of Athletes')
    fig.update_xaxes(dtick=8)
    fig.update_yaxes(dtick=1000)
    st.title('No.of Athletes Over the Years')
    st.plotly_chart(fig)


    st.title('No.of Events Over time FOR Every Sports')
    fig,ax=plt.subplots(figsize=(40,35))
    ax=sns.heatmap(
        df[['Year', 'Sport', 'Event']].drop_duplicates().pivot_table(index='Sport', columns='Year', values='Event',
                                                                     aggfunc='count').fillna(0).astype('int'),
        annot=True)
    st.pyplot(fig)

    st.title('Most Successful Athletes')
    sport_list=np.unique(df['Sport'].values).tolist() # this will sor
   #df['Sport'].values.tolist().sort() will not work
    sport_list.sort()
    sport_list.insert(0,'Overall')

    selected_sport=st.selectbox('Select Sport',sport_list)
    X=helper.most_successful(df,selected_sport)
    st.dataframe(X)

   #Most Successful countries in a sport
    if selected_sport == 'Overall' :
          st.title('Most Successful countries in a sport')  # fetched
    if selected_sport!= 'Overall':
        st.header('Most Successful Countries in '+selected_sport)
    Y = helper.most_successful_country(df, selected_sport)
    st.dataframe(Y)

    # if st.empty:
    #         st.info('Select a sport')

#_________________________________________________ Country_wise_Analysis____________________________________________________________________
if user_menu== 'Country-wise Analysis' :
    col1, col2 = st.columns([1, 5])

    with col1:
        st.image("image.png", width=200)

    with col2:
        st.title("Country wise Analysis")

        st.info(' select country⮟⮟')

        st.sidebar.subheader('Country-wise Analysis')
        st.sidebar.info('Select country⟶')
        st.sidebar.info('Select Sport⟶')

        country_list=np.unique(df['region'].dropna().values).tolist()
        country_list.sort()
        # selected_country=st.sidebar.selectbox('Select  a  Country',country_list)
        selected_country = st.selectbox('Select  a  Country', country_list)

        country_df=helper.yearwise_medal_tally(df,selected_country)
        fig = px.line(country_df, x='Year', y='No. of Medals')
        fig.update_xaxes(dtick=8)
        fig.update_yaxes(dtick=25)
        st.title('Medal tally for '+ selected_country +' over the years')
        st.plotly_chart(fig)


        st.header('Medals in a Sport in OLympics for '+selected_country)
        pt=helper.country_event_heatmap(df,selected_country)
        fig,ax=plt.subplots(figsize=(40,35))
        ax=sns.heatmap(pt, annot=True)
        st.pyplot(fig)


        st.title('Most Successful Athletes of '+selected_country)
        top_10_df=helper.most_successful_countrywise(df,selected_country)
        st.dataframe(top_10_df)

        #Most successful sports of a country / craze of sport in a country
        craze_df= helper.craze_of_sport(df, selected_country)
        st.header('🏅 Sports-wise Medal Tally for '+selected_country +' in Olympics')
        st.table(craze_df)

        st.title('')
        st.info('Select a country⮝⮝')
        st.title('Highest Medal holder for a country in a selected sport')
        # st.info('Select a country⮝⮝')
        st.info('select a sport ⮟⮟')
        sport_list = np.unique(df['Sport'].dropna().values).tolist()
        sport_list.sort()
        sport_list.insert(0,'select any sport')
        selected_sport= st.selectbox('Select Sport', sport_list)
        st.subheader('Top-10 of '+selected_sport+' in '+selected_country)
        top10_country_df = helper.top10_country_sport(df, selected_country,selected_sport)
        st.table(top10_country_df)
        # if st.empty:
        #     st.info('select a sport ⮝⮝')

        #Men_vs _women medal tally for usa over the years
        st.title('')
        st.title('Men vs Women Medals for '+selected_country +' in Olympics')
        men_v_df=helper. men_medal_women(df,selected_country)
        fig = px.line(men_v_df, x='Year', y=['F', 'M', 'total'])
        fig.update_layout(title='Men vs Women Medals for '+selected_country,
                          xaxis_title='Year',
                          yaxis_title='Number of medals')
        # fig.add_box(x=Z['Year'],y=Z['Total'])
        fig.update_xaxes(dtick=8)
        fig.update_yaxes(dtick=100)
        st.plotly_chart(fig)
#_________________________________________________________Athlete_wise_Analysis__________________________________________________
#Now Athlete Wise Analysis
if user_menu == 'Athlete wise Analysis':
#_______________________________________ title_view_________________________________________________________________
    # if user_menu == 'Athlete wise Analysis':
    #     st.markdown("""
    #     <div style="
    #         padding: 15px 20px;
    #         border-radius: 15px;
    #         background: linear-gradient(90deg, rgba(255,255,255,0.10), rgba(255,255,255,0.03));
    #         border: 1px solid rgba(255,255,255,0.15);
    #         text-align: center;
    #         margin-bottom: 25px;
    #     ">
    #         <h1 style="
    #             font-size: 38px;
    #             margin: 1;
    #             font-weight: 700;
    #         ">
    #             🏅 Athlete wise Analysis
    #         </h1>
    #         <p style="
    #             font-size: 20px;
    #             margin: 8px 0 0 0;
    #             opacity: 0.7;
    #         ">
    #             A Journey Through the Olympic Games • 1896 – 2016
    #         </p>
    #     </div>
    #     """, unsafe_allow_html=True)

    import streamlit as st
    import streamlit.components.v1 as components

    athlete_card_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    body {
        background: transparent;
    }
    .timeline-card {
        background: linear-gradient(145deg, #111827 0%, #1f2937 100%);
        border-radius: 16px;
        padding: 24px 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
    }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(253, 224, 71, 0.12);
        border: 1px solid rgba(253, 224, 71, 0.35);
        padding: 4px 12px;
        border-radius: 9999px;
        color: #fde047;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .badge-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #fde047;
    }
    .title {
        font-size: 32px;
        font-weight: 800;
        color: #f8fafc;
        margin: 10px 0 4px 0;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .subtitle {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 16px;
    }
    .timeline-track-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin: 14px 0 16px 0;
    }
    .timeline-endpoint {
        font-size: 12px;
        font-weight: 700;
        color: #fde047;
        background: rgba(253, 224, 71, 0.1);
        border: 1px solid rgba(253, 224, 71, 0.3);
        padding: 2px 8px;
        border-radius: 5px;
    }
    .timeline-track {
        position: relative;
        flex-grow: 1;
        max-width: 460px;
        height: 4px;
        background: rgba(255, 255, 255, 0.12);
        border-radius: 2px;
    }
    .timeline-line {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, #f59e0b, #fde047);
        border-radius: 2px;
    }
    .timeline-dot {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 12px;
        height: 12px;
        background: #fde047;
        border: 2px solid #111827;
        border-radius: 50%;
        box-shadow: 0 0 8px rgba(253, 224, 71, 0.8);
    }
    .info-guide {
        background: rgba(15, 23, 42, 0.7);
        border-left: 4px solid #fde047;
        border-radius: 6px;
        padding: 10px 14px;
        font-size: 13px;
        color: #cbd5e1;
        line-height: 1.4;
    }
    .info-guide strong {
        color: #fde047;
    }
    </style>
    </head>
    <body>
    <div class="timeline-card">
        <div class="badge">
            <span class="badge-dot"></span>
            OLYMPIC GAMES
        </div>
        <div class="title">
            <span></span> Athlete-wise Analysis
        </div>
        <div class="subtitle">A Journey Through the Olympic Games • 1896 – 2016</div>
        <div class="timeline-track-wrap">
            <span class="timeline-endpoint">1896</span>
            <div class="timeline-track">
                <div class="timeline-line"></div>
                <div class="timeline-dot"></div>
            </div>
            <span class="timeline-endpoint">2016</span>
        </div>
        <div class="info-guide">
            💡 <strong>Pro Tip:</strong> Search for any athlete to uncover individual medal counts, age-distribution profiles,Weight vs Height Distribution  relative to medals .
        </div>
    </div>
    </body>
    </html>
    """

    components.html(athlete_card_html, height=240)

    # st.title('Athlete-wise Analysis')
    st.title('Individual Medal Counts & Analysis:')
    df['Total'] = df['Gold'] + df['Silver'] + df['Bronze']
    idx = df[df['Total'] != 0].index
    df = df.loc[idx]
    name1 = np.unique(df['Name']).tolist()
    name1.sort()
    name1.insert(0, 'Select Name of Athlete')

    # event_wise_medal for a athlete analysis
    select_name = st.selectbox('Select Athlete Name', name1)
    name_df = helper.name_event_wise(df, select_name)

    name1_df = helper.name_year_wise(df, select_name)
    name2_df = helper.overall_name_wise(df, select_name)

    st.subheader('Event wise Analysis')
    st.table(name_df)
    if name_df.empty:
        st.info("Select Athlete Name")

    st.subheader('Year wise Analysis')
    st.table(name1_df)
    if name1_df.empty:
        st.info("Select Athlete Name")

    st.subheader(select_name + ' in Olympics')
    st.table(name2_df)
    if name2_df.empty:
        st.info("Select Athlete Name")

    # year,event_name and got results
    st.title('')
    st.title('Event-wise result in Olympics')
    st.text("ex: Athletics Men's 100 m results in 2012 Olympics ")
    year1 = np.unique(df['Year']).tolist()
    year1.sort()
    year1.insert(0, 'Select year')
    event1 = np.unique(df['Event']).tolist()
    event1.sort()
    event1.insert(0, 'select name of the event')

    select_year = st.selectbox('Select year', year1)
    if select_year == 'Select year':
        st.info('Select Year')

    select_event = st.selectbox('Select Event', event1)

    choose_df = helper.choose(df, select_year, select_event)

    st.subheader(select_event + ' results in ' + str(select_year) + ' Olympics')
    st.table(choose_df)
    if choose_df.empty:
        st.info("This event was not held in the selected Olympic season.")

    ####Append used here ,Medal comparison with age
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()
    fig = ff.create_distplot([x1, x2, x3, x4],
                             ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'], show_hist=False,
                             show_rug=False)
    fig.update_layout(title='Ex. obs. 𝘐𝘯 𝘢𝘨𝘦 20-25,𝘤𝘩𝘢𝘯𝘤𝘦 𝘵𝘰 𝘨𝘦𝘵 𝘢 𝘨𝘰𝘭𝘥 𝘪𝘴 𝘮𝘢𝘹𝘪𝘮𝘶𝘮 𝘵𝘩𝘦𝘯 𝘰𝘵𝘩𝘦𝘳𝘴',autosize=False, width=1000, height=550)
    fig.update_xaxes(dtick=5)
    fig.update_layout(xaxis_title='Age', yaxis_title='Density')
    # fig.update_xaxes(dtick=10)
    st.title('Distribution of Age for medals ')
    st.text('                  Plot shows distribution of Age for medals')

    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']

    for sport in famous_sports:
        temp_df = athlete_df[(athlete_df['Sport'] == sport)]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)
    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=550)
    fig.update_layout(xaxis_title='Age', yaxis_title='Density')
    fig.update_xaxes(dtick=5)
    st.title('Distribution of Age For Gold Medals(Every Sport)')
    st.plotly_chart(fig)

# drawing height_V_weight graph for a medal and for a sex for a sport
    sport_list = np.unique(athlete_df['Sport']).tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('')
    st.title('Weight vs Height')
    st.info('Select a sport⮟⮟')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    # st.info('Select a sport⮝⮝')
    temp_df = helper.weight_v_height(df, selected_sport)
    fig, ax = plt.subplots(figsize=(12, 12))
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=35,
                         alpha=1)
    # fig.update_xaxes(dtick=10) for plotly not matplotlib
    st.title(selected_sport)
    st.pyplot(fig)

#wrrr______________
# men vs women participation
    st.title('Men vs Women participation Over years')
    final = helper.men_vs_women(df)
    fig = px.line(final, x='Year', y=['M', 'F','total'],
                  width=1000, height=700)
    fig.update_layout(xaxis_title='Year', yaxis_title='No.of Athletes participated',title='Men vs women participation')
    st.plotly_chart(fig, use_container_width=True)


#comparison between two athletes
st.title('')
st.title('Compare two Athletes')
n1=np.unique(df['Name']).tolist()
n1.sort()
n2=np.unique(df['Name']).tolist()
n2.sort()
select_name1=st.selectbox('Select First Athlete',n1)
select_name2=st.selectbox('Select Second Athlete',n2)
compare_df=helper.compare(df, select_name1, select_name2)
st.table(compare_df)






#____________________________________________________-Year_wise_analysis_________________________________________________________________-
if user_menu=='Year-wise Analysis':
    ## frontend
#_________________ title_view__________________________________________________________________________

    import streamlit.components.v1 as components

    card_html = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    body {
        background: transparent;
    }
    .timeline-card {
        background: linear-gradient(145deg, #111827 0%, #1f2937 100%);
        border-radius: 16px;
        padding: 24px 28px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
    }
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(253, 224, 71, 0.12);
        border: 1px solid rgba(253, 224, 71, 0.35);
        padding: 4px 12px;
        border-radius: 9999px;
        color: #fde047;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .badge-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: #fde047;
    }
    .title {
        font-size: 32px;
        font-weight: 800;
        color: #f8fafc;
        margin: 10px 0 4px 0;
        letter-spacing: -0.5px;
    }
    .subtitle {
        font-size: 14px;
        color: #94a3b8;
        margin-bottom: 16px;
    }
    .timeline-track-wrap {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 12px;
        margin: 14px 0 16px 0;
    }
    .timeline-endpoint {
        font-size: 12px;
        font-weight: 700;
        color: #fde047;
        background: rgba(253, 224, 71, 0.1);
        border: 1px solid rgba(253, 224, 71, 0.3);
        padding: 2px 8px;
        border-radius: 5px;
    }
    .timeline-track {
        position: relative;
        flex-grow: 1;
        max-width: 460px;
        height: 4px;
        background: rgba(255, 255, 255, 0.12);
        border-radius: 2px;
    }
    .timeline-line {
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(90deg, #f87171, #fb7185);
        border-radius: 2px;
    }
    .timeline-dot {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 12px;
        height: 12px;
        background: #fb7185;
        border: 2px solid #111827;
        border-radius: 50%;
        box-shadow: 0 0 8px rgba(251, 113, 133, 0.8);
    }
    .info-guide {
        background: rgba(15, 23, 42, 0.7);
        border-left: 4px solid #fde047;
        border-radius: 6px;
        padding: 10px 14px;
        font-size: 13px;
        color: #cbd5e1;
        line-height: 1.4;
    }
    .info-guide strong {
        color: #fde047;
    }
    </style>
    </head>
    <body>
    <div class="timeline-card">
        <div class="badge">
            <span class="badge-dot"></span>
                Olympic Games
        </div>
        <div class="title">Year-wise Analysis</div>
        <div class="subtitle">Year-wise participation trajectory, Gender-wise performance distribution, Sport wise distribution</div>
        <div class="timeline-track-wrap">
            <span class="timeline-endpoint">1896</span>
            <div class="timeline-track">
                <div class="timeline-line"></div>
                <div class="timeline-dot"></div>
            </div>
            <span class="timeline-endpoint">2016</span>
        </div>
        <div class="info-guide">
            💡 <strong>Pro Tip:</strong> Select <strong>Year</strong> and <strong>Category</strong> to view top athletes for that edition. Add a <strong>Sport</strong> filter to drill down into discipline-specific podium dominators.
        </div>
    </div>
    </body>
    </html>
    """
    components.html(card_html, height=240)
#________________________________--code______________________________________________________________________________________________
    st.sidebar.header('Year-wise Analysis')# when we will open Year-wise analysis , this will we the heading of it in the sidebar
    st.sidebar.info('Select a year ⟶')
    st.sidebar.info('Select category⟶')
    st.sidebar.info('select sport ⟶')
    # st.title('T-10 Athletes of '+str(select_year))
    year = np.unique(df['Year']).tolist()
    year.sort()
    year.insert(0, 'Select year')
    sex=np.unique(df['Sex']).tolist()
    sex.insert(0,'Overall')
    select_year = st.selectbox('Select year', year)
    select_sex =st.selectbox('Select category',sex)
    #st.title('T-10 Athletes of ' + str(select_year))

    if select_year=='Select year':
         st.header('T-10 Athletes  ')
    else:
          st.header('T-10 Athletes of ' + str(select_year)+' Olympics'+' '+select_sex)
    top10_df = helper.top10_year(df, select_year,select_sex)

    #st.subheader(select_event + ' results in ' + str(select_year) + ' Olympics')
    st.table(top10_df)
    if select_year == 'Select year':
        st.info('Select Year ↑')


    ##top 10 athlete in a sport in a given year
    sport = np.unique(df['Sport']).tolist()
    sport.insert(1,'Overall Analysis')
    sport.insert(0,'Select any sport')
    select_sport = st.selectbox('Select  Sport',sport)
    top10_sport_df = helper.top10_year_sport(df, select_year,select_sport,select_sex)
    if select_sport == 'Select any sport':
        st.header('T-10 Athletes in a sport ')
    else:
        st.header('Top 10 Athletes in '+select_sport+' '+str(select_year)+' '+select_sex)
    st.table(top10_sport_df)
    if select_sport== 'Select any sport':
        st.info('select year ↑')

    st.title('')
    st.title('No.of athletes participated over the years for a country')
    country=np.unique(df['region'].dropna()).tolist()
    country.sort()
    # country.insert(0,'Overall Analysis')
    st.header('select a country')
    select_country = st.selectbox('Select country',country)
    parti_df=helper.parti(df,select_country)
    fig = px.line(parti_df, x='Year', y=['F', 'M', 'Total'])
    fig.update_layout(title='Number of '+select_country+' Athletes Participated Over Years',
                      xaxis_title='Year',
                      yaxis_title='Number of Athletes')
    fig.update_xaxes(dtick=8)
    fig.update_yaxes(dtick=100)
    st.plotly_chart(fig)

    ## Compare any two athletes

#___________________________________________________________Good Luck___________________________________________________________________________















