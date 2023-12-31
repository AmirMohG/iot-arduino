# Import Relevant libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import csv
from datetime import datetime
from flask import Flask, request, render_template   
app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/ai", methods=["GET"])
def greet():
    value = float(request.args.get("value"))
    if value:
        x_test = [value]

        y_test = model.predict(x_test)

        return f"{y_test[0]}"
    else:
        return "value parameter required"




# Define the file path
file_path = "new_dataset.txt"

# Create an empty list to store the data objects
data_objects = []
x_train = []
y_train = []

with open(file_path, "r") as file:
    # Create a CSV reader object
    reader = csv.reader(file, delimiter=";")

    # Skip the header row
    next(reader)

    # Iterate over each row in the file
    for row in reader:
        # Extract date and time strings from the row
        date_str = row[0]
        time_str = row[1]

        # Convert date string to datetime object
        date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()

        # Convert time string to datetime object
        time_obj = datetime.strptime(time_str, "%H:%M:%S").time()

        # Create a data object
        data = {
            "Date": date_obj,
            "Time": time_obj,
            "Global_active_power": float(row[2]),
            "Global_reactive_power": float(row[3]),
            "Voltage": float(row[4]),
            "Global_intensity": float(row[5]),
            "Sub_metering_1": float(row[6]),
            "Sub_metering_2": float(row[7]),
            "Sub_metering_3": float(row[8])
        }

        # Append the data object to the list
        data_objects.append(data)

for data in data_objects:
    # Extract the 'Time' and 'Global_active_power' values
    date = data['Date']
    time = data['Time']

    Global_active_power = data['Global_active_power']

    # if (date.year == 2010) and (date.month == 1) and (date.day == 25) and (time.minute == 0):
    float_value = time.hour + (time.minute / 60)
    x_train.append(float_value)
    y_train.append(Global_active_power)



print(x_train)

# Learning rate
learning_rate = 0.1

# Number of loops for training through all your data to update the parameters
training_epochs = 100



# declare weights


weight = tf.Variable(0.)
bias = tf.Variable(0.)



###### Maghz
# # Define linear regression expression y
# def linreg(x):
#     y = weight*x + bias
#     return y

# def squared_error(y_pred, y_true):
#     return tf.reduce_mean(tf.square(y_pred - y_true))
# # train model
# for epoch in range(training_epochs):

# # Compute loss within Gradient Tape context
#     with tf.GradientTape() as tape:
#         y_predicted = linreg(x_train)
#         loss = squared_error(y_predicted, y_train)
    
# # Get gradients
# gradients = tape.gradient(loss, [weight,bias])

# # Adjust weights
# weight.assign_sub(gradients[0]*learning_rate)
# bias.assign_sub(gradients[1]*learning_rate)

# # Print output
# print(f"Epoch count {epoch}: Loss value: {loss.numpy()}")

# plt.scatter(x_train, y_train)
# plt.xlabel('Time')
# plt.ylabel('Global Active Power')
# plt.title('Global Active Power vs. Time')
# plt.plot(x_train, linreg(x_train), 'r')
# plt.show()

######


##### New maghz
# Define your neural network model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1)
])


# Compile the model (optional)
model.compile(loss='mae', optimizer='adam')

model.fit(x_train, y_train, epochs=15, batch_size=32)

# Generate a plot of the neural network architecture
tf.keras.utils.plot_model(model, to_file='neural_network.png', show_shapes=True)

fig = plt.figure()

plt.scatter(x_train, y_train)

################### Plot
def predictAndDraw(i):

    x_out = []
    y_out = []
    x_test = [i/41]
    x_test = [float(input(""))]
    print(type(x_test[0]))
    y_test = model.predict(x_test)
    
    print(y_test)

    x_out.append(x_test)
    y_out.append(y_test)
    plt.scatter(x_out, y_out, color='red')

# def animate():
#     for i in range(0, 2400, 1):
#         predictAndDraw(i)
        



ani = animation.FuncAnimation(fig ,predictAndDraw, interval=3, frames=1000)

plt.xlabel('Time')
plt.ylabel('Global Active Power')
plt.title('Global Active Power vs. Time')
plt.draw()
plt.show()

###################


####


# if __name__ == "__main__":
#     app.run()