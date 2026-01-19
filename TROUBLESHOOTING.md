# 🔧 Troubleshooting Guide

## ❌ Pandas Import Error (Current Issue)

### Problem:
```
AttributeError: partially initialized module 'pandas' from 'C:\Users\Dhathri M\AppData\Local\Programs\Python\Python313\pandas.py' has no attribute 'DataFrame'
```

### Cause:
There's a file named `pandas.py` in your Python directory that conflicts with the pandas library.

### ✅ Solution:

**Option 1: Rename the conflicting file (Recommended)**
```powershell
# In PowerShell, navigate to:
cd "C:\Users\Dhathri M\AppData\Local\Programs\Python\Python313\"

# Rename the file:
Rename-Item pandas.py pandas_old.py
```

**Option 2: Delete the conflicting file**
```powershell
# Only if you're sure you don't need it:
Remove-Item "C:\Users\Dhathri M\AppData\Local\Programs\Python\Python313\pandas.py"
```

After fixing, restart the backend server.

---

## Alternative: Run Without Environment Conflicts

If you continue to have issues, you can create a **virtual environment** to avoid conflicts:

### Using Virtual Environment (Best Practice)

```powershell
# Navigate to project backend folder
cd "C:\Users\Dhathri M\OneDrive\Desktop\1m1b projecct\backend"

# Create virtual environment
python -m venv venv

# Activate it
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

This creates an isolated Python environment without conflicts!

---

## Other Common Issues

### Backend Won't Start
- Check if port 8000 is already in use
- Verify all dependencies installed: `pip list`
- Check Python version: `python --version` (need 3.8+)

### No Documents Loaded
- Ensure `.txt` files exist in `documents/` folder
- Check file encoding is UTF-8
- Restart backend after adding documents

### Frontend Can't Connect
- Verify backend is running on http://localhost:8000
- Check browser console for errors (F12)
- Try accessing http://localhost:8000/health directly

### Slow Performance
- First query is slow (model loading)
- Subsequent queries should be fast
- Reduce document size if needed

---

## Quick Test Commands

### Test Backend is Running:
```powershell
# In browser or PowerShell:
curl http://localhost:8000/health
```

Should return: `{"status":"healthy"}`

### Test Document Loading:
```powershell
curl http://localhost:8000/documents
```

Should list your loaded documents.

---

## Need Help?

1. Check if pandas.py exists in your Python directory
2. Use a virtual environment (recommended)
3. Ensure all dependencies are installed
4. Check the full README.md for detailed setup


