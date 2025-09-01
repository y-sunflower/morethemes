.PHONY: all

readme:
	quarto render docs/README.qmd --output-dir ..

index:
	quarto render docs/index.qmd

coverage:
	uv run coverage run --source=morethemes -m pytest
	uv run coverage report -m
	uv run coverage xml
	uv run genbadge coverage -i coverage.xml
	rm coverage.xml

preview:
	uv run mkdocs serve

test:
	uv run pytest
