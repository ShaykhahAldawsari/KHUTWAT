[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/tLvnbFIl)
# Khotwa: a ML Project  

## Problem Statement and Motivation
##### This project aims to explore and understand personality traits by developing an unsupervised clustering model using the Big Five personality dataset. The objective is to uncover hidden patterns and categorize individuals into meaningful personality clusters based on their traits. By analyzing these clusters, the model will offer personalized insights to users upon completing a personality test, helping them gain a deeper understanding of their characteristics.

  
## The Solution: Khotwa
_here
  _

## Key Features


## Team Members
- Shaykhah Aldawsari
- Adwa
- Alwai
- Naif


## Libraries and Tools
  

- **Python Libraries**
  
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)  
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Seaborn](https://img.shields.io/badge/Seaborn-%23137980.svg?style=for-the-badge&logo=seaborn&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)


- **Deployment Tools**
  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

- **Version Control**
  
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)


## Project Structure

```
├├── data/
│   ├── raw/
│   │   ├── Dataset-Mental-Disorders.csv       # Original mental disorders dataset
│   │   ├── Mental-Health-in-Tech.csv         # Original tech mental health dataset
│   │   ├── big5_sample.csv                   # Original Big Five personality dataset
│   │   ├── codebook.txt                      # Codebook for Big Five dataset 
│   ├── cleaned/
│   │   ├── Dataset-Mental-Disorders_cleaned_data.csv    # Cleaned mental disorders data
│   │   ├── Mental-Health-in-Tech_cleaned_data.csv       # Cleaned tech mental health data
│   │   ├── big5_sample_cleaned.csv                      # Cleaned Big Five dataset
│   │   ├── data_with_clusters.csv                       # Clustered data (Big Five)
│   │   ├── mini_data_with_clusters.csv                  # Clustered mini data (Big Five)
├── deployment/
│   ├── big5_cluster_model.pkl             # Big Five cluster model
│   ├── mini_big5_cluster_model.pkl        # Mini cluster model
│   ├── survey.py                          # Survey script
│   ├── survey_mini.py                     # Mini survey script
├── notebooks/
│   ├── data-cleaning/
│   │   ├── Big5_cleaned.ipynb             # Data cleaning for Big Five dataset
│   │   ├── Dataset-Mental-Disorders_cleaned.ipynb  # Data cleaning for mental disorders dataset
│   │   ├── Mental-Health-in-Tech_cleaned.ipynb     # Data cleaning for tech mental health dataset
│   ├── models/
│   │   ├── Big5_models.ipynb              # Model building for Big Five dataset
├── slides/
│   ├── thisproj_slides.pdf                # Project presentation slides
├── README.md                              # Project overview and instructions
├── requirements.txt                       # Python dependencies

```

## Usage 
1. Clone the repository:
   ```bash
   git clone [repo_url]
   ```
2. Install required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. Run notebooks in the specified order:
   1. `cleaning.ipynb`
   2. `deployment.ipynb`



## Access the Website 
- Get insights on your personality through [appname](Applink)

## Data 
  ### Raw Data
  - **Link**

    [![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/moayadalkhozayem/job-postings-in-saudi-arabia)
  - **About the Data**: _here_.
  - **Raw Data Features**


    ### Cleaned Data
      - **Link**:
        
        [![Kaggle](https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/shaykhaaldawsari/jadarat-cleaned-data-csv/data)
      - **Cleaned Data Features**
        




## License

[MIT](https://choosealicense.com/licenses/mit/)
