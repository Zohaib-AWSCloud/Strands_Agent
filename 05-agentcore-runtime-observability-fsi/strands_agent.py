from strands import Agent, tool
from strands.models import BedrockModel
from strands_tools import calculator
import boto3
from bedrock_agentcore.runtime import BedrockAgentCoreApp

app = BedrockAgentCoreApp()

# Setup Nova Pro model ID based on AWS region
NOVA_PRO_MODEL_ID = "us.amazon.nova-pro-v1:0"
region = boto3.session.Session().region_name
if region.startswith("eu"):
    NOVA_PRO_MODEL_ID = "eu.amazon.nova-pro-v1:0"
elif region.startswith("ap"):
    NOVA_PRO_MODEL_ID = "apac.amazon.nova-pro-v1:0"

@tool
def validate_transaction(amount: float, merchant_category: str = "general") -> str:
    '''Validate a transaction against risk rules.
    Args:
        amount: Transaction amount in AUD
        merchant_category: Category (general, crypto, gambling, high_risk)
    '''
    risk_score = 0
    flags = []
    if amount > 10000: flags.append("HIGH_VALUE"); risk_score += 3
    if merchant_category in ("crypto", "gambling"): flags.append(f"HIGH_RISK_{merchant_category.upper()}"); risk_score += 4
    decision = "BLOCKED" if risk_score >= 7 else "REVIEW" if risk_score >= 4 else "APPROVED"
    return f"Decision: {decision} | Risk: {risk_score}/10 | Flags: {flags}"

@tool
def get_account_balance(account_id: str) -> str:
    '''Get account balance.
    Args:
        account_id: Account identifier
    '''
    balances = {"ACC-001": "$125,430.50", "ACC-002": "$2,340,000.00", "ACC-003": "$45,200.75"}
    return f"Account {account_id}: Balance {balances.get(account_id, 'Not found')}"

agent = Agent(
    model=BedrockModel(model_id=NOVA_PRO_MODEL_ID, max_tokens=4096),
    system_prompt="You are a banking operations assistant. Validate transactions and check accounts. Be concise.",
    tools=[validate_transaction, get_account_balance, calculator],
)

@app.entrypoint
async def fsi_agent(payload, context):
    """Invoke the FSI agent with a payload"""
    user_input = payload.get("prompt", "No prompt found")
    response = agent(user_input)
    return response

if __name__ == "__main__":
    app.run()
