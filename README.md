# Netflix Data Analysis and Type Prediction

This project explores the Netflix titles dataset using **Pandas, NumPy, Matplotlib, and Seaborn** for data analysis and visualization, and uses **Scikit-learn** to build a machine learning model that predicts whether a title is a **Movie** or a **TV Show**.

## Project Overview

The project is divided into two main parts:

1. **Exploratory Data Analysis (EDA)**
   - Understanding the structure of the dataset
   - Checking missing values and duplicates
   - Exploring content distribution, release trends, and other patterns
   - Visualizing insights using Matplotlib and Seaborn

2. **Machine Learning**
   - Preprocessing selected features
   - Encoding categorical variables
   - Training a classification model using Scikit-learn
   - Predicting whether a Netflix title is a Movie or TV Show
   - Evaluating model performance using accuracy, classification report, and confusion matrix

## Dataset

The dataset used in this project is the **Netflix Titles Dataset**, which contains information about Netflix content such as:
- Title
- Type
- Director
- Cast
- Country
- Release year
- Rating
- Duration
- Genre
- Description

## Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**

## Workflow

### 1. Data Loading
The dataset is loaded using Pandas and inspected using:
- `head()`
- `info()`
- `describe()`
- `shape`

### 2. Data Cleaning
The project includes:
- Checking missing values
- Filling missing values in columns like `country`, `rating`, and `duration`
- Checking duplicates
- Preparing columns for analysis

### 3. Exploratory Data Analysis
EDA questions explored include:
- What is the distribution of Movies and TV Shows?
- Which years have the highest number of releases?
- What are the most common ratings?
- Which countries contribute the most content?
- What patterns can be observed in Netflix titles?

### 4. Feature Engineering
To prepare data for machine learning:
- Useful columns were selected
- The numeric part of the `duration` column was extracted
- Categorical columns were encoded using `LabelEncoder`

### 5. Machine Learning Model
A **Logistic Regression** model was used to predict the `type` column:
- `Movie`
- `TV Show`

#### Features used:
- `release_year`
- `rating`
- `duration_num`
- `country`

### 6. Model Evaluation
The model was evaluated using:
- Accuracy score
- Classification report
- Confusion matrix

## Project Structure

```bash
netflix-data/
│
├── netflix_titles.csv
├── netflixx.py
└── README.md
