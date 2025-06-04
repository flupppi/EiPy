import json

path = "02_netana_ex04.ipynb"

with open(path, "r", encoding="utf-8") as f:
    notebook = json.load(f)

# Fix nbformat version
if notebook.get("nbformat", 0) > 4:
    print(f"Downgrading nbformat version from {notebook['nbformat']} to 4")
    notebook["nbformat"] = 4
    notebook["nbformat_minor"] = 5  # safe baseline

# Add language_info if missing
metadata = notebook.setdefault("metadata", {})
if "language_info" not in metadata:
    metadata["language_info"] = {
        "codemirror_mode": {"name": "ipython", "version": 3},
        "file_extension": ".py",
        "mimetype": "text/x-python",
        "name": "python",
        "nbconvert_exporter": "python",
        "pygments_lexer": "ipython3",
        "version": "3.12.10"
    }

# Write fixed file (overwrite original or write to new one)
fixed_path = path  # or path.replace(".ipynb", "_fixed.ipynb")
with open(fixed_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=1)

print(f"Notebook '{fixed_path}' fixed.")
