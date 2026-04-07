# Incident Notes API

A small API for registering and querying operational incidents in a fictional system, designed as a practical Azure learning lab with a simple, modern, and low-cost stack.

## Objective

The goal of this project is to practice a realistic Azure workflow without building an unnecessarily complex architecture or depending on a managed relational database.

The idea is to use an easy-to-understand use case to work with:

- API deployment
- cloud persistence
- observability
- secrets management
- service-to-service authentication
- cost control

## Use Case

The API represents an internal tool used by a technical team to register incidents affecting different services.

Examples of incidents:

- increased latency in an API
- intermittent authentication errors
- partial service outage
- issues detected manually through monitoring

Each incident is stored as an independent document with information such as:

- title
- affected service
- severity
- status
- owner
- tags
- notes
- additional metadata

## Stack

- FastAPI
- Azure Cosmos DB
- Azure App Service
- Azure Key Vault
- Azure Monitor / Application Insights
- Managed Identity
- python-dotenv

## Why FastAPI

FastAPI was chosen because this project does not need an ORM or relational migrations.

The focus is on:

- exposing HTTP endpoints
- validating payloads
- working with JSON documents
- integrating cleanly with Azure services

## Why Cosmos DB

Cosmos DB was chosen because the use case fits well with self-contained documents and avoids the need to model complex relationships.

Each incident can live as an independent document, which keeps the design simple for this lab.

## Initial Scope

The first version of the API should allow:

- creating incidents
- listing incidents
- retrieving an incident by id
- updating basic fields
- adding notes to an incident
- filtering by status, severity, or service

## Example Document

```json
{
  "id": "inc_001",
  "title": "API latency spike during peak hours",
  "service": "billing-api",
  "severity": "high",
  "status": "open",
  "reported_at": "2026-04-07T18:30:00Z",
  "owner": "augusto",
  "tags": ["latency", "production"],
  "notes": [
    {
      "at": "2026-04-07T18:35:00Z",
      "text": "Latency increase detected on /invoices"
    }
  ],
  "metadata": {
    "region": "westeurope",
    "source": "manual"
  }
}
```

## Current Status

At this point, the project already has:

- GitHub repository created
- local environment ready
- `.gitignore`
- dependencies installed
- minimal `main.py` working
- API running correctly in local development

## Installation

Create and activate the virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

## Run the API Locally

```bash
uvicorn main:app --reload
```

Then open:

- `http://127.0.0.1:8000`
- `http://127.0.0.1:8000/docs`

## Next Steps

- define the base project structure
- create Pydantic schemas
- create initial routes
- implement Cosmos DB access
- build the basic incident CRUD
- prepare environment-based configuration
- deploy to Azure
- add observability
- integrate secrets with Key Vault

## Project Philosophy

This project is not meant to be big or complex.

It is meant to be:

- small
- clear
- useful for learning
- inexpensive to maintain
- close to a real Azure workflow

## Note

The priority of this project is to use Azure as much as possible without introducing components that make the lab more complex or create unnecessary costs.
