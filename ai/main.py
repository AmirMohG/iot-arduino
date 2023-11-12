# Import Relevant libraries
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import csv
from datetime import datetime



# Define linear regression expression y
def linreg(x):
    y = weight*x + bias
    return y

def squared_error(y_pred, y_true):
    return tf.reduce_mean(tf.square(y_pred - y_true))


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

    global_active_power = data['Global_active_power']
    if (date.year == 2010):
    # if (date.year == 2010) and (date.month == 1) and (date.day == 25) and (time.minute == 0):
        float_value = time.hour + (time.minute / 60)
        x_train.append(float_value)
        y_train.append(global_active_power)


print(x_train)

# Learning rate
learning_rate = 0.01

# Number of loops for training through all your data to update the parameters
training_epochs = 100



# declare weights
weight = tf.Variable(0.)
bias = tf.Variable(0.)


# train model
for epoch in range(training_epochs):

# Compute loss within Gradient Tape context
    with tf.GradientTape() as tape:
        y_predicted = linreg(x_train)
        loss = squared_error(y_predicted, y_train)
    
# Get gradients
gradients = tape.gradient(loss, [weight,bias])

# Adjust weights
weight.assign_sub(gradients[0]*learning_rate)
bias.assign_sub(gradients[1]*learning_rate)

# Print output
print(f"Epoch count {epoch}: Loss value: {loss.numpy()}")



plt.scatter(x_train, y_train)
plt.xlabel('Time')
plt.ylabel('Global Active Power')
plt.title('Global Active Power vs. Time')
plt.plot(x_train, linreg(x_train), 'r')
plt.show()

