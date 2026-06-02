# Bedrock AgentCore with Strands Agents SDK and Nova Pro — FSI Edition

This workshop provides hands-on experience with Amazon Bedrock AgentCore, demonstrating how to build sophisticated AI agents using various tools and runtime environments — all framed around Financial Services Industry (FSI) use cases. You'll learn to integrate code interpreters, browser automation, memory capabilities, and deploy scalable agent solutions.

## Workshop Overview

The workshop consists of 6 progressive labs that build upon each other:

| Lab | Title | Description | Key Learning Points | Directory |
|-----|-------|-------------|--------------------:|-----------|
| **Lab 0** | Getting Started with Strands Agents | Introduction to Strands Agents with FSI tools (loan calculator, stock lookup, FX rates) | • Learn Strands Agents fundamentals<br>• Create your first AI agent<br>• Build custom financial tools<br>• Understand the agent loop and conversation memory | [00-strands-agents-fsi/](./00-strands-agents-fsi/) |
| **Lab 1** | Code Interpreter Integration | Integrate Strands Agents with AgentCore Code Interpreter for dynamic financial analysis | • Fraud detection on transaction data<br>• Portfolio risk analysis (sector concentration, P&L)<br>• Custom Code Interpreter with network access<br>• Live market data via yfinance | [01-agentcore-code-interpreter-fsi/](./01-agentcore-code-interpreter-fsi/) |
| **Lab 2** | Browser Automation | Use AgentCore Browser to navigate financial websites and extract regulatory data | • Create custom browser with public network<br>• Navigate RBA website with Playwright<br>• Extract monetary policy information<br>• Browser fetch + Agent summarize pattern | [02-agentcore-browser-fsi/](./02-agentcore-browser-fsi/) |
| **Lab 4** | MCP Server Deployment | Deploy transaction validation tools as a managed MCP server with authentication | • Build FSI MCP server (validate, sanctions, risk profile)<br>• Set up Cognito authentication<br>• Deploy to AgentCore Runtime<br>• Connect Strands Agent to deployed server | [04-agentcore-runtime-mcp-fsi/](./04-agentcore-runtime-mcp-fsi/) |
| **Lab 5** | Agent Runtime with Observability | Deploy Strands Agents to AgentCore Runtime with comprehensive tracing for compliance | • Deploy agent with tools to AgentCore Runtime<br>• Invoke via boto3 with IAM auth<br>• View traces in CloudWatch (audit trail)<br>• GenAI Observability for FSI compliance | [05-agentcore-runtime-observability-fsi/](./05-agentcore-runtime-observability-fsi/) |
| **Lab 6** | Memory Integration | Integrate persistent memory for client context across sessions | • Three memory strategies (summary, preference, semantic)<br>• Store rich FSI client conversations<br>• Memory-enabled agent for personalized responses<br>• Session handover demo | [06-agentcore-memory-fsi/](./06-agentcore-memory-fsi/) |

## Prerequisites

Before starting the workshop, ensure you have:

- **AWS Account** with appropriate permissions for Bedrock AgentCore and related services
  - `BedrockAgentCoreFullAccess` managed policy
  - `AmazonBedrockFullAccess` managed policy
  - `CloudWatchFullAccessV2` managed policy
  - `Caller permissions`: See detailed policy [here](https://github.com/aws/bedrock-agentcore-starter-toolkit/blob/main/documentation/docs/user-guide/runtime/permissions.md#developercaller-permissions)
- [Enable CloudWatch Transaction Search](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-configure.html#observability-configure-builtin) for AgentCore Observability
- **AWS Credentials** configured (IAM role or environment variables)
- **Python Environment** with required packages (listed in `pyproject.toml` and instructions in each notebook)

### AWS Regions

We suggest using `ap-southeast-2` (Sydney) for this workshop to align with FSI customers in Australia. Bedrock AgentCore is available in specific AWS regions — ensure you're working in a supported region.

### Environment Setup

```bash
git clone https://github.com/Zohaib-AWSCloud/Strands_Agent.git
cd Strands_Agent
uv sync
uv run jupyter lab
```

If not using an IAM role, configure your AWS credentials:

```python
import os

os.environ["AWS_ACCESS_KEY_ID"] = "<YOUR_ACCESS_KEY>"
os.environ["AWS_SECRET_ACCESS_KEY"] = "<YOUR_SECRET_KEY>"
os.environ["AWS_SESSION_TOKEN"] = "<OPTIONAL_SESSION_TOKEN>"
os.environ["AWS_REGION"] = "<AWS_REGION>"
```

## Workshop Structure

```
Strands_Agent/
├── README.md
├── pyproject.toml
├── data/
│   ├── transactions.csv                   # 25 transactions with fraud patterns
│   └── portfolio.csv                      # Client portfolios (Vanguard, Block)
├── 00-strands-agents-fsi/
│   └── 00-strands-agents-fsi.ipynb
├── 01-agentcore-code-interpreter-fsi/
│   └── 01-agentcore-code-interpreter-fsi.ipynb
├── 02-agentcore-browser-fsi/
│   └── 02-agentcore-browser-fsi.ipynb
├── 04-agentcore-runtime-mcp-fsi/
│   ├── 04-agentcore-runtime-mcp-fsi.ipynb
│   └── mcp_server.py
├── 05-agentcore-runtime-observability-fsi/
│   ├── 05-agentcore-runtime-observability-fsi.ipynb
│   └── strands_agent.py
└── 06-agentcore-memory-fsi/
    └── 06-agentcore-memory-fsi.ipynb
```

## FSI Use Cases

| Customer Type | Use Cases Demonstrated |
|---------------|----------------------|
| **BNPL / Payments** (Afterpay) | Fraud detection, transaction validation, regulatory monitoring (ASIC) |
| **Fintech Platform** (Block) | Multi-currency operations, cost optimization, platform monitoring |
| **Asset Management** (Vanguard) | Portfolio risk analysis, ESG compliance, client advisory with memory |

## References

- [Strands Agents Documentation](https://strandsagents.com/)
- [Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [Original Workshop](https://github.com/aws-samples/sample-bedrock-agentcore-with-strands-and-nova)
- [AgentCore Starter Toolkit](https://github.com/aws/bedrock-agentcore-starter-toolkit)
