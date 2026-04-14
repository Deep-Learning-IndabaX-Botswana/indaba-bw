# PythonAnywhere Deployment Guide

## Step-by-Step Instructions

### 1. Create a PythonAnywhere Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up for a free account

### 2. Clone Your Repository
- Log in to PythonAnywhere
- Open a Bash console (New console → Bash)
- Clone your GitHub repository:
  ```bash
  git clone https://github.com/YOUR_USERNAME/indaba-bw.git
  ```

### 3. Create a Virtual Environment
```bash
cd indaba-bw
mkvirtualenv --python=/usr/bin/python3.10 indaba-bw
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure a Web App
- Go to **Web** in the PythonAnywhere dashboard
- Click **Add a new web app**
- Choose "Manual configuration" and Python 3.10
- PythonAnywhere will create a WSGI config file

### 6. Edit the WSGI Configuration File
- Open the WSGI config file (usually at `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
- Replace the contents with:

```python
import sys
path = '/home/yourusername/indaba-bw'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

### 7. Configure Source Code Location
- In the Web tab, under "Code":
  - Source code: `/home/yourusername/indaba-bw`
  - Working directory: `/home/yourusername/indaba-bw`

### 8. Link Virtual Environment
- In the Web tab, under "Virtualenv":
  - Path to virtualenv: `/home/yourusername/.virtualenvs/indaba-bw`

### 9. Reload Your Web App
- Click the "Reload" button in the Web tab
- Your app should now be live at `yourusername.pythonanywhere.com`

## Troubleshooting

- **Check error logs**: View logs in the Web tab to debug issues
- **Update requirements.txt**: Always keep dependencies listed
- **Static files**: Ensure static files path is configured if needed
- **Restart after changes**: Always reload after code changes

## Notes
- Free tier has limited resources
- Monitor error logs regularly
- Keep your git repository updated and sync changes regularly
