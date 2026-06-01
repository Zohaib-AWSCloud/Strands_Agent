# 🏦 FSI AgentCore Workshop: AI Agents for Financial Services

> A hands-on workshop demonstrating Amazon Bedrock AgentCore + Strands Agents SDK. The content in this workshop is aligned with Financial Services Customer for demo purposes.

## 🎯 What You'll Build

An AI agent that can:
- Calculate loan repayments and compare mortgage scenarios
- Detect fraud patterns in transaction data
- Monitor regulatory websites (APRA, ASX) for updates
- Run portfolio risk analysis (VaR, sector exposure)
- Remember client preferences across sessions
- Provide full audit trails for compliance

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Strands Agent (Brain)                  │
│  - Reasons about user requests                          │
│  - Decides which tools to call                          │
│  - Maintains conversation context                       │
└──────────┬──────────┬──────────┬──────────┬─────────────┘
           │          │          │          │
    ┌──────▼──┐ ┌─────▼────┐ ┌──▼───┐ ┌───▼────┐
    │  Code   │ │ Browser  │ │ MCP  │ │ Memory │
    │Interpret│ │  Auto    │ │Server│ │        │
    │  (01)   │ │  (02)    │ │ (04) │ │  (06)  │
    └─────────┘ └──────────┘ └──────┘ └────────┘
    Run Python   Navigate     Deployed   Persistent
    in sandbox   websites     tools      client context
```

## 📋 Workshop Labs

| Lab | Feature | FSI Use Case | Duration |
|-----|---------|--------------|----------|
| [00](00-strands-agents-fsi/) | **Strands Basics** | Loan calculator, stock lookup, FX rates | 20 min |
| [01](01-agentcore-code-interpreter-fsi/) | **Code Interpreter** | Fraud detection, portfolio VaR analysis | 30 min |
| [02](02-agentcore-browser-fsi/) | **Browser Automation** | APRA regulatory monitoring, bank rate comparison | 25 min |
| [04](04-agentcore-runtime-mcp-fsi/) | **Runtime MCP** | Deploy transaction validation as managed service | 30 min |
| [05](05-agentcore-runtime-observability-fsi/) | **Observability** | Audit trail for compliance (traces, logs) | 25 min |
| [06](06-agentcore-memory-fsi/) | **Memory** | Client context: risk appetite, migration plans | 25 min |

## 🏦 FSI Customer Scenarios

### Afterpay / BNPL
- Real-time transaction fraud scoring
- Velocity checks and geo-anomaly detection
- Regulatory compliance monitoring (ASIC)

### Block (Square / CashApp)
- Multi-currency FX operations
- Cost optimization analysis
- Platform reliability monitoring

### Vanguard / Asset Management
- Portfolio risk calculations (VaR, Sharpe ratio)
- Regulatory reporting (CPS 230, CPS 234)
- Client advisory with persistent memory

## 🚀 Quick Start

### Prerequisites
- AWS Account with [Nova Pro model access](https://console.aws.amazon.com/bedrock/home#/modelaccess)
- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) package manager

### Setup
```bash
git clone https://github.com/Zohaib-AWSCloud/Strands_Agent.git
cd Strands_Agent
uv sync
uv run jupyter lab
```

Then open Lab 00 and run cells with Shift+Enter.

### AWS Region Configuration
The workshop auto-detects your region for the correct Nova Pro model ID:
- `us-*` → `us.amazon.nova-pro-v1:0`
- `eu-*` → `eu.amazon.nova-pro-v1:0`
- `ap-*` → `apac.amazon.nova-pro-v1:0`

## 📁 Repository Structure

```
Strands_Agent/
├── README.md                              # This file
├── pyproject.toml                         # Python dependencies
├── data/                                  # Synthetic FSI datasets
│   ├── transactions.csv                   # 25 transactions with fraud patterns
│   └── portfolio.csv                      # Client portfolios (Vanguard, Block)
├── 00-strands-agents-fsi/                 # Lab 00: Strands Basics
│   └── 00-strands-agents-fsi.ipynb
├── 01-agentcore-code-interpreter-fsi/     # Lab 01: Code Interpreter
│   └── 01-agentcore-code-interpreter-fsi.ipynb
├── 02-agentcore-browser-fsi/             # Lab 02: Browser Automation
│   └── 02-agentcore-browser-fsi.ipynb
├── 04-agentcore-runtime-mcp-fsi/         # Lab 04: Runtime MCP Deploy
│   ├── 04-agentcore-runtime-mcp-fsi.ipynb
│   └── mcp_server.py
├── 05-agentcore-runtime-observability-fsi/ # Lab 05: Observability
│   └── 05-agentcore-runtime-observability-fsi.ipynb
└── 06-agentcore-memory-fsi/              # Lab 06: Memory
    └── 06-agentcore-memory-fsi.ipynb
```

## 🔑 Key Concepts

### Why AI Agents for FSI?
- **Compliance automation** — Agents provide audit trails of every action
- **Operational efficiency** — Automate repetitive analysis (cost reviews, risk reports)
- **Client experience** — Persistent memory enables personalized advisory
- **Regulatory monitoring** — Proactive alerts on policy changes

### AgentCore Features Used
| Feature | What It Does | FSI Value |
|---------|-------------|-----------|
| Code Interpreter | Executes Python in sandbox | Safe financial calculations |
| Browser | Controls web browser | Monitor regulators, extract market data |
| Runtime | Deploys tools as managed services | Scalable, always-on tools |
| Observability | Traces every agent action | Compliance audit trail |
| Memory | Persists context across sessions | Client relationship continuity |

## 👥 Target Audience

- TAMs supporting FSI customers
- Solutions Architects in financial services
- Anyone wanting to understand AgentCore through practical FSI examples

## 📚 References

- [Strands Agents Documentation](https://strandsagents.com/)
- [Bedrock AgentCore Documentation](https://docs.aws.amazon.com/bedrock-agentcore/)
- [Original Workshop](https://github.com/aws-samples/sample-bedrock-agentcore-with-strands-and-nova)
