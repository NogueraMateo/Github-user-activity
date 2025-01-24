import requests
from EventManager import EventManager

def get_user_activity(username):
    headers = {
        'Accept': 'application/vnd.github+json',
    }
    response = requests.get("https://api.github.com/users/{}/events".format(username), headers=headers)
    
    data = response.json()
    event_manager = EventManager()
    if response.status_code == 200:
        for event in data:
            event_manager.handle_event(event)


if __name__ == '__main__':
    username = input("Enter GitHub username: ")
    user_activity = get_user_activity(username)
    print(user_activity)


