NOTE: Ignore the errors and run the exact code to get the result


Crop disease detection is a deep learning project where it detects the disease of the crop. In this project i've used a CNN-VGGI9 algorithm to train the model and by using this algorithm i've achieved an accuracy of 98.4% which means the model is trained well. Along with that i've used Django (A popular python framework) to integrate the frontend of the project where it consists an input and and submit button whenever an user gives an image of a diseased crop and clicks on the submit button then our model starts running at the backend and gives the result as the name of the disease. 


You can get the dataset from the kaggle, Roboflow and some other sources.

DJANGO Files
settings.py, urls.py, and views.py are the files which are present in django environment. once you create a virtual environment and install django there, these files are generated and we have to make changes which are necessary for our code.

model.py is a python code in django environment where it consists of the class names of your dataset in the form list.


templates is a folder where it consists of frontend and designing part of the model.

