# ClarifyAI --- Assignment 2 Prototype

README prose word count: approximately 200 (excluding setup commands).

## Project status

A browser-based prototype comparing three clarification strategies:
direct answer, ask-before-answer, and answer-then-clarify.

The system uses rule-based ambiguity estimation and simulated chatbot
responses. It is not connected to a live language model. It records
perceived task success, dialogue turns, clarification questions,
ambiguity estimates, mental effort and satisfaction. Data is stored in
browser local storage and can be exported as CSV.

## Technology

-   Python 3 standard library: runs the local web server.
-   HTML/CSS: provides the user interface.
-   JavaScript: controls interaction flow, simulated responses, feedback
    and CSV export.
-   No external packages or API keys required.

## Run

1.  Install Python 3.
2.  Open a terminal in the project folder.
3.  Run:

``` bash
python server.py
```

4.  Open `http://127.0.0.1:8000` in a browser.
5.  Press `Ctrl+C` to stop the server.

## Development record

-   **Stage 1:** Built the interface and three clarification strategies
    to compare different interaction approaches.
-   **Stage 2:** Added scenario-specific prompts and rule-based
    ambiguity estimation to make the responses more relevant to each
    task.
-   **Stage 3:** Added different test questions covering low, medium and
    high ambiguity levels to compare how the three clarification
    strategies handle different types of requests.
-   **Stage 4:** Added task-success feedback and CSV export to support
    experiment data collection.
-   **Final checks:** Test each strategy, try the sample tasks, save
    multiple records, export the CSV and inspect the exported data.

## AI assistance

ChatGPT was used to assist with code modifications, debugging and
documentation. Some suggestions were adapted and changed to fit the
project. The code was checked by running the prototype, testing the
interactions and inspecting the exported CSV data. The project design
and final implementation were reviewed by the project owner.

## Files

-   `server.py`: local web server.
-   `index.html`: interface structure.
-   `static/style.css`: interface styling.
-   `static/app.js`: simulated interaction logic and experiment data
    handling.

## Clearing saved experiment data

Use **Clear saved data** in the feedback panel to remove all ClarifyAI
feedback records from this browser. Confirmation is required. Export the
CSV before clearing if you want to keep a copy.

**Reset conversation** only resets the current chat. It does not delete
saved records.
