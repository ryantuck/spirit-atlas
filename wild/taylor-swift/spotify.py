import json
import os
import sys
import time

import requests

USER_ID = "1219121420"
PAGE_SIZE = 50
PAGINATION_SLEEP_S = 3

def get_token():
    r = requests.post(
        url="https://accounts.spotify.com/api/token",
        headers={"Content-type": "application/x-www-form-urlencoded"},
        data={
            "grant_type": "client_credentials",
            "client_id": os.environ["SPOTIFY_CLIENT_ID"],
            "client_secret": os.environ["SPOTIFY_CLIENT_SECRET"],
        },
    )
    r.raise_for_status()
    return r.json()



def _get(url, page_num=0):
    offset = page_num * PAGE_SIZE
    token = get_token()["access_token"]
    r = requests.get(
        url=url,
        headers={"Authorization": f"Bearer {token}"},
        params={"limit": PAGE_SIZE, "offset": offset},
    )
    r.raise_for_status()
    return r.json()


def _get_playlists(page_num=0):
    return _get(
        url=f"https://api.spotify.com/v1/users/{USER_ID}/playlists",
        page_num=page_num,
    )['items']


def _get_playlist_tracks(playlist_id, page_num=0):
    return _get(
        url=f"https://api.spotify.com/v1/users/{USER_ID}/playlists/{playlist_id}/tracks",
        page_num=page_num,
    )['items']


def _get_liked_songs(page_num=0):
    # TODO this doesn't work using existing method, might need auth?
    return _get(
        url=f"https://api.spotify.com/v1/me/tracks",
        page_num=page_num,
    )['items']


def get_playlists():
    page = 0
    all_results = []

    while True:
        batch = _get_playlists(page_num=page)
        all_results += batch
        if len(batch) < PAGE_SIZE:
            break
        page += 1
        time.sleep(PAGINATION_SLEEP_S)

    return all_results


def get_liked_songs():
    page = 0
    all_results = []

    while True:
        batch = _get_liked_songs(page_num=page)
        all_results += batch
        if len(batch) < PAGE_SIZE:
            break
        page += 1
        time.sleep(PAGINATION_SLEEP_S)

    return all_results


def get_playlist_tracks(playlist_id):
    page = 0
    all_results = []

    while True:
        batch = _get_playlist_tracks(playlist_id, page_num=page)
        all_results += batch
        if len(batch) < PAGE_SIZE:
            break
        page += 1
        time.sleep(PAGINATION_SLEEP_S)

    return all_results

def get_oauth_token():
    import spotipy
    from spotipy.oauth2 import SpotifyOAuth
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    return sp.auth_manager.get_access_token()


def add_to_playlist(track_ids, playlist_id, position):
    """
    """

    token = get_oauth_token()['access_token']
    print(token)

    uris = [f"spotify:track:{track_id}" for track_id in track_ids]
    print(uris)

    r = requests.post(
        url=f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks',
        headers={
            "Authorization": f"Bearer {token}",
            "Content-type": "application/json",
        },
        data=json.dumps({
            'uris': uris,
            'position': position,
        }),
    )
    r.raise_for_status()
    return r.json()




if __name__ == "__main__":
    arg = sys.argv[1]

    if arg == 'token':
        token = get_token()
        print(json.dumps(token))

    if arg == 'oauth-token':
        # NOTE - need to fetch this interactively at first
        token = get_oauth_token()
        print(json.dumps(token))

    if arg == 'playlists':
        playlists = get_playlists()
        for playlist in playlists:
            print(json.dumps(playlist))

    if arg == 'playlist-tracks':
        playlist_id = sys.argv[2]
        tracks = get_playlist_tracks(playlist_id)
        for track in tracks:
            print(json.dumps(track))

    if arg == 'liked-songs':
        liked_songs = get_liked_songs()
        for song in liked_songs:
            print(json.dumps(song))


    if arg == 'add-to-playlist':
        playlist_id = sys.argv[2]
        position = sys.argv[3]
        track_ids = [line.strip() for line in sys.stdin]
        assert all(' ' not in track_id for track_id in track_ids)
        response = add_to_playlist(track_ids, playlist_id, position)
        print(json.dumps(response))
