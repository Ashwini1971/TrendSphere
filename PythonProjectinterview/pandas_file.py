"""
1. easy to cleaning and transformation
2. efficient handling large dataset
3. integration with other python libraries like
matplotlib and seaborn for visualization
"""

'key data-structure in pandas'
'''
1. series(1 dimensional)
2. dataframe(2 dimensional)
'''
import pandas as pd
# s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print(s)
#
# df = pd.DataFrame({'name': ['aswini', 'aswin', 'anil', 'chethan'],
#                    'age': [25, 30, 35, 24],
#                    'marks': [100, 98, 87, 89]},
#                   index=[101, 102, 103, 104])
# print(df)

df1 = pd.read_csv('Movies Dataset.csv',
                  encoding='utf-8',
                  encoding_errors='ignore')
'extracting data'
# print(df1)

'get first 5 columns'
# first_5_cols = df1.filter(df1.columns[:5])
# print(first_5_cols)

'get first 5 rows'
# first_5_row = df1.head()
# print(first_5_row)

'get last 5 rows'
# last_5_rows = df1.tail()
# print(last_5_rows)
'based on index --> iloc'
# print('selecting first row: \n', df1.iloc[0])
'based on label --> loc'
# print('selecting first row: \n', df1.loc[8])

'describe'
# print(df1.describe())
'get one column'
# print(df1['id'])

'check datatype'
# print(type(df1['id']))
'get 2 cols'
# print(df1[['id', 'original_language']])

duplicate_df = pd.read_csv(r'Movies Dataset - Copy.csv',
                            encoding='utf-8',
                            encoding_errors='ignore')
# print(duplicate_df)
'drop rows with NAN values'
# print(duplicate_df.dropna())
'replace nan to 0'
# duplicate_df.fillna(0, inplace=True)
# print(duplicate_df)

'to rename the column name'
duplicate_df.rename(columns={'original_language':'Native_language'},
                    inplace=True)
'To get all the headers'
'1.'
# header_cols = list(duplicate_df.columns)
# print(header_cols)
'2.'
# print(duplicate_df.info())

'To change the datatype'
# duplicate_df['popularity'] = duplicate_df['popularity'].astype(int)
# print(duplicate_df.info())

'To get one data'
# print(duplicate_df['id'][0])

'To add a column'
# duplicate_df['zeros'] = [0 for i in range(len(duplicate_df))]
# print(duplicate_df.info())

''
# def fx(a):
#     return a * a
# duplicate_df['zeros + 1'] = duplicate_df['revenue'].apply(fx)
# print(duplicate_df[['revenue', 'zeros + 1']])
# duplicate_df.to_csv('export.csv', index=False)

'To merge 2 dataframe'
# d_f1 = pd.DataFrame({
#     'Employee': ['roopa', 'chanthana', 'aishu', 'priya'],
#     'salary': [34, 23, 45, 20]
# })
# print('DataFrame 1:\n', d_f1)

# d_f2 = pd.DataFrame({
#     'Employee': ['anil', 'aswini'],
#     'salary': [45, 20]
# })
# print('DataFrame 2:\n', d_f2)
'-------------'
# concat_data = pd.concat([d_f1, d_f2], ignore_index=True)
# print(concat_data)

'using merge -- to merge diff named cols'
d_f = pd.DataFrame({
    'Employee': ['anil', 'aswini', 'aswin'],
    'salary': [45, 20, 1000]
})

d_f_ = pd.DataFrame({
    'Employee': ['anil', 'aswini'],
    'employee_id': [3421, 2043]
})
# print(d_f_)
# print(d_f)
'The data uncommon will be removed'
merged_data = pd.merge(d_f, d_f_, on='Employee')
# print(merged_data)
'setting index as a col-name'
# print(merged_data.set_index('Employee'))
'reset'
# print(merged_data.reset_index())

merged_data['job'] = ['Mobile-Tester', 'Automation-Eng']
# print(merged_data)

d_f_1 = pd.DataFrame({
    'Employee': ['roopa', 'Teju', 'vivek', 'chethan'],
    'salary': [34, 23, 89, 45],
    'employee_id': [3421, 2043, 4325, 6745],
    'job': ['Re', 'Re', 'developer', 'automation-eng']
})
merged_data1 = pd.concat([d_f_1, merged_data], ignore_index=True)
# print(merged_data1)
# merged_data1.to_csv('export1.csv')

df = pd.read_csv('export1.csv')
# df.to_json('mydata.json')
# print(df.to_dict())
# merged_data1.reset_index()
# print(df.sample(3))
# print(list(df.columns))

'To increase the size'
# pd.options.display.max_columns = 500
# print(df)

'indexing'
# print(df)
# print(df.loc[0])
# print(df.iloc[0])

df = df.set_index('Employee')
# print('roopa"s details\n', df.loc['roopa'])
# print('roopa"s salary\n', df.loc['roopa', 'salary'])

# print(df.iloc[0, 3])

# print(df.loc['aswini', 'salary'])
# df.loc['aswini', 'salary'] = 40
# print(df)

# df.loc['aswini'] = [5, 45, 4532, 'auto-eng']
# print(df)

# print(df.iloc[0])
# print(df.iloc[0:2])
# print(df.iloc[0:2, 2])
# print(df.iloc[0:1])
# df['salary'] = df['salary'] * 10000
# print(df)

'To add a user-defined function'
def my_function(x):
    if x % 2 == 0:
        return x ** 2
    else:
        return x // 2

print(df.salary.apply(my_function))



