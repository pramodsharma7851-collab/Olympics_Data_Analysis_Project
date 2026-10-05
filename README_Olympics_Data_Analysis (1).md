# 🏅 Olympics Data Analysis

An interactive **Olympics Data Analysis dashboard** built with **Python, Pandas, and Streamlit** to explore Olympic history, medal records, countries, athletes, sports, and events from **1896 to 2016**.

The project transforms raw Olympic data into an interactive WebApp where users can explore overall Olympic trends, medal tallies, country-wise performance, athlete-level records, and year-wise analysis.

## 📌 Project Overview

The Olympic Games generate a large amount of historical data across countries, athletes, sports, events, and medals. This project provides an interactive analytical platform called **"Find Olympic Record"** to make that information easier to explore.

### Main Analysis Sections

- 🏆 **Medal Tally**
- 📊 **Overall Olympic Analysis**
- 🌍 **Country-wise Analysis**
- 🧑 **Athlete-wise Analysis**
- 📅 **Year-wise Analysis**

The dashboard covers Olympic data from **1896 to 2016**.

## 🎯 Project Objectives

- Analyse historical Olympic data from 1896–2016.
- Understand medal distribution across countries and Olympic editions.
- Analyse the performance of individual countries.
- Explore athlete-level Olympic records.
- Examine trends across different sports and events.
- Build an interactive dashboard for data exploration.
- Present complex Olympic data through meaningful visualizations.

## 📊 Dataset

The project uses two primary datasets:

### `athlete_events.csv`

The main athlete-event dataset containing information related to:

- Athletes
- Countries / NOCs
- Sports
- Events
- Olympic Games
- Year
- Season
- Medal information
- Athlete attributes

### `noc_regions.csv`

This dataset maps **NOC (National Olympic Committee) codes** to corresponding country/region names and is used to make country-wise analysis more readable.

## 🔍 Key Features

### 🏆 1. Medal Tally

Explore medal performance across countries, including:

- Gold medals
- Silver medals
- Bronze medals
- Total medals
- Country-level medal performance

### 📊 2. Overall Olympic Analysis

Explore the broader history of the Olympic Games through:

- Olympic editions
- Participating nations
- Athletes
- Sports
- Events
- Medal records
- Historical trends

### 🌍 3. Country-wise Analysis

Select a country and explore its historical Olympic record, including:

- Medal performance
- Participation over the years
- Sports participation
- Athlete participation
- Olympic performance trends

### 🧑 4. Athlete-wise Analysis

Explore individual Olympic records, including:

- Athlete participation
- Sports and events
- Olympic appearances
- Medal records
- Athlete-level performance

### 📅 5. Year-wise Analysis

Analyse different Olympic editions to understand:

- Changes in participation
- Medal distribution
- Growth of sports and events
- Historical Olympic trends

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data manipulation and analysis |
| **NumPy** | Numerical operations |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical visualization |
| **Streamlit** | Interactive web dashboard |
| **Jupyter Notebook / PyCharm** | Development environment |

## 🏗️ Project Architecture

```text
              Olympic Dataset
                    │
                    ▼
        ┌──────────────────────┐
        │   Data Preprocessing │
        └──────────────────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │ Data Transformation  │
        │ & Preparation        │
        └──────────────────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │      Helper Logic    │
        └──────────────────────┘
                    │
                    ▼
        ┌──────────────────────┐
        │  Streamlit Dashboard │
        └──────────────────────┘
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
  Medal Tally   Overall      Country/Athlete
                Analysis       Analysis
```

## 📂 Project Structure

```text
Olympics_Data_Analysis_Project/
│
├── app.py
├── helper.py
├── preprocessor.py
│
├── athlete_events.csv
├── noc_regions.csv
│
├── requirements.txt
│
└── assets/
    └── images / dashboard assets
```

### File Description

- **`app.py`** — Main Streamlit application and dashboard navigation.
- **`helper.py`** — Supporting functions used for analysis and dashboard calculations.
- **`preprocessor.py`** — Data preparation and preprocessing.
- **`athlete_events.csv`** — Main Olympic athlete-event dataset.
- **`noc_regions.csv`** — NOC-to-country/region mapping.
- **`requirements.txt`** — Required Python dependencies.
- **`assets/`** — Visual assets used by the dashboard.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pramodsharma7851-collab/Olympics_Data_Analysis_Project.git
```

### 2. Navigate to the Project Directory

```bash
cd Olympics_Data_Analysis_Project
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The dashboard will open in your browser.

## 📈 Example Questions You Can Explore

- Which country has won the most medals?
- How has a country's Olympic performance changed over time?
- Which athletes have won the most medals?
- Which sports have the highest participation?
- How has the number of participating athletes changed over the years?
- Which countries have performed strongly in particular sports?
- How has Olympic participation evolved from 1896 to 2016?

## 💡 Key Insights

The dashboard enables users to identify historical patterns such as:

- Differences in medal performance between countries.
- Changes in participation across Olympic editions.
- Growth and evolution of sports and events.
- Performance patterns of individual athletes.
- Historical changes in Olympic participation and medal distribution.

Because the dashboard is interactive, users can explore these patterns dynamically rather than relying only on static charts.

## 📚 Skills Demonstrated

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Data Aggregation
- Data Transformation
- Statistical Analysis
- Data Visualization
- Python Programming
- Pandas
- Streamlit Dashboard Development
- Interactive Data Analytics
- Working with Multiple CSV Datasets

## 🔮 Future Improvements

- Add more advanced interactive visualizations.
- Add additional Olympic performance metrics.
- Improve dashboard responsiveness.
- Add more athlete-level comparisons.
- Add advanced filtering and comparison features.
- Extend the analysis to newer Olympic editions when compatible datasets are available.
- Add more detailed statistical analysis.

## 👨‍💻 Author

**Pramod Sharma**

GitHub:  
https://github.com/pramodsharma7851-collab

## ⭐ Project Repository

https://github.com/pramodsharma7851-collab/Olympics_Data_Analysis_Project

## ⭐ WebApp Live Link :
https://find-olympics-analysis-and-records120.streamlit.app/


## 📄 License

This project is intended for educational and portfolio purposes.

