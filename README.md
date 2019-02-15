## Boosting Cat Adoptions:

*Predicting Outcomes of Cats at the Austin Animal Center*



Metis Project 3: Project McNulty - Classification / Supervised Learning



### Data sources

- Austin Animal Center data from Austin open data portal:
  - [Intake Data](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm)
  - [Outcome Data](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)
- weather data from [Farmer's Almanac](https://www.almanac.com/weather/history)



### Goal

- Predict whether a cat will be adopted or transferred to another facility using a CatBoost classification model in order to build a tool that will let volunteers / citizens know whether to bring the animal into the shelter or to bring it to a partner facility



| Tools            |
| ---------------- |
| Pandas           |
| NumPy            |
| Matplotlib       |
| Seaborn          |
| Tableau          |
| scikit-learn     |
| Jupyter Notebook |
| Sublim Text      |
| PostgreSQL       |



### Code, data, notebooks

**Jupyter Notebooks** 

- *AAC Intakes + Outcomes Raw Data Clean.ipynb* - Importing the raw csv files, cleaning and filtering features, feature engineering
- *Final Feature Engineering Before Modeling.ipnyb* - Final formatting of data, creating specific dataframes for various models based on the unique requirements of different models
- *RF and Logistic Modeling.ipynb* - Training and cross-validation of Random Forest and Logistic Regression models
- *Random Forest - V2.ipynb* - Training and cross validation of a version of Random Forest with fewer features, using grid search instead of randomsearch
- *CatBoost Model.ipynb* - Training and cross-validation of our final model, the CatBoost model

- *code/old* - EDAs on a few other datasets that I looked through prior to choosing this cat adoption problem



**Data**

- */data/raw_data* - Raw data files for weather and animal center
- */data/interim_data* - Some interim data files that were pickled or created along the way
- */data/final_feature_sets_for_modeling/* - Final pickle files that were used for various models
- */final_model/* - final pickle file for the CatBoost model



### Summary files (/docs/)

- *Project McNulty - Final Presentation RP.pdf* - Presentation Slides
- *Project McNulty - Final Writeup.md* - High level written summary of project
- *project_3_proposal* - Original proposal for project idea