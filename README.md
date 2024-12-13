The "Titanic Passenger Survival System" is an ML-based project designed to predict whether passengers on the Titanic survived or not.
The focus is on deploying the machine learning model using Flask for backend functionality, with HTML and CSS for the user interface.

Key Features:

Dataset: The Titanic dataset is used with basic preprocessing techniques, specifically one-hot encoding, to handle categorical variables.
Model: A Decision Tree Classifier is trained to make survival predictions.
Model Handling: The trained model is saved and extracted using the joblib library, ensuring efficient storage and loading.

Flask Concepts Explored:

Secret Key: Ensures security by signing session cookies and protecting data.
Flash Module: Provides a mechanism to display temporary messages, such as alerts or notifications, to users.
Request Module: Enables handling of HTTP requests, including accessing form data and query parameters.
