import sys
import os

print("--- ENVIRONMENT VERIFICATION ---")
# This verifies that Python is using your root .venv folder, not your system
print(f"Python Executive Path: {sys.executable}")

try:
    import dotenv
    print("✅ Success: 'python-dotenv' package found in root environment!")
except ImportError:
    print("❌ Error: Package not found.")

