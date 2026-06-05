from mcp.server.fastmcp import FastMCP
from ddgs import DDGS
from ddgs.exceptions import RatelimitException, DDGSException

mcp = FastMCP(host="0.0.0.0", stateless_http=True)


@mcp.tool()
def websearch(keywords: str, region: str = "us-en", max_results: int | None = None) -> list:
    """Search the web to get updated information.
    Args:
        keywords (str): The search query keywords.
        region (str): The search region: wt-wt, us-en, uk-en, ru-ru, etc..
        max_results (int | None): The maximum number of results to return.
    Returns:
        List of dictionaries with search results.
    """
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except RatelimitException:
        return "RatelimitException: Please try again after a short delay."
    except DDGSException as d:
        return f"DuckDuckGoSearchException: {d}"
    except Exception as e:
        return f"Exception: {e}"


@mcp.tool()
def validate_bsb(bsb: str) -> dict:
    """Validate an Australian BSB (Bank-State-Branch) number and identify the bank.
    Args:
        bsb (str): The BSB number to validate (e.g., "062-000" or "062000").
    Returns:
        Dictionary with validation result, bank name, and details.
    """
    bsb_bank_map = {
        "01": "ANZ Banking Group", "03": "Westpac Banking Corporation",
        "06": "Commonwealth Bank of Australia", "08": "National Australia Bank",
        "09": "Reserve Bank of Australia", "12": "Bank of Queensland",
        "18": "Macquarie Bank", "30": "Bankwest", "33": "St George Bank",
        "34": "HSBC Bank Australia", "42": "Deutsche Bank", "48": "Rabobank",
        "55": "Bank of China", "73": "Westpac (BankSA/St George)",
        "76": "Commonwealth Bank (Bankwest)", "92": "Westpac (BankSA)",
    }
    clean = bsb.replace("-", "").replace(" ", "")
    if len(clean) != 6 or not clean.isdigit():
        return {"valid": False, "error": "BSB must be 6 digits"}
    prefix = clean[:2]
    bank = bsb_bank_map.get(prefix)
    formatted = f"{clean[:3]}-{clean[3:]}"
    if bank:
        return {"valid": True, "bsb": formatted, "bank": bank}
    return {"valid": False, "bsb": formatted, "error": f"Unknown bank prefix: {prefix}"}


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
