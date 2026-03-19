# Netflix Data Analysis 🎬📊

This project performs **Exploratory Data Analysis (EDA)** on the Netflix dataset using Python.
The goal is to understand the dataset structure, handle missing values, and visualize content distribution.

---

## 📌 Project Overview

The Netflix dataset contains information about movies and TV shows available on Netflix, including:

* Title
* Type (Movie/TV Show)
* Cast
* Country
* Release Year
* Rating
* Duration

---

## 🛠 Technologies Used

* Python 🐍
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📂 Dataset

Dataset used: **Netflix Titles Dataset**

Make sure the dataset is placed correctly:

```bash
netflix/
└── netflix_titles.csv
```

---

## 🔎 Steps Performed

1. Loaded dataset using **Pandas**
2. Displayed dataset structure using `info()`
3. Viewed first few rows using `head()`
4. Generated statistical summary using `describe()`
5. Checked missing values
6. Checked duplicate records
7. Filled missing values with `0`
8. Checked dataset shape
9. Created visualization using Seaborn

---

## 📊 Visualization

### Distribution of Movies vs TV Shows

A count plot is used to show the number of:

* 🎬 Movies
* 📺 TV Shows

```python
sns.countplot(x="type", data=df)
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/S-SaiReddy31083/netflix-data.git
```

2. Navigate to the project folder:

```bash
cd netflix-data
```

3. Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

4. Run the Python script:

```bash
python netflixx.py
```

---

## 📈 Output

The program will display:

* Dataset information
* Missing values summary
* Duplicate count
* Dataset shape
* Graph showing distribution of Movies and TV Shows

---

## 👨‍💻 Author

**Sai Reddy**

GitHub:
https://github.com/S-SaiReddy31083

---

⭐ If you found this project useful, consider giving it a star!
