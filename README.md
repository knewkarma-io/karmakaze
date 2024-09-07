<h2 align="center">Karma Kaze (カルマの風)</h2>

<p align="center">Data sanitisation engine for <a href="https://pypi.org/project/knewkarma" target="_blank">Knew Karma</a>.</p>

```python
from karmakaze.klean import Klean
from karmakaze.strukt import Strukt
import requests

username = "AutoModerator"
response = requests.get(f"https://www.reddit.com/user/{username}/about.json").json()

klean = Klean()  # Sanitises the data
strukt = Strukt()  # Restructures the sanitised data

sanitised_data = klean.subreddit_or_user(response)
restructured_data = strukt.users(sanitised_data)

print(sanitised_data)
print(restructured_data)
```

## License

MIT License © [Richard Mwewa](https://gravatar.com/rly0nheart)

   <a href="https://gravatar.com/rly0nheart" target="_blank">
      <img src="https://github.com/user-attachments/assets/5b29ee58-ea36-4ec0-aea3-4b2f9f7999fb" alt="richard-mwewa">
   </a>