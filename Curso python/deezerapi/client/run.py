import os

from test import DeezerC


def run():
	test = DeezerC(os.getenv('DEEZER_AUTH_TOKEN'))
	random_tracks = test.get_random_tracks()
	track_ids = [track['id'] for track in random_tracks]

	was_added_to_library = test.add_tracks_to_library(track_ids)
	if was_added_to_library:
		for track in random_tracks:
			print(f"Added {track['name']} to your library")


if __name__ == '__main__':
	run()