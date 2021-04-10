
# Stack-over/underflow
Stack Overflow Usage and Community Analysis Using 2020 Stack Overflow developer survey 
[Link to medium post](https://gpsalm.medium.com/stack-over-under-flow-572e46f2be53) 


### Table of Contents

1. [Installation](#installation)
2. [File Descriptions](#files)
3. [Project Motivation](#motivation)
4. [Data Modelling & Analysis](#modelling&analysis)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.


## File Descriptions <a name="files"></a>

There are 2 notebooks available here to showcase work related to the above questions.  One of the notebooks (split_functions) contained the defined functions imported in the the main (stack overflowunderflow) notebook to make the main notebook clear and easy to understand. Markdown cells were used to assist in walking through the thought process for individual steps.  

## Project Motivation <a name="motivation"></a>
For this project, I was interested in finding out more about stack overflow usage and community participation using the Stack Overflow 2020 questionnaire conducted by stack overflow. This project answered some questions bothering on how welcome respondents felt compared to the previous year, their preference on relaxation of restrictions on off-topic, the precentage of respondents with stack over flow account and those that see themselves as a member of the stack overflow community.
Additionally, I assess the percentage of the respondents who uses stack overflow as an option when stucked. Below are the five questions answered in this project:

1. 	How many of the respondents have a stack overflow account, as well as see themselves as a member of the stack overflow community?
2.	What is the most visited stack overflow sites by the respondents?
3.	How well does stack overflow ranks in terms of the options used by the respondents when stucked?
4.	The views of respondents as regards the relaxation of restriction on what is considered off-topic
5.	Did respondents feel welcomed compared in 2020 to the previous year (2019) on the platform?

## Data Modelling & Analysis <a name = "modelling&analysis"></a>

#### Data Understanding:
The dataset used was gotten from stack overflow 2020 developer survey questionnaire.
The questionnaire was filled by 64,461 respondents. However, the field used in this analysis were optional fields. Missing values were replaced with zeros. Replacing missing values with zeroes allows for discarding options not filled by the respondents in a particular column/question rather than doing away with all the responses from the respondents who chooses not to answer any of the questions. This way, I am able to analyze the responses from respondents for a particular question.
A look at the basic demographics of respondents was done to have a general understanding of the respondents employment status, educational level and job profession.

#### Data Preparation
The columns were cleaned such that the columns with more than one options were separated using the split_functions function. The string values were extracted into a list to have a view of the values as well as the count of their apperance as chosen by the respondents. There are no outliers in the data used for the analysis.

#### Data Visualization
Horizontal bar chart measuring the proportion of respondents who gave a particluar answer to the questions measured was used for the the visualization and answering the five questions raised in this project.


## Results<a name="results"></a>
Even though more than 70% of the respondents did mention that they do have a stack overflow account, just about 40% do consider themselves as a member of the stack overflow community. Participation of the respondents on stack overflow appears to be low. Other metrics also point to the fact that most do not feel more welcomed than they were last year albeit with more people neutral or not interested in relaxation of off-topics. However, a look at the off-topic should be considered with a significant number of the respondents mentioning that they would like some sort of relaxations on what is considered off topic. This likely will help to drive participation and community.



## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Stack Overflow for the data.  You can find the Licensing for the data and other descriptive information at the Kaggle link available [here](https://insights.stackoverflow.com/survey).  Otherwise, feel free to use the code here as you would like! 


