from mcp.server.fastmcp import FastMCP
import json
from datetime import datetime

mcp = FastMCP(host="0.0.0.0", stateless_http=True)


@mcp.tool()
def validate_transaction(amount: float, currency: str = "AUD", merchant_category: str = "general", customer_risk_level: str = "medium") -> dict:
    """Validate a financial transaction against risk rules.
    Args:
        amount (float): Transaction amount.
        currency (str): Currency code (AUD, USD, EUR, GBP).
        merchant_category (str): Category: general, gambling, crypto, high_risk, electronics.
        customer_risk_level (str): Customer risk: low, medium, high.
    Returns:
        Dictionary with validation result, risk score, and any flags.
    """
    flags = []
    risk_score = 0

    # Amount-based rules
    if amount > 10000:
        flags.append("HIGH_VALUE_TRANSACTION")
        risk_score += 3
    if amount > 50000:
        flags.append("REPORTING_THRESHOLD_EXCEEDED")
        risk_score += 2

    # Category-based rules
    high_risk_categories = {"gambling": 3, "crypto": 2, "high_risk": 4}
    if merchant_category in high_risk_categories:
        flags.append(f"HIGH_RISK_CATEGORY_{merchant_category.upper()}")
        risk_score += high_risk_categories[merchant_category]

    # Customer risk adjustment
    risk_multiplier = {"low": 0.5, "medium": 1.0, "high": 2.0}
    risk_score = int(risk_score * risk_multiplier.get(customer_risk_level, 1.0))

    # Decision
    if risk_score >= 7:
        decision = "BLOCKED"
    elif risk_score >= 4:
        decision = "REVIEW_REQUIRED"
    else:
        decision = "APPROVED"

    return {
        "decision": decision,
        "risk_score": min(risk_score, 10),
        "flags": flags,
        "amount": amount,
        "currency": currency,
        "timestamp": datetime.now().isoformat(),
    }


@mcp.tool()
def check_sanctions(entity_name: str) -> dict:
    """Check if an entity appears on sanctions lists.
    Args:
        entity_name (str): Name of person or organization to check.
    Returns:
        Dictionary with sanctions check result.
    """
    # Simulated sanctions list for demo
    sanctioned = ["north star trading", "shadow finance ltd", "blocked entity corp"]
    is_match = entity_name.lower() in sanctioned

    return {
        "entity": entity_name,
        "is_sanctioned": is_match,
        "lists_checked": ["OFAC SDN", "UN Consolidated", "AU DFAT", "EU Sanctions"],
        "timestamp": datetime.now().isoformat(),
        "action": "BLOCK_TRANSACTION" if is_match else "CLEAR",
    }


@mcp.tool()
def get_customer_risk_profile(customer_id: str) -> dict:
    """Retrieve customer risk profile for transaction decisioning.
    Args:
        customer_id (str): Customer identifier.
    Returns:
        Dictionary with customer risk profile.
    """
    # Simulated customer profiles
    profiles = {
        "CUST-4421": {"name": "John Smith", "risk_level": "high", "kyc_status": "verified", "daily_limit": 5000, "flags": ["velocity_alert", "geo_mismatch"]},
        "CUST-7832": {"name": "Sarah Chen", "risk_level": "low", "kyc_status": "verified", "daily_limit": 50000, "flags": []},
        "CUST-9156": {"name": "Mike Johnson", "risk_level": "medium", "kyc_status": "pending_review", "daily_limit": 20000, "flags": ["large_transactions"]},
    }
    profile = profiles.get(customer_id, {"name": "Unknown", "risk_level": "high", "kyc_status": "not_found", "daily_limit": 0, "flags": ["unknown_customer"]})
    profile["customer_id"] = customer_id
    return profile


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
