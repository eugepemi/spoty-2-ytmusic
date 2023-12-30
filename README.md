# spoty-2-ytmusic
This project is intented to migrate playlists from Spotify to Youtube Music

## Dependencies
```bash
pip install -r requirements.txt
```

## Authentication
### Spotify
1. Go to https://developer.spotify.com/dashboard/applications
2. Create an app
3. Define the Client ID and Client Secret as environment variables:
```js
SPOTIFY_CLIENT_ID=changeme
SPOTIFY_CLIENT_SECRET=changeme
``` 

### Youtube Music
- We will be using [OAuth authentication](https://ytmusicapi.readthedocs.io/en/stable/setup/oauth.html) to authenticate with Youtube Music from `ytmusicapi` dependency.
- Follow the steps on the link above to get the `oauth.json` file to the root of the project.

### Usage
When the conditions above are met, as environment variables, provide the ID of the Spotify playlist you want to migrate, and the name and description of the Youtube Music playlist that will be created:
```js
SPOTIFY_PLAYLIST_ID=changeme
YT_PLAYLIST_NAME=changeme
YT_PLAYLIST_DESCRIPTION=changeme
```

Run the script with:
```bash
python src/main.py
```

Enjoy your music!