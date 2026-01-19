@echo off
echo ========================================
echo   Green Policy Chatbot - Frontend
echo ========================================
echo.
echo Starting frontend server on http://localhost:3000
echo.
echo Make sure the backend is running first!
echo.

cd frontend
python -m http.server 3000

pause

