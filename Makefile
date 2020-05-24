message="changes"

push:
	git add .
	git commit -a -m $(message)
	git push origin master

format:
	black collider/ examples/

test:
	python -m unittest discover -v

coverage:
	coverage run -m unittest discover -v
	coverage report --skip-empty -m
	rm .coverage

update: format test push

setup:
	pip3 install virtualenv
	virtualenv -p $(shell which python3) venv
	bash -c "source venv/bin/activate && pip install -r requirements.txt"
