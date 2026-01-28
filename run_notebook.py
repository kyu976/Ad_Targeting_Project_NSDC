#!/usr/bin/env python3
"""
Script to execute all cells in the Jupyter notebook
"""
import json
import sys
import subprocess
import tempfile
import os

def execute_notebook(notebook_path):
    """Execute all code cells in a Jupyter notebook"""
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Extract and execute code cells
    code_cells = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            if source.strip():  # Only add non-empty cells
                code_cells.append(source)
    
    # Combine all code into a single script
    full_script = '\n\n'.join(code_cells)
    
    # Create a temporary Python file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(full_script)
        temp_script = f.name
    
    try:
        # Execute the script
        print("Executing notebook cells...")
        # Try to use venv python if available, otherwise use system python
        venv_python = os.path.join(os.path.dirname(notebook_path) or '.', 'venv', 'bin', 'python3')
        if os.path.exists(venv_python):
            python_exec = venv_python
            print("Using virtual environment Python")
        else:
            python_exec = sys.executable if sys.executable else 'python3'
            print("Using system Python")
        
        result = subprocess.run(
            [python_exec, temp_script],
            cwd=os.path.dirname(notebook_path) or '.',
            capture_output=False,
            text=True
        )
        return result.returncode
    finally:
        # Clean up
        if os.path.exists(temp_script):
            os.unlink(temp_script)

if __name__ == '__main__':
    notebook_path = 'Ad_Targeting.ipynb'
    if not os.path.exists(notebook_path):
        print(f"Error: {notebook_path} not found")
        sys.exit(1)
    
    exit_code = execute_notebook(notebook_path)
    sys.exit(exit_code)
