Pre-requisites:
1. Python 3.6
2. Pip (Python package manager)
3. Chrome/Firefox webdriver available in PATH

Steps to run tests:
1. Install virtual enviroment with pip
   $ pip install virtualenv

2. Clone the repository with $ git clone

3. Cd into the repository

4. Create and activate a virtual environment
   $ virtualenv -p 3.6 venv
   $ cd venv/Scripts
   $ activate.bat
   $ cd ../..

5. Install required python libraries
   $ pip install -r requirements.txt

6. Run the test script
   $ python run_tests.py
