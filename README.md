# ml-course

Minimal ML project scaffold for learning and experiments.

Setup

1. Create a virtual environment and activate it (macOS / Linux):

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Or without activating the venv, you can install directly into it:

```bash
python3 -m venv venv
./venv/bin/python -m pip install --upgrade pip
./venv/bin/python -m pip install -r requirements.txt
```

Try it

- Run the sample script:

```bash
./venv/bin/python -m src.main
```

- Or run the tests (from project root):

```bash
./venv/bin/python -m pytest -q
```

Continuous Integration

This project includes a minimal GitHub Actions workflow that runs tests on push and pull requests to `main`.

Files added:

- `.github/workflows/ci.yml` — runs tests using a Python 3.10/3.11/3.12 matrix.

To initialize the git repo locally and push to GitHub (replace <your-repo-url> with your repository URL):

```bash
git init
git branch -M main
git add .
git commit -m "chore: initial project scaffold"
git remote add origin <your-repo-url>
git push -u origin main
```

If you prefer to use the GitHub CLI and create a new repo from the command line:

```bash
gh repo create my-org-or-username/ml-course --public --source=. --remote=origin --push
```
