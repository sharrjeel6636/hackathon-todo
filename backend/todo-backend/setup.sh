#!/bin/bash
# Setup script for backend dependencies

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows: venv\Scripts\activate
# On Unix/Mac: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt