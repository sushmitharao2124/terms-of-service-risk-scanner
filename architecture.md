# 🏗 Architecture & System Design

The **Fine Print Detective** leverages specialized foundational models via Agent.ai to scan Terms of Service quickly and accurately.

## High-Level Workflow
1. **Input Stage**: The user provides the legal text (via CLI).
2. **Chunking**: The text is broken down into manageable legal contexts to avoid context-window limitations while maintaining logical structure.
3. **Dual-Agent processing**: 
   - *Agent A (Summarizer)* reads the chunks and synthesizes plain-english rules.
   - *Agent B (Risk Detective)* explicitly looks for "red flags" (arbitration, predatory data collection).
4. **Output Synthesis**: A final aggregator formats the output into a readable markdown report with structured Risk Flags and a Verdict.

## Why this approach?
- Separation of concerns ensures the 'Summarizer' does not get distracted by legal jargon anomalies, while the 'Risk Detective' remains highly sensitive to negative patterns.
- Calling Agent.ai APIs allows us to treat the entire intelligence layer as a unified microservice, greatly simplifying the local codebase.
