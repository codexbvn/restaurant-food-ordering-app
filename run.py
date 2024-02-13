from backend.app import app as backend_app
from frontend.app import app as frontend_app


if __name__ == "__main__":
    
    backend_app.run(port=5000)
    frontend_app.run(port=8000)
