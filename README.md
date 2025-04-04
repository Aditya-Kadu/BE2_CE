
# The Social Media Paradox 
## Predicting Social Media Application Usage and Its Impact on Mental and Physical Well-being.

## 🔍 Project Overview
This project aims to analyze user engagement based on dominant emotions using machine learning models. It involves:
✅ Data preprocessing (encoding categorical variables, handling missing values)
✅ Feature engineering (e.g., engagement metrics, total interaction score)
✅ Oversampling with SMOTE for class imbalance handling
✅ Hyperparameter tuning using GridSearchCV and Optuna
✅ Comparing multiple classifiers (Random Forest, SVM, Decision Tree, Gradient Boosting, etc.)
✅ Evaluating model performance using accuracy, F1-score, and confusion matrices

## 📂 Dataset
df_train: Training dataset used for model training

df_test: Separate test dataset used for final evaluation

Features include user interactions, emotions, and engagement metrics

## 📊 Data Preprocessing & Feature Engineering
Categorical features (e.g., Gender, Platform, Dominant_Emotion) are encoded

Created age groups (18-24 vs. others)

Engineered Engagement_Received as the sum of likes, comments, and messages

Addressed class imbalance using SMOTE

## 🤖 Model Training & Hyperparameter Tuning
Machine Learning Models Used:
✅ Random Forest
✅ Gradient Boosting
✅ Linear SVM
✅ Decision Tree

Hyperparameter Optimization:

GridSearchCV (for exhaustive tuning)

Optuna (for automated hyperparameter search)

Performance evaluated on validation and test sets

## 📈 Results & Evaluation
Best-performing model: [Model Name]

Achieved [Accuracy/F1-Score] on the test set

Insights:

Emotion [X] resulted in higher/lower engagement

Users aged 18-24 engaged more/less than other groups
