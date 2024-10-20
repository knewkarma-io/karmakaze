<h2 align="center">Karma Kaze (カルマの風)</h2>

<p align="center">Data sanitation engine for <a href="https://pypi.org/project/knewkarma" target="_blank">Knew Karma</a>.</p>

<p align="center">
      <img alt="Code Style" src="https://img.shields.io/badge/code%20style-black-000000?logo=github&link=https%3A%2F%2Fgithub.com%2Frly0nheart%2Fkarmakaze">
</p>

```python
import karmakaze
import requests

snp = karmakaze.SanitiseAndParse()
username = "AutoModerator"
response = requests.get(f"https://www.reddit.com/user/{username}/about.json").json()

print(snp.user(response=response))
```

## License

GPL-3.0+ © [Richard Mwewa](https://gravatar.com/rly0nheart)

***
<a href="https://gravatar.com/rly0nheart" target="_blank">
      <img src="https://github.com/user-attachments/assets/5b29ee58-ea36-4ec0-aea3-4b2f9f7999fb" alt="richard-mwewa">
</a>
