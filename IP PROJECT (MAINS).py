.print('WELCOME TO THE DIRECTORY ON RAINWATER HARVESTING')
import pandas as pd
import matplotlib.pyplot as plt
c='y'
df=pd.read_csv('RAINWATER HARVESTING.csv')
print('*****MENU*****')
print('1.Add new detail')
print('2.Remove detail')
print('3.Rename any of the column')
print('4.Change the values in any State')
print('5.Displaying first 2 rows')
print('6.Graph')
print('7.Display the DataFrame')
print('8.Displaying data from any point')
print('9.Exit')
while True:
    a=int(input('Enter your choice: '))
    if a==1:
        print(df)
        print()
        ind=int(input('Enter the index: '))
        n=input('Enter the State name: ')
        dam=input('Enter the amount of water in dams: ')
        t=input('Enter the amount of water in trenches: ')
        roof=input('Enter the amount of water in rooftops: ')
        total=int(input('Enter the total amount of water: '))
        df.loc[ind]=([n,dam,t,roof,total])
        print(df)
        print()

    elif a==2:
        a=input('Enter the State name to be deleted: ')
        print('Details deleted successfully')
        df=df.drop(df[df.State==a].index,axis=0)
        print(df)
        print()

    elif a==3:
        print('Changing of the Column name')
        old=input('Enter the current column name: ')
        new=input('Enter the new column name: ')
        df=df.rename({old:new},axis=1)
        print(df)
        print()
        
    elif a==4:
        print('Change the values of each rainwater saving technique in a State')
        ind=int(input('Enter the index: '))
        n=input('Enter the State name: ')
        dam=input('Enter the amount of water in dams: ')
        t=input('Enter the amount of water in trenches: ')
        roof=input('Enter the amount of water in rooftops: ')
        total=int(input('Enter the total amount of water: '))
        df.loc[ind]=([n,dam,t,roof,total])
        print(df)
        print()

    elif a==5:
        print('Displaying the first "n" rows')
        n=int(input('Enter the number of rows you want to display: '))
        print(df.head(n))
        print()
        
    elif a==6:
        print('OPTIONS FROM DISPLAYING')
        print('1.State and Check Dams')
        print('2.State and Trenches')
        print('3.State and Rooftops')
        g=int(input('Enter the option number for the water storage "BAR GRAPH" you want to display: '))
        
        if g==1:
            plt.title('STATES & WATER STORAGE RATES')
            plt.xlabel('STATES')
            plt.ylabel('AMOUNT OF WATER STORED IN CHECKDAM')
            plt.bar(df.State,df.CheckDam,color='r',width=0.20)
            plt.savefig('WATER IN CHECK DAMS')
            plt.show()
            print()
            
        elif g==2:
            plt.title('STATES & WATER STORAGE RATES')
            plt.xlabel('STATES')
            plt.ylabel('AMOUNT OF WATER STORED IN TRENCHES')
            plt.bar(df.State,df.Trench,color='g',width=0.21)
            plt.savefig('WATER IN TRENCHES')
            plt.show()
            print()
            
        elif g==3:
            plt.title('STATES & WATER STORAGE RATES')
            plt.xlabel('STATES')
            plt.ylabel('AMOUNT OF WATER STORED IN ROOFTOP')
            plt.bar(df.State,df.Rooftop,color='c',width=0.22)
            plt.savefig('WATER IN ROOFTOPS')
            plt.show()
            print()
            
    elif a==7:
        print('Displaying the entire dataframe')
        print(df)
        print()
        
    elif a==8:
        a=int(input('Enter the start value index: '))
        b=int(input('Enter the end value index: '))
        print(df[a:b])
        print()

    elif a==9:
        print('Breaking')
        print('Bye Bye')
        break


