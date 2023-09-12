### Environment & Interpreter
> Conda 23.5.2, Python3.8

# Unified POC

### Overview

> The concept of this experiment is to create a solution for extracting insights about the campaign data from the raw data about advertisements.


#### Created sample dataset 
>Overview - Created sample dataset according to the format of the unified client dataset

We have taken these parameters according to the sample data - 
>> ['User', 'Date', 'Facebook_Clicks', 'Facebook_Views', 'Facebook_bought', 'Youtube_Views','Youtube_Clicks','Youtube_Followers','Youtube_bought','Youtube_Subscription','Instagram_Views','Instagram_Clicks','Instagram_Followers']


In this dataset, We have taken three users ( Ram, Aman, and Durgesh). We have given entry to each user on every platform every day.

This dataset consists of 2 months of data.

At the end of running the project, we will have a CSV file.

#### Analysis Engine
We have created an analysis engine for basic functionalities like calculating min, max and average value of the entire dataframe or column specific series for numerical columns.

#### Building script for prompt generation
We have created a script for prompt generation, where we are creating prompts with a generic pattern, and saving them in a csv file to feed our model.
