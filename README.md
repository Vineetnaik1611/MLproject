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