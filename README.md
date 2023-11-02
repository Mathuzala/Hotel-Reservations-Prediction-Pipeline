# Hotel-Reservations-Prediction-Pipeline
This project leverages the Random Forest Classifier to predict whether a customer will cancel a hotel booking based on a range of features such as lead time, room type, and number of guests aiming to reduce revenue loss due to cancellations and no-shows in online hotel booking channels.

## Hotel Booking Cancellation Prediction Pipeline

## Libraries Used
- pandas
- numpy
- matplotlib
- seaborn
- sklearn
- joblib
- sqlite3
- flask

## Motivation
The motivation for this project is to predict whether a customer will honor a hotel reservation or cancel it, given the increasing trend of cancellations and no-shows in online hotel booking channels. Cancellations can significantly impact hotels' revenue and operations.

## Files in the Repository
- `Hotel Reservations.csv` - The dataset used for the analysis and model training. It contains 36,275 entries with 19 columns, including features like the number of adults, children, weekend nights, week nights, meal plan, room type, lead time, and more. The target variable is 'booking_status'.
- `preprocess.py` This file contains the preprocessing functions used to clean and prepare the data for model training. It may include functions for handling missing values, encoding categorical variables, and normalizing numerical variables.
- `training.py` This file contains the code for training the machine learning model. It loads the preprocessed data, splits it into training and testing sets, trains the model, and evaluates its performance. The trained model is then saved for future use.
- `preprocessor.pkl` - The preprocessor file used to preprocess the data before feeding it into the machine learning model.
- `app4.py` - The Flask app file that is used to deploy the model as a web application.
- `requirements.txt` - The file containing the list of libraries and their versions required to run the project.
- `index.html` - The HTML file for the homepage of the web application.
- `script.js` - The JavaScript file used to add interactivity to the web application.
- `result.html` - The HTML file that displays the result of the hotel booking cancellation prediction.
- 'Hotel Reservations Project.ipynb - The Jupyter notebook contains the data analysis, visualization, and machine learning model development process for predicting hotel booking cancellations.
  
## Summary of Results
The project used different machine learning models to predict hotel booking cancellations. The Random Forest classifier achieved the highest accuracy of approximately 88.6% on the test data.

## Launching the Flask App
1. Install the necessary libraries listed in `requirements.txt` using the command `pip install -r requirements.txt`.
2. Navigate to the directory containing `app.py`.
3. Run the command `python app4.py` to start the Flask server.
4. Open a web browser and go to the URL provided by the Flask server (usually `http://127.0.0.1:5000/`).

## Acknowledgements
- Dataset: [Kaggle - Hotel Reservations Classification Dataset](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset/)
- Front-End to Flask App Contract: [Codepen - Front-End to Flask App](https://codepen.io/jaycbrf/pen/NWYjYr)
