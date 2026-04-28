# Ai GuardRail System

A modular, Flask-based security layer designed to monitor, evaluate, and control AI agent actions in real-time. This engine acts as an intermediary, preventing semantic privilege escalation by ensuring all AI requests comply with organizational security policies before execution.

## Features
* **Real-time Interception:** Catches and evaluates AI agent requests.
* **Policy-Based Routing:** Classifies actions as `ALLOWED`, `BLOCKED`, or `HUMAN_APPROVAL_REQUIRED`.
* **Modular Architecture:** Clean separation of configuration, business logic, and routing.
* **Lightweight REST API:** Easy to integrate with existing AI agent workflows.

## Project Structure
* `config.py` - Defines security policies and restricted action lists.
* `services.py` - Core logic for evaluating actions against the defined policies.
* `app.py` - Flask application setup, JSON parsing, and routing (`/agent_action`).
* `run.py` - Entry point to start the development server.
