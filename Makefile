init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

test:
	#pipenv install --dev
	pipenv run pytest tests --doctest-glob='*.rst'

publish:
	pip install 'twine>=1.5.0'
	python setup.py sdist
	python setup.py bdist_wheel --universal
	twine upload dist/*
	rm -fr build dist .egg icssplit.egg-info
