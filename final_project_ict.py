#Establishing Interface and importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



print('`Welcome To the Stock Market Analysis of OGDC of Pakistan ')
print('You can check for past 5 years history individually or can have an yearly analysis of 5-years in\
which you can check for its prices, Volumes, Moving Averages and some Future Predictions')
print('Please Give Detail What you would like to analyze (Yearly or Single Year)')
b = input('Enter valid option you want to see: ')
c=b.lower()





if c== 'yearly':
    #Start
    data_file = 'ict_project_stckyearly.xlsx'#file path 
    stock_data_yearly = pd.read_excel(data_file)#importing excel file
    print(stock_data_yearly.head(12))#printing excel file into python
    #Calculating the 5-month and 10-month moving averages
    stock_data_yearly['MA5'] = stock_data_yearly['Close'].rolling(window=5).mean()
    stock_data_yearly['MA10'] = stock_data_yearly['Close'].rolling(window=10).mean()
    #for prediction training module
    #Droping rows with missing values in the relevant columns
    stock_data_yearly.dropna(subset=['Close', 'MA5', 'MA10'], inplace=True)
    #Defining features (X) and target (y)
    p = stock_data_yearly[['MA5', 'MA10']]
    q = stock_data_yearly['Close']
    #spliting the data into training and testing sets
    p_train, p_test, q_train, q_test = train_test_split(p, q, test_size=1, shuffle=False)
    # Training the model
    model = LinearRegression()
    model.fit(p_train, q_train)
    #making predictions
    q_pred = model.predict(p_test)
    #taking Input From user for process
    print('What do you want for analysis i.e. Closingprice, Profits, Volume, Movingaverage and Prediction')
    a = input('Enter which analysis you want: ').lower()
    if a=="volume":
        print('Your Graph is plotted')
        # Plot the Volume over time
        plt.figure(figsize=(12, 10))
        plt.plot(stock_data_yearly['Volume'], label='OGDC yearly Volume 2020-2024', color='Green', marker='o')
        plt.title('OGDC Yearly Stock Volume Over Time')
        plt.xlabel('Duration 2020-2024')
        plt.ylabel('Volume (PKR) 210000000-470000000')
        plt.yticks([1,2,4],[210000000,300000000,470000000])
        plt.legend()
        plt.show()
    elif a=='profits':
        # Plot the opening price over time
        plt.figure(figsize=(12, 10))
        plt.plot(stock_data_yearly['Profits'], label='OGDC Yearly Profits 2020-2024', color='Black', marker='o')
        plt.title('OGDC Stock Profits Over Time')
        plt.xlabel('Duration 2020-2024')
        plt.ylabel('Price 80000000-225000000(PKR)')
        plt.legend()
        plt.show()
    elif a=='Closing price':
        # Plot the closing price over time
        plt.figure(figsize=(12, 10))
        plt.plot(stock_data_yearly['Close'], label='OGDC Closing Price 2020-2024', color='Orange', marker='o')
        plt.title('OGDC Stock Price Over Time')
        plt.xlabel('Duration 2020-2024')
        plt.ylabel('Price 79-230(PKR)')
        plt.legend()
        plt.show()
    elif a=='movingaverage':
        # Plot the closing price with moving averages
        plt.figure(figsize=(10, 6))
        plt.plot(stock_data_yearly['MA5'], label='1-year Moving Average', marker='o')
        plt.plot(stock_data_yearly['MA10'], label='2-year Moving Average', marker='*')
        plt.title('OGDC Stock Price with Moving Averages')
        plt.xlabel('Date (Increasing)')
        plt.ylabel('Price 80-230(PKR)')
        plt.legend()
        plt.show()
    elif a=='prediction':
        # Evaluate the model
        mse = mean_squared_error(q_test, q_pred)
        print(f'Mean Squared Error: {mse}')
        # Visualize the actual vs predicted prices
        plt.figure(figsize=(10, 6))
        plt.plot(q_test.index, q_test, label='Actual Price', marker='o')
        plt.plot(q_test.index, q_pred, label='Predicted Price', marker='o')
        plt.title('OGDC Stock Price Prediction after 2024')
        plt.xlabel('Time (Increasing)')
        plt.ylabel('Price 79-230(PKR)')
        plt.legend()
        plt.show()
    else:
        print('Invalid Input')



    
    
elif c== 'single year':
    print('For single year select which year you want to analyze from 2020-2024')
    s_year= input('Enter yera to analyze: ').lower()
    if s_year == '2020':
        #Start
        data_file = 'ict_project_stck20.xlsx'#file path 
        stock_data = pd.read_excel(data_file)#importing excel file
        print(stock_data.head(24))#printing excel file into python
        #Calculating the 5-month and 10-month moving averages
        stock_data['MA5'] = stock_data['Close'].rolling(window=5).mean()
        stock_data['MA10'] = stock_data['Close'].rolling(window=10).mean()
        #for prediction training module
        #Droping rows with missing values in the relevant columns
        stock_data.dropna(subset=['Close', 'MA5', 'MA10'], inplace=True)
        #Defining features (X) and target (y)
        X = stock_data[['MA5', 'MA10']]
        y = stock_data['Close']
        #spliting the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        # Training the model
        model = LinearRegression()
        model.fit(X_train, y_train)
        #making predictions
        y_pred = model.predict(X_test)
        #taking Input From user for process
        print('Please give details, What do you need to plot\
            (Volume , Closing price, Opening price, Moving average, Predict)')
        x= input('What you want to plot: ')
        if x=="Volume":
            print('Your Graph is plotted')
            # Plot the Volume over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Volume'], label='OGDC Volume 2020', color='Green', marker='o')
            plt.title('OGDC Stock Volume Over Time')
            plt.xlabel('Duration Jan2020-Dec2020')
            plt.ylabel('Volume (PKR) 450000-6500000')
            plt.yticks([1,2,4],[45000,3000000,6500000])
            plt.legend()
            plt.show()
        elif x=='Opening price':
            # Plot the opening price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Open'], label='OGDC Opening Price 2020', color='Black', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2020-Dec2020')
            plt.ylabel('Price 85-145(PKR)')
            plt.legend()
            plt.show()
        elif x=='Closing price':
            # Plot the closing price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Close'], label='OGDC Closing Price 2020', color='Orange', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2020-Dec2020')
            plt.ylabel('Price 85-145(PKR)')
            plt.legend()
            plt.show()
        elif x=='Moving average':
            # Plot the closing price with moving averages
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['MA5'], label='5 month Moving Average', marker='o')
            plt.plot(stock_data['MA10'], label='10 month Moving Average', marker='*')
            plt.title('OGDC Stock Price with Moving Averages')
            plt.xlabel('Date (Increasing)')
            plt.ylabel('Price 85-145(PKR)')
            plt.legend()
            plt.show()
        elif x=='Predict':
            # Evaluate the model
            mse = mean_squared_error(y_test, y_pred)
            print(f'Mean Squared Error: {mse}')
            # Visualize the actual vs predicted prices
            plt.figure(figsize=(10, 6))
            plt.plot(y_test.index, y_test, label='Actual Price', marker='o')
            plt.plot(y_test.index, y_pred, label='Predicted Price', marker='o')
            plt.title('OGDC Stock Price Prediction')
            plt.xlabel('Time (Increasing)')
            plt.ylabel('Price 85-145(PKR)')
            plt.legend()
            plt.show()
        else:
            print('Invalid Input')

    elif s_year == '2021':
        #Start
        data_file = 'ict_project_stck21.xlsx'#file path 
        stock_data = pd.read_excel(data_file)#importing excel file
        print(stock_data.head(24))#printing excel file into python
        #Calculating the 5-month and 10-month moving averages
        stock_data['MA5'] = stock_data['Close'].rolling(window=5).mean()
        stock_data['MA10'] = stock_data['Close'].rolling(window=10).mean()
        #for prediction training module
        #Droping rows with missing values in the relevant columns
        stock_data.dropna(subset=['Close', 'MA5', 'MA10'], inplace=True)
        #Defining features (X) and target (y)
        p = stock_data[['MA5', 'MA10']]
        q = stock_data['Close']
        #spliting the data into training and testing sets
        p_train, p_test, q_train, q_test = train_test_split(p, q, test_size=0.2, shuffle=False)
        # Training the model
        model = LinearRegression()
        model.fit(p_train, q_train)
        #making predictions
        q_pred = model.predict(p_test)
        #taking Input From user for process
        print('Please give details, What do you need to plot\
            (Volume , Closing price, Opening price, Moving average, Predict)')
        a= input('What you want to plot: ')
        if a=="Volume":
            print('Your Graph is plotted')
            # Plot the Volume over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Volume'], label='OGDC Volume 2021', color='Green', marker='o')
            plt.title('OGDC Stock Volume Over Time')
            plt.xlabel('Duration Jan2021-Dec2021')
            plt.ylabel('Volume (PKR) 800000-6000000')
            plt.yticks([1,2,4],[800000,3000000,6000000])
            plt.legend()
            plt.show()
        elif a=='Opening price':
            # Plot the opening price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Open'], label='OGDC Opening Price 2021', color='Black', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2021-Dec2021')
            plt.ylabel('Price 80-115(PKR)')
            plt.legend()
            plt.show()
        elif a=='Closing price':
            # Plot the closing price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data['Close'], label='OGDC Closing Price 2021', color='Orange', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2021-Dec2021')
            plt.ylabel('Price 81-114(PKR)')
            plt.legend()
            plt.show()
        elif a=='Moving average':
            # Plot the closing price with moving averages
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data['MA5'], label='5 month Moving Average', marker='o')
            plt.plot(stock_data['MA10'], label='10 month Moving Average', marker='*')
            plt.title('OGDC Stock Price with Moving Averages')
            plt.xlabel('Date (Increasing)')
            plt.ylabel('Price 80-115(PKR)')
            plt.legend()
            plt.show()
        elif a=='Predict':
            # Evaluate the model
            mse = mean_squared_error(q_test, q_pred)
            print(f'Mean Squared Error: {mse}')
            # Visualize the actual vs predicted prices
            plt.figure(figsize=(10, 6))
            plt.plot(q_test.index, q_test, label='Actual Price', marker='o')
            plt.plot(q_test.index, q_pred, label='Predicted Price', marker='o')
            plt.title('OGDC Stock Price Prediction after 2021')
            plt.xlabel('Time (Increasing)')
            plt.ylabel('Price 80-115(PKR)')
            plt.legend()
            plt.show()
        else:
            print('Invalid Input')
    elif s_year == '2023':
        #Start 2023 analysis
        data_file = 'ict_project_stck23.xlsx'#file path 
        stock_data23 = pd.read_excel(data_file)#importing excel file
        print(stock_data23.head(24))#printing excel file into python
        #Calculating the 5-month and 10-month moving averages
        stock_data23['MA5'] = stock_data23['Close'].rolling(window=5).mean()
        stock_data23['MA10'] = stock_data23['Close'].rolling(window=10).mean()
        #for prediction training module
        #Droping rows with missing values in the relevant columns
        stock_data23.dropna(subset=['Close', 'MA5', 'MA10'], inplace=True)
        #Defining features (X) and target (y)
        p = stock_data23[['MA5', 'MA10']]
        q = stock_data23['Close']
        #spliting the data into training and testing sets
        p_train, p_test, q_train, q_test = train_test_split(p, q, test_size=0.2, shuffle=False)
        # Training the model
        model = LinearRegression()
        model.fit(p_train, q_train)
        #making predictions
        q_pred = model.predict(p_test)
        #taking Input From user for process
        print('Please give details, What do you need to plot\
            (Volume , Closing price, Opening price, Moving average, Predict)')
        a= input('What you want to plot from 2023: ')
        if a=="Volume":
            print('Your Graph is plotted')
            # Plot the Volume over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data23['Volume'], label='OGDC Volume 2023', color='Green', marker='o')
            plt.title('OGDC Stock Volume Over Time')
            plt.xlabel('Duration Jan2023-Dec2023')
            plt.ylabel('Volume (PKR) 800000-23000000')
            plt.yticks([1,2,4],[800000,12000000,23000000])
            plt.legend()
            plt.show()
        elif a=='Opening price':
            # Plot the opening price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data23['Open'], label='OGDC Opening Price 2023', color='Black', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2023-Dec2023')
            plt.ylabel('Price 74-116(PKR)')
            plt.legend()
            plt.show()
        elif a=='Closing price':
            # Plot the closing price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data23['Close'], label='OGDC Closing Price 2023', color='Orange', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2023-Dec2023')
            plt.ylabel('Price 74-115(PKR)')
            plt.legend()
            plt.show()
        elif a=='Moving average':
            # Plot the closing price with moving averages
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data23['MA5'], label='5 month Moving Average', marker='o')
            plt.plot(stock_data23['MA10'], label='10 month Moving Average', marker='*')
            plt.title('OGDC Stock Price with Moving Averages')
            plt.xlabel('Date (Increasing)')
            plt.ylabel('Price 74-116(PKR)')
            plt.legend()
            plt.show()
        elif a=='Predict':
            # Evaluate the model
            mse = mean_squared_error(q_test, q_pred)
            print(f'Mean Squared Error: {mse}')
            # Visualize the actual vs predicted prices
            plt.figure(figsize=(10, 6))
            plt.plot(q_test.index, q_test, label='Actual Price', marker='o')
            plt.plot(q_test.index, q_pred, label='Predicted Price', marker='o')
            plt.title('OGDC Stock Price Prediction after 2023')
            plt.xlabel('Time (Increasing)')
            plt.ylabel('Price 74 onward(PKR)')
            plt.legend()
            plt.show()
        else:
            print('Invalid Input')
    elif s_year=='2024':
        #Start 2024 analysis
        data_file = 'ict_project_stck24.xlsx'#file path 
        stock_data24 = pd.read_excel(data_file)#importing excel file
        print(stock_data24.head(24))#printing excel file into python
        #Calculating the 5-month and 10-month moving averages
        stock_data24['MA5'] = stock_data24['Close'].rolling(window=5).mean()
        stock_data24['MA10'] = stock_data24['Close'].rolling(window=10).mean()
        #for prediction training module
        #Droping rows with missing values in the relevant columns
        stock_data24.dropna(subset=['Close', 'MA5', 'MA10'], inplace=True)
        #Defining features (X) and target (y)
        p = stock_data24[['MA5', 'MA10']]
        q = stock_data24['Close']
        #spliting the data into training and testing sets
        p_train, p_test, q_train, q_test = train_test_split(p, q, test_size=0.2, shuffle=False)
        # Training the model
        model = LinearRegression()
        model.fit(p_train, q_train)
        #making predictions
        q_pred = model.predict(p_test)
        #taking Input From user for process
        print('Please give details, What do you need to plot\
            (Volume , Closing price, Opening price, Moving average, Predict)')
        a= input('What you want to plot from 2024: ')
        if a=="Volume":
            print('Your Graph is plotted')
            # Plot the Volume over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data24['Volume'], label='OGDC Volume 2024', color='Green', marker='o')
            plt.title('OGDC Stock Volume Over Time')
            plt.xlabel('Duration Jan2024-Dec2024')
            plt.ylabel('Volume (PKR) 1230000-20000000')
            plt.yticks([1,2,4],[1230000,10000000,20000000])
            plt.legend()
            plt.show()
        elif a=='Opening price':
            # Plot the opening price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data24['Open'], label='OGDC Opening Price 2024', color='Black', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2024-Dec2024')
            plt.ylabel('Price 114-234(PKR)')
            plt.legend()
            plt.show()
        elif a=='Closing price':
            # Plot the closing price over time
            plt.figure(figsize=(12, 10))
            plt.plot(stock_data24['Close'], label='OGDC Closing Price 2024', color='Orange', marker='o')
            plt.title('OGDC Stock Price Over Time')
            plt.xlabel('Date  Jan2024-Dec2024')
            plt.ylabel('Price 114-233.4(PKR)')
            plt.legend()
            plt.show()
        elif a=='Moving average':
            # Plot the closing price with moving averages
            plt.figure(figsize=(10, 6))
            plt.plot(stock_data24['MA5'], label='5 month Moving Average', marker='o')
            plt.plot(stock_data24['MA10'], label='10 month Moving Average', marker='*')
            plt.title('OGDC Stock Price with Moving Averages')
            plt.xlabel('Date (Increasing)')
            plt.ylabel('Price 114-240(PKR)')
            plt.legend()
            plt.show()
        elif a=='Predict':
            # Evaluate the model
            mse = mean_squared_error(q_test, q_pred)
            print(f'Mean Squared Error: {mse}')
            # Visualize the actual vs predicted prices
            plt.figure(figsize=(10, 6))
            plt.plot(q_test.index, q_test, label='Actual Price', marker='o')
            plt.plot(q_test.index, q_pred, label='Predicted Price', marker='o')
            plt.title('OGDC Stock Price Prediction after 2024')
            plt.xlabel('Time (Increasing)')
            plt.ylabel('Price 115 onwards(PKR)')
            plt.legend()
            plt.show()
        else:
            print('Invalid Input')







    
   
else:
    print('Invalid Input, Restart Program')


