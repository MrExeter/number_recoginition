# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory in the container
WORKDIR /app

# Install OpenGL libraries needed for OpenCV
RUN apt-get update && apt-get install -y libgl1-mesa-dev

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code
COPY . /app

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
