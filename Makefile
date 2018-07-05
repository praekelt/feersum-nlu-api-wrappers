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

update_spec:
	-rm -rf swagger/build/docs
	-rm -rf swagger/build/feersum_nlu
	@swagger-codegen generate -i swagger/swagger.yaml -l python -c swagger/swagger_codegen-python_config.json -o swagger/build
	rm -rf docs
	rm -rf feersum_nlu
	cp -a swagger/build/docs .
	cp -a swagger/build/feersum_nlu .

