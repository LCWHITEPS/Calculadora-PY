import subprocess
import sys
from pathlib import Path

calculadora = Path(__file__).resolve().parent / "calculator.py"

if __name__ == "__main__":
    subprocess.run([sys.executable, str(calculadora)])
