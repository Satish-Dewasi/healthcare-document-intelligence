# API Contract — V1

## Overview

This document defines the API contract between the Spring Boot backend and the FastAPI ML service.

The V1 API processes one healthcare document per request and returns document classification and medical entity extraction results.

---

## Analyze Document

### Endpoint

```http
POST /api/v1/analyze-document
