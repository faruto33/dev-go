.DEFAULT_GOAL := default
#################### PACKAGE ACTIONS ###################
reinstall_package:
	@pip uninstall -y encoder || :
	@pip install -e .

run_api:
	uvicorn api.fast:app --reload
