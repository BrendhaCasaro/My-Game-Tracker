import os
os.environ["FLASK_ENV"] = "development"

from routes import app

if __name__ == "__main__":
   app.run(debug=True)


