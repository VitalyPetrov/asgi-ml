check: check-imports check-format


check-imports:
	@isort -rc -c src


check-format:
	@flake8 src


fix: fix-imports fix-format


fix-imports:
	@isort -rc -y src


fix-format:
	@black src
