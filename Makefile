_checkfiles = examples/ feersum_nlu_util/
checkfiles = $(_checkfiles) *.py

mypy_flags = --ignore-missing-imports --follow-imports=silent --check-untyped-defs --warn-no-return --warn-unused-ignores

flake8_flags = --max-line-length=140 --exclude db_migrations

pylint_flags = --max-line-length=140
# pylint_flags = --max-line-length=140 --disable=E1126
# ! False positives ... python 3.5.3+ #1295 - https://github.com/PyCQA/pylint/issues/1295

help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    requirements	Update requirements files."
	@echo  "    deps        	Ensure dependencies are installed."
	@echo  "    update_spec 	Generate updated api code."

requirements:
	@pip-compile -o requirements.txt etc/requirements.in -U

deps:
	@pip-sync requirements.txt

check:
	@echo [setup.py check]:
	@python setup.py check -mrs
	# @echo [mypy]:
	# @mypy $(mypy_flags) --incremental $(_checkfiles)
	@echo [pylint]:
	@pylint -E $(pylint_flags) $(_checkfiles) # ! False positives ... python 3.5.3+ #1295 - https://github.com/PyCQA/pylint/issues/1295
	@echo [flake8]:
	@flake8 $(flake8_flags) $(checkfiles)

update_spec:
	-rm -rf swagger/build/docs
	-rm -rf swagger/build/feersum_nlu
	# @swagger-codegen generate -i swagger/swagger.yaml -l python -c swagger/swagger_codegen-python_config.json -o swagger/build
	# Use swagger-codegen 2.4.6 - has Python3.7 fix and still does swagger 2.0 named body params!!!
	#  - brew install swagger-codegen@2
	@/usr/local/opt/swagger-codegen\@2/bin/swagger-codegen generate -i swagger/swagger.yaml -l python -c swagger/swagger_codegen-python_config.json -o swagger/build
	rm -rf docs
	rm -rf feersum_nlu
	cp -a swagger/build/docs .
	cp -a swagger/build/feersum_nlu .

