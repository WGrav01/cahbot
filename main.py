from mastodon import Mastodon, MastodonError, StreamListener
from dotenv import load_dotenv
import os
import random

load_dotenv(override=True)

username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

try:
    mastodon = Mastodon(
        client_id="cahbot_clientcred.secret",
    )  # create mastodon api instance
except MastodonError as e:
    print(
        "[FATAL] App not registered or is missing credentials. Have you tried running register_app.py?"
    )
    print(f'Above exception was: "{e}"')
else:
    mastodon.log_in(  # log into above mastodon api instance
        str(username), str(password)
    )

account = mastodon.account_verify_credentials()
print(f"Logged in as {account.username}")


def random_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        return random.choice(lines)


class MentionListener(StreamListener):
    def on_update(self, status):
        print(f"got update: {status.content}")
        ...

    def on_notification(self, notification):
        if notification["type"] == "mention":
            print(f'got mention: {notification["status"].content}')

            card = random_line("cards.txt")

            # reply to the mention with a random card
            mastodon.status_post(
                status=card,
                in_reply_to_id=notification["status"],
                spoiler_text='Press "Show More" to reveal potentially offensive card.',
            )
            print(f"posted card: {card}")


print("Starting stream...")
listener = MentionListener()
mastodon.stream_user(listener)
