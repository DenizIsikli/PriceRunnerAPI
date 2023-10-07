import subprocess
import venv


def create_virtual_environment():
    venv.create("venv", with_pip=True)


def install_dependencies():
    subprocess.run(["venv/bin/python", "-m", "pip", "install", "--upgrade", "-r", "requirements.txt"])


create_virtual_environment()
install_dependencies()
