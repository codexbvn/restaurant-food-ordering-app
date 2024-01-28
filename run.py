from backend.app import app as backend_app
from frontend.app import app as frontend_app


if __name__ == "__main__":
    # Run the backend and frontend apps separately
    backend_app.run(port=5000)
    frontend_app.run(port=8000)

