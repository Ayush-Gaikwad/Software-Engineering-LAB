# Static Code Analysis - Issue Documentation

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Shell command execution | Security - High | 61 | os.system() executes a shell command and may allow command injection. | Replace with subprocess.run() using an argument list and shell=False. |
| Hardcoded temporary directory | Security - Medium | 8 | The program uses a fixed /tmp path, which is not portable and may be insecure. | Use tempfile.gettempdir() or a securely created temporary directory. |
| Insecure temporary filename | Security - Medium | 55 | tempfile.mktemp() can create a race condition because the file is not securely created. | Use tempfile.NamedTemporaryFile() or tempfile.mkstemp(). |
| Hardcoded password | Security - Low | 5 | A password is stored directly in the source code. | Read the password from an environment variable. |
| Broad exception handling | Code Quality | 41 | Catching Exception hides unexpected programming errors. | Handle the specific exception or check for an empty list before max(). |
| Global variable usage | Code Quality | 29 | setBudget() modifies a global variable. | Use a clearly defined configuration or budget-management approach. |
| Naming conventions | Code Quality | Multiple | Function and variable names do not follow Python snake_case conventions. | Rename functions and variables using snake_case and constants using UPPER_CASE. |
| Missing documentation | Code Quality | Multiple | Module and functions lack docstrings. | Add meaningful module and function docstrings. |
| Formatting violations | Style | 15, 44, 74, 77 | Flake8 reports whitespace, blank-line, comment-spacing and line-length violations. | Apply PEP 8 formatting. |
| Inefficient iteration | Code Quality | 45 | Uses range(len()) to iterate over a list. | Use enumerate() instead. |

