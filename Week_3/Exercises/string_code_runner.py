def run_python_code(source_code: str) -> str:
    if not isinstance(source_code, str):
        raise TypeError("source_code must be a string")

    exec(source_code)

    return "Code executed correctly"


run_python_code("""
for x in range(5):
    print(f"Hello {x}")
""")

run_python_code("print('Hello, world!')")
