"""Core guardrail evaluation logic."""

from config import APPROVAL_REQUIRED, BLOCKED_ACTIONS


def evaluate_action(action: str) -> dict:
    """Evaluate a requested agent action against configured security policies."""
    normalized_action = action.strip()

    if normalized_action in BLOCKED_ACTIONS:
        return {
            "status": "BLOCKED",
            "reason": "Security policy violation",
        }

    if normalized_action in APPROVAL_REQUIRED:
        return {
            "status": "HUMAN_APPROVAL_REQUIRED",
        }

    return {
        "status": "ALLOWED",
    }
