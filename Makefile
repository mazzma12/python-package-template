.PHONY: test test-template clean help

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

test: install-test-deps ## Run template generation tests
	uv run python -m pytest tests/ -v

test-template: ## Test template generation with default values
	@echo "Testing template generation..."
	python -m cookiecutter . --no-input --output-dir /tmp --overwrite-if-exists
	@echo "Generated project structure:"
	ls -la /tmp/alpacasay/
	@echo "Testing Python syntax..."
	cd /tmp/alpacasay && python -m py_compile src/alpacasay/*.py tests/*.py
	@echo "Template test completed successfully!"

clean: ## Clean up test artifacts
	rm -rf /tmp/alpacasay /tmp/test_package /tmp/minimal_package /tmp/docs_package /tmp/docker_package /tmp/ci_package /tmp/publishing_package
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -rf {} +

install-test-deps: ## Install test dependencies
	uv sync --dev
