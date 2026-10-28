A small task-manager REST API used in the "From Code to Cloud" workshop.

## Run locally

From PowerShell on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If `(.venv)` is already shown in the prompt, the virtual environment is
already active and the activation command can be skipped.

On macOS or Linux, activate the environment with:

```bash
source .venv/bin/activate
```