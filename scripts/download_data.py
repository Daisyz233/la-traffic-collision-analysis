"""Download LA traffic collision data from the Los Angeles Open Data Portal.

This script downloads the public CSV export from the Socrata API and saves it
locally under data/raw/. The raw data folder is ignored by Git because the file
can be large.
"""

from pathlib import Path
from urllib.request import urlretrieve

DATA_URL = "https://data.lacity.org/api/views/d5tf-ez2w/rows.csv?accessType=DOWNLOAD"
OUTPUT_PATH = Path("data/raw/traffic_collision_data.csv")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading data from: {DATA_URL}")
    print(f"Saving to: {OUTPUT_PATH}")
    urlretrieve(DATA_URL, OUTPUT_PATH)
    print("Download complete.")


if __name__ == "__main__":
    main()
