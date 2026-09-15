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
