import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from joblib import dump
# from sklearn.metrics import Accuracy_score

# load the dataset,
data = pd.read_csv('C:\\Users\\sarua\\OneDrive\\Desktop\\Data\\TitanicMLandFlaskDeployment-main\\TitanicMLandFlaskDeployment-main\\titanic.csv')

# apply one hot encoder to Sex,
encoder = OneHotEncoder( sparse_output=False,dtype=int)
data[['female' , 'male']]=encoder.fit_transform(data[['Sex']])

# drop null values for now,
data=data.dropna()

# separate dependent and independent variables,
X = data[['Pclass','Age','female','male']]
y = data['Survived']

# split the dataset into train and test variable:
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=0)

# built the model,
model = DecisionTreeClassifier()
model.fit(X_train,y_train)
# print(model.predict(X_test))

# extract and save the model in the form of joblib using dump method
dump(model,'demo_model.joblib')
print('successfully done all the mess')





