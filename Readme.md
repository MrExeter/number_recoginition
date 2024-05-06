# Handwritten Digits Image Classifier
___
### This is a simple Image Classifier for handwritten digits from (0-9)

___
## Files: 

### Dockerfile
Docker file to build required Docker Container to run application.  This project was created using PyCharm <br/>
Python 3.11<br/>
Tensorflow 2.16 setup for GPU utilization

### trainer.py 
Downloads mnist dataset, defines model, train and test datasets.
### evaluator.py 
Loads the created and saved model from trainer.py, measures the accuracy and loss of the model 

### requirements.txt
Requirements & dependencies file,
___

### Building Container
I developed this using PyCharm, instructions on how to build the container from a dockerfile are available online<br/>
More information regarding installing and running with docker will be added in the future.


___
### Saving Model

This code saves the model to a '/models' folder under the filename 'mnist_handwritten_numbers.keras'.
Feel free to choose your own location and filename.
