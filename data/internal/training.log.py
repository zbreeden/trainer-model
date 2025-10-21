import pandas as pd

# This file contains the current status of the user's training progress.

skill_track_name = ['Excel','Python','SQL','Power BI','Tableau','CSharp','Websites','Data Analyst','AWS','Snowflake','R','Business Analysis','Business Intelligence'] # name of each skill tract
skill_track_code = ['SK-EXCEL','SK-PYTHON','SK-SQL','SK-POWERBI','SK-TABLEAU','SK-CSHARP','SK-WEBSITES','SK-DA','SK-AWS','SK-SNOWFLAKE','SK-R','SK-BA','SK-BI'] # unique identifier for each skill tract
skill_is_completed = [False, False, False, False, False, False, False, False, False, False, False, False, False]
skill_track_last_update_date = ['2025-10-15','2025-10-15','2025-10-12','2025-10-11','','2025-10-10','2025-10-15','2025-10-12','2025-10-09','2025-10-09','','2025-10-11','2025-10-13'] # last date the skill tract was updated

##### 

training_id_name = ['Excel Fundamentals','Python Data Fundamentals','SQL Fundamentals','Power BI Fundamentals','Python, SQL, Tableau for Data Science','Microsoft Power BI Data Analyst','IBM Business Intelligence (BI) Analyst','Certified Business Analysis Professional','IBM Data Analyst','Coding for Data','Introduction to C#','Introduction to JavaScript','Introduction to SQL','Introduction to HTML','Introduction to CSS','The Little Book of Data by Justin Evans','Getting Started with Data Analytics on AWS','Snowflake Onboarding','R Programming Fundamentals','The Art of Statistics by David Spiegelhalter','The Data Detective by Tim Harford','Naked Statistics by Charles Wheelen'] # name of each training
training_id = ['datacamp_excel','datacamp_python','datacamp_sql','datacamp_powerbi','coursera_pysqltab','microsoft_powerbi','ibm_bi','coursera_cbap','ibm_da','sololearn_coding','sololearn_csharp','sololearn_js','sololearn_sql','sololearn_html','sololearn_css','the_little_book_of_data','coursera_aws','snowflake','datacamp_r','the_art_of_statistics','the_data_detective','naked_statistics'] # unique identifier for each training
training_is_completed = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False] # whether each training has been completed

#####

step_id_name = ['Introduction to Excel','Data Preparation in Excel','Part 1: How We Got Here','Part 2: Good and Bad Data People','Part 3: Superpowers','Part 4: How We Use Data','What is Data Analytics','Why Data Analytics on the Cloud','What Else Can I Do With Data Analytics on AWS','Introduction to Data Analytics','Excel Basics for Data Analysis','Data Visualization and Dashboards with Excel and Cognos','Python for Data Science, AI & Development','Python Project for Data Science','Databases and SQL for Data Science with Python','Data Analysis with Python','Data Visualization with Python','IBM Data Analyst Capstone Project','Generative AI: Enhance your Data Analytics Career','Data Analyst Career Guide and Interview Preparation','Getting Started','Operators & Strings','Decision Making','Loops','Methods','Getting Started with CSS','Styling Elements','Track 1','Track 2','Introduction: How to Lie with Statistics','Business Analysis: Key Definitions & Strategy Analysis','Advanced Business Analysis: Elicitation & Analysis','Introduction to Power BI','Introduction to DAX in Power BI','Data Visualization in Power BI','Part 1 - Track 1','Part 1 - Track 2','Part 1 - Track 3','Part 1 - Track 4','Business Intelligence Essentials','Getting Started With HTML','Going Deeper with HTML','Getting Started with SQL','Going Deeper with SQL','Preparing Data for Analysis with Microsoft Excel','Introduction to Python','Intermediate Python'] # name of each step
step_id = ['DC-EXCEL-101','DC-EXCEL-201','LBOD-1','LBOD-2','LBOD-3','LBOD-4','C-AWS-1','C-AWS-2','C-AWS-3','IBM-DA-1','IBM-DA-2','IBM-DA-3','IBM-DA-4','IBM-DA-5','IBM-DA-6','IBM-DA-7','IBM-DA-8','IBM-DA-CS','IBM-DA-X1','IBM-DA-X2','SL-CSHARP=1','SL-CSHARP-2','SL-CSHARP-3','SL-CSHARP-4','SL-CSHARP-5','SL-CSS-1','SL-CSS-2','TAOS-1','TAOS-2','TDD-1','C-CBAP-1','C-CBAP-2','DC-PBI-1','DC-PBI-2','DC-PBI-3','NS-1','NS-2','NS-3','NS-4','IBM-BI-1','SL-HTML-1','SL-HTML-2','SL-SQL-1','SL-SQL-2','MICRO-PBI-1','DC-PY-1','DC-PY-2'] # unique identifier for each step
step_status = ['completed', 'cooled', 'completed', 'completed', 'completed', 'cooled', 'completed', 'completed', 'completed', 'completed', 'simmer', 'cooled', 'cooled', 'cooled', 'cooled', 'cooled', 'cooled', 'cooled', 'cooled', 'cooled', 'completed', 'cooled', 'cooled', 'cooled', 'cooled', 'completed', 'completed', 'completed', 'completed','completed','completed','completed','completed','completed','completed','completed','completed','completed','cooled','completed','completed','completed','completed','cooled','completed','cooled','cooled'] # current status of each step (e.g. cooled, fire, bloom, mundane, etc.)
step_last_update_date = ['2025-10-08', '2025-10-14', '2025-10-09', '2025-10-09', '2025-10-10', '2015-10-09', '2025-10-09', '2025-09-18', '2025-10-10', '2025-10-02', '2025-10-10','2025-09-28', '2025-10-13', '2025-10-11', '2025-10-11', '2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-11','2025-10-10','2025-09-18','2025-10-11','2025-09-21','2025-10-01','','2025-10-12','2025-10-12','2025-10-12','2025-10-05','2025-10-12','2025-10-12','2025-10-03','2025-10-01','2025-10-15','2025-10-01','2025-10-05','2025-10-15','2025-10-01','2025-10-15'] # last date the step was updated
step_is_completed = [True, False, True, True, True, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, True, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, True, False, True, True] # whether each step has been completed

#####

chapter_id_name = ['Getting Started with Excel','Managing Data and Applying Aggregate Functions','Other Functions and Visualizing Data','Starting Data Preparation in Excel','Functions for Data Preparation','Conditional Formulas','Data is Everywhere: Here is my Number','Life After The Data Revolution: The Library','Data Science: Data During Wartime','Artificial Intelligence: A Sport For Cyborgs','Data Bullies: A Story Where Bankers Are The Heroes (No Really)','Data People and Why I Love Them: The Day Priya Saw The Line','Omniscience: Solving One Big Problem: Skate The Lake','Omniscience: Solving Many Small Problems: But it is a Map!','Data Directs Resources to Where They Are Needed: A True Spartan','Data is Light in a Dark Room: Tiny Submarines','Data Crystallizes Complex Information: The Railroad Nerd','Welcome to Getting Started with Data Analytics on AWS','What is Data Analytics?','Most Common Data Analysis Nowadays','How is Data Analytics Present in Your Life?','Data Collection and Storage in the AWS Cloud','Popular AWS Services Used for Analytics Solutions','High-Level Content Summary: AWS Services for Data Analytics','Demo - Hello Data Analytics World','Amazon S3/AWS CloudTrail/Amazon Athena/AWS Datasets/Amazon QuickSight/Others','What Else can you do with Data Analytics?','Course Wrap-Up','Final Assessment','Modern Data Ecosystem and the Role of Data Analytics','The Data Analyst Role','Introduction to Data Analysis Using Spreadsheets','Getting Started with Using Excel Spreadsheets','Cleaning & Wrangling Data Using Spreadsheets','Analyzing Data Using Spreadsheets','Final Project','Your first C# Program','Multiple Statements','Program Structure','Basic Concepts','Variables','Data Types','Doing Math','Arithmetic Operators','Assignment Operators','User Input','More on Strings','Concatenation & Interpolation','Welcome to CSS','Styling Techniques','The Anatomy of CSS','Style Inheritance','ID and Class Selectors','Standards and Best Practices','Profile Page Project Step 1','Introduction to Color','Dimensions','Styling Text','Font Styles','Profile Page Project Step 2','Styling Links','Styling Tables','Styling Lists','Profile Page Project Step 3','Styling Forms','Introduction','Key Definitions','Strategy Analysis','Final Assessment','Elicitation & Collaboration','Requirements Analysis & Design Definition','Getting Started with Power BI','Transforming Data','Visualizing Data','Filtering','Getting Started With DAX','Context in DAX Formulas','Working with Dates','The Audience is King','Getting an Emotional Response','Reducing Cognitive Load','Less is More','Introduction to Business Intelligence','The Data Ecosystem','BI Analytics Landscape','Gathering and Wrangling Data','The Core Web Technology','HTML Code','Headings','Images','Landing Page Project','Comments','Standards & Best Practices','Text Formatting','Links','Lists','Landing Page Project','Working with Data','Running SQL Queries','Relational Databases','Debugging','Standards & Best Practices','Sorting Data','Limiting Data''Data Types','Filtering Data','Excel Fundamentals','Formulas & Functions','Preparing data for analysis using functions','Python Basics','Python Lists','Functions & Packages','Numpy','Matplotlib','Dictionaries & Pandas'] # name of each chapter
chapter_id_code = ['DC-EXCEL-101-1','DC-EXCEL-101-2','DC-EXCEL-101-3','DC-EXCEL-201-1','DC-EXCEL-201-2','DC-EXCEL-201-3','LBOD-1-1','LBOD-1-2','LBOD-1-3','LBOD-1-4','LBOD-2-1','LBOD-2-2','LBOD-3-1','LBOD-3-2','LBOD-3-3','LBOD-3-4','LBOD-3-5','C-AWS-1-1','C-AWS-1-2','C-AWS-1-3','C-AWS-1-4','C-AWS-2-1','C-AWS-2-2','C-AWS-2-3','C-AWS-2-4','C-AWS-2-5','C-AWS-3-1','C-AWS-3-2','C-AWS-3-3','IBM-DA-1-1','IBM-DA-1-2','IBM-DA-2-1','IBM-DA-2-2','IBM-DA-2-3','IBM-DA-2-4','IBM-DA-2-5','SL-CSHARP-1-1','SL-CSHARP-1-2','SL-CSHARP-1-3','SL-CSHARP-1-4','C-CSHARP-1-5','C-CSHARP-1-6','SL-CSHARP-1-7','SL-CSHARP-2-1','SL-CSHARP-2-2','SL-CSHARP-2-3','SL-CSHARP-2-4','SL-CSHARP-2-5','SL-CSS-1-1','SL-CSS-1-2','SL-CSS-1-3','SL-CSS-1-4','SL-CSS-1-5','SL-CSS-1-6','SL-CSS-1-7','SL-CSS-2-1','SL-CSS-2-2','SL-CSS-2-3','SL-CSS-2-4','SL-CSS-2-5','SL-CSS-2-6','SL-CSS-2-7','SL-CSS-2-8','SL-CSS-2-9','SL-CSS-2-10','C-CBAP-1-1','C-CBAP-1-2','C-CBAP-1-3','C-CBAP-1-4','C-CBAP-2-1','C-CBAP-2-2','DC-PBI-1-1','DC-PBI-1-2','DC-PBI-1-3','DC-PBI-1-4','DC-PBI-2-1','DC-PBI-2-2','DC-PBI-2-3','DC-PBI-3-1','DC-PBI-3-2','DC-PBI-3-3','DC-PBI-3-4','IBM-BI-1-1','IBM-BI-1-2','IBM-BI-1-3','IBM-BI-1-4','SL-HTML-1-1','SL-HTML-1-2','SL-HTML-1-3','SL-HTML-1-4','SL-HTML-1-5','SL-HTML-2-1','SL-HTML-2-2','SL-HTML-2-3','SL-HTML-2-4','SL-HTML-2-5','SL-HTML-2-6','SL-SQL-1-1','SL-SQL-1-2','SL-SQL-1-3','SL-SQL-1-4','SL-SQL-2-1','SL-SQL-2-2','SL-SQL-2-3','SL-SQL-2-4','MICRO-PBI-1-1','MICRO-PBI-1-2','MICRO-PBI-1-3','DC-PY-1-1','DC-PY-1-2','DC-PY-1-3','DC-PY-1-4','DC-PY-2-1','DC-PY-2-2'] # unique identifier for each chapter
chapter_last_update_date = ['2025-10-09','2025-10-09','2025-10-09','2025-10-09','2025-10-09','2025-10-09','2025-10-09','2025-10-09','2025-09-18','2025-09-18','2025-09-24','2025-09-25','2025-10-10','2025-09-22','2025-09-22','2025-09-22','2025-09-23','2025-09-23','2025-09-24','2025-09-25','2025-10-01','2025-10-01','2025-10-01','2025-10-02','2025-10-10','2025-09-28','2025-09-28','2025-09-28','2025=09-28','2025-09-29','2025-09-29','2025-09-29','2025-10-10','2025-10-11','2025-10-11','2025-10-13','2025-10-13','2025-10-13','2025-10-13','2025-10-13','2025-10-13','2025-10-13','2025-09-18','2025-09-18','2025-09-18','2025-09-18','2025-10-11','2025-09-21','2025-09-21','2025-09-21','2025-09-21','2025-10-01','2025-10-01','2025-10-01','2025-10-04','2025-10-11','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-12','2025-10-03','2025-10-03','2025-10-13','2025-10-13','2025-10-01','2025-10-01','2025-10-01','2025-10-01','2025-10-01','2025-10-14','2025-10-14','2025-10-15','2025-10-15','2025-10-15','2025-10-15','2025-10-01','2025-10-01','2025-10-01','2025-10-01','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-05','2025-10-02','2025-10-02','2025-10-15','2025-10-01','2025-10-01','2025-10-01','2025-10-01','2025-10-08'] # last date the chapter was updated
chapter_is_completed = [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True] # whether each chapter has been completed

skills_df = pd.DataFrame({
    'skill_track_name': skill_track_name,
    'skill_track_code': skill_track_code,
    'skill_is_completed': skill_is_completed,
    'skill_track_last_update_date': skill_track_last_update_date
})

training_df = pd.DataFrame({
    'training_id_name': training_id_name,
    'training_id': training_id,
    'training_is_completed': training_is_completed
})

steps_df = pd.DataFrame({
    'step_id_name': step_id_name,
    'step_id': step_id,
    'step_status': step_status,
    'step_last_update_date': step_last_update_date,
    'step_is_completed': step_is_completed
})

chapters_df = pd.DataFrame({
    'chapter_id_name': chapter_id_name,
    'chapter_id_code': chapter_id_code,
    'chapter_last_update_date': chapter_last_update_date,
    'chapter_is_completed': chapter_is_completed
})

# Export the developed DataFrames to CSV files in this script's directory (the model's data/internal chamber).
from pathlib import Path

# Determine the directory where this script lives (training-model/data/internal)
script_dir = Path(__file__).resolve().parent
export_dir = script_dir
export_dir.mkdir(parents=True, exist_ok=True)

# Define output file paths
skill_csv = export_dir / 'skills_df.csv'
training_csv = export_dir / 'training_df.csv'
step_csv = export_dir / 'steps_df.csv'
chapter_csv = export_dir / 'chapters_df.csv'


# Write DataFrames to CSV (no index column)
skills_df.to_csv(skill_csv, index=False)
training_df.to_csv(training_csv, index=False)
steps_df.to_csv(step_csv, index=False)
chapters_df.to_csv(chapter_csv, index=False)

print(f"Exported DataFrames to CSV in: {export_dir}")




