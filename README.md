# 🌱 Crop Disease Detection & Precaution Management

**🔍 Project Overview**

Crop Disease Detection and Precaution Management is a deep learning-based project that identifies crop diseases using a CNN-VGG19 model. The model achieves an impressive 98.4% accuracy, ensuring reliable disease classification. The project integrates a Django web application, allowing users to upload images of diseased crops and receive instant disease predictions along with recommended precautions.

**🚀 Key Features**

Deep Learning Model: Trained using CNN-VGG19, achieving 98.4% accuracy.

Django Integration: User-friendly web interface for disease detection.

Automated Precaution Suggestions: Each detected disease is mapped to a set of precautions using label.json.

Dataset Sources: Kaggle, Roboflow, and other open datasets.

**Folder Structure**

📂 Crop-Disease-Detection
│── 📂 dataset/                 # Dataset used for training

│── 📂 models/                  # Trained model and related files

│── 📂 django_project/           # Django project directory

│   │── 📂 templates/            # Frontend files (HTML, CSS)

│   │── settings.py              # Django settings file

│   │── urls.py                  # URL routing configuration

│   │── views.py                 # Logic for handling requests

│   │── model.py                 # Class names and model integration

│── label.json                   # Precaution details for each disease

│── requirements.txt              # Required dependencies

│── README.md                     # Project documentation (this file)

**Use the Web App**

Upload an image of a diseased crop.

Click the Submit button.

The model will predict the disease and display precautionary measures.

**The Dataset Evaluation:**

![output2](https://github.com/user-attachments/assets/c313d72e-5624-4e70-aa4c-7637aa6e8c8d)

**Sample Test 1:-**

![web](https://github.com/user-attachments/assets/c483e452-5327-42d8-ace0-ac8ab7eae5c5)

**Sample Test 2:-**

![web1](https://github.com/user-attachments/assets/10b334a6-cce8-470f-9255-a43c5de8757d)

**Results**

![web2](https://github.com/user-attachments/assets/7decec72-2aae-4d26-943b-ec65a232252b)

**📌 Notes**

Ensure the folder structure is maintained as it plays a crucial role in project execution.

Run the code as is, ignoring minor errors, to get the desired results.

The Django files (settings.py, urls.py, views.py) are auto-generated when Django is installed in a virtual environment.

**🏆 Results**

98.4% accuracy achieved with CNN-VGG19.

Efficient disease classification with real-time predictions.

**💬 Want to Collaborate?**

Feel free to fork the repo, submit PRs, and give your feedback! 🔥💡

**📜 License**

This project is open-source under the MIT License. Feel free to use and
modify it! 🚀

