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
    

def analyze_code_coverage(source_dir: str, tests_dir: str) -> dict[str, float]:
    """Run pytest --cov to check coverage in source_code"""
    if not isinstance(source_dir, str) or not isinstance(tests_dir, str):
        raise ValueError("source_dir and tests_dir must be strings")
    
    # Running pytest --cov on the file
    result = subprocess.run(
        [
            "pytest", f"--cov={source_dir}", 
            "--cov-report=term", tests_dir
        ],
        capture_output=True,
        text=True
    )

    # Storing output
    output = result.stdout
    lines = output.splitlines()
    
    # Creating dictionary and adding filename and the percantage
    coverage: dict[str, float] = {}
    for line in lines:
        s = line.strip()
        # Skip irrelevant lines
        if not s or s.startswith("Name") or s.startswith("TOTAL"):
            continue
        if ".py" not in s or "%" not in s:
            continue
        
        # Adding relevant information to dictionary
        parts = s.split()
        filename = parts[0]
        percent_token = parts[-1]
        if percent_token.endswith("%"):
            try:
                coverage[filename] = float(percent_token.rstrip("%"))
            except ValueError:
                pass
            
    return coverage


def check_minimum_coverage(source_dir: str, tests_dir: str, minimum: float) -> bool:
    """Run pytest --cov to check coverage in source_code"""
    if not isinstance(source_dir, str) or not isinstance(tests_dir, str):
        raise ValueError("source_dir and tests_dir must be strings")
    if not isinstance(minimum, float):
        raise ValueError("minimum must be a number")
    
    # Running pytest --cov on the file
    result = subprocess.run(
        [
            "pytest", f"--cov={source_dir}", 
            "--cov-report=term", tests_dir
        ],
        capture_output=True,
        text=True
    )

    # Storing output
    output = result.stdout
    lines = output.splitlines()
    
    # Creating dictionary and adding filename and the percantage
    coverage: dict[str, float] = {}
    for line in lines:
        s = line.strip()
        # Skip irrelevant lines
        if not s or s.startswith("Name") or s.startswith("TOTAL"):
            continue
        if ".py" not in s or "%" not in s:
            continue
        
        # Adding relevant information to dictionary
        parts = s.split()
        filename = parts[0]
        percent_token = parts[-1]
        if percent_token.endswith("%"):
            try:
                coverage[filename] = float(percent_token.rstrip("%"))
            except ValueError:
                pass
    
    # Checking if the scores passes minimum
    for filename, score in coverage.items():
        if score <= minimum:
            return False
    
    return True


def generate_quality_report(source_code: str) -> dict[str, any]:
    """Combine pycodestyle and pylint checks"""
    if not isinstance(source_code, str):
        raise ValueError("source_code must be a string")
    
    # Creating a temporary file for the source_code
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name
        
    # Running pycodestyle
    pycodestyle_result = subprocess.run(["pycodestyle", tmp_path], capture_output=True, text=True)
    
    # Checking amount of issues from pycodestyle
    pycodestyle_output = pycodestyle_result.stdout
    issues = 0 if pycodestyle_output == "" else len(pycodestyle_output.splitlines())
    
    # Running pylint and storing output
    pylint_result = subprocess.run(["pylint", tmp_path], capture_output=True, text=True)
    pylint_output = pylint_result.stdout
    
    # Searching for the score and storing it
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", pylint_output)
    pylint_score = float(match.group(1)) if match else 0.0
    
    # Assessment of the code
    style_passed = (issues == 0) and (pylint_score >= 9.0)
    
    # Returning the report
    return {
        "pycodestyle_issues": issues,
        "pylint_score": pylint_score,
        "style_passed": style_passed
    }
    
    
code = "def add(a,b):\n return a+b"
#print(check_pep8_compliance(code))
#print(check_pep8_compliance_ignored(code, ["E231"]))
#print(run_pylint_score(code))
#print(analyze_code_coverage("Week_2/Assignment", "Week_2/Assignment"))
#print(check_minimum_coverage("Week_2/Assignment", "Week_2/Assignment", 80.0))
print(generate_quality_report(code))
