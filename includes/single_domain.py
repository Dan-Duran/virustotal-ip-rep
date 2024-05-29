import os
import json
import urllib.request
import urllib.parse
from datetime import datetime
from settings import API_KEY, API_URL_DOMAIN

def fetch_data(url):
    request = urllib.request.Request(url, headers={'x-apikey': API_KEY})
    try:
        with urllib.request.urlopen(request) as response:
            data = json.load(response)
            return data
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data: {e}")
        return None

def display_domain_info(domain):
    url = API_URL_DOMAIN + urllib.parse.quote(domain)
    data = fetch_data(url)
    if not data:
        return

    attributes = data.get('data', {}).get('attributes', {})
    last_analysis_stats = attributes.get('last_analysis_stats', {})
    
    result = [
        f"Domain: {domain}",
        f"Categories: {', '.join(attributes.get('categories', {}).values())}",
        f"Creation Date: {attributes.get('creation_date')}",
        f"Last Analysis Date: {attributes.get('last_analysis_date')}",
        f"Last Analysis Stats:",
        f"  Harmless: {last_analysis_stats.get('harmless', 0)}",
        f"  Malicious: {last_analysis_stats.get('malicious', 0)}",
        f"  Suspicious: {last_analysis_stats.get('suspicious', 0)}",
        f"  Timeout: {last_analysis_stats.get('timeout', 0)}",
        f"  Undetected: {last_analysis_stats.get('undetected', 0)}",
        f"Last Modification Date: {attributes.get('last_modification_date')}",
        f"Reputation Score: {attributes.get('reputation')}",
        f"Tags: {', '.join(attributes.get('tags', []))}",
        f"Total Votes: Harmless - {attributes.get('total_votes', {}).get('harmless', 0)}, Malicious - {attributes.get('total_votes', {}).get('malicious', 0)}",
        "-" * 40
    ]

    # Ensure the output directory exists
    output_dir = "output/single-domain"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{domain}.txt")
    with open(output_path, 'w') as f:
        f.write("\n".join(result))

    print("\n".join(result))
