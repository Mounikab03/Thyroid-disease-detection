
from flask import Flask, request, jsonify
import traceback  
import numpy as np
import joblib
import os
from sklearn.impute import SimpleImputer
import numpy as np
app = Flask(__name__)

# Loading pre-trained model
model_path = os.path.join(os.path.dirname(__file__), '../models/hyper_model1.pkl')
model = joblib.load(model_path)

EXPECTED_FEATURES = 21

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        input_data = request.json.get('input_data')

        if input_data is None:
            return jsonify({'error': 'Missing input_data'}), 400

        input_array = np.array(input_data).reshape(1, -1)

        prediction = model.predict(input_array)[0]

        return jsonify({
            'prediction': int(prediction),
            'message': 'Prediction successful'
        })
    except Exception as e:
        print("Prediction error:", e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)