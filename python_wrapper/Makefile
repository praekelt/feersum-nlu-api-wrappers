help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    deps			Ensure dependencies are installed."
	@echo  "    requirements	Update requirements files."

requirements:
	@pip-compile -o requirements.txt etc/requirements.in -U

deps:
	@pip-sync requirements.txt
