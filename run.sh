#!/bin/bash

start_backend() {
    echo "Starting Backend..."
    cd backend
    python manage.py runserver 8001 &
    cd ..
}

start_frontend() {
    echo "Starting Frontend..."
    cd frontend
    python manage.py runserver 8000 &
    cd ..
}

start_backend & start_frontend

# Keep the script running
wait