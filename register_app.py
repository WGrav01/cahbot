from mastodon import Mastodon

# from mastodon.py documentation:
"""
Register your app!
 This only needs to be done once (per server, or when distributing rather than hosting an application,
  most likely per device and server).
  substitute in your information and run the file:
"""


Mastodon.create_app(
    "cahbot", api_base_url="https://botsin.space", to_file="cahbot_clientcred.secret"
)
