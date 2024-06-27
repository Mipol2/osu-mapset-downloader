import os
import requests
from tqdm import tqdm

def download_beatmap(mapset_id):
    url = f"https://proxy.nerinyan.moe/d/{mapset_id}"
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        # Create the directory if it doesn't exist
        directory = "downloaded_beatmaps"
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_name = os.path.join(directory, f"{mapset_id}.osz")
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024

        with open(file_name, "wb") as file:
            with tqdm(total=total_size, unit='iB', unit_scale=True, desc=file_name) as pbar:
                for data in response.iter_content(block_size):
                    file.write(data)
                    pbar.update(len(data))
        
        print(f'Beatmap {mapset_id} downloaded successfully as {file_name}.')
        os.startfile(file_name)
    else:
        print(f"Failed to download beatmap {mapset_id}. Status code: {response.status_code}")

if __name__ == "__main__":
    flag = True
    while flag:
        mapset_id = input("Enter the mapset ID: ")
        if mapset_id == "exit":
            flag = False
        download_beatmap(mapset_id)
