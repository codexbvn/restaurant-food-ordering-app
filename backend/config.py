# backend/config.py

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for session management (change this to a secure value in production)
    SECRET_KEY = 'your-secret-key'

    # CORS settings (customize these as needed)
    CORS_ORIGINS = ['http://localhost:3000']

    # Enable debugging mode (set to False in production)
    DEBUG = True

