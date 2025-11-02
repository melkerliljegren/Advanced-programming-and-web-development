import subprocess
import tempfile
import re


def check_pep8_compliance(source_code: str) -> list[str]:
    """Check python code string for PEP8 issues and return list of messages"""
    if not isinstance(source_code, str):
        raise ValueError("source_code must be a string")
    
    # Creating a temporary file for the source_code
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name
        
    # Run pycodestyle on the temporary file consisting the source_code
    result = subprocess.run(["pycodestyle", tmp_path], capture_output=True, text=True)
    
    # Gathering the issues from pycodestyle
    output = result.stdout
    
    # If no issues return an empty list
    if output == "":
        return []
    
    # Splitting the output in lines and removing filename
    cleaned = []
    for line in output.splitlines():
        parts = line.split(":", 1)
        cleaned.append(parts[1])
    
    return cleaned


def check_pep8_compliance_ignored(source_code: str, ignore_rules: list[str]) -> list[str]:
    """Check python code string for PEP8 issues and return list of messages"""
    if not isinstance(source_code, str):
        raise ValueError("source_code must be a string")
    if not isinstance(ignore_rules, list):
        raise ValueError("ignored must be a list of strings")
    
    # Creating a temporary file for the source_code
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name
        
    # Run pycodestyle on the temporary file consisting the source_code
    result = subprocess.run(["pycodestyle", tmp_path], capture_output=True, text=True)
    
    # Gathering the issues from pycodestyle
    output = result.stdout
    
    # If no issues return an empty list
    if output == "":
        return []
    
    # Splitting the output in lines and removing filename
    cleaned = []
    for line in output.splitlines():
        parts = line.split(":", 1)
        msg = parts[1]
        
        # Checking if the error of the output is in ignore_rules
        error_msg = msg.split()[1]
        if error_msg not in ignore_rules:
            cleaned.append(msg)
    
    return cleaned


def run_pylint_score(source_code: str) -> float:
    """Check the pylint score of a python code string"""
    if not isinstance(source_code, str):
        raise ValueError("source_code must be a string")
    
    # Creating temporary file for the source_code
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name
    
    # Running pylint on the source_code
    result = subprocess.run(["pylint", tmp_path], capture_output=True, text=True)
    
    # Gathering output
    output = result.stdout or ""
     
    # Searching for the score
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", output)
    if match:
        return float(match.group(1))
    else:
        return 0.0

code = "def add(a,b):\n return a+b"
#print(check_pep8_compliance(code))
#print(check_pep8_compliance_ignored(code, ["E231"]))
print(run_pylint_score(code))


    
    