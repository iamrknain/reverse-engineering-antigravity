import subprocess
import os

def run_command(command, cwd=None):
    """
    Executes a shell command.
    """
    if cwd is None:
        cwd = os.getcwd()
        
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            capture_output=True,
            text=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode
        }
    except Exception as e:
        return f"Error running command: {e}"
