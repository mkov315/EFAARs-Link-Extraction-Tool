# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:04:35 2023

Mary Kate O'Leary - Wayne State University MLIS '23
Cleveland State University Practicum Student
Fall 2023

@author: moleary
"""

import pandas as pd
import re

myfile1 = 'college_of_arts_sciences_scholarly_report_2020-2023.csv'
myfile2 = 'college_of_business_scholarly_report_2020-2023.csv'
myfile3 = 'college_of_engineering_scholarly_report_2020-2023.csv'
myfile4 = 'college_of_health_scholarly_report_2020-2023.csv'
myfile5 = 'college_of_law_scholarly_report_2020-2023.csv'
myfile6 = 'levin_college_of_public_affairs and education_scholarly_report_2020-2023.csv'


raw_text_file = 'citations_summer2020-spring23.txt'


read_df1 = pd.read_csv(myfile1, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')
read_df2 = pd.read_csv(myfile2, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')
read_df3 = pd.read_csv(myfile3, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')
read_df4 = pd.read_csv(myfile4, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')
read_df5 = pd.read_csv(myfile5, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')
read_df6 = pd.read_csv(myfile6, index_col=False, on_bad_lines='warn', low_memory=False, encoding='utf-8')

read_df1 = read_df1.replace(to_replace='\xa0', value=' ', regex=True)
read_df2 = read_df2.replace(to_replace='\xa0', value=' ', regex=True)
read_df3 = read_df3.replace(to_replace='\xa0', value=' ', regex=True)
read_df4 = read_df4.replace(to_replace='\xa0', value=' ', regex=True)
read_df5 = read_df5.replace(to_replace='\xa0', value=' ', regex=True)
read_df6 = read_df6.replace(to_replace='\xa0', value=' ', regex=True)

read_df1 = read_df1.replace(to_replace="\’",value="'", regex=True)
read_df2 = read_df2.replace(to_replace="\’",value="'", regex=True)
read_df3 = read_df3.replace(to_replace="\’",value="'", regex=True)
read_df4 = read_df4.replace(to_replace="\’",value="'", regex=True)
read_df5 = read_df5.replace(to_replace="\’",value="'", regex=True)
read_df6 = read_df6.replace(to_replace="\’",value="'", regex=True)

read_df1 = read_df1.replace(to_replace='â€™s', value="'", regex=True)
read_df2 = read_df2.replace(to_replace='â€™s', value="'", regex=True)
read_df3 = read_df3.replace(to_replace='â€™s', value="'", regex=True)
read_df4 = read_df4.replace(to_replace='â€™s', value="'", regex=True)
read_df5 = read_df5.replace(to_replace='â€™s', value="'", regex=True)
read_df6 = read_df6.replace(to_replace='â€™s', value="'", regex=True)


read_df1 = read_df1.replace(to_replace='â€œ', value="", regex=True)
read_df2 = read_df2.replace(to_replace='â€œ', value="", regex=True)
read_df3 = read_df3.replace(to_replace='â€œ', value="", regex=True)
read_df4 = read_df4.replace(to_replace='â€œ', value="", regex=True)
read_df5 = read_df5.replace(to_replace='â€œ', value="", regex=True)
read_df6 = read_df6.replace(to_replace='â€œ', value="", regex=True)

read_df1 = read_df1.replace(to_replace=["\“", "\”"],value="", regex=True)
read_df2 = read_df2.replace(to_replace=["\“", "\”"],value="", regex=True)
read_df3 = read_df3.replace(to_replace=["\“", "\”"],value="", regex=True)
read_df4 = read_df4.replace(to_replace=["\“", "\”"],value="", regex=True)
read_df5 = read_df5.replace(to_replace=["\“", "\”"],value="", regex=True)
read_df6 = read_df6.replace(to_replace=["\“", "\”"],value="", regex=True)

df = pd.concat([read_df1, read_df2, read_df3, read_df4, read_df5, read_df6], ignore_index=True)


df2 = pd.read_csv(raw_text_file, encoding = "utf-8", sep='\t')

df2 = df2.replace(to_replace=["\“", "\”"],value="", regex=True)
df2 = df2.replace(to_replace='\xa0', value=' ', regex=True)
df2 = df2.replace(to_replace='â€™s', value="\'", regex=True)
# This line is NOT working, it's completely removing the apostrpohe
df2 = df2.replace(to_replace=r'\’',value=r"'", regex=True)


# For the dataframe and all the rows,

# If you see a row starting with "https", append it to df3 as a column
# when row beings with https

df3= df2.loc[df2["College of Arts & Sciences"].str.startswith("http")]
df3['index1']=df3.index
df3['index2']=df3['index1']-1
s = df3['index2']
s2=pd.Series(range(len(s)))

for i in s2:
    for X in s:
        s2[i]=df2.loc[X,:]
        i=i+1
    break

df2=df2.rename(columns={'College of Arts & Sciences': 'Raw Text'})
df2['Raw Text'] = df2['Raw Text'].astype('string')

#regex=r"\d{4}\)\..............................."
regex=r"\)\..........................."

s3 = pd.Series(range(len(s)))
# Make a for loop
for z in range(350):
    for q in s:
        s3[z] = df2['Raw Text'][q]
        z=z+1
    break
    
s4 = pd.Series(range(len(s)))
    

for f in range(350):
   s4[f] = re.findall(regex,s3[f])
   s4[f] = [sub.replace('). ', '') for sub in s4[f]]


    
df3=df3.rename(columns={'College of Arts & Sciences': 'Links'})
df3.reset_index(drop=True, inplace=True)
df3['TitleID'] = s4

#Just to test theory

df['TitleID']=df['Title'].str.extract(r'(^.{25})')
df['TitleID']=df['TitleID'].replace(to_replace="'",value="", regex=True)

df3['Links'] = df3['Links'].astype('string')
df3['TitleID'] = df3['TitleID'].astype('string')
df['TitleID'] = df['TitleID'].astype('string')
df3['TitleID']=df3['TitleID'].str.replace(r"[\"'\[\]]", '')


df_final = pd.merge(df,df3, how='outer', on='TitleID')
#df_final = df.join(df3.set_index('TitleID'), on='TitleID')

df_final.to_csv('EFAARs output.csv')
