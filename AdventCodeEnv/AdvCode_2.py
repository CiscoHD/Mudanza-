import pandas as pd

'''
We read the file in the .csv (comma-separated values) format
and asign it to a variable called inputs
'''
inputs = pd.read_csv('reportes.csv')
#We create a DataFrame with 'inputs' as data
df = pd.DataFrame(data = inputs)
#Then we fill the NaN values with 0 to avoid errors
df = df.fillna(0)
#Show some properties of the Dataframe 
print('DataFrame shape: {}'.format(df.shape))
print('Columns DataTypes: \n{}'.format(df.dtypes))
#Mach data types to int 
df = df.convert_dtypes()
print(df)

safe_reports =  0 #To count the number of safe reports 

for row in range(len(df)): #Iterate the rows 
    end_report, end_reached = 8, False 
    differences = []
    for col in df: #Iterate the columns
        #Find the last element with data in the DataFrame
        if end_reached == False:
            if df[col][row] == 0:
                end_report = int(col) - 1 # last column with data
                end_reached = True
    #Differences between consecutive pairs converted to a list 
    differences = df.iloc[row, 0:end_report].diff().dropna().tolist()
    """
        Check if the elements in the difference list are:
        ->Negative by checking if they are in the range(-3, 0), which means [-3, -2. -1] 
        OR
        ->Positive by checking if they are in the range(1, 4), which means [1, 2. 3]
    """
    if (all(x in range(-3, 0) for x in differences) or
        all(x in range(1, 4) for x in differences)):
        #print('Row {} is safe'.format(row))
        safe_reports = safe_reports + 1

#Show the number of safe reports 
print('Safe rows: {}'.format(safe_reports))
