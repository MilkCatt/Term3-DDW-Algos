'''Importing necessary functions'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

'''Fetching and printing a DataFrame'''
df = pd.read_csv('W8 pokemon.csv')

'''Fetching some Dataframe Attributes'''
print("columns:",df.columns,type(df.columns))
print("index:",df.index)
print("shape:", df.shape)

'''Indexing and Filtering Data'''
column_name = 'Name'
column_index = 1
list_of_column_names = ['Name','HP','Attack']
start_row,stop_row,step_row = 0,10,2
# df.loc[rows,columns] -> label-based indexing
# df.iloc[rows,columns] -> index-based indexing
# both of these return a single column as a Series
df[column_name]
df.loc[:,column_name]
# returns multiple columns as a DataFrame
df.loc[:,list_of_column_names]
df.iloc[:,0:3]
# returns a single row as a Series
df.loc[0,:]
df.iloc[0,:]
# returns multiple rows as a Dataframe
df.loc[start_row:stop_row:step_row,:]
df.iloc[start_row:stop_row:step_row,:]
# selecting data based on conditions
df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison'),list_of_column_names]
# getting unique entries from a categorical set of data
np.unique(df['Type 1'])
# iterating through data
for i in range(0, df.shape[0]):
        for j in range(0, df.shape[1]):
            df.iloc[i,j]


'''Series and Datframe functions'''
column_name2 = "HP"
# Creating an empty DataFrame & Series
dataframe1 = pd.DataFrame()
series1 = pd.Series()
# Converting to DataFrame
df1 = pd.DataFrame(series1)
# Copying DataFrame
df2 = df1.copy()
# Statistical Functions
df.describe() # Will create a dataframe containing data on numerical columns (like 5 number summary)
df[column_name2].mean()
df[column_name2].std()
df[column_name2].min()
df[column_name2].max()
df[column_name2].quantile(q =0.75)
# Transposeing a DataFrame (row,column) -> (column,row)
df_transposed = df.T
# Vector Operations
   # Performs a function on every item within a column
df['low HP'] = df['HP'].apply(lambda hp: True if hp <= 45 else False)

'''Data Normalization'''
# Z Normalization -> mean = 0  and SD = 1
def normalize_z(dfin):
    dfout = (dfin-dfin.mean(axis=0))/dfin.std(axis=0)
    return dfout
# Min-Max Normalization -> min = 0, max = 1
def normalize_minmax(dfin):
    dfout = (dfin-dfin.min(axis=0))/(dfin.max(axis=0)-dfin.min(axis=0))
    return dfout

'''Splitting a Dataset'''
# Dataset to be split into training and test
def split_data(df, random_state = None, test_size = 0.5):

   indexes = df.index # Gets an pd.Index object, which specifies the indexes in the df
   if random_state != None: # Sets a seed if specified
      np.random.seed(random_state)
   testlen = int(test_size * len(indexes)) # Length of test array
   test_index = np.random.choice(indexes, testlen, replace = False) # Returns a list of random indexes

   indexes = set(indexes) # Set of all row indexes in df
   test_index = set(test_index) # Set of row indexes for test
   train_index = indexes = test_index # Set of remaining row indexes (for train)

   df_test = df.loc[test_index:]
   df_train = df.loc[train_index:]
   return df_test,df_train


'''Visualising Data'''
sns.se() # Use seaborn default setting

# Modifying Labels and Titles
   #Seaborn is built on top of Matplotlib, so we use Matplotlib functions
plt = sns.histplot(x = column_name, data = df)
plt.xlabel('str', fontsize = int)
plt.ylabel('str', fontsize = int) 
plt.set_title("Title", fontsize = int)

# Histplot & Boxplot
sns.histplot(x = column_name, data = df, hue= None) # Normal Histplot
sns.histplot(y = column_name, data = df, bins = 10) # Tilted Histplot with fixed bin number
sns.histplot(x = column_name, data = df, binwidth = 10, binrange = (0,50)) # Manually setting bin items
sns.boxplot(x = column_name, data = df, hue = None)

# What is Hue?
sns.histplot(x = column_name, data = df, hue= column_name2)
   # The histplot will be sorted according to column 1, but coloured depending on column 2

# Scatterplot & Lineplot
myplot = sns.scatterplot(x='Attack', y='Defense', 
                         hue='Type',
                         data=df)
myplot.set_xlabel('Pokemon Attack Stat')
myplot.set_ylabel('Pokemon Defense Stat')

# Pairplot
sns.pairplot (data = df)
   # This basically creates a bunch of plots in a grid
   # Diagonals -> Histplot, 1 var
   # Else -> Scatterplot, 2 var