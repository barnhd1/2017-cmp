import numpy as np  
import matplotlib.pyplot as plt  
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data"

names = ['Quality','Maintenance','Doors','People','Trunk Size','Safety','Rating']

dataset = pd.read_csv(url, names = names)



dataset["Quality"] = dataset["Quality"].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3})
dataset["Maintenance"] = dataset["Maintenance"].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3})
dataset["Doors"] = dataset["Doors"].map({'2': 2, '3': 3, '4': 4, '5more': 0})
dataset["People"] = dataset["People"].map({'2':2, '3': 3, '4': 4, 'more': 0})
dataset["Trunk Size"] = dataset["Trunk Size"].map({'small': 0, 'med': 1, 'big': 2})
dataset["Safety"] = dataset["Safety"].map({'high': 0, 'med': 1, 'low': 2})
dataset["Rating"] = dataset["Rating"].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3})


X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,6].values





X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)


classifier = KNeighborsClassifier(n_neighbors=5)

#print(dataset)

classifier.fit(X_train, Y_train)



y_predicted = classifier.predict(X_test)

#test the accuracy
accuracy = np.mean(Y_test == y_predicted) *100
print("The accuracy is {0:.1f}%".format(accuracy))




scores = cross_val_score(classifier, X, Y, scoring = 'accuracy')
average_accuracy = np.mean(scores)*100
print("The accuracy is {0:.1f}%".format(average_accuracy))
