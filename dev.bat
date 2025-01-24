@echo off
poetry run pytest . && allure serve .\allure-results\