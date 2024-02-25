# Iris-Species-classification

## Dataset Description
The Iris Flower dataset is a classic dataset in the field of machine learning. It contains measurements of various attributes of three different species of iris flowers: setosa, versicolor, and virginica. The attributes include sepal length, sepal width, petal length, and petal width.

## Iris Flower Categories
![Iris Categories](https://github.com/Nikhil7787/Iris-Species-classification/assets/123885552/65532b3d-2284-4e74-8456-abe08183f865)
<br>
<img src="https://github.com/Nikhil7787/Iris-Species-classification/assets/123885552/f43e5812-8ee0-4d4f-a2a7-202648352ff8" alt="image" width="400"/>
<br>

## Model Building Process

### To build the predictive model for iris flower species classification, the following steps were followed: </br>


1.	Data Exploration: Exploratory Data Analysis (EDA) was performed to understand the structure and characteristics of the dataset. This included summary statistics, data visualization, and handling missing values if any. </br>
2.	Data Preprocessing: Data preprocessing steps such as splitting the dataset into training and testing sets were carried out. </br>
3.	Model Selection: Various machine learning algorithms were considered and evaluated for their performance on the dataset. The algorithm with the highest accuracy was selected for further tuning. </br>
4.	Model Training and Evaluation: The selected model was trained on the training dataset and evaluated using appropriate evaluation metrics.</br>
5.	Model Persistence: Once the optimal model was obtained, it was saved using the pickle library to a file for future use. </br>



## Flask App for Model Deployment

A Flask web application was developed to deploy the trained model for iris flower species prediction. The app provides a basic form where users can input sepal and petal measurements, and the model predicts the species of the iris flower based on the input. <br>

## Running the Flask App Locally
### To run the Flask app locally on your system, follow these steps:

1. Clone the Repository:
```
git clone https://github.com/Nikhil7787/Iris-Species-classification.git

```
2. Navigate to the Repository Directory:
```
cd Iris-Species-classification
```
3. Install Dependencies:
```
pip install -r requirements.txt
```
4. Run the Flask App:
```
python model.py
```
5. Access the App: </br>
Open a web browser and go to http://localhost:5000 to access the Flask app.

## Localhost Page Demo
![image](https://github.com/Nikhil7787/Iris-Species-classification/assets/123885552/6b434abf-7abf-44c8-abb1-1fb382d7e077)



## License

This project is licensed under the MIT License - see the LICENSE file for details.







