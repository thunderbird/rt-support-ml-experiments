import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urlparse

# List of Thunderbird release note URLs
urls = [
    "https://www.thunderbird.net/en-US/thunderbird/128.0esr/releasenotes/",
    "https://www.thunderbird.net/en-US/thunderbird/128.0.1esr/releasenotes/",
    "https://www.thunderbird.net/en-US/thunderbird/128.1.0esr/releasenotes/",
    # Add all remaining URLs here
]

def extract_section(soup, section_id):
    section = soup.find('h3', id=section_id)
    if not section:
        return []
    notes = []
    for sibling in section.find_next_siblings():
        if sibling.name == 'h3':
            break
        if sibling.name == 'div' and 'note-text' in sibling.get('class', []):
            notes.append(sibling.get_text(strip=True))
    return notes

def parse_release_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    release_name = url.strip('/').split('/')[-2]

    date_div = soup.select_one('div.release-text-container > h4')
    release_date = date_div.get_text(strip=True).replace("Released ", "") if date_div else ""

    whats_new = extract_section(soup, 'whatsnew')
    whats_changed = extract_section(soup, 'changed')
    whats_fixed = extract_section(soup, 'fixes')
    known_issues = extract_section(soup, 'known-issues')

    return {
        "link": url,
        "release_name": release_name,
        "release_date": release_date,
        "whats_new": whats_new,
        "whats_changed": whats_changed,
        "whats_fixed": whats_fixed,
        "known_issues": known_issues
    }

results = []
for url in urls:
    try:
        results.append(parse_release_page(url))
        print(f"Processed {url}")
        time.sleep(60)  # Wait 1 minute between requests
    except Exception as e:
        print(f"Failed to process {url}: {e}")

with open('thunderbird_releases.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Scraping completed.")
