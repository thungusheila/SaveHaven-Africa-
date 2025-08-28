import os
from flask import Flask
from flask_cors import CORS
from database import db
from models import Report  # ensure model is imported
from routes import bp as api_bp
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///safehaven.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "change-me")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    CORS(app, resources={r"/api/*": {"origins": os.getenv("CORS_ORIGINS", "*")}})
    app.register_blueprint(api_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
