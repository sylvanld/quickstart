
host	?= localhost
port	?= 8000
serve:
	uvicorn --port $(port) --host $(host) {{ project_key }}.asgi:api
