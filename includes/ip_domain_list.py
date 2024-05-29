import os
import csv
import json
import urllib.request
import urllib.parse
from datetime import datetime
from settings import API_KEY, API_URL_IP, API_URL_DOMAIN

def fetch_data(url):
    request = urllib.request.Request(url, headers={'x-apikey': API_KEY})
    try:
        with urllib.request.urlopen(request) as response:
            data = json.load(response)
            return data
    except urllib.error.URLError as e:
        print(f"Failed to retrieve data: {e}")
        return None

def process_ip_or_domain_list(file_path):
    items = read_ips_from_file(file_path)
    if not items:
        print(f"No valid IPs or domains found in the file: {file_path}")
        return

    results = []
    for item in items:
        if is_ip(item):
            results.append(get_ip_summary(item))
        else:
            results.append(get_domain_summary(item))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = "output/domain-ip-lists"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"list-{timestamp}.txt")
    with open(output_path, 'w') as f:
        f.write("\n".join(results))

    print("\n".join(results))

def get_ip_summary(ip):
    url = API_URL_IP + urllib.parse.quote(ip)
    data = fetch_data(url)
    if not data:
        return f"IP: {ip} - No data"

    attributes = data.get('data', {}).get('attributes', {})
    last_analysis_results = attributes.get('last_analysis_results', {})
    malicious_count = sum(1 for result in last_analysis_results.values() if result['category'] == 'malicious')
    total_engines = len(last_analysis_results)
    reputation_score = f"{malicious_count}/{total_engines}" if total_engines > 0 else "N/A"

    return f"IP: {ip}, Country: {attributes.get('country')}, Last Analysis Results Count: {malicious_count}, Malicious Count: {malicious_count}, Total Engines: {total_engines}, Reputation Score: {reputation_score}"

def get_domain_summary(domain):
    url = API_URL_DOMAIN + urllib.parse.quote(domain)
    data = fetch_data(url)
    if not data:
        return f"Domain: {domain} - No data"

    attributes = data.get('data', {}).get('attributes', {})
    last_analysis_results = attributes.get('last_analysis_results', {})
    malicious_count = sum(1 for result in last_analysis_results.values() if result['category'] == 'malicious')
    total_engines = len(last_analysis_results)
    reputation_score = f"{malicious_count}/{total_engines}" if total_engines > 0 else "N/A"

    return f"Domain: {domain}, Country: {attributes.get('country')}, Last Analysis Results Count: {malicious_count}, Malicious Count: {malicious_count}, Total Engines: {total_engines}, Reputation Score: {reputation_score}"

def read_ips_from_file(file_path):
    items = []
    with open(file_path, 'r') as file:
        try:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    item = item.strip()
                    if item and not item.startswith('#'):
                        items.append(item)
        except csv.Error:
            file.seek(0)
            for line in file:
                line = line.strip()
                if line and not line.startswith('#'):
                    items.append(line)
    return items

def is_ip(item):
    """Check if the given item is an IP address."""
    try:
        urllib.parse.quote(item)
        ip_parts = item.split('.')
        return len(ip_parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in ip_parts)
    except ValueError:
        return False
