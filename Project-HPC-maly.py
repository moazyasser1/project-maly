# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

# List containing all days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def weekly_report(habits, tasks, file_name):
    # Print a header showing which data file this report corresponds to
    print(f"\n===== Weekly Report ({file_name}) =====")

    # Display weekly summary for habits
    print("--- Habits ---")
    if not habits:
        print("No habits are being tracked.")
    else:
        for habit, habit_days in habits.items():
            # Count how many days out of 7 the habit was completed
            count = 0
            for day in days:
                if habit_days.get(day, False):
                    count += 1
            print(f"{habit}: {count}/7 days complete")

    # Display weekly summary for tasks
    print("--- Tasks ---")
    completed = []
    not_completed = []

    # Separate tasks into completed and not completed lists
    for day in days:
        for task, done in tasks.get(day, {}).items():
            if done:
                completed.append(f"{task} ({day})")
            else:
                not_completed.append(f"{task} ({day})")

    # Print both task lists or a message if no tasks exist
    if not completed and not not_completed:
        print("No tasks have been added.")
    else:
        print("Completed tasks:")
        if not completed:
            print("None")
        for item in completed:
            print(f"✅ {item}")

        print("Not completed tasks:")
        if not not_completed:
            print("None")
        for item in not_completed:
            print(f"❌ {item}")


# Provide the list of data files to process.
# Each file contains a list of two dictionaries: [habits, tasks].
# Make sure all data files are in the same directory as this script.
file_list = [
    'dictionaries_1.txt',
    'dictionaries_2.txt',
    'dictionaries_3.txt',
    'dictionaries_4.txt',
    'dictionaries_5.txt',
    'dictionaries_6.txt',
    'dictionaries_7.txt',
    'dictionaries_8.txt',
    'dictionaries_9.txt',
    'dictionaries_10.txt',
]

# Loop through each file, parse its Python data structures, and generate a weekly report
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        # Pass habits (data[0]), tasks (data[1]), and the filename
        weekly_report(data[0], data[1], file_name)