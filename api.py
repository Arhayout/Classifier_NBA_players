
import numpy as np
from flask import Flask, jsonify, request
import pickle



app = Flask(__name__)

# Load the trained model

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data as a dictionary
    data = request.get_json(force=True)

    # Transform the data into a numpy array
    data_arr = np.array([data['GP'], data['MIN'], data['PTS'], data['FGM'], data['FGA'], data['FG%'], data['3P Made'], data['3PA'], data['3P%'], data['FTM'], data['FTA'], data['FT%'], data['OREB'], data['DREB'], data['REB'], data['AST'], data['STL'], data['BLK'], data['TOV']]).reshape(1, -1)

    # Make a prediction
    prediction = model.predict(data_arr)

    # Convert the prediction to a boolean value
    prediction = bool(prediction[0])

    # Return the prediction as a JSON response
    return jsonify(prediction=prediction)

if __name__ == "__main__":
     app.run(debug=True ,port=8082,use_reloader=False)



