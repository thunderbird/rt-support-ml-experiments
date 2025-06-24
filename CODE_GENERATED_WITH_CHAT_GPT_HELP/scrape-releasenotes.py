import requests
from bs4 import BeautifulSoup
import json
import time

# List of release note URLs
release_urls = [
    "https://www.thunderbird.net/en-US/thunderbird/128.0esr/releasenotes/",
    "https://www.thunderbird.net/en-US/thunderbird/128.0.1esr/releasenotes/",
    # Add all other URLs here
]

releases = []

for url in release_urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract release name
    release_name = soup.find('h1').text.strip() if soup.find('h1') else None

    # Extract release date
    release_date = None
    for p in soup.find_all('p'):
        if 'Released' in p.text:
            release_date = p.text.strip()
            break

    # Extract sections
    def extract_section(header_text):
        header = soup.find(lambda tag: tag.name.startswith('h') and header_text.lower() in tag.text.lower())
        if header:
            content = []
            for sibling in header.find_next_siblings():
                if sibling.name and sibling.name.startswith('h'):
                    break
                content.append(sibling.text.strip())
            return content
        return []

    whats_new = extract_section("What's New")
    whats_changed = extract_section("What's Changed")
    whats_fixed = extract_section("What's Fixed")
    known_issues = extract_section("Known Issues")

    release_info = {
        "link": url,
        "release_name": release_name,
        "release_date": release_date,
        "whats_new": whats_new,
        "whats_changed": whats_changed,
        "whats_fixed": whats_fixed,
        "known_issues": known_issues
    }

    releases.append(release_info)

    # Wait for 60 seconds before the next request
    time.sleep(60)

# Save to JSON file
with open('thunderbird_releases.json', 'w', encoding='utf-8') as f:
    json.dump(releases, f, ensure_ascii=False, indent=4)

