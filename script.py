import subprocess
import os
import sys
from pathlib import Path

def run_command(command, cwd=None, shell=True):
    # Execute a command, optionally in a specific working directory.
    try:
        subprocess.run(command, cwd=cwd, shell=shell, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute command: {e}", file=sys.stderr)
        sys.exit(1)


def setup_virtualenv():

    # Create the virtual environment if it does not exist
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        run_command("virtualenv venv --python=python3")
    else:
        print("Virtual environment already exists.")
    

def install_dependencies():
    
    # Install Python dependencies within the virtual environment
    # Using the pip in the virtual environment
    print("Installing Python dependencies...")
    pip_path = Path('venv/bin/pip') if sys.platform != 'win32' else Path('venv/Scripts/pip')
    run_command(f"{str(pip_path)} install -r requirements.txt")
def install_npm_dependencies():

    # Install npm dependencies
    print("Installing npm dependencies...")
    # Ensure correct working directory for npm install, adjust 'lab2' as needed
    project_dir = 'lab2' 
    os.chdir(project_dir)
    run_command("npm install")

def build_js():

    # Build JavaScript using esbuild
    print("Building JavaScript with esbuild...")
    # Adjust paths as necessary
    run_command("npx esbuild main.js --bundle --minify --sourcemap --outfile=./emojis/static/main.min.js")

def run_django():

    # Start the Django development server
    # print("Starting Django development server...")
    # # python manage.py runserver not working while venv not activated
    # run_command("python manage.py runserver")
    print("Starting Django development server...")
    os.chdir('..') # Go back to the project root
    django_manage_path = Path('lab2/manage.py')
    python_path = Path('venv/bin/python') if sys.platform != 'win32' else Path('venv/Scripts/python') 
    run_command(f"{str(python_path)} {str(django_manage_path)} runserver")

def main():
    setup_virtualenv()
    install_dependencies()
    install_npm_dependencies()
    build_js()
    run_django()

if __name__ == "__main__":
    main()
