"""
Main Application Entry Point

This file serves as the entry point for the Todo CLI application.
"""

import argparse
import subprocess
import sys
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up logging first
from src.logging_config import setup_logging
setup_logging()

def run_console():
    """Run the console application."""
    print("Starting the Todo CLI application...")
    # Import and run the demo app directly instead of using subprocess
    from demo_app import demo_application
    demo_application()

def run_tests():
    """Run the application tests."""
    print("Running tests...")
    subprocess.run([sys.executable, "test_app.py"])

def run_migrations():
    """Run database migrations."""
    print("Running database migrations...")
    subprocess.run([sys.executable, "migrate_db.py"])

def main():
    parser = argparse.ArgumentParser(description="Todo CLI Application")
    parser.add_argument(
        "command",
        choices=["console", "test", "migrate"],
        help="Command to run: console, test, or migrate"
    )

    args = parser.parse_args()

    if args.command == "console":
        run_console()
    elif args.command == "test":
        run_tests()
    elif args.command == "migrate":
        run_migrations()

if __name__ == "__main__":
    main()