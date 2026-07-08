import re
import requests
from bs4 import BeautifulSoup


def decode_secret_message(doc_url: str) -> None:
    """
    Downloads the Given doc and prints the grid
    """

    # Convert a normal published Google Doc URL into a plain HTML export.
    match = re.search(r"/d/([a-zA-Z0-9_-]+)", doc_url)
    if match:
        doc_id = match.group(1)
        url = f"https://docs.google.com/document/d/{doc_id}/export?format=html"
    else:
        url = doc_url

    html = requests.get(url)
    html.raise_for_status()

    soup = BeautifulSoup(html.text, "html.parser")
    table = soup.find("table")
    if table is None:
        raise ValueError("No table found in document.")

    points = []
    max_x = 0
    max_y = 0

    rows = table.find_all("tr")[1:]  # Skip header

    for row in rows:
        cols = [c.get_text(strip=True) for c in row.find_all(["td", "th"])]
        if len(cols) != 3:
            continue

        x = int(cols[0])
        ch = cols[1]
        y = int(cols[2])

        points.append((x, y, ch))
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    # Fill grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, ch in points:
        grid[y][x] = ch

    for row in grid:
        print("".join(row))
        
        
decode_secret_message(
    "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
)