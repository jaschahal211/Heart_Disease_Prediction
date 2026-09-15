# Heart Disease Risk Prediction System

A Python-based machine learning application that predicts the likelihood of heart disease from structured patient health data. The project combines machine learning models, data processing, a desktop GUI, and database integration into an end-to-end prediction workflow.

## Overview

The system accepts patient health parameters as input, processes the data, and generates a heart disease prediction using trained machine learning models. An interactive Tkinter-based interface provides a user-friendly way to enter patient information and view prediction results.

The project demonstrates a complete machine learning application workflow, from dataset handling and preprocessing to model training, evaluation, prediction, GUI integration, and database connectivity.

## Key Features

- Machine learning-based heart disease risk prediction
- Structured patient data processing
- Data preprocessing and feature preparation
- Classification using Random Forest and K-Nearest Neighbors (KNN)
- Interactive Tkinter desktop interface
- Real-time prediction based on user-provided inputs
- MySQL database integration
- Patient information management
- Appointment-related data management
- Modular Python-based application components
- CSV-based dataset for model development

## Technology Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Tkinter
- MySQL
- CSV
- Git
- GitHub

## Machine Learning Models

### Random Forest

Random Forest is implemented as one of the classification approaches for predicting heart disease. It combines multiple decision trees to generate a classification result and is suitable for handling structured tabular data.

### K-Nearest Neighbors (KNN)

KNN is implemented as an additional classification approach. It generates predictions based on the similarity between a patient's input features and neighboring observations in the dataset.

## Machine Learning Workflow

```text
              Heart Disease Dataset
                       |
                       v
              Data Preprocessing
                       |
                       v
               Feature Preparation
                       |
                       v
                Model Training
                       |
             +---------+---------+
             |                   |
             v                   v
       Random Forest            KNN
             |                   |
             +---------+---------+
                       |
                       v
                  Prediction
                       |
                       v
                Tkinter GUI
                       |
                       v
                 User Result


Application Architecture
                 +----------------------+
                 |     Tkinter GUI      |
                 |   User Input Layer   |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |    Data Processing   |
                 |   & Feature Handling |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   Machine Learning   |
                 |   Prediction Models  |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |   Prediction Result  |
                 +----------+-----------+
                            |
                            v
                 +----------------------+
                 |    MySQL Database    |
                 |   Data Management    |
                 +----------------------+
Project Workflow
Load the structured heart disease dataset.
Prepare and preprocess the input data.
Select and prepare relevant features for model training.
Train classification models using the prepared dataset.
Evaluate the trained models.
Accept patient health parameters through the Tkinter interface.
Pass the processed input to the prediction model.
Generate and display the corresponding prediction.
Use database components for persistent application data management.
Project Structure
Heart_Disease_Prediction/
│
├── main.py
├── backend.py
├── randomforestback.py
├── knnback.py
├── MySQL.py
├── loginform.py
├── info.py
├── report.py
├── heart.csv
├── datasheet.txt
├── appointments.db
├── appointments.txt
├── requirements.txt
├── images/
└── README.md
Database Integration

The application includes database components for persistent data management.

MySQL connectivity is implemented through Python components, allowing the application to interact with structured database records.

The project also contains application components related to patient information and appointment management.

GUI

The application uses Tkinter to provide an interactive desktop interface.

The interface allows users to:

Enter required patient information
Submit health parameters for prediction
View prediction results
Interact with application modules
Manage relevant patient and appointment information
Dataset

The project uses a structured heart disease dataset stored in:

heart.csv

The dataset is used for data preparation, model training, evaluation, and prediction.

Installation
1. Clone the Repository
git clone https://github.com/jaschahal211/Heart_Disease_Prediction.git
2. Navigate to the Project
cd Heart_Disease_Prediction
3. Create a Virtual Environment
python -m venv venv
4. Activate the Environment
Windows
venv\Scripts\activate
macOS / Linux
source venv/bin/activate
5. Install Dependencies
pip install -r requirements.txt
6. Run the Application
python main.py
Requirements

The project dependencies are listed in:

requirements.txt

Install them using:

pip install -r requirements.txt
Development Highlights
Implemented an end-to-end machine learning prediction workflow.
Integrated trained classification models with a desktop application.
Connected Python application components with MySQL for persistent data handling.
Structured the application into separate backend, model, GUI, and database components.
Used Git and GitHub for source-code management and project versioning.
Future Improvements
Add comprehensive model comparison using accuracy, precision, recall, and F1-score.
Improve input validation and exception handling.
Add automated unit and integration tests.
Develop a web-based version of the application.
Expose the prediction model through REST APIs.
Containerize the application using Docker.
Add model versioning and experiment tracking.
Deploy the prediction service to a cloud environment.
Disclaimer

This project is intended for educational and software-development purposes. It demonstrates machine learning, application development, and database integration concepts and should not be used as a substitute for professional medical diagnosis or advice.
