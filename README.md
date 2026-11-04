# Python Learning Environment

My personal path from zero to advanced Python developer: learning by doing.

## Folder layout

| Folder | What goes there |
|---|---|
| `01_fundamentals/` | Phase 1: syntax, variables, conditions, loops, functions, collections |
| `02_intermediate/` | Phase 2: comprehensions, exceptions, files, OOP, JSON, APIs |
| `03_advanced/` | Phase 3: decorators, generators, async, testing, design patterns |
| `04_practical_projects/` | Phase 4: databases, FastAPI, auth, Docker, deployment, plus phase projects |
| `05_ai_automation/` | Phase 5: NumPy/Pandas, scraping, AI APIs, agents, RAG |
| `tests/` | pytest tests for my code |

Lesson files are added **as I reach each topic**. There are no empty placeholder files.

## Key documents

- [ROADMAP.md](ROADMAP.md): the full learning plan
- [PROGRESS.md](PROGRESS.md): what I've completed, where I struggled, what's next

## Setup (one time)

```powershell
cd D:\Files\reign\python-learning
python -m venv .venv
```

## Every session

```powershell
cd D:\Files\reign\python-learning
.\.venv\Scripts\Activate.ps1        # prompt now starts with (.venv)
python 01_fundamentals\00_hello.py   # run a file
deactivate                           # when finished
```

If PowerShell refuses to run `Activate.ps1` ("running scripts is disabled"), run this once:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Install dependencies (after activating):

```powershell
pip install -r requirements.txt
```

Run tests:

```powershell
pytest
```
