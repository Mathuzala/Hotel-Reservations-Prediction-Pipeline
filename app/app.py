import joblib
import pandas as pd
from flask import Flask, render_template
from flask import Flask, request, jsonify
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from flask import Flask, render_template, request, redirect, url_for

print("Flask app started")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Load the model and preprocessor
model = joblib.load('model.pkl')
preprocessor = joblib.load('preprocessor.pkl')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print("Data received from form:", data)  # Add this line
        result = predict(data)
        return render_template('result.html', result=result)

def predict(data):
    # Clean the data
    data.pop('Booking_ID', None)
    data.pop('no_of_previous_bookings_not_canceled', None)
    data.pop('no_of_previous_cancellations', None)
    
    # Specify the order of the features as they appear in the form
    feature_order = [
        'no_of_adults',
        'no_of_children',
        'no_of_weekend_nights',
        'no_of_week_nights',
        'type_of_meal_plan',
        'required_car_parking_space',
        'room_type_reserved',
        'lead_time',
        'arrival_year',
        'arrival_month',
        'arrival_date',
        'market_segment_type',
        'repeated_guest',
        'avg_price_per_room',
        'no_of_special_requests',
    ]
    
    # Extract the features from the data in the specified order
    features = [data.get(feature) for feature in feature_order]

    print("Features after extraction:", features)

    # Convert features to the format expected by the model
    print(features)
    features = [float(feature) if isinstance(feature, str) and feature.replace('.', '', 1).isdigit() else feature for feature in features]

    # Convert features to a DataFrame
    features_df = pd.DataFrame([features], columns=feature_order)
    print("Columns of DataFrame:", features_df.columns)

    
    # Preprocess the features
    features = preprocessor.transform(features_df)
    
    # Make prediction
    prediction = model.predict(features)
    
    # Convert prediction to response format
    response = prediction.tolist()[0]
    
    return response

if __name__ == '__main__':
    app.run(debug=True)