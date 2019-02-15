## Boosting Cat Adoptions:

*Predicting Outcomes of Cats at the Austin Animal Center*

**Robert Pagano - February 14th, 2019**



## Summary

The Austin Animal Center is the largest no-kill animal shelter in the United States. The city of Austin passed the [No Kill Implementation Plan](http://www.austintexas.gov/sites/default/files/files/Animal_Services/aac_no_kill_implementation_plan.pdf) in 2010, which required that the Austin Animal Center must save 90% of all animals that come through it's doors. Due to this progressive policy, the city saves countless animals, but requires more resources to do so.

The AAC partners with several other local orginizations in the area to transfer animals when they are either at capacity, or if the animal has needs that cannot be met at the center. My goal for this project was to analyze intake and outcome data from 2013-2019, and see if I could create a model that could reliably predict a cat's outcome when they enter the shelter, using only information available at intake. This model could then potentially be used in a flask app which could be used by volunteers or good samaritans to see if the animal should be taken to another shelter instead.

My main metrics for sucess with my model were precision and accuracy, and by achieving a precision of ~79% and an accuracy of ~75%, I believe I was successful. In the future, I would love to implement a flask app to further flesh out my original concept.

## Tools and Packages Used

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



##  Data Collection and Feature Selection

As mentioned before, I used Austin Animal Center's own self reported data for the majority of my data. I merged together intake and outcome data by a unique ID that each animal is assigned at it's first intake.

I also used weather data for Austin, Texas, to append daily temperature and precipitation totals to each observation - the temperature actually proved to be fairly important in the final model.

When I was first doing my analysis, I considered including dogs with my model, or even creating a separate model for dogs. I realized, however, that there was a third extremely significant outcome for this animal - "return to owner". Lost dogs being reunited with their owners made up nearly a third of all outcomes, but less than 1% of all cat outcomes. I decided to limit my scope in the interest of focusing on one solid model and outcome, but in the future, I would be interested in coming back to this and exploring dogs further.

The data for cats ended up being very balanced by outcome - roughly 53% of outcomes were transfer, and 47% were adoptions. One interesting thing I found while working on my EDAs was that there was a spike in transfers in May of 2015 - I looked into why this might be and discovered that there was historic flooding in Austin at the same time:

![image-20190214213455181](/Users/robertpagano/Library/Application Support/typora-user-images/image-20190214213455181.png)

After running through the process of data cleaning, analysis, feature engineering, and feature selection, I ended up with my final set of features. I did have to process these features in multiple ways in order to fit different models. For example:

- The Logistic modeling had to be done after dropping a dummy variable
- The Random Forest modeling had to keep all categorical features one hot encoded
- The CatBoost model needed to take all features in as is.

Here are a list of the final features in the CatBoost model, ranked in order of importance:

![image-20190214212852971](/Users/robertpagano/Library/Application Support/typora-user-images/image-20190214212852971.png)

Note that nearly all data in original files were categorical (or dates) - I created some numerical features myself by calculating:

- Age at intake (this was formatted in several ways as text, like "20 days", "6 months", "5 years", "6 weels", etc, so had to code this)
- Intakes in the last week - just did a rolling count using date 
- Weather data



**NB: My brief psql work is saved under /code/Sql Work.ipynb**



## Model Analysis and Results



The first model I tried to get to my MVP with just a few features was a logistic model. I mainly got to this point as quickly as possible just to get used to using this new model, and since it was so similar to a Linear Regression model, it seemed like a great entry point for this project. With just a few basic features, my accuracy was arFuture Work

After doing some more data cleaning and feature engineering, I did another round of modeling, this time starting with Logistic, moving on to Random Forest, and then finally settling on CatBoost.

- The Logistic model had a maximum accuracy of .65 after using cross validation within a grid search.

- The Random Forest model had a maximum accuracy of .72 after cross validation within a random search. This model was more useful not just because it was more accurate thouh - I used it to trim some unimportant features from my final selection.

- Finally, my CatBoost model ended up with an an accuracy of .75, and a precision of .77.

In this specific case, I was hoping to boost my precision, as I figure it's more OK to have false negatives (predicting adoption that end up being transferred), then false positives (predicting transfer when the cat would be adopted). I'd hate to be sending adoptable animals to smaller facilities - we're trying to maximize the number of adoped animals:



![image-20190214214208410](/Users/robertpagano/Library/Application Support/typora-user-images/image-20190214214208410.png)



## Future Work

- As I mentioned earlier, I think completing a Flask App as a proof of concept would be great. There are some interesting problems I'd have to figure out - how could I automate weather data, how many intakes there have been in the last week, etc.

- Do a similar analysis on dogs (or potentially the other animals in the center such as birds, rabbits, reptiles, etc.)