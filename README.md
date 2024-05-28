# damnxss
Attention! Don't upload on production server, or you know all the risks.

# How to Run
To start the web server you need to follow instructions as described below:
1. Clone the repository by running `git clone https://github.com/hermanka/damnxss.git` or just download the source code.
2. Open your terminal and move to the `damnxss` or directory of choosing.
3. Run `pip install -r requirements.txt` commands (Run on native or virtual environment).
4. Start web server by running `flask --app app run`.
5. Visit the http://localhost:5000 in web browser
6. To move  between different levels try to manually change the suffix of the URL to your level. For example, if you want to visit level1 then go to http://localhost:5000/level1 URL in the web browser.

# Virtual environment Setup (Optional)

1. Run this command to install virtual environment `py -3.11 -m pip install virtualenv`
2. Create virtual environment `py -3.11 -m virtualenv venv`
3. Activate virtual environment `venv\Scripts\activate`