test-watch:
	@watch --interval=2 python3 -m unittest discover --pattern='*_tests.py';

install:
	@pip install -r requirements.txt;

venv:
	@python3 -m venv venv;
	@echo "To use this project's version of python run the following..."
	@echo ". venv/bin/activate && which python"
