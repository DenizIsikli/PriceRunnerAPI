import subprocess
import venv


# Only run this function if you haven't already created a virtual environment
def create_virtual_environment():
    venv.create("venv", with_pip=True)


def install_dependencies():
    subprocess.run(["venv/bin/python", "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"])


if __name__ == "__main__":
    install_dependencies()
