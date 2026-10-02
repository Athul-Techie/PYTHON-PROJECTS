import pandas as pd
'''THIS PART IS PYTHON PANDAS'''
#QN1)
print('Creation of empty dataframe')
df=pd.DataFrame()
print(df)
print()

#QN2)
data=[
    {'Course':'Data Science','Duration':12},
    {'Course':'Artificial Intelligence','Duration':18},
    {'Course':'Web Development','Duration':6}
    ]
df=pd.DataFrame(data)
print(df)
print()

#QN3)
df['Course Code']=['C01','C02','C03']
print(df)
print()

#QN4)
df.loc[3]=['Desing Thinking',5,'C04']
print(df)
print()

df.loc[1]=['Artificial Intelligence',20,'C02']
print(df)
print()


'''THIS PART IN DATA VISUALIZATION'''
import matplotlib.pyplot as plt
print()
print()
print()
print()
print('THIS PART IN DATA VISUALIZATION')
data={
    'Name':['Atulya','Disha','Kavita','John'],
    'Score':[12.5,9.0,16.5,15.0],
    'Attempts':[1,3,2,1],
    'Qualify':['Yes','No','Yes','No']
    }
df1=pd.DataFrame(data)
print(df1)
print()

#QN1
df2=df1.to_csv('Registration File.csv',sep=',',index=False,header=True)


#QN2
regis=pd.read_csv('Registration File.csv')
print('Regis File')
print(regis)
print()

#QN3
print('Plotting the Line Graph')
plt.title('NAME AND SCORE')
plt.xlabel('NAME')
plt.ylabel('SCORE')
plt.plot(df1.Name,df1.Score,color='r')
plt.savefig('names&scores.jpg')
plt.show()
