from flask import Flask, request
import tensorflow as tf

app = Flask(__name__)

model = tf.keras.models.load_model('model.h5')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.get_json()
    predictions = model.predict(input_data)
    return predictions.tolist()

if __name__ == '__main__':
    app.run(debug=True)
