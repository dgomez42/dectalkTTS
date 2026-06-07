import subprocess
import os
import stat
from pathlib import Path

PACKAGE_DIR = Path(__file__).parent.resolve()

if os.name == "nt":
    executable = PACKAGE_DIR / "say.exe"
else:
    executable = PACKAGE_DIR / "say"
    if executable.exists() and not os.access(executable, os.X_OK):
        executable.chmod(executable.stat().st_mode | stat.S_IEXEC)
def dectalk(text):
    subprocess.run([str(executable)], input=text + "\n", text=True, cwd=PACKAGE_DIR)