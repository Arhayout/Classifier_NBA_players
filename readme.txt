This repository contains three Python scripts to analyze and train machine learning models using NBA players statistics from the 'nba_logreg.csv' dataset, and deploy a Flask API to predict if a player will last 5 years in the NBA based on his statistics.

nba_classifier.py
This script performs a random 3-fold cross-validation to evaluate the performance of several classifiers, such as Support Vector Machine, Random Forest, Logistic Regression and K-Nearest Neighbors. The best performing classifier is then saved as a pickle file named 'model.pkl' in the same directory.(We can choose between more than these classifiers)

api.py
This script loads the trained model from the 'model.pkl' file, and defines a Flask API endpoint '/predict'. When a POST request is received containing a JSON object with the player statistics, the script uses the trained model to predict if the player will last 5 years in the NBA, and returns the prediction as a JSON response.

nba_predictor.py
This script sends a POST request to the '/predict' endpoint of the Flask API defined in the 'api.py' script. It contains an example of a JSON object with player statistics used for prediction.

To run the application, follow these steps:

Run the 'nba_classifier.py' script to train the classifiers and save the best one in the 'model.pkl' file.
Run the 'api.py' script to deploy the Flask API and start listening for requests.
In another terminal, run the 'nba_predictor.py' script to send a POST request to the Flask API and receive the prediction as a JSON response
