# Learn Python: Beginner to Advanced

A free, hands-on Python course for **complete beginners**. No experience needed.

You learn by doing: read a short lesson file, run it, change it, then solve an exercise.

---

## How to start (about 10 minutes)

### 1. Install Python
Download it from [python.org/downloads](https://www.python.org/downloads/).
**Windows:** on the first install screen, tick **"Add Python to PATH"**.

Check that it worked by opening a terminal and typing:

```
python --version
```

(On Mac/Linux, use `python3` instead of `python` everywhere in this guide.)

### 2. Get this project
- **Easy way:** click the green **Code** button on GitHub → **Download ZIP** → unzip it.
- **With Git:** `git clone https://github.com/CharmReign/python-learning.git`

### 3. Open a terminal inside the project folder
In VS Code: **File → Open Folder**, then **Terminal → New Terminal**.

### 4. Create a virtual environment (one time)
A virtual environment is a private Python setup just for this project, so its packages don't mix with the rest of your computer.

```bash
python -m venv .venv
```

Activate it each time you open a new terminal:

| System | Command |
|---|---|
| Windows (PowerShell) | `.\.venv\Scripts\Activate.ps1` |
| Mac / Linux | `source .venv/bin/activate` |

You'll see `(.venv)` at the start of the line when it's active.
If Windows says *"running scripts is disabled"*, run this once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

Then install the tools:

```bash
pip install -r requirements.txt
```

### 5. Run your first program
```bash
python 01_fundamentals/00_hello.py
```

If you see `Hello, Python!`, you're ready. 🎉

---

## How to use each lesson

1. **Read** the lesson file. The comments explain every line.
2. **Run** it and compare the output with the code.
3. **Break it on purpose.** Change values, delete things, and read the error messages.
4. **Solve** the exercise in `exercises.py` yourself before looking anything up.
5. **Track** your progress in [PROGRESS.md](PROGRESS.md).

Stuck? Try the hints at the bottom of each exercise first. Searching the error message is a real developer skill too.

---

## What's inside

| Folder | Topics | Status |
|---|---|---|
| `01_fundamentals/` | variables, data types, conditions, loops, functions, lists & dictionaries | ✅ Lessons 1–2 ready, more coming |
| `02_intermediate/` | error handling, files, classes (OOP), JSON, APIs | 🔜 Coming soon |
| `03_advanced/` | decorators, generators, async, testing | 🔜 Coming soon |
| `04_practical_projects/` | databases, FastAPI, Docker, Git, deployment | 🔜 Coming soon |
| `05_ai_automation/` | data analysis, web scraping, automation, AI apps | 🔜 Coming soon |

The full plan is in [ROADMAP.md](ROADMAP.md).
