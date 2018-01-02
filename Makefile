init:
	pip install pipenv
	pipenv lock
	pipenv install --dev

install:
	pipenv run python setup.py develop

test:
	pipenv install --dev
	# have to run as module instead of pytest to get '.' added to sys.path[]
	pipenv run python -m pytest tests --doctest-glob='*.rst' # or tox

version:
	# 1) Update 3 places in icssplit.py, setup.py
	# 2) git add -A && git ci -m "..."
	# 3) git tag 0.1 -m "...
	# 4) git push --tags origin master # triggers travis
	# 5) make pipy_upload

pypi_upload:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel
	#gpg --detach-sign -a dist/package-1.0.1.tar.gz
	pipenv run python setup.py sdist upload
	rm -fr build dist .egg icssplit.egg-info
