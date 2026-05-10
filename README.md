# QA Decision Helper

A Python command-line tool that helps QA engineers make common testing decisions based on requirement and bug characteristics.

## What It Demonstrates
- Conditional logic (if, elif, else)
- Input validation with while loops
- Error handling for invalid user input
- Applied QA domain knowledge in a Python tool

## How to Run
```bash
python3 qa_helper.py
```

## What It Does
The tool presents three decisions a QA engineer makes regularly:

1. **How much testing should I run for this requirement?**
   Recommends smoke, regression, or full testing based on risk and history.

2. **Is this bug severe enough to block the release?**
   Recommends block, do not block, or escalate based on impact and workarounds.

3. **Where should I focus my testing effort for this release requirement?**
   Recommends a testing focus area based on recent changes, traffic, and history.

## Built With
- Python 3
