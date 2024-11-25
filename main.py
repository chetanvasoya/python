import os
import schedule
import time
from datetime import datetime

# Path to your local Git repository
REPO_PATH = "D:\gitautomation\python"  # Update with your actual repo path

# Commit message template
def generate_commit_message():
    return f"Auto-update on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

# Function to perform Git update
def git_update():
    try:
        # Change directory to the repo
        os.chdir(REPO_PATH)

        # Run Git commands
        os.system("git add .")  # Add all changes
        commit_message = generate_commit_message()
        os.system(f'git commit -m "{commit_message}"')  # Commit with a message
        os.system("git push")  # Push to the remote repository

        print(f"GitHub update successful at {datetime.now()}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Schedule the task to run every 10 minutes
schedule.every(1).minutes.do(git_update)

# Print a message to indicate the script is running
print("GitHub auto-update script is running. Updates scheduled every 10 minutes...")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)