# End - to - End ML project

## Step 1 -  Python Environment Setup, Industry Project Configuration And Package Management

Set up a professional-grade Python project structure that's ready for serious development!

i. Professional Python Package Structure
✅ Created proper Python package with src/ directory

✅ Set up setup.py with package configuration

✅ Configured dependency management with requirements.txt

✅ Implemented editable installation with -e .

ii. Development Environment
✅ Set up virtual environment (venv/) for isolated development

✅ Created .gitignore to exclude unnecessary files from version control

✅ Initialized Git repository with proper project structure


## Step 2  Implementing Project Structure, Logging And Exception Handling

1. In src create a new folder 'components' and create a '__init__.py' in it. (Components contains modules of the project , such as data injestion, preprocessing etc)
2. Create a folder named 'pipeline' in src (training and prediction pipeline)
3. Create 3 important files in src - 1. logger.py for logging, 2. exception.py  for exception handling, 3. utils.py (any functionalities to be uised in entire project can be written here)
4. Created a custom exception system that extracts full traceback details (file name, line number, and error message) and formats them into a readable error description. (exception.py)
5. Created a logging setup that generates a new timestamped log file inside a logs/ folder every time the program runs. (logger.py)


## Step 3   Data Ingestion Module 

I built a **Data Ingestion module** that automates the first step of the ML pipeline.

The ingestion component handles four key tasks:

1. **Reads the raw dataset** from the source location.  
2. **Creates a structured artifacts directory** to store all generated files.  
3. **Saves the raw data** to ensure reproducibility.  
4. **Performs a train–test split** and saves the split datasets separately.

I encapsulated this logic within a `DataIngestion` class and used a `DataIngestionConfig` dataclass to manage file paths cleanly.  
Finally, the ingestion function **returns the paths of the train and test files**, which are then passed to the data transformation and model training modules.

This approach keeps the pipeline **modular, reproducible, and easy to maintain**.


###### important questions
1. What is @dataclass

@dataclass is a Python decorator that automatically generates the init and other boilerplate methods for classes that only store data, making the code cleaner and easier to maintain.


## Step 4 Data transformation using pipelines Implementation

### Data Transformation Module 

I built a **Data Transformation module** to preprocess the dataset before model training.

First, I created a configuration class using `@dataclass` to store the path where the preprocessor object (pickle file) will be saved.

Then, inside the `DataTransformation` class, I performed three main tasks:

---

### 1️⃣ Built Preprocessing Pipelines

- **Numerical columns:** Used a pipeline with **median imputation** and **StandardScaler**.  
- **Categorical columns:** Used **most-frequent imputation**, **One-Hot Encoding**, and **scaling (without centering)**.  

These pipelines were combined using a **ColumnTransformer**, creating a reusable preprocessing object.

---

### 2️⃣ Applied Preprocessing to Train and Test Sets

- Loaded the train and test datasets.  
- Split them into **input features** and **target**.  
- Fitted the preprocessor on the training data and transformed both train and test sets.  
- Used `np.c_` to **combine processed features with the target arrays**.

---

### 3️⃣ Saved the Preprocessing Object

- Saved the fitted preprocessor as a **pickle file** in the `artifacts` folder.  
- This ensures the same transformations can be applied during inference.

---

### ✅ Benefits

- **Consistent** preprocessing  
- **Automated** workflow  
- **Reproducible** results  
- **Production-ready** pipeline



## Step 5 - Model Trainer Implementation
I built a **Model Trainer module** to automate model training, evaluation, and saving in my ML pipeline.

First, I created a configuration class using `@dataclass` to store the path where the trained model will be saved (`artifacts/model.pkl`).

Inside the `ModelTrainer` class, I did the following:

1️⃣ **Split data:** The method `initiate_model_trainer` takes the processed `train_array` and `test_array`, and splits them into input features and target labels for training and testing.

2️⃣ **Defined models and hyperparameters:** I included multiple regressors—Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, and AdaBoost—and specified their hyperparameter grids.

3️⃣ **Model evaluation and selection:** I call a helper function `evaluate_models` to train and evaluate each model, then select the one with the highest R² score.

4️⃣ **Save the best model:** If the best model passes a threshold, I save it as a pickle file so it can be used later for inference.

5️⃣ **Final evaluation:** I predict on the test set and calculate the R² score to confirm the model’s performance.

**In short:** This module **automates model training, evaluation, and storage**, making the pipeline **modular, reproducible, and production-ready**.
