class Event:
    def __init__(self, name, date, max_participants=3):
        self.name = name
        self.date = date
        self.participants = []
        self.max_participants = max_participants

    def add_participant(self, participant_name):
        if len(self.participants) < self.max_participants:
            self.participants.append(participant_name)
            print(f"Participant '{participant_name}' added to '{self.name}'")
        else:
            print(f"Sorry, '{self.name}' is already full. No more participants can be added.")

    def get_participant_count(self):
        return len(self.participants)

events = {}

while True:
    action = input("Enter action (add, count, display, exit): ").lower()

    if action == "exit":
        break

    try:
        if action == "add":
            name = input("Enter event name: ")
            date = input("Enter event date: ")
            participant = input("Enter guest: ")
            max_participants = int(input("Enter maximum number of participants (default is 100): ") or 100)
            events[name] = Event(name, date, max_participants)
            events[name].add_participant(participant)
            print(f"Event '{name}' added successfully.")
        elif action == "count":
            event_name = input("Enter event name: ")
            if event_name in events:
                count = events[event_name].get_participant_count()
                print(f"Participant Count for '{event_name}': {count}")
            else:
                print(f"Event '{event_name}' not found.")
        elif action == "display":
            for event in events.values():
                event.displaye_event()
        else:
            print("Invalid action. Please try again.")

    except Exception as e:
        print("An error occurred:", e)
