# Ad_Targeting_Project_NSDC

## Setup Instructions

### 1. Install Dependencies

The project uses a virtual environment to manage dependencies. To set up:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Download the Dataset

Download the advertising dataset from Kaggle:
- **Link**: https://www.kaggle.com/datasets/hiimanshuagarwal/advertising-ef
- Place the CSV file in the project directory as `advertising.csv`

### 3. Run the Notebook

**Option A: Using the run script (executes all cells)**
```bash
source venv/bin/activate  # Activate venv first
python3 run_notebook.py
```

**Option B: Using Jupyter Notebook**
```bash
source venv/bin/activate
jupyter notebook Ad_Targeting.ipynb
```

**Option C: Using Google Colab**
- Upload the notebook to Google Colab
- Upload the dataset to your Google Drive
- Update the dataset path in the notebook if needed

## Project Structure

- `Ad_Targeting.ipynb` - Main Jupyter notebook with the complete analysis
- `requirements.txt` - Python package dependencies
- `run_notebook.py` - Script to execute all notebook cells programmatically
- `advertising.csv` - Dataset file (download from Kaggle)

## Notes

- The notebook has been modified to work both locally and in Google Colab
- All code cells and answer sections have been completed
- The virtual environment ensures package isolation and avoids permission issues