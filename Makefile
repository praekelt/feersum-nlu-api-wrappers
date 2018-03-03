help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    deps        	Ensure dependencies are installed."
	@echo  "    requirements	Update requirements files."
	@echo  "    update_spec 	Generate updated api code."

requirements:
	@pip-compile -o requirements.txt etc/requirements.in -U

deps:
	@pip-sync requirements.txt

update_spec:
	@swagger-codegen generate -i spec/swagger.yaml -l python -c spec/swagger_codegen-python_config.json -o spec/build
	rm -rf docs
	rm -rf feersum_nlu
	cp -a spec/build/docs .
	cp -a spec/build/feersum_nlu .

