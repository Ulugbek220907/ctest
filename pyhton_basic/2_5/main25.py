#threading example
import threading
import time

def walk_the_dog(name):
    time.sleep(8)  # Simulate time taken to walk the dog
    print(f"{name} is walking the dog...")

def take_out_the_trash():
    time.sleep(5)  # Simulate time taken to take out the trash
    print("Taking out the trash...")

def get_mail():
    time.sleep(3)  # Simulate time taken to get the mail
    print("Getting the mail...")

if __name__ == "__main__":
    # Create threads for each task
    walk_thread = threading.Thread(target=walk_the_dog, args=("Ben",))
    trash_thread = threading.Thread(target=take_out_the_trash)
    mail_thread = threading.Thread(target=get_mail)

    # Start the threads
    walk_thread.start()
    trash_thread.start()
    mail_thread.start()

    # Wait for all threads to complete
    walk_thread.join()
    trash_thread.join()
    mail_thread.join()

    print("All tasks completed.")