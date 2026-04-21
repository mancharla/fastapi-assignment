# Hospital FastAPI Project

# Overview

This project is a REST API built using FastAPI and Python to manage Doctors and Patients.

# Features

# Doctor APIs

* POST /doctors
* GET /doctors
* GET /doctors/{doctor_id}

# Patient APIs

* POST /patients
* GET /patients

# Tech Stack

* Python
* FastAPI
* Pydantic
* Uvicorn

# Setup Instructions

# 1. Create Virtual Environment

python -m venv env

# 2. Activate Environment

env\Scripts\activate

# 3. Install Dependencies

pip install fastapi uvicorn email-validator

# 4. Run Project

uvicorn main:app --reload

# API Documentation

Open in browser:

http://127.0.0.1:8000/docs

# Validation Rules

 Email must be valid
 Age must be greater than 0
 Doctor not found

# Notes

 In-memory storage resets after restart
 SQLite can be used for persistent storage

