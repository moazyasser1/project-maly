# Weekly Task & Habit Tracker

A command-line Python application built in Jupyter Notebook to help users organize weekly tasks, build daily habits, and monitor their progress through daily and weekly summary reports.

## How It Works

The tracker stores your data in two separate Python dictionaries:

- **Tasks (`tasks`)**: Organized by day of the week (`Monday` through `Sunday`). Each task is tied to a specific day and tracks whether it is complete (`True`) or incomplete (`False`).
- **Habits (`habits`)**: Organized by habit name (e.g., *Drink Water*, *Exercise*). Each habit automatically tracks completion (`True`/`False`) across all 7 days of the week.

All user inputs are cleaned with `.strip()` and `.title()` (or `.lower()` for menu choices), and invalid inputs display helpful error messages without crashing the program.

## How to Use the Tracker

1. **Open the Notebook**: Launch `maly.ipynb` in JupyterLab (or Jupyter Notebook).
2. **Run All Cells**: Go to **Run → Run All Cells** to initialize the data structures, load all functions, and launch the interactive menu.
3. **Choose an Option (1–5)**:
   - **1 – Add a Task or Habit**: Enter `T` to add a task to a specific day, or `H` to add a new daily habit for the week.
   - **2 – Mark a Task or Habit as Complete**: Enter `T` to view incomplete tasks and mark one complete, or `H` to mark a habit complete for a chosen day.
   - **3 – Remove a Task or Habit**: Enter `T` to delete a task from a day, or `H` to stop tracking a habit.
   - **4 – View Reports**: Enter `W` for a weekly summary (habit counts out of 7 days plus completed/incomplete tasks) or `D` for a single day's report with ✅ and ❌ status icons.
   - **5 – Exit**: Closes the tracker safely.

> **Note:** Re-running the Part 1 setup cell resets all stored tasks and habits to empty.
