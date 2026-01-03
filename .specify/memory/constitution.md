<!-- 
Sync Impact Report:
- Version change: N/A → 1.0.0
- Modified principles: N/A (new constitution)
- Added sections: All principles and sections
- Removed sections: N/A
- Templates requiring updates: ✅ .specify/templates/plan-template.md, ✅ .specify/templates/spec-template.md, ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->
# Todo CLI Project Constitution

## Core Principles

### Python 3.13+ and Clean Code
Use Python 3.13+ features and maintain clean, readable code following established best practices. All code must be well-structured, maintainable, and follow Python design patterns that enhance readability and reduce complexity.

### CLI Only Interface
The application is a command-line interface only with no GUI components. All interactions with the application must occur through command-line arguments and standard input/output streams.

### In-Memory Storage
Store all todo data in memory during runtime with no persistent storage. The application state exists only for the duration of the program execution and is lost when the program terminates.

### PEP8 Compliance
Follow PEP8 style guidelines for all Python code. All code must pass PEP8 linting checks and maintain consistency with Python style conventions to ensure readability and maintainability.

### Structured Todo Model
Each todo must have id, title, description, and completed status fields. The data model is fixed and must not be extended with additional fields beyond these four required attributes.

### Modular Code Structure
Split code into main.py, models.py, services.py with clear separation of concerns. Each module has a distinct responsibility: main.py handles CLI parsing, models.py defines data structures, and services.py contains business logic.

## Additional Constraints

No extra features beyond the specified requirements. The implementation must strictly adhere to the defined functionality without adding bells and whistles that weren't explicitly requested.

## Implementation Guidelines

Use dataclasses where appropriate for structured data representation. Dataclasses provide clean, readable code for representing structured data like todo items while reducing boilerplate code.

## Governance

Constitution supersedes all other practices; amendments require documentation and approval. All development must comply with these principles, and any deviation requires explicit amendment to this constitution with proper approval.

**Version**: 1.0.0 | **Ratified**: 2026-01-03 | **Last Amended**: 2026-01-03