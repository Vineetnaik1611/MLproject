# End - to - End ML project


### Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/Vineetnaik1611/ML-Pipeline-Architecture.git
cd ML-Pipeline-Architecture
```
2. **Set up virtual environment**
```bash
python -m venv venv
source venv/Scripts/activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Start the Flask web application**
```bash
python app.py
```

5. ***Access the web interface***

```text
Open http://localhost:5000 in your browser
```




## Step 1 – Python Environment Setup, Industry Project Configuration, and Package Management

Setting up a professional-grade Python project structure ready for development.

### i. Professional Python Package Structure
- Created proper Python package with `src/` directory  
- Set up `setup.py` with package configuration  
- Configured dependency management using `requirements.txt`  
- Implemented editable installation using `-e .`  

### ii. Development Environment
- Created a virtual environment (`venv/`) for isolated development  
- Added `.gitignore` to exclude unnecessary files  
- Initialized Git repository with proper structure  


---

## Step 2 – Implementing Project Structure, Logging, and Exception Handling

1. In `src`, created a new folder `components` and added an `__init__.py` inside it.  
2. Created a `pipeline` folder in `src` for training and prediction pipelines.  
3. Added three core files in `src`:  
   - `logger.py` for logging  
   - `exception.py` for custom exception handling  
   - `utils.py` for reusable utilities  
4. Implemented a custom exception system that extracts file name, line number, and full traceback for clear error descriptions.  
5. Implemented a logging setup that creates a new timestamped log file inside a `logs/` folder for every run.  


---

## Step 3 – Data Ingestion Module

Built a **Data Ingestion module** that automates the first stage of the ML pipeline.

### Core Tasks:
1. Reads the raw dataset from the source.  
2. Creates a structured `artifacts/` directory.  
3. Saves the raw dataset for reproducibility.  
4. Performs a train–test split and stores both datasets.

The logic is encapsulated in a `DataIngestion` class, and paths are managed with a `DataIngestionConfig` dataclass.  
The ingestion function returns the paths of the train and test files for downstream modules.

### Important Question  
**What is `@dataclass`?**  
`@dataclass` is a Python decorator that auto-generates `__init__` and other boilerplate methods for classes that primarily store data, making the code cleaner and easier to maintain.  


---

## Step 4 – Data Transformation Using Pipelines

### Data Transformation Module

Created a module to preprocess data before model training.

### 1. Built Preprocessing Pipelines
- **Numerical columns:** median imputation + StandardScaler  
- **Categorical columns:** most-frequent imputation + One-Hot Encoding + scaling (without centering)  
- Combined both using `ColumnTransformer` to build a reusable preprocessing object.

### 2. Applied Preprocessing to Train and Test Sets
- Loaded datasets and split into features and target.  
- Fitted the preprocessor on the training data and transformed both datasets.  
- Combined transformed features with target arrays using `np.c_`.

### 3. Saved the Preprocessing Object
- Saved the fitted preprocessor as a pickle file in the `artifacts/` directory.

### Benefits
- Consistent preprocessing  
- Automated workflow  
- Reproducible transformations  
- Production-ready pipeline  


---

## Step 5 – Model Trainer Implementation

Built a **Model Trainer module** to automate model training and evaluation.

### Main Steps:

1. Split processed data into features and target for training and testing.  
2. Defined multiple regression models and their hyperparameter grids:  
   Random Forest, Decision Tree, Gradient Boosting, Linear Regression, XGBoost, AdaBoost.  
3. Evaluated all models using a helper function `evaluate_models` and selected the best one based on R² score.  
4. Saved the best-performing model as a pickle file in `artifacts/model.pkl`.  
5. Performed final evaluation by predicting on the test set and computing R² score.

This makes the pipeline modular, automated, and ready for production deployment.  


---

## Step 6 – Building Predict Pipeline and Flask App

### Flask Web Application for Real-Time Student Score Prediction

Created a Flask app to make model predictions interactive.

### 1. `app.py` – The Flask Application
- Two routes:  
  - `'/'` for the home page  
  - `'/predictdata'` for handling prediction form submissions  
- Captured user inputs using `request.form.get()`.  
- Converted inputs into a structured `CustomData` object.  
- Passed the data to `PredictPipeline` for model inference.  
- Rendered predicted results on the webpage.

### 2. `predict_pipeline.py` – Prediction Logic
Created two classes:

- **`CustomData`**  
  - Stores user input  
  - Converts values into a DataFrame for model compatibility  
- **`PredictPipeline`**  
  - Loads trained model and preprocessor  
  - Applies preprocessing and returns predictions  

### 3. Workflow Summary
1. User enters details in the HTML form.  
2. Flask collects and structures the input.  
3. Preprocessing and prediction occur via `PredictPipeline`.  
4. Prediction is displayed on the webpage.

### Key Points
- Clear separation between web interface and ML logic  
- Reuse of the same preprocessing steps ensures consistency  
- Modular design for easy maintenance  
- Enables real-time prediction for end users  
