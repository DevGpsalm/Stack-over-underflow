
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def col_plot(df, col, title):
    '''THis function returns the plot of a column
    INPUT:
    survey DataFrame & Column to plot
    
    OUTPUT:
    A chart of the values count for the specified column
    '''
    #Provide a pandas series of the counts for the column
    vals_count = df[col].value_counts()
    
    (vals_count/df[col].shape[0]).plot(kind = 'barh')
    plt.title(title)
    
    return


def list_options(df, col = 'NEWSOSites'):
    '''Function to return the number of different options in df['col'] rows as well as return the list of the options
    INPUT:
    
    DataFrame & Column
    OUTPUT:
    Displays the number of options and returns a list of the options
    '''
    #declare an empty list
    options = []
    
    #looop through the column
    for val in df[col]:
        try:
            options.extend(val.split(';'))
        except AttributeError:
            pass
    #Apply set to remove duplicates in the options. List converts the set object to a list
    options = list(set(options))
    
    print("The number of options in {} is {}.".format(col,(len(options))))
    
    return options


def volume_count(df, col1, col2, look_for):
    '''
    This function generates the count of each string (options) in the specified column of a DataFrame
    INPUT:
    df - the pandas dataframe you want to search
    col1 - the column name you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of the dataframe column

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it shows up
    '''
    new_df = defaultdict(int)
    
    #loop through list of values you want to count in the column
    for val in look_for:
        #loop through rows
        for idx in range(df.shape[0]):
            #if the val type is in the row add 1
            if val in df[col1][idx]:
                new_df[val] += int(df[col2][idx])
    new_df = pd.DataFrame(pd.Series(new_df)).reset_index()
    new_df.columns = [col1, col2]
    new_df.sort_values('count', ascending=False, inplace=True)
    return new_df
    
    
def clean_and_plot(df, col = 'NEWSOSites', title='Most Visited Stackoverflow Site', plot=True):
    '''
    
    INPUT 
        df - a dataframe holding the Stackoverflow sites visited column
        title - string the title of your plot
        axis - axis object
        plot - bool providing whether or not you want a plot back
        
    OUTPUT
        study_df - a dataframe with the count of how many individuals
        Displays a plot of showing the count of the site visited by developers who answered the questionnaire.
    '''
    site = df[col].value_counts().reset_index()
    site.rename(columns={'index': 'method', col: 'count'}, inplace=True)
    site = volume_count(site, 'method', 'count', list_options(df, col))

    site.set_index('method', inplace=True)
    if plot:
        (site/site.sum()).plot(kind='barh', legend=None);
        plt.title(title);
        plt.show()
    props_site = site/site.sum()
    return props_site
    

