class EventManager:

    def __init__(self):
        pass

    def handle_event(self, event: dict):
        event_type = event.get('type')
        if event_type == 'CommitCommentEvent':
            self.commit_comment_event(event)
        elif event_type == 'CreateEvent':
            self.create_event(event)
        elif event_type == 'DeleteEvent':
            self.delete_event(event)
        elif event_type == 'ForkEvent':
            self.fork_event(event)
        elif event_type == 'GollumEvent':
            self.gollum_event(event)
        elif event_type == 'IssueCommentEvent':
            self.issue_comment_event(event)
        elif event_type == 'IssuesEvent':
            self.issue_event(event)
        elif event_type == 'MemberEvent':
            self.member_event(event)
        elif event_type == 'PublicEvent':
            self.public_event(event)
        elif event_type == 'PullRequestEvent':
            self.pull_request_event(event)
        elif event_type == 'PullRequestReviewEvent':
            self.pull_request_review_event(event)
        elif event_type == 'PullRequestReviewCommentEvent':
            self.pull_request_review_comment_event(event)
        elif event_type == 'PullRequestReviewThreadEvent':
            self.pull_request_review_thread_event(event)
        elif event_type == 'PushEvent':
            self.push_event(event)
        elif event_type == 'ReleaseEvent':
            self.release_event(event)
        elif event_type == 'WatchEvent':
            self.watch_event()
        elif event_type == 'SponsorshipEvent':
            self.sponsorship_event(event)
        else:
            print(f"Unknown event type: {event_type}")

    def commit_comment_event(self, event: dict):
        print(f"-  Created a commit comment event in {event.get('repo').get('name')}")

    def create_event(self, event: dict):
        print(f"-  Created a {event.get('payload').get('ref_type')} event in {event.get('repo').get('name')}")

    def delete_event(self, event: dict):
        print(f"-  Deleted a {event.get('payload').get('ref_type')} event in {event.get('repo').get('name')}")

    def fork_event(self, event: dict):
        print(f"-  Forked a repository")
    
    def gollum_event(self, event:dict):
        pages = event.get('payload').get('pages')
        for page in pages:
            if page['action'] == 'created':
                print(f"-  Created a new wiki page in {event.get('repo').get('name')}. Url is {page.get('html_url')}")
            elif page['action'] == 'edited':
                print(f"-  Edited a wiki page in {event.get('repo').get('name')}. Url is {page.get('html_url')}")
    
    def issue_comment_event(self, event: dict):
        action = event.get('payload').get('action')
        if action == 'created':
            print(f"-  Created an issue comment in {event.get('repo').get('name')}. The issue was {event.get('payload').get('issue').get('title')}")
        elif action == 'edited':   
            print(f"-  Edited an issue comment in {event.get('repo').get('name')}. The issue was {event.get('payload').get('issue').get('title')}")
        elif action == 'deleted':   
            print(f"-  Deleted an issue comment in {event.get('repo').get('name')}. The issue was {event.get('payload').get('issue').get('title')}")

    def issue_event(self, event: dict):
        action: str = event.get('payload').get('action')
        print(f"-  {action} an issue in {event.get('repo').get('name')}. The issue is {event.get('payload').get('issue').get('title')}")
    
    def member_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a member in {event.get('repo').get('name')}. The member is {event.get('payload').get('member').get('login')}")
    
    def public_event(self, event: dict):
        print(f"-  Made a repository public")
    
    def pull_request_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a pull request in {event.get('repo').get('name')}. The pull request is {event.get('payload').get('pull_request').get('title')}")
    
    def pull_request_review_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a pull request review in {event.get('repo').get('name')}. The pull request is {event.get('payload').get('pull_request').get('title')}")
    
    def pull_request_review_comment_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a pull request review comment in {event.get('repo').get('name')}. The pull request is {event.get('payload').get('pull_request').get('title')}")

    def pull_request_review_thread_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a pull request review thread in {event.get('repo').get('name')}. The pull request is {event.get('payload').get('pull_request').get('title')}")
    
    def push_event(self, event: dict):
        print(f"-  Pushed {event.get('payload').get('size')} commits to {event.get('repo').get('name')}")
    
    def release_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a release in {event.get('repo').get('name')}")

    def watch_event(self):
        print(f"-  Starred a repository")

    def sponsorship_event(self, event: dict):
        action = event.get('payload').get('action')
        print(f"-  {action} a sponsorship in {event.get('repo').get('name')}")