Pre-requisites:
1. Python 3.6
2. Pip (Python package manager)
3. Chrome/Firefox webdriver available in PATH<br />
Firefox: https://github.com/mozilla/geckodriver/releases<br />
Chrome: https://chromedriver.chromium.org/downloads

Steps to run tests:
1. Install virtual enviroment with pip<br />
   $ pip install virtualenv

2. Clone the repository with $ git clone

3. Cd into the repository

4. Create and activate a virtual environment<br />
   $ virtualenv -p 3.6 venv<br />
   $ cd venv/Scripts<br />
   $ activate.bat<br />
   $ cd ../..

5. Install required python libraries<br />
   $ pip install -r requirements.txt

6. Run the test script<br />
   $ python run_tests.py
