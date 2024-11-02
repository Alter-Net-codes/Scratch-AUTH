import scratchattach as sa
import time
import getpass
import random

try:
    username = input("Enter your Scratch username: ")
    password = getpass.getpass("Enter your Scratch password: ")
    session = sa.login(username, password)
    
    verification_project_id = 1090320725
    verification_code = str(random.randint(100000, 999999))

    print("Please comment this code at: https://scratch.mit.edu/projects/1090320725/")
    print("Verification Code:", verification_code)

    # Access the project object
    project = session.connect_project(verification_project_id)

    # Verification loop with a 2-minute timeout
    start_time = time.time()
    timeout = 120  # seconds

    while True:
        comments = project.comments()  # Fetch comments from the project
        if any(verification_code in comment.content for comment in comments):  # Access content attribute
            print("Verification successful!")
            break
        elif time.time() - start_time > timeout:
            print("Verification timed out. Please try again.")
            break
        time.sleep(5)

except sa.utils.exceptions.FetchError:
    print("Connection error: Unable to connect to Scratch. Please check your internet connection and try again.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
