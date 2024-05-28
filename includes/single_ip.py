import os
import json
import urllib.request
import urllib.parse
from datetime import datetime
from settings import API_KEY, API_URL_IP

def fetch_data(url):
    request = urllib.request.Request(url, headers={'x-apikey': API_KEY})
    try:
        with urllib.request.urlopen(request) as response:
            data = json.load(response)
            return data
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data: {e}")
        return None

def get_associated_domains(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}/resolutions"
    request = urllib.request.Request(url, headers={'x-apikey': API_KEY})
    associated_domains = []
    try:
        with urllib.request.urlopen(request) as response:
            data = json.load(response)
            associated_domains.extend([res['attributes']['host_name'] for res in data.get('data', [])])
    except urllib.error.URLError as e:
        print(f"Failed to retrieve associated domains for {ip}: {e}")
    return associated_domains

def display_ip_info(ip):
    url = API_URL_IP + urllib.parse.quote(ip)
    data = fetch_data(url)
    if not data:
        return

    attributes = data.get('data', {}).get('attributes', {})
    last_analysis_stats = attributes.get('last_analysis_stats', {})
    associated_domains = get_associated_domains(ip)

    result = [
        f"IP: {ip}",
        f"AS Owner: {attributes.get('as_owner')}",
        f"ASN: {attributes.get('asn')}",
        f"Continent: {attributes.get('continent')}",
        f"Country: {attributes.get('country')}",
        f"JARM: {attributes.get('jarm')}",
        f"Last Analysis Date: {attributes.get('last_analysis_date')}",
        f"Reputation Score: {attributes.get('reputation')}",
        f"Tags: {', '.join(attributes.get('tags', []))}",
        f"Total Votes: Harmless - {attributes.get('total_votes', {}).get('harmless', 0)}, Malicious - {attributes.get('total_votes', {}).get('malicious', 0)}",
        "Last Analysis Stats:",
        f"  Harmless: {last_analysis_stats.get('harmless', 0)}",
        f"  Malicious: {last_analysis_stats.get('malicious', 0)}",
        f"  Suspicious: {last_analysis_stats.get('suspicious', 0)}",
        f"  Timeout: {last_analysis_stats.get('timeout', 0)}",
        f"  Undetected: {last_analysis_stats.get('undetected', 0)}",
        f"Last HTTPS Certificate Date: {attributes.get('last_https_certificate_date')}",
        f"Last Modification Date: {attributes.get('last_modification_date')}",
        f"Network: {attributes.get('network')}",
        f"Regional Internet Registry: {attributes.get('regional_internet_registry')}",
        f"WHOIS: {attributes.get('whois')}",
        f"WHOIS Date: {attributes.get('whois_date')}",
        f"Associated Domains: {', '.join(associated_domains) if associated_domains else 'No associated domains'}",
        "-" * 40
    ]

    # Ensure the output directory exists
    output_dir = "output/single-ip"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, f"{ip}.txt")
    with open(output_path, 'w') as f:
        f.write("\n".join(result))

    print("\n".join(result))
