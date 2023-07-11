import streamlit as st
from pandas.plotting import scatter_matrix

from sklearn import datasets
import pandas as pd

st.title("Here is your data:")

st.write("The following data is derived from the Iris dataset. It is a Pandas Dataframe, with the columns being the different characteristics of the flowers.")

# Load dataset
iris = datasets.load_iris()

#create a Pandas DataFrame to store the data from the Iris dataset
# the iris.data array is the data rows
# the iris.feature_names list are the column names

X = pd.DataFrame(iris.data, columns = iris.feature_names)
Y = pd.Series(iris.target, name = 'class')

# st.write(Y)

df = pd.concat([X,Y], axis=1)

df['class'] = df['class'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

st.write(df)




# # Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
# names = ["sepal-length", "sepal-width", "petal-length", "petal-width", "class"] #column names #attributes
# dataset = read_csv(url, names=names)

# # box and whisker plots
# dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# pyplot.show()

# # histograms
# dataset.hist()
# pyplot.show()

# # scatter plot matrix
# scatter_matrix(dataset)
# pyplot.show()