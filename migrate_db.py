"""
Database Migration Script

This script handles database migrations for the Todo application.
It creates the necessary tables based on the SQLModel models.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging
from src.logging_config import setup_logging
setup_logging()

from src.database import create_db_and_tables
import sys

def run_migrations():
    """Run database migrations to create tables."""
    print("Starting database migration...")

    try:
        create_db_and_tables()
        print("Database migration completed successfully!")
        print("All tables have been created/updated as needed.")
    except Exception as e:
        print(f"Error during database migration: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_migrations()