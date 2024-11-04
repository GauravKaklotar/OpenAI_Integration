from flask import Flask
from config.config import Config
from routes.api_routes import api_bp  # Import the Blueprint

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(api_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
