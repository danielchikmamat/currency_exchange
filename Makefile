# Configuration
PYTHON := python3
VENV := .venv
BIN := $(VENV)/bin
APP := app.main:app
HOST := 0.0.0.0
PORT := 8000

.PHONY: help venv install run dev test clean

help:
	@echo "Available targets:"
	@echo "  make venv     Create virtual environment"
	@echo "  make install  Install dependencies"
	@echo "  make run      Run FastAPI app"
	@echo "  make dev      Run FastAPI with reload"
	@echo "  make test     Run tests"
	@echo "  make clean    Remove virtual environment"

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV)

# Install dependencies
install: venv
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt

# Run FastAPI (no reload)
run:
	$(BIN)/uvicorn $(APP) --host $(HOST) --port $(PORT)

# Run FastAPI with auto-reload (development)
dev:
	$(BIN)/uvicorn $(APP) --host $(HOST) --port $(PORT) --reload

# Run tests
test:
	$(BIN)/pytest -s

# Remove virtual environment
clean:
	rm -rf $(VENV)
