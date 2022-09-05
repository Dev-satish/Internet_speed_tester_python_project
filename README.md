# Speed Testing Web Application

## Setup

Open CMD and run the following command:
```cmd
python -m pip install virtualenv
```

Navigate to the project folder in CMD.
Create a virtual environment using:
```cmd
python -m venv .venv
```

Install the dependencies:
```cmd
pip install -r requirements.txt
```

## Running the app

Activate the virtual environment:
```cmd
".venv\Scripts\activate.bat"
```

In CMD, in the same folder as `app.py` file:
```cmd
flask run
```

That's it! Visit http://127.0.0.1:5000 in your browser.
