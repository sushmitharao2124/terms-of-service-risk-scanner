<div align="center">
  <img src="https://agent.ai/favicon.ico" alt="Agent.ai Logo" width="80"/>
  <h1>🕵️ The Fine Print Detective</h1>
  <p><em>Never sign away your rights blindly again.</em></p>
  
  [![Agent.ai Profile](https://img.shields.io/badge/Agent.ai-View_Profile-blue?style=for-the-badge&logo=ai)](https://agent.ai/profile/termsofservice_scanner)
  [![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
</div>

---

>**Paste any Terms of Service and get a plain-English summary plus risk flags before you click Accept.**

The Fine Print Detective is an AI-powered agent designed to scan, analyze, and summarize complex legal jargon often found in Terms of Service (ToS) agreements, Privacy Policies, and EULAs. It highlights potential risks, hidden clauses, and gives you a digestible summary so you know exactly what you're agreeing to.

Try it live on Agent.ai 👉 **[The Fine Print Detective!](https://agent.ai/profile/termsofservice_scanner)**

## ✨ Key Features

- **📖 Plain-English Translation:** Turns legalese into simple, readable text.
- **🚩 Risk Flagging:** Automatically detects clauses that might infringe on your privacy, data rights, or IP.
- **⚡ Breakneck Speed:** Analyzes multi-page documents in just seconds (~20s average).
- **💡 Actionable Insights:** Gives a final verdict: "Safe to Accept" or "Proceed with Caution".
- 🔌 **API Integration:** Built on Agent.ai, enabling programmatic access via API for embedding TOS analysis into external workflows and applications.
---

## ⚡ Why This Matters

Every day, users agree to contracts they don’t understand.

This leads to:
- Hidden legal exposure  
- Overly broad data permissions  
- Unfair dispute terms  

**This project bridges that gap**, turning dense legal language into decisions users can actually make.

---


## 🚀 Quick Start (API Usage)

While you can always use the web interface at [Agent.ai](https://agent.ai/profile/termsofservice_scanner), you can also integrate "The Fine Print Detective" directly into your Python apps!

### 1. Install Dependencies

You'll need the `requests` library to make calls to the API.

```bash
pip install -r requirements.txt
```

### 2. Set Up Your API Key

Get your API key from Agent.ai and set it as an environment variable:

```bash
export AGENT_AI_KEY="your_api_key_here"
```

### 3. Usage Example

Create a simple script (`scanner.py`) to query the agent:

```python
import os
import requests

AGENT_ID = "6ufgw07yfwldddps"
API_KEY = os.getenv("AGENT_AI_KEY")

def scan_tos(tos_text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "agent_id": AGENT_ID,
        "inputs": {
            "terms_of_service_text": tos_text
        }
    }
    
    response = requests.post("https://api.agent.ai/v1/run", json=payload, headers=headers)
    return response.json()

if __name__ == "__main__":
    sample_tos = "By using this service, you grant us an irrevocable, perpetual, royalty-free license to use your data..."
    print("🕵️ Analyzing Terms of Service...")
    result = scan_tos(sample_tos)
    print("\n📝 Report:\n", result.get("output", "Analysis failed."))
```

## 📂 Project Structure

```text
terms-of-service-risk-scanner/
├── README.md                # Project overview and usage
├── app.py                  # Minimal script to run TOS analysis
├── prompts/                # Prompt engineering (core intelligence)
│   ├── risk_detection.txt
│   └── summarization.txt
├── examples/               # Sample inputs and outputs
│   ├── sample_tos.txt
│   └── sample_analysis.md
├── architecture.md         # System design and decisions
├── client.py               # Agent.ai API client
└── requirements.txt        # Dependencies
```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## ⭐ Support

If you find this useful, consider giving it a ⭐ and trying the live demo!
