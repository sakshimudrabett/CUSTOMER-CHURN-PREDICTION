# Customer Churn Prediction Project  

## 📌 Project Overview  
Customer churn is a major challenge for businesses, as retaining existing customers is often more cost-effective than acquiring new ones.  
In this project, we analyzed a customer dataset to identify factors that influence churn and built a machine learning model to predict which customers are at risk of leaving.  

The workflow covered:  
1. **Data cleaning & preprocessing**  
2. **Exploratory Data Analysis (EDA)** with dashboards for churn vs. non-churn groups  
3. **Feature engineering** and handling class imbalance (SMOTE)  
4. **Model building & evaluation** (using cross-validation with ROC-AUC as the main metric)  
5. **Feature importance analysis** to interpret model results  

---

## 📊 Dashboard Insights (EDA)  
Before modeling, an interactive dashboard was created to visualize the original dataset and uncover key insights:  
- Churn distribution (imbalanced dataset)  
- Customer demographics and tenure  
- Transaction patterns and spending behavior differences between churners and non-churners  


---

## 🛠 Data Preprocessing  
- **Missing values** were handled appropriately.  
- **Categorical variables** were encoded.  
- **Numerical features** were standardized where necessary.  
- **Imbalanced classes** were addressed using **SMOTE (Synthetic Minority Oversampling Technique)** to generate synthetic churn samples.  

---

## 🤖 Model Development  
We tested multiple algorithms including Logistic Regression, Random Forest, and Gradient Boosting models.  

- **Cross-validation**: Applied **Stratified K-Fold (k=5)** to ensure balanced churn representation across folds.  
- **Performance Metric**:  
  - Chosen metric was **ROC-AUC**, as accuracy is misleading on imbalanced datasets.  
  - Final model achieved an **ROC-AUC ≈ 0.86 .  

---

## 📈 Model Evaluation  
Key steps included:  
- Comparing models with cross-validation ROC-AUC scores  
- Evaluating final model on a **held-out test set** (untouched during training)  
- Interpreting results to understand business impact  

---

## 📦 Tools & Libraries Used  
- Python (pandas, numpy, matplotlib, seaborn)  
- scikit-learn (LogisticRegression, RandomForest, ROC-AUC evaluation)  
- imbalanced-learn (SMOTE)  
- Jupyter Notebook & VS Code  
- Tableau/Power BI (for dashboarding)  

---

## 🚀 Business Value  
- Identifies customers at risk of churn with reasonable accuracy  
- Provides actionable insights (key drivers of churn)  
- Supports data-driven retention strategies  

---  

