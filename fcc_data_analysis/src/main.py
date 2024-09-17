import matplotlib
matplotlib.use('Qt5Agg')
import pandas as pd   # Set the backend to Qt5Agg for interactive environments
import numpy as np
import matplotlib.pyplot as plt
# pip install scipy


sales = pd.read_csv('../data/sales_data.csv',parse_dates=['Date'])
#print(sales.describe())
#print(sales['Cost'].describe())
#print(sales['Cost'].mean())


#plt.savefig('../data/cost_box.png') #para una foto de lo hecho


#DENSIDAD (curva gaus)
#sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde #requires install scipy
#den = sales['Unit_Cost'].plot(kind='density', figsize=(14,6)) # kde
#den.axvline(sales['Unit_Cost'].mean(), color='red')
#den.axvline(sales['Unit_Cost'].median(), color='green')



#HISTOGRAMA (barras)
#histo = sales['Unit_Cost'].plot(kind='hist',figsize=(14,6))
#histo.set_ylabel('Number of sales')
#histo.set_xlabel('Dollars')


#BOX (trading)
#sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))


#plt.show()


#sales['Age_Group'].value_counts() #cuenta cuantos hay de cada tipo, categorias de 1 columna

#TORTA CATEGORIAS
#sales['Age_Group'].value_counts().plot(kind='pie', figsize=(6,6)) #grafico de torta

#BARRAS CATEGORIAS
##barras = sales['Age_Group'].value_counts().plot(kind='bar', figsize=(14,6)) #grafico de torta
#barras.set_ylabel('Number of sales')
#plt.show()

#correlacion CUADRITOS
numeric_sales = sales.select_dtypes(include=[np.number]) #solo numericos
corr = numeric_sales.corr() 
#print(corr)
#GRAFICO CUADRITOS  #correlation dbe ser numerica
"""
fig = plt.figure(figsize=(8,8))
plt.matshow(corr, cmap='RdBu', fignum=fig.number)
plt.xticks(range(len(corr.columns)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr.columns)), corr.columns)
#plt.show()
"""
# azul es correlacion muy alta



#PUNTITOS
#sales.plot(kind='scatter', x='Customer_Age', y='Revenue', figsize=(6,6))
#sales.plot(kind='scatter', x='Revenue', y='Profit', figsize=(6,6))  



# BARRITAS TRADING VERTICAL
#ax = sales[['Profit', 'Age_Group']].boxplot(by='Age_Group', figsize=(10,6))
#ax.set_ylabel('Profit')

plt.show()


# TRADING 6 cuadritps
boxplot_cols = ['Year', 'Customer_Age', 'Order_Quantity', 'Unit_Cost', 'Unit_Price', 'Profit']

#sales[boxplot_cols].plot(kind='box', subplots=True, layout=(2,3), figsize=(14,8))
plt.show()


# calcular nueva columna

sales['Revenue_per_Age'] = sales['Revenue'] / sales['Customer_Age']

print(sales['Revenue_per_Age'].head())



#LINEA GAUS
#sales['Revenue_per_Age'].plot(kind='density', figsize=(14,6))
#plt.show()

ken = sales.loc[sales['State'] == 'Kentucky'] #filtrar todo solo en kentuky
print(ken.head())