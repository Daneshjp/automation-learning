# Prompt Engineering – Structured AI Automation

This module demonstrates structured prompt engineering using JSON-based prompts
and Python runner scripts.

## Features
- Manual test case → automation steps conversion
- Application log → root cause analysis
- Tool-agnostic design (Selenium / Playwright friendly)
- Secure OpenAI API usage via environment variables

## Structure
- structured_prompts/: Prompt definitions (JSON)
- runners/: Execution scripts

## How to Run
```bash
export OPENAI_API_KEY=your_key_here
python runners/run_test_case_to_steps.py
python runners/run_logs_to_root_cause.py
