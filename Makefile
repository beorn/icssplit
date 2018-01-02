init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

install:
	pipenv run python setup.py develop

test:
	pipenv install --dev
	@# have to run as module instead of pytest to get '.' added to sys.path[]
	pipenv run python -m pytest tests --doctest-glob='*.rst' # or tox

build:
	pipenv install wheel
	pipenv run python setup.py bdist_wheel

publish:
	pipenv pip install 'twine>=1.5.0'
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel
	#gpg --detach-sign -a dist/package-1.0.1.tar.gz
	#twine upload dist/package-1.0.1.tar.gz package-1.0.1.tar.gz.asc
	pipenv run twine upload dist/*
	rm -fr build dist .egg icssplit.egg-info
