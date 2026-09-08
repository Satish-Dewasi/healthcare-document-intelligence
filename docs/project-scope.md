# Project Scope — V1 MVP

## Project

AI-Powered Healthcare Document Intelligence & Classification System

## Objective

Build an AI-powered system that processes healthcare documents and produces structured information using OCR, Transformer-based document classification, and medical Named Entity Recognition (NER).

## V1 Input

The system will support:

- PDF documents
- Images

## V1 Document Categories

The document classification model will initially support four categories:

1. Prescription
2. Lab Report
3. Discharge Summary
4. Medical Report

## V1 Medical Entities

The initial NER model will extract:

- DRUG
- DISEASE
- SYMPTOM
- DOSAGE
- PROCEDURE

## Processing Pipeline

```text
Document
    ↓
OCR
    ↓
Extracted Text
    ↓
Document Classification
    ↓
Medical NER
    ↓
Post-processing
    ↓
Structured JSON
