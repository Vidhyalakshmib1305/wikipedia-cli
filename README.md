# Wikipedia CLI

A command-line tool that fetches Wikipedia article summaries for any topic.

## Features
- Search any topic from the command line
- Fetches real data from Wikipedia API
- Saves summary to a text file
- Handles invalid topics gracefully
- Loop mode — search multiple topics without restarting

## Tech Stack
- Python
- requests library
- Wikipedia REST API

## How to Run
```
pip install requests
python wiki.py
```

## Example
```
Enter a topic (or 'quit' to exit): cricket
Cricket
==================================================
Cricket is a bat-and-ball game...
Saved to cricket.txt ✅
```

