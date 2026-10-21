# Day 1 — Development Environment and Python Introduction

## 1. Learning Objectives

By the end of this lesson, I should be able to:

- Explain Python and its common applications.
- Explain the roles of VS Code, the Python interpreter, Git and GitHub.
- Install and verify the required tools on Windows.
- Create and execute a Python script.
- Inspect basic Python environment information.
- Organize a learning repository using a consistent folder structure.
- Track changes with Git and publish the repository to GitHub.

## 2. What Is Python?

Python is a high-level, general-purpose programming language known for readable syntax and a broad ecosystem of libraries.

A programming language provides rules for expressing instructions that a computer can execute through an interpreter or other execution tools.

Python is commonly used for:

- Artificial intelligence and machine learning.
- Data science and statistical analysis.
- Backend development and REST APIs.
- Automation and scripting.
- Scientific computing.
- Testing and developer tools.
- Natural language processing.
- Computer vision.

### Why Learn Python for AI/ML?

Python has a mature ecosystem for data manipulation, numerical computation, machine learning and deep learning.

Examples of important libraries include:

- NumPy — numerical arrays and operations.
- Pandas — structured data manipulation.
- Matplotlib — data visualization.
- Scikit-learn — traditional machine learning.
- PyTorch — deep learning.
- Transformers — working with pretrained transformer models.

Python itself does not automatically provide all these capabilities. Libraries extend what developers can do.

### Advantages

- Readable and approachable syntax.
- Large developer community.
- Extensive libraries and documentation.
- Useful for prototyping and production systems.
- Works across major operating systems.

### Limitations

- Often slower than compiled languages for CPU-intensive tasks written entirely in Python.
- Dynamic typing can allow some errors to appear at runtime.
- Dependency management requires care.
- It is not always the best choice for every performance-critical or resource-constrained application.

Many numerical and machine-learning libraries use optimized native code underneath Python interfaces.

## 3. What Is an Interpreter?

An interpreter is software that executes a programming language's instructions.

For standard Python implementations such as CPython, source code is commonly compiled to bytecode and executed by the Python virtual machine.

The interpreter:

- Reads and processes Python programs.
- Executes supported language instructions.
- Reports syntax and runtime errors.
- Provides access to built-in functions and standard libraries.

The interpreter is different from the code editor. VS Code helps write the code; Python executes it.

## 4. What Is VS Code?

Visual Studio Code is a source-code editor with extensions for additional development functionality.

Common uses include:

- Editing Python files.
- Syntax highlighting and code completion.
- Debugging programs.
- Using an integrated terminal.
- Navigating files and folders.
- Integrating Git into a development workflow.

The Microsoft Python extension improves Python development support, but the Python interpreter must still be installed separately.

VS Code is also different from Visual Studio, which is a separate development environment.

## 5. What Is Git?

Git is a distributed version-control system.

It records changes to a project's files through commits. A commit represents a snapshot of the tracked project at a point in its history.

Git helps developers:

- Review historical changes.
- Compare versions.
- Recover from mistakes.
- Work on separate branches.
- Collaborate on code.
- Track project development over time.

Important terms:

- Working tree: the files currently being edited.
- Staging area: changes selected for the next commit.
- Commit: a saved snapshot in repository history.
- Branch: a separate line of development.
- Remote: a repository location outside the local repository.

Git can be used entirely offline on a local computer.

## 6. What Is GitHub?

GitHub is an online platform for hosting Git repositories and collaborating on software.

It provides features such as:

- Remote repository hosting.
- Pull requests and code review.
- Issues and project discussions.
- Collaboration and contribution history.
- Public portfolios and open-source participation.

Git and GitHub are related but not interchangeable.

Git manages version history. GitHub hosts repositories and provides collaboration services.

A Git repository does not have to be hosted on GitHub.

## 7. Git vs GitHub vs VS Code vs Python

| Tool               | Primary purpose                               |
| ------------------ | --------------------------------------------- |
| Python             | Programming language and runtime ecosystem    |
| Python interpreter | Executes Python programs                      |
| VS Code            | Writes, edits and debugs code                 |
| Git                | Tracks versions of project files              |
| GitHub             | Hosts repositories and supports collaboration |
| Terminal           | Runs commands and programs                    |

These tools solve different problems and work together in a development workflow.

## 8. Install and Verify the Environment

### Python

Official downloads: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)

Verify:

`python --version`

If necessary, try:

`py --version`

### VS Code

Official downloads: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)

Install Microsoft's Python extension.

### Git

Official installation: [https://git-scm.com/install/windows](https://git-scm.com/install/windows)

Verify:

`git --version`

Configure your commit identity:

`git config --global user.name "Your Name"`

`git config --global user.email "YOUR_EMAIL"`

Replace these example values with your preferred name and email.

## 9. First Python Program

File: `hello.py`

```python
print("Hello, World!")
print("My AI/ML engineering journey starts today.")
print("Today I am learning Python, VS Code, Git, and GitHub.")
```

### Explanation

- `print()` is a built-in Python function.
- Parentheses contain the argument passed to the function.
- Quotation marks delimit the string.
- Each statement displays one line of output.
- Statements execute in order in this example.

Run the file:

`python python/day-01/hello.py`

## 10. Environment Inspection

File: `environment-check.py`

```python
import platform
import sys

print("Python environment check")
print("------------------------")
print("Python version:", sys.version)
print("Python executable:", sys.executable)
print("Operating system:", platform.system())
print("Platform details:", platform.platform())
```

### Explanation

`import` makes a module available to the program.

`sys` provides information and interfaces related to the Python interpreter.

`sys.version` reports the Python version information.

`sys.executable` reports the path to the interpreter running the program.

`platform` provides information about the current operating system and platform.

This is useful when diagnosing issues caused by different Python installations.

## 11. Folder Structure

```text
ai-ml-engineer-roadmap/
├── README.md
├── .gitignore
└── python/
    ├── README.md
    └── day-01/
        ├── README.md
        ├── hello.py
        ├── environment-check.py
        ├── notes/
        │   └── learning-log.md
        └── exercises/
            └── exercise-01.py
```

The root README documents the overall roadmap. The Python README documents the Python track. The daily README contains the full theory and practical work for that day.

## 12. Git Workflow

The standard daily workflow is:

1. Inspect changes.
2. Stage the intended files.
3. Commit with a descriptive message.
4. Push the commit to GitHub.
5. Verify that the files appear in the remote repository.

Commands:

`git status`

`git add .`

`git commit -m "Day 1: Set up Python development environment"`

`git push`

The push command requires an appropriate remote repository to have been configured.

For the first push, follow the repository setup instructions in the main roadmap guide.

## 13. Exercises

### Exercise 1

Create a Python script that prints:

- Your introduction.
- Your education.
- Your target career.
- One reason you want to learn Python.

### Exercise 2

Run the environment-check script and record the interpreter path and Python version in your learning log.

### Exercise 3

Explain the difference between Python, VS Code, Git and GitHub in your own words.

### Exercise 4

Create the folder structure and inspect it in VS Code.

### Exercise 5

Commit your work and verify that the repository contains the Day 1 files.

## 14. Troubleshooting

### Python command not found

Try `py --version`, reopen the terminal, and verify the installation and PATH configuration.

### VS Code does not recognize Python

Install the Microsoft Python extension and select the correct interpreter using the command palette.

### Git command not found

Verify Git installation and reopen the terminal.

### Push rejected

Inspect the error message, confirm the configured remote, and resolve the underlying authentication or history issue before retrying.

Never publish passwords, API keys, tokens or other secrets.

## 15. Key Takeaways

- Python is the programming language used throughout this roadmap.
- The interpreter executes Python programs.
- VS Code is the editor used to write and debug code.
- Git records version history.
- GitHub hosts repositories and supports collaboration.
- Good project structure and documentation are part of professional software engineering.
- A successful setup is verified by running actual commands and programs.

## 16. Completion Checklist

- [x] Python installed and verified.
- [x] VS Code installed.
- [x] Python extension installed.
- [x] Git installed and configured.
- [x] GitHub account accessible.
- [x] Folder structure created.
- [x] First Python program executed.
- [x] Environment-check program executed.
- [x] Exercises completed.
- [x] README reviewed and saved.
- [x] Git commit created and pushed.
- [x] LinkedIn learning post prepared.