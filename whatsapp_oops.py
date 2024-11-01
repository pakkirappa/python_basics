# Encapsulation: Wrapping data (attributes) and methods (functions) into a single unit (class).

class User:
    def __init__(self, user_id, name):
        # Initialize user with user ID and name
        self.user_id = user_id
        self.name = name
        self.contacts = []
        self.groups = []

    def add_contact(self, user):
        # Add a contact to the user's contact list
        self.contacts.append(user)

    def join_group(self, group):
        # Add the user to a group
        self.groups.append(group)
        group.add_member(self)

    def send_message(self, recipient, content):
        # Send a message to another user or group
        message = Message(self, content)
        recipient.receive_message(message)

    def receive_message(self, message):
        # Receive a message
        print(f"{self.name} received a message from {message.sender.name}: {message.content}")

    def get_details(self):
        # Return user details as a string
        return f"User [ID: {self.user_id}, Name: {self.name}]"


class Message:
    def __init__(self, sender, content):
        # Initialize message with sender and content
        self.sender = sender
        self.content = content

    def get_details(self):
        # Return message details as a string
        return f"Message [Sender: {self.sender.name}, Content: {self.content}]"


class Group:
    def __init__(self, group_id, name):
        # Initialize group with group ID and name
        self.group_id = group_id
        self.name = name
        self.members = []

    def add_member(self, user):
        # Add a member to the group
        self.members.append(user)

    def send_message(self, sender, content):
        # Send a message to all group members
        message = Message(sender, content)
        for member in self.members:
            if member != sender:
                member.receive_message(message)

    def get_details(self):
        # Return group details as a string
        return f"Group [ID: {self.group_id}, Name: {self.name}, Members: {[member.name for member in self.members]}]"


class WhatsApp:
    def __init__(self):
        # Initialize WhatsApp with empty lists of users and groups
        self.users = []
        self.groups = []

    def add_user(self, user):
        # Add a user to WhatsApp
        self.users.append(user)

    def create_group(self, group):
        # Create a group in WhatsApp
        self.groups.append(group)

    def get_user(self, user_id):
        # Retrieve a user by their ID
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def get_group(self, group_id):
        # Retrieve a group by its ID
        for group in self.groups:
            if group.group_id == group_id:
                return group
        return None


# Example usage:
if __name__ == "__main__":
    # Create WhatsApp instance
    whatsapp = WhatsApp()

    # Create users
    user1 = User(1, "Alice")
    user2 = User(2, "Bob")
    user3 = User(3, "Charlie")

    # Add users to WhatsApp
    whatsapp.add_user(user1)
    whatsapp.add_user(user2)
    whatsapp.add_user(user3)

    # Add contacts
    user1.add_contact(user2)
    user2.add_contact(user1)
    user2.add_contact(user3)

    # Create a group and add members
    group1 = Group(101, "Friends")
    whatsapp.create_group(group1)
    user1.join_group(group1)
    user2.join_group(group1)

    # Send messages
    user1.send_message(user2, "Hello Bob!")
    user2.send_message(user1, "Hi Alice!")
    user2.send_message(group1, "Hello everyone!")

    # Print details
    print(user1.get_details())
    print(user2.get_details())
    print(group1.get_details())
    
#     User Class:

# __init__ Method: Initializes the user with a user ID, name, contacts, and groups.
# add_contact Method: Adds a contact to the user's contact list.
# join_group Method: Adds the user to a group and the group to the user's group list.
# send_message Method: Sends a message to another user or group.
# receive_message Method: Receives a message.
# get_details Method: Returns user details as a string.
# Message Class:

# __init__ Method: Initializes the message with a sender and content.
# get_details Method: Returns message details as a string.
# Group Class:

# __init__ Method: Initializes the group with a group ID, name, and members.
# add_member Method: Adds a member to the group.
# send_message Method: Sends a message to all group members except the sender.
# get_details Method: Returns group details as a string.
# WhatsApp Class:

# __init__ Method: Initializes WhatsApp with empty lists of users and groups.
# add_user Method: Adds a user to WhatsApp.
# create_group Method: Creates a group in WhatsApp.
# get_user Method: Retrieves a user by their ID.
# get_group Method: Retrieves a group by its ID.



# OOP Features Explained:
# Encapsulation:

# Wrapping data (attributes) and methods (functions) into a single unit (class).
# Example: The User, Message, Group, and WhatsApp classes encapsulate their respective attributes and methods.
# Abstraction:

# Hiding the complex implementation details and showing only the necessary features.
# Example: The send_message and receive_message methods provide a simple interface for sending and receiving messages without exposing the internal workings.
# Inheritance:

# Creating a new class from an existing class to reuse code.
# Note: This example does not explicitly demonstrate inheritance, but it can be extended to include it. For example, you could create a GroupMessage class that inherits from the Message class.
# Polymorphism:

# The ability to use a common interface for multiple forms (data types).
# Example: The send_message method in the User class can send messages to both individual users and groups, demonstrating polymorphism.
