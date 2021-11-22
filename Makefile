test-watch:
	@watch --interval=2 python3 -m unittest discover --pattern='*_tests.py';

install:
	@pip install -r requirements.txt;

venv:
	@python3 -m venv venv;
	@echo "To use this project's version of python run the following..."
	@echo ". venv/bin/activate && which python"

fizzbuzz.console:
	# make fizzbuzz.console start=1 length=100
	@python3 fizzbuzz.py console $(start) $(length);

fizzbuzz.file:
	@python3 fizzbuzz.py file $(start) $(length);
