
# The Social Media Paradox 📊
## Predicting Social Media Application Usage and Its Impact on Mental and Physical Well-being.

## 🔍 Project Overview
This project aims to analyze user engagement based on dominant emotions using machine learning models. It involves:<br>
✅ Data preprocessing (encoding categorical variables, handling missing values)<br>
✅ Feature engineering (e.g., engagement metrics, total interaction score)<br>
✅ Oversampling with SMOTE for class imbalance handling<br>
✅ Hyperparameter tuning using GridSearchCV and Optuna<br>
✅ Comparing multiple classifiers (Random Forest, SVM, Decision Tree, Gradient Boosting, etc.)<br>
✅ Evaluating model performance using accuracy, F1-score, and confusion matrices<br>

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
Best-performing model: RandomForest and XGBoost

Achieved accuracy of 12% on the test set


