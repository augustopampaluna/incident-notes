# Incident Notes API

## Idea del proyecto

Este proyecto es una API pequeña orientada a registrar y consultar incidencias operativas de un sistema ficticio.

La idea no es construir una aplicación compleja de negocio, sino usar un caso simple, realista y fácil de entender para practicar servicios de Azure en un contexto cercano al trabajo real.

Cada incidencia se modela como un documento independiente, con información como título, servicio afectado, severidad, estado, notas y metadata adicional.

## Objetivo principal

Aprender Azure de forma práctica, montando una solución simple pero bien planteada, con foco en:

- despliegue de una API real
- persistencia en la nube
- observabilidad
- gestión segura de secretos
- autenticación entre servicios
- control de costes

La prioridad es usar Azure lo más posible sin introducir una base de datos relacional gestionada que complique el laboratorio o consuma crédito innecesariamente.

## Decisiones técnicas

### Framework
Se usará **FastAPI** en lugar de Django.

Motivos:
- no se necesita ORM
- no se necesitan migraciones
- el proyecto estará centrado en una API HTTP simple
- encaja mejor con documentos JSON y Cosmos DB
- reduce complejidad innecesaria

### Base de datos
Se usará **Azure Cosmos DB**.

Motivos:
- el caso de uso encaja bien con documentos independientes
- evita relaciones complejas y joins
- permite trabajar con un modelo NoSQL más alineado con este proyecto
- tiene sentido para una API de incidencias donde cada incidencia puede ser autocontenida

### Tipo de solución
La API estará orientada a documentos, no a entidades fuertemente relacionadas.

Cada incidencia será un documento con estructura similar a:

- id
- title
- service
- severity
- status
- reported_at
- owner
- tags
- notes
- metadata

## Stack previsto

- **FastAPI**
- **Azure Cosmos DB**
- **Azure App Service**
- **Azure Key Vault**
- **Azure Monitor / Application Insights**
- **Managed Identity**
- **python-dotenv** para desarrollo local

## Objetivos de aprendizaje en Azure

Este proyecto busca practicar:

### 1. Hosting de la API
Desplegar la API en Azure App Service.

### 2. Persistencia en NoSQL
Guardar y consultar incidencias en Cosmos DB.

### 3. Gestión de secretos
Guardar secretos y configuraciones sensibles en Key Vault.

### 4. Observabilidad
Registrar logs, métricas y trazas con Application Insights / Azure Monitor.

### 5. Seguridad entre servicios
Usar Managed Identity cuando sea posible para evitar credenciales hardcodeadas.

### 6. Cost control
Mantener la solución dentro del free tier o dentro del crédito inicial de Azure, evitando recursos innecesarios o costosos.

## Restricciones del proyecto

- no usar ORM relacional como centro de la solución
- no usar PostgreSQL como base principal
- evitar relaciones complejas
- evitar infraestructura cara o innecesaria
- mantener la solución pequeña, clara y entendible
- priorizar aprendizaje práctico sobre complejidad arquitectónica

## Caso de uso ficticio

La API representa una herramienta interna usada por un equipo técnico para registrar incidencias de servicios.

Ejemplos:
- aumento de latencia en una API
- errores intermitentes en autenticación
- caída parcial de un servicio
- problemas detectados manualmente durante monitoreo

Cada incidencia puede recibir notas, cambios de estado y etiquetas.

## Alcance inicial

La primera versión debería permitir:

- crear incidencias
- listar incidencias
- obtener una incidencia por id
- actualizar campos básicos de una incidencia
- añadir notas a una incidencia
- filtrar por estado, severidad o servicio

## Estructura conceptual del documento

Una incidencia debería ser un documento autocontenido, por ejemplo:

```json
{
  "id": "inc_001",
  "title": "API lenta en horario pico",
  "service": "billing-api",
  "severity": "high",
  "status": "open",
  "reported_at": "2026-04-07T18:30:00Z",
  "owner": "augusto",
  "tags": ["latency", "production"],
  "notes": [
    {
      "at": "2026-04-07T18:35:00Z",
      "text": "Se detecta aumento de latencia en /invoices"
    }
  ],
  "metadata": {
    "region": "westeurope",
    "source": "manual"
  }
}