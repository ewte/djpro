@echo off
python manage.py makemigrations
IF %ERRORLEVEL% NEQ 0 (
    echo "Произошла ошибка при выполнении команды makemigrations"
    exit /b %ERRORLEVEL%
)
python manage.py migrate