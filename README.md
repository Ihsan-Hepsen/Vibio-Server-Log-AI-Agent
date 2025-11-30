# Vibio Server Log AI Agent

AI-powered log monitoring that costs $5/month instead of $500/month. Built for Vibio, designed to show small-to-medium products how to monitor smarter, not harder.

## What It Does

Analyzes server logs daily using AI and sends intelligent reports. No complex setup, no expensive monitoring platforms—just a Python script and a cron job.

## Why It Matters

Traditional monitoring solutions cost $50-500+/month. This uses the OpenAI API on-demand for ~$2-10/month. Perfect for startups and growing products that need intelligent monitoring without enterprise costs.

## How It Works

```bash
# Runs daily at 10:23 AM via cron
23 10 * * * /usr/bin/python3 /home/ihsan/log-ai-agent/main.py
```

The agent reads logs, identifies issues, detects patterns, and generates actionable reports—all automatically.

## Quick Start

```bash
git clone https://github.com/Ihsan-Hepsen/Vibio-Server-Log-AI-Agent.git
cd Vibio-Server-Log-AI-Agent
pip install -r requirements.txt
cp .env.example .env  # Add your OpenAI API key
python3 main.py       # Test it manually

# Set up cron for automated daily reports
crontab -e
# Add: 23 10 * * * /usr/bin/python3 /path/to/main.py
```

## Example Output

```
--- R E P O R T ---
🔴 ALERT (0)
🟠 Critical (2):
- Log:
    2025-08-11T12:05:43.723Z INFO - Error parsing HTTP request header
    java.lang.IllegalArgumentException: Invalid character found in request target
    
    Possible cause: Malformed HTTP requests, possibly an attempted attack
    Possible remedy: Evaluate request source. Consider IP blocking if attack suspected.

- Log:
    2025-08-12T07:39:19.978Z INFO - Error parsing HTTP request header
    Invalid character found in request target [/?id=%25{{{11}}*{{11}}}]
    
    Possible cause: Malformed HTTP request - faulty client or potential attack
    Possible remedy: Review origin and implement security measures if needed.

🟡 Warning (0):
--- END OF REPORT ---
```

## The Bottom Line

This is Vibio-specific, but the approach works for any product. Smart scheduling + AI = powerful monitoring tailored for your needs.

---

**Built by [Hepsen](https://github.com/Ihsan-Hepsen)** for [Vibio](https://vibio.co) | © 2025 All Rights Reserved