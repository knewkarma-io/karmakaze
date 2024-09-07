<h2 align="center">Karma Kaze (カルマの風)</h2>

<p align="center">Response deserialisation &amp; parsing engine for Knew Karma.</p>

```python
from karmakaze.klean import Klean
from karmakaze.strukt import Strukt
import requests

username = "AutoModerator"
response = requests.get(f"https://www.reddit.com/user/{username}/about.json").json()

klean = Klean  # Sanitises the data
strukt = Strukt()  # Restructures the sanitised data

print(
    strukt.users(
        klean.subreddit_or_user(response)
    )
)
```

```python
namespace(name='AutoModerator',
          id='6l4z3',
          avatar_url='https://styles.redditmedia.com/t5_1yz875/styles/profileIcon_klqlly9fc4l41.png?width=256&amp;height=256&amp;crop=256:256,smart&amp;s=94486fc13b9ca9e154e9e8926e3d8c43ccc80be3',
          is_verified=True,
          has_verified_email=True,
          is_gold=True,
          is_mod=True,
          is_blocked=False,
          is_employee=False,
          hidden_from_bots=False,
          accepts_followers=True,
          comment_karma=1000,
          link_karma=1000,
          awardee_karma=2482684,
          total_karma=2484684,
          subreddit={'accept_followers': True,
                     'allowed_media_in_comments': [],
                     'banner_img': '',
                     'banner_size': None,
                     'community_icon': None,
                     'default_set': True,
                     'description': '',
                     'disable_contributor_requests': False,
                     'display_name': 'u_AutoModerator',
                     'display_name_prefixed': 'u/AutoModerator',
                     'free_form_reports': True,
                     'header_img': None,
                     'header_size': None,
                     'icon_color': '',
                     'icon_img': 'https://styles.redditmedia.com/t5_1yz875/styles/profileIcon_klqlly9fc4l41.png?width=256&amp;height=256&amp;crop=256:256,smart&amp;s=94486fc13b9ca9e154e9e8926e3d8c43ccc80be3',
                     'icon_size': [256, 256],
                     'is_default_banner': True,
                     'is_default_icon': False,
                     'key_color': '',
                     'link_flair_enabled': False,
                     'link_flair_position': '',
                     'name': 't5_1yz875',
                     'over_18': False,
                     'previous_names': [],
                     'primary_color': '',
                     'public_description': '',
                     'quarantine': False,
                     'restrict_commenting': False,
                     'restrict_posting': True,
                     'show_media': True,
                     'submit_link_label': '',
                     'submit_text_label': '',
                     'subreddit_type': 'user',
                     'subscribers': 0,
                     'title': '',
                     'url': '/user/AutoModerator/',
                     'user_is_banned': None,
                     'user_is_contributor': None,
                     'user_is_moderator': None,
                     'user_is_muted': None,
                     'user_is_subscriber': None},
          is_friend=False,
          snoovatar_img='',
          awarder_karma=0,
          pref_show_snoovatar=False,
          has_subscribed=True,
          created='05/01/12, 07:24:28')
```
