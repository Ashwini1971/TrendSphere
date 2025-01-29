@echo off
call venv\scripts\activate
pytest -sv "sanity" --html .\reports\test_report.html --browser firefox
pytest -sv "regression" --html .\reports\test_report.html --browser chrome
pytest -sv "sanity or regression" --html .\reports\test_report.html --browser chrome
pause