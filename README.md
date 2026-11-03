# RAG Journey

This repository uses one uv-managed virtual environment at the repository root:

```text
RAG_Journey\.venv\
```

The learning projects under `day1`, `day2`, and `Practice\day3` are uv workspace
members. Run commands from the repository root or from any member directory;
uv will use the root environment.

## Setup

From Git Bash:

```bash
cd ~/Downloads/LEARN_PUSH/RAG_Journey
uv sync
source .venv/Scripts/activate
```

From PowerShell:

```powershell
Set-Location C:\Users\rahim_ullah\Downloads\LEARN_PUSH\RAG_Journey
uv sync
.\.venv\Scripts\Activate.ps1
```

## Run a child project

`uv run` can be called from the child directory without creating another
environment:

```bash
cd Practice/day3
uv run main.py
```

To verify which interpreter is active:

```bash
uv run python -c "import sys; print(sys.executable)"
```

It should print a path ending in `RAG_Journey\.venv\Scripts\python.exe`.

Do not use `source` with `python.exe`; `source` is for shell activation
scripts. On Windows Git Bash, use `source .venv/Scripts/activate` from the
repository root, or run the executable directly with `uv run`.
