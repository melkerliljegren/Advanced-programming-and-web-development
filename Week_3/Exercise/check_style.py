import subprocess
import tempfile
import re
import sys


def check_style(file_path: str) -> str:
    if not isinstance(file_path, str):
        raise TypeError("file_path must be a string")

    result = subprocess.run(["pycodestyle", file_path], capture_output=True, text=True)

    if result.stdout == "":
        return "No style issues found"
    
    cleaned = []
    for line in result.stdout.splitlines():
        parts = line.split(":", 1)
        cleaned.append(parts[1])

    return cleaned


def filter_ignored(messages: list[str], ignore: list[str]) -> list[str]:
    if not isinstance(messages, list) or not isinstance(ignore, list):
        raise ValueError("messages must be a list")
    
    filtered = []
    
    for error in messages:
        for e_ignore in ignore:
            if e_ignore in error:
                continue
            else:
                filtered.append(error)
    return filtered


def run_pylint_score(source_code: str) -> str:
    if not isinstance(source_code, str):
        raise ValueError("source_code must be a string")
    
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name
        
    result = subprocess.run(
        [sys.executable, "-m", "pylint", "--disable=R,C", tmp_path],
        capture_output=True,
        text=True
    )
    
    output = result.stdout
    
    match = re.search(r"Your code has been rated at ([\d\.]+)/10", output)
    if match:
        return match.group(1) + "/10"
    else:
        return "No score found"
    
    
def parse_coverage_output(lines: str) -> dict[str, float]:
    coverage = {}
    for line in lines:
        if "/" in line and "%" in line and not line.strip().startswith("TOTAL"):
            parts = line.split()
            filename = parts[0]
            procent_str = parts[-1].replace("%", "")
            try:
                coverage[filename] = float(procent_str)
            except:
                continue
    return coverage


def check_minimum_coverage(coverage: dict[str, float], minimum: float) -> bool:
    if not isinstance(coverage, dict):
        raise TypeError("coverage must be a dict")
    if not isinstance(minimum, (int, float)):
        raise TypeError("minimum must be a number")

    for value in coverage.values():
        if value < minimum:
            return False
    return True


def generate_quality_report(source_code: str) -> dict[str, float | int | bool]:
    """Run pycodestyle + pylint on given code and return a summary report."""
    if not isinstance(source_code, str):
        raise TypeError("source_code must be a string")

    # Writing the code as a temporary .py file
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as tmp:
        tmp.write(source_code)
        tmp_path = tmp.name

    # Running pycodestyle
    pycodestyle_result = subprocess.run(
        [sys.executable, "-m", "pycodestyle", tmp_path],
        capture_output=True,
        text=True
    )
    pycodestyle_output = pycodestyle_result.stdout.strip()
    # Coutning the numbers of rows with errors
    issues = 0 if pycodestyle_output == "" else len(pycodestyle_output.splitlines())

    # Running pylint
    pylint_result = subprocess.run(
        [sys.executable, "-m", "pylint", "--disable=R,C", tmp_path],
        capture_output=True,
        text=True
    )
    pylint_output = pylint_result.stdout or pylint_result.stderr

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
    

#print(check_style("Week_3/Exercise/bad_code.py"))
#print(filter_ignored(check_style("Week_3/Exercise/bad_code.py"), ["E231"]))
#print(run_pylint_score("def add(a,b): return a + b"))   

sample_output = """
Name                    Stmts   Miss  Cover
---------------------------------------
src/main.py                 10      1    90%
src/utils.py                 8      0   100%
---------------------------------------
TOTAL                       18      1    94%
""".strip().splitlines()

#print(parse_coverage_output(sample_output))
#print(check_minimum_coverage(parse_coverage_output(sample_output), 91))

print(generate_quality_report("def add(a,b): return a+b"))