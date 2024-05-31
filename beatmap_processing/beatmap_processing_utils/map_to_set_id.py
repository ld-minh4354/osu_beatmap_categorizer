import requests, time


def get_beatmapset_id(beatmap_id):
    # wait to avoid excessive api requests
    time.sleep(0.5)

    # API endpoint for retrieving beatmap information
    url = f"https://osu.ppy.sh/api/get_beatmaps?k=ea01bae795dbb0e7fdad98e12ddb69cd9b24fa59&b={beatmap_id}"

    try:
        # Send GET request to the API
        response = requests.get(url)
        data = response.json()

        # Extract the beatmapset ID from the response
        if data and len(data) > 0:
            beatmapset_id = data[0]['beatmapset_id']
            return beatmapset_id
        else:
            print("No beatmapset found for the given beatmap ID.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == '__main__':
    beatmap_id = 4476808
    beatmapset_id = get_beatmapset_id(beatmap_id)
    print("Beatmapset ID:", beatmapset_id)