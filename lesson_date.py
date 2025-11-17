import pandas as pd

# months = ['Jan', 'Feb', 'Mar', 'Apr']
# sales = {
#     'revenue': [100, 200, 300, 400],
#     'items_sold': [23, 43, 54, 65],
#     'new_clients': [10, 20, 30, 40]
# }

# df = pd.DataFrame(data=sales, index=months)
# print(df)

# vector = [1, 2, 3]
# print(vector * 2)

# series_str = pd.Series(['a', 'b', 'c'])
# print(series_str[0])

# months = ['Jan', 'Feb', 'Mar', 'Apr']
# sales = [100, 200, 300, 400]
# data = pd.Series(data=sales, index=months)
# print(data)
# print(data['Feb'])

# print(df.head(2)) # виводить за замовчуванням ПЕРШІ 5 рядків() 
# print(df.tail(1)) # виводить за замовчуванням ОСТАННІ 5 рядків()

# print(df.revenue) # виводить необхідний стовпчик

# print(df.info())
# print(df.shape) #(row, colum)
# print(df.columns)
# print(df.describe())
# print(df.dtypes)

# df.revenue = ['100a', '200', '300', '400']
# print(df)
# print(df.revenue.dtypes)
# df.revenue = pd.to_numeric(df.revenue, errors='coerce')
# # print(df.describe())
# print(df.revenue.dtypes)

# print(df.loc[['Feb', 'Apr']]) #вписувати ключі в подвійних дужках [[]]


movies_df = pd.read_csv('data/movies_metadata.csv')
# print(movies_df.to_string())

pd.options.display.max_rows = 10
print(pd.options.display.max_rows)