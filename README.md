# Water Potability Prediction Using Machine Learning

## 🌐 Project Links

- 🚀 **Live Demo:** 👉 [Try the Water Potability Prediction App](https://water-potability-prediction-ml-vr3z64jw5yq6spmyye2ra7.streamlit.app/)
- 💻 **Source Code:** [GitHub Repository](https://github.com/kibromhailu11/water-potability-prediction-ml)
An interactive web application that predicts whether water is potable or not potable based on water-quality measurements.

## 📌 Project Overview

This project uses machine learning classification models to predict water potability from nine water-quality features.

...

The problem is treated as a **binary classification problem**, where:

* `0` = Not Potable
* `1` = Potable

Several machine learning classification algorithms were trained and compared using multiple evaluation metrics. The **Decision Tree** was selected as the final model because it achieved the highest **F1 Score** among the evaluated models.

The trained model and preprocessing components were saved for future predictions and deployment.

---

## 🎯 Project Objective

The main objective of this project is to develop a machine learning model that can classify water samples as potable or not potable based on their chemical and physical properties.

The project follows a complete machine learning workflow:

1. Load the dataset
2. Explore the data
3. Clean and preprocess the data
4. Visualize the data
5. Prepare features and target
6. Split the data into training and testing sets
7. Handle missing values
8. Scale features where required
9. Train multiple machine learning models
10. Compare model performance
11. Tune SVM hyperparameters
12. Evaluate the final model
13. Analyze feature importance
14. Save the trained model
15. Test the model with new water samples
16. Prepare the model for deployment

---

## 📊 Dataset

The dataset contains water-quality measurements and a target variable called `Potability`.

### Features

The model uses the following 9 input features:

| Feature           | Description                   |
| ----------------- | ----------------------------- |
| `ph`              | pH value of the water         |
| `Hardness`        | Hardness of the water         |
| `Solids`          | Total dissolved solids        |
| `Chloramines`     | Chloramines concentration     |
| `Sulfate`         | Sulfate concentration         |
| `Conductivity`    | Electrical conductivity       |
| `Organic_carbon`  | Organic carbon concentration  |
| `Trihalomethanes` | Trihalomethanes concentration |
| `Turbidity`       | Turbidity of the water        |

### Target Variable

The target variable is:

`Potability`

* `0` → Not Potable
* `1` → Potable

---

## 🔍 Exploratory Data Analysis

The dataset was explored before model training.

The analysis included:

* Dataset information
* Statistical summary
* Missing-value analysis
* Duplicate-value checking
* Target distribution
* Feature distributions
* Histograms
* Boxplots
* Correlation matrix
* Correlation heatmap

These analyses were used to understand the characteristics and distribution of the water-quality data.

---

## 🧹 Data Preprocessing

Several preprocessing steps were applied.

### 1. Data Type Conversion

The `ph` column was converted to numeric values. Invalid values were converted to missing values (`NaN`).

### 2. Duplicate Removal

Duplicate rows were removed from the dataset.

### 3. Missing-Value Handling

Missing values were handled using `SimpleImputer` with the **median strategy**.

The imputer was fitted using the training data and then applied to the test data.

### 4. Feature Scaling

`StandardScaler` was used for models that benefit from feature scaling:

* Logistic Regression
* Support Vector Machine (SVM)

Tree-based models were trained using the imputed but unscaled data.

### 5. Train/Test Split

The dataset was divided into:

* **80% training data**
* **20% testing data**

The split used:

```text
random_state=42
stratify=y
```

This helps maintain the target-class distribution between the training and testing sets.

---

## 🤖 Machine Learning Models

The following models were trained and evaluated:

### 1. Logistic Regression

A linear classification model used as one of the baseline models.

### 2. Decision Tree

A tree-based classification algorithm that makes predictions using decision rules based on feature values.

### 3. Random Forest

An ensemble of multiple decision trees used to improve prediction performance and generalization.

### 4. Support Vector Machine (SVM)

An SVM with an RBF kernel was trained using scaled features.

### 5. XGBoost

A gradient-boosting algorithm based on an ensemble of decision trees.

### 6. Tuned SVM

Grid Search with 5-fold cross-validation was used to search for better SVM hyperparameters.

The parameters tested included:

* `C`: 0.1, 1, 10, 100
* `gamma`: scale, 0.01, 0.1, 1
* `kernel`: RBF

The tuning process used **F1 Score** as the optimization metric.

---

## 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix
* ROC Curve

### Model Comparison

| Model               |   Accuracy |  Precision | Recall |   F1 Score |    ROC-AUC |
| ------------------- | ---------: | ---------: | -----: | ---------: | ---------: |
| Logistic Regression |     0.6098 |     0.0000 | 0.0000 |     0.0000 |     0.5481 |
| Decision Tree       |     0.5960 |     0.4813 | 0.4531 | **0.4668** |     0.5703 |
| Random Forest       |     0.6631 |     0.6446 | 0.3047 |     0.4138 |     0.6411 |
| Original SVM        | **0.6707** | **0.7041** | 0.2695 |     0.3898 |     0.6487 |
| Tuned SVM           |     0.6387 |     0.5576 | 0.3594 |     0.4371 |     0.6303 |
| XGBoost             |     0.6601 |     0.6435 | 0.2891 |     0.3989 | **0.6592** |

### Best Results

**Best F1 Score**

* Model: **Decision Tree**
* F1 Score: **0.4668**

**Best Accuracy**

* Model: **Original SVM**
* Accuracy: **0.6707**

**Best ROC-AUC**

* Model: **XGBoost**
* ROC-AUC: **0.6592**

---

## 🏆 Final Model Selection

The **Decision Tree** was selected as the final model.

The selection criterion was the **highest F1 Score**.

```text
Selected Model: Decision Tree
F1 Score: 0.4668
```

Although the Original SVM achieved higher accuracy and XGBoost achieved higher ROC-AUC, the Decision Tree achieved the highest F1 Score.

Therefore, based on the project's primary selection criterion, the Decision Tree was chosen for the final model and deployment.

---

## 🔬 Feature Importance

Feature importance was analyzed using:

* Random Forest
* XGBoost

This analysis helps identify which water-quality features contributed most strongly to the predictions of the tree-based models.

The project generates feature-importance tables and visualizations for both models.

---

## 💾 Model Saving

The final model and preprocessing components were saved using `joblib`.

The following files are generated:

```text
water_potability_model.pkl
water_potability_imputer.pkl
water_potability_features.pkl
```

### Saved Components

**`water_potability_model.pkl`**

Contains the selected Decision Tree model.

**`water_potability_imputer.pkl`**

Contains the median-value imputer used during preprocessing.

**`water_potability_features.pkl`**

Contains the feature names and their correct order.

Saving these components allows the trained model to be reused without retraining it every time a prediction is required.

---

## 🧪 Prediction with New Water Samples

The final model was tested using new water-quality measurements.

Example input:

```python
{
    "ph": 7.0,
    "Hardness": 200.0,
    "Solids": 20000.0,
    "Chloramines": 7.0,
    "Sulfate": 300.0,
    "Conductivity": 400.0,
    "Organic_carbon": 10.0,
    "Trihalomethanes": 60.0,
    "Turbidity": 4.0
}
```

The saved model can process the input and return:

* Predicted class
* Potable / Not Potable result
* Probability of potable water

---

## ✅ Input Validation

The project also includes input validation based on the ranges observed in the dataset.

The validation ranges include:

| Feature         | Dataset-Based Range |
| --------------- | ------------------: |
| pH              |          0.0 – 14.0 |
| Hardness        |    47.432 – 323.124 |
| Solids          | 320.943 – 61227.196 |
| Chloramines     |      0.352 – 13.127 |
| Sulfate         |     129.0 – 481.031 |
| Conductivity    |   181.484 – 753.343 |
| Organic Carbon  |          2.2 – 28.3 |
| Trihalomethanes |       0.738 – 124.0 |
| Turbidity       |        1.45 – 6.739 |

> **Note:** These ranges are based on the values observed in the project dataset. They should not be interpreted as official drinking-water safety or regulatory limits.

---

## 📁 Project Structure

```text
water-potability-prediction-ml/
│
├── data/
│   └── water_potability.csv
│
├── notebook/
│   └── water_potability_ml_project.ipynb
│
├── deployment/
│   ├── app.py
│   ├── water_potability_features.pkl
│   ├── water_potability_imputer.pkl
│   └── water_potability_model.pkl
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **XGBoost**
* **Joblib**
* **Jupyter Notebook**
* **Streamlit** for deployment

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/kibromhailu11/water-potability-prediction-ml.git
```

Move into the project directory:

```bash
cd water-potability-prediction-ml
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Notebook

Open the project using Jupyter Notebook or VS Code.

The main notebook is located at:

```text
notebook/water_potability_ml_project.ipynb
```

Run the steps in order from data loading and exploration through model evaluation and saving.

---

## 🚀 Running the Deployment Application

The deployment application is located in:

```text
deployment/app.py
```

After installing the required packages, run:

```bash
streamlit run deployment/app.py
```

The Streamlit application provides an interface where water-quality measurements can be entered and the trained model can generate a potability prediction.

---

## 📌 Important Note

This project is an **educational machine learning project**.

The prediction produced by the model should not be considered a substitute for laboratory water testing, professional water-quality analysis, or official regulatory standards.

The model's performance is limited by the dataset used for training and testing.

---

## 🔮 Future Improvements

Possible future improvements include:

* Collecting a larger and more diverse water-quality dataset
* Addressing class imbalance
* Applying more advanced preprocessing techniques
* Testing additional machine learning algorithms
* Improving hyperparameter optimization
* Using cross-validation for more robust model evaluation
* Improving the deployment interface
* Adding interactive visualizations
* Deploying the application to a cloud platform
* Improving model performance on the potable-water class

---

## 👨‍💻 Author

**Kibrom Hailu**

GitHub: `kibromhailu11`

---

## 📜 License

This project is intended for educational and learning purposes.
