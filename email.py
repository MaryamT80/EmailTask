class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Initialize the Email object with the sender's email address, subject line,
        and email content. Set has_been_read to False by default.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """
        Mark the email as read by setting the has_been_read attribute to True.
        """
        self.has_been_read = True

# Initialize an empty inbox list to store email objects
inbox = []

def populate_inbox():
    """
    Populate the inbox with three sample emails.
    """
    sample_emails = [
        Email("user1@example.com", "Welcome to HyperionDev!", "We're excited to have you on board."),
        Email("user2@example.com", "Great work on the bootcamp!", "Keep up the excellent progress."),
        Email("user3@example.com", "Your excellent marks!", "Congratulations on your high scores!")
    ]
    inbox.extend(sample_emails)

def list_emails():
    """
    List all emails in the inbox with their subject lines and corresponding indices.
    """
    if not inbox:
        print("\nYour inbox is empty.\n")
        return

    print("\nInbox:")
    for index, email in enumerate(inbox):
        print(f"{index} {email.subject_line}")

def read_email(index):
    """
    Display the email details at the given index and mark it as read.
    """
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nFrom: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}\n")
        email.mark_as_read()
        print(f"Email from {email.email_address} marked as read.\n")
    else:
        print("\nInvalid index. Please try again.\n")

# Menu-driven application
def email_simulator():
    """
    Email simulator main menu.
    """
    populate_inbox()  # Populate the inbox with sample emails at start-up

    while True:
        print("\nEmail Simulator Menu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            list_emails()
            try:
                index = int(input("\nEnter the index of the email you want to read: "))
                read_email(index)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")

        elif choice == "2":
            print("\nUnread Emails:")
            for email in inbox:
                if not email.has_been_read:
                    print(f"{email.subject_line}")

        elif choice == "3":
            print("\nExiting the email simulator. Goodbye!\n")
            break

        else:
            print("\nInvalid choice. Please select a valid option.\n")

if __name__ == "__main__":
    email_simulator()