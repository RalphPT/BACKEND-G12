from flask import Flask

app= Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] =

@app.route('/')
def index():
    return 'Hello world! :)'

if __name__ == "__main__":
    app.run(debug=True)