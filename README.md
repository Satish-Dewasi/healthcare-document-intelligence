# AI-Powered Healthcare Document Intelligence System

An AI-powered system for analyzing healthcare documents using OCR, NLP, and Transformer-based models.

## Project Overview

The system will process medical documents such as prescriptions, lab reports, and discharge summaries.

The planned pipeline is:

Document
↓
OCR
↓
Extracted Text
↓
Document Classification
↓
Medical Entity Extraction
↓
Structured JSON

## Architecture

The project uses a monorepo structure with separate services for:

- Python ML service
- Java Spring Boot backend

The Python service will handle OCR, NLP preprocessing, document classification, and medical entity extraction.

The Spring Boot service will act as the application/backend layer and communicate with the Python ML service through HTTP APIs.

## Repository Structure

```text
healthcare-document-intelligence/
├── ml-service/
├── backend/
├── sample-documents/
└── docs/
