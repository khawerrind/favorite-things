flake8:
	docker-compose exec api flake8 . --exclude=.svn,CVS,.bzr,.hg,.git,__pycache__,.tox,venv,static,frontend,.vscode,migrations

eslint:
	docker-compose exec api bash -c 'cd frontend && npm run lint'

test:
	docker-compose exec api ./manage.py test

deploy:
	cd frontend
	rm -r dist
	npm install
	npm run build
	cd ../
	pip install -r requirements.txt
	pip install zappa==0.48.2
	zappa deploy dev
	zappa manage dev migrate
	zappa manage dev loaddata categories
	python manage.py collectstatic --noinput -i admin -i rest_framework
