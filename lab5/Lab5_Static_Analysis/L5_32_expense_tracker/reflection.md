\# Lab 5 – Static Code Analysis Reflection



\### 1. What is static code analysis, and why is it useful?



Static code analysis examines source code without executing it. It helps identify programming errors, security vulnerabilities and formatting issues. It improves code quality, readability, security and maintainability.



\### 2. What is the difference between Pylint, Bandit and Flake8?



\- \*\*Pylint:\*\* Checks code quality, naming conventions, missing documentation and programming practices.

\- \*\*Bandit:\*\* Identifies potential security vulnerabilities and unsafe coding practices.

\- \*\*Flake8:\*\* Checks Python code formatting and compliance with PEP 8 guidelines.



\### 3. What issues did you identify and fix?



The analysis identified hardcoded passwords, insecure temporary file handling, shell command execution, broad exception handling, global variable usage, naming convention violations and formatting issues. These were addressed using environment variables, secure temporary files, safer functions, improved naming and proper formatting.



\### 4. How did static analysis improve your program?



Static analysis improved the security, readability and maintainability of the expense tracker. The final program achieved a Pylint score of 10/10, zero Bandit security findings and zero Flake8 violations.

