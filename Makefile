.PHONY: help
help: ## Show help menu
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-35s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: dev
dev: ## Run development
	@bash uvicorn.sh

.PHONY: build
build: ## [ENVIRONMENT] Build new Docker image sparkui-middleware
	@docker build -t matheusjerico/weather-api:latest -f environment/Dockerfile .

.PHONY: run
run: ## [ENVIRONMENT] Run locally to test executation of a container
	@docker run  -p 8000:8000 matheusjerico/weather-api:latest

.PHONY: push
push: ## [ENVIRONMENT] Push a Docker image sparkui-middleware
	@docker push matheusjerico/weather-api:latest
