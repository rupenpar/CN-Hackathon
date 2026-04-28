"""Security policy configuration for the Guardrail Engine."""

# Actions that are strictly forbidden.
BLOCKED_ACTIONS = [
    "delete_logs",
    "shutdown_server",
]

# Actions that require a human approval workflow.
APPROVAL_REQUIRED = [
    "transfer_money",
    "access_finance",
]
