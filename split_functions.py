
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict


def col_plot(df, col, title):
    '''
    This function returns horizontal bar plot of a column in a dataframe df, with a title
    INPUT:
    survey DataFrame, Column to plot & the title of the chart
    
    OUTPUT:
    A chart of the values count for the specified column
    '''

    df = df.dropna(subset=[col])

    #Provide a pandas series of the counts for the column
    vals_count = df[col].value_counts()
    
    (vals_count/df[col].shape[0]).plot(kind = 'barh')

    print(vals_count/df[col].shape[0])
    print(df.shape)
    
    plt.title(title)
    
    return


def list_options(df, col = 'NEWSOSites'):
    '''
    Function to return the number of different options/string values in a dataframe row as well as return the list of the string         values
       
    INPUT:
    DataFrame & Column in the dataframe
    
    OUTPUT:
    Displays the number of string values and returns a list of the string values
    '''
    #declare an empty list
    string_val = []
    #loop through the column in the df
    for val in df[col]:
        try:
            string_val.extend(val.split(';'))
        except AttributeError:
            pass
    #Apply set to remove duplicates in the options. List converts the set object to a list
    string_val = list(set(string_val))
    
    print("The number of options in {} is {}.".format(col,(len(string_val))))
    
    return string_val


def volume_count(df, col1, col2, look_for):
    '''
    This function generates the count of each string (options) in the specified column of a DataFrame
    INPUT:
    df - the pandas dataframe
    col1 - the column you want to look through
    col2 - the column you want to count values from
    look_for - a list of strings you want to search for in each row of the dataframe column

    OUTPUT:
    new_df - a dataframe of each look_for with the count of how often it appeared in the dataframe column
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
    This function plots the porportion of a string value in a dataframe column
    INPUT 
        df - a dataframe holding the column
        title - string the title of the plot
        plot - bool providing whether or not you want a plot back
        
    OUTPUT
        study_df - a dataframe with the count of how many individuals
        Displays a plot of showing the proportion count of the values in the column.
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
    

