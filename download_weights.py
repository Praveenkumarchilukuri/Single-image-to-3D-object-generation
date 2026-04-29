import urllib.request
import os

url = "https://github.com/intel-isl/DPT/releases/download/1_0/dpt_hybrid-midas-501f0c75.pt"
dest_folder = "dpt_weights"
dest_path = os.path.join(dest_folder, "dpt_hybrid-midas-501f0c75.pt")

if not os.path.exists(dest_folder):
    os.makedirs(dest_folder)

print(f"Downloading DPT weights to {dest_path}...")
try:
    urllib.request.urlretrieve(url, dest_path)
    print("Download complete!")
except Exception as e:
    print(f"Download failed: {e}")
