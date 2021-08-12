install:
	poetry install

run:
	poetry run hypercorn main.py

load:
	ab -c 10 -n 1000 http://127.0.0.1:8000/ping