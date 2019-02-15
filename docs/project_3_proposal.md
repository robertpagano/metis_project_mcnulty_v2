# Project McNulty Proposal

*Predicting the outcome of a cat intake at a no-kill animal shelter in Austin, TX*

**Robert Pagano**



![img](http://www.austintexas.gov/sites/default/files/aac_logo.jpg)



### Scope

The Austin Animal Shelter is a no-kill shelter for cats, dogs, and other animals, in Austin, Texas. From 1998 to 2011, the euthanasia rate of animals that entered an Austin, TX animal shelter went from 85% to less than 10% ([source: wikipedia.org](https://en.wikipedia.org/wiki/No-kill_shelter)). 

Due to this rather progressive policy, managing these facilities is no easy task. After reviewing the data, my initial findings showed me that a vast majority of outcomes from cats that were brought into this shelter resulted in either an adoption or a transfer to a partner facility. My goal is to create a model that can predict an outcome between transfer and adoption, with the intention of using this model to better redirect intakes to other shelters in the area when needed. I think this could have a massive benefit in helping to manage capacity at one of the largest no-kill animal shelters in the country.



### Data Source

- https://www.kaggle.com/aaronschlegel/austin-animal-center-shelter-intakes-and-outcomes/home - this is data that has already been processed a bit. May decide to use the raw data and process it in my own way. The raw data is updated at [Austin's Open Data Initiative](https://data.austintexas.gov/ ) regularly. 
- It is actually two data files, one for intakes and one for outcomes, that can be merged on animal ID



### Target Variable

The target value I will try to predict is whether or not an intake resulted in an adoption or a transfer to another facility. There are several other outcomes listed, such as euthanasia or death, but these seem to be directly related to animals that are brought on that could not be saved for medical reasons, and therefore not relevant to my analysis.



### Observations

There are around 80k records that match each other between intakes and outcomes, the vast majority of which are either adopted or transferred



### Potential Features

- Age at outcome
- Cat or Kitten
- Length of stay at shelter
- sex
- spayed/neutered or intact 
- month
- day of week
- breed (domestic / exotic)
- coat pattern
- color
- intake condition
- intake type (stray, owner surrender, etc.)



### Potential Challenges

- The data may take a large amount of cleaning. For example, several of the categorical variables are not standardized, meaning they are just open-ended entries from whoever was recording the data into the database. 
- Most of the features are categorical - not entirely sure how much / badly that could affect things



### Considerations

- This data includes both cats and dogs (+ other animals) - if I have time / if running into issues with cat data, may see if dog data makes a bit more sense. My gut feeling tells me things like breed, for example, would be a bigger indicator for dogs
- A flask app could potentially be developd to let you know if the cat you are bringing to the shelter would likely be transferred. This could be used to then instead redirect you to a partner facility, and can be adjusted during times when the shelter is particularly crowded









