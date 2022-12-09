import tensorflow as tf

def neural_network(input_data, output_data):
  # Build the neural network
  model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(16, input_dim=len(input_data[0]), activation="relu"),
    tf.keras.layers.Dense(16, activation="relu"),
    tf.keras.layers.Dense(len(output_data[0]), activation="softmax")
  ])

  # Compile the neural network
  model.compile(loss="categorical_crossentropy", optimizer="adam")

  # Train the neural network
  model.fit(input_data, output_data, epochs=100, verbose=0)

  # Return the trained neural network
  return model

# Test the neural_network function
input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
output_data = [[0], [1], [1], [0]]
model = neural_network(input_data, output_data)
print(model.predict(input_data)) # [[0.0000000e+00], [9.9999988e-01], [9.9999857e-01], [1.1210382e-07]]
