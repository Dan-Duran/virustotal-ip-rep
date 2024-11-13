# VirusTotal IP and Domain Reputation Checker

This Python script allows you to check the reputation of IP addresses and domains using the VirusTotal API. The script fetches detailed information about each IP address and domain, including security information, location, and network details.

- **👉 Checkout some more awesome tools at [GetCyber](https://getcyber.me/tools)**
- **👉 Subscribe to my YouTube Channel [GetCyber - YouTube](https://youtube.com/getCyber)**
- **👉 Discord Server [GetCyber - Discord](https://discord.gg/YUf3VpDeNH)**

## Features

- Fetches detailed information about IP addresses and domains from VirusTotal.
- Provides security details (reputation score, malicious counts, etc.).
- Outputs results to timestamped files in the `output` directory. (the output directory will be created on your first run)

## Prerequisites

- Python 3.6 or later.
- An API key from [VirusTotal](https://www.virustotal.com/).

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Dan-Duran/virustotal-ip-rep.git
    cd virustotal-ip-rep
    ```

2. Save your API key in the `settings.py` file:

    Open `settings.py` and replace the placeholder `YOUR_API_KEY` with your actual API key.

    ```python
    API_KEY = 'YOUR_API_KEY'
    ```

## Usage

1. Prepare your input file with IP addresses and/or domains:

    Create a file (e.g., `input.txt`) and add IP addresses and/or domains to it, one per line.

    Example `input.txt`:

    ```plaintext
    # Add your IP and/or domain list here (one IP/domain per line)
    8.8.8.8
    example.com
    1.1.1.1
    anotherexample.com
    ```

2.1 Run the script (Linux & Mac):

    ```bash
    python3 vt.py
    ```
2.2 Run the script (Windows):

    ```bash
    python vt.py
    ```

3. Follow the on-screen menu to choose the type of check you want to perform:

    - Single IP Address: All info of a single IP
    - Single Domain: All info of a single domain
    - IP/Domain List: Reputation score, country, and stats for each IP/Domain in the list
    - Exit

## File Structure

```plaintext
virustotal-ip-rep/
├── includes/
│   ├── single_ip.py
│   ├── single_domain.py
│   └── ip_domain_list.py
├── output/
│   ├── single-ip/
│   ├── single-domain/
│   └── domain-ip-lists/
├── settings.py
├── vt.py
├── input.txt
└── README.md
```
## Parameters Explained

### Security
- **VPN**: Determines if IP address is a VPN.
- **Proxy**: Determines if IP address is a Proxy.
- **Tor**: Determines if IP address is a Tor Node.
- **Relay**: Determines if IP address is a Relay (e.g., iCloud Private Relay).

### Location
- **City**: Displays the approximate city of the IP address location.
- **Region**: Displays the approximate region or state of the IP address location.
- **Country**: Displays the approximate country of the IP address location.
- **Continent**: Displays the approximate continent of the IP address location.
- **Region Code**: Displays the IP address ISO 3166-1 country code.
- **Country Code**: Displays the IP address region/state code.
- **Continent Code**: Displays the IP address continent code.
- **Latitude**: Displays the latitude of the IP address.
- **Longitude**: Displays the longitude of the IP address.
- **Time Zone**: Displays the approximate time zone of the IP address.
- **Locale Code**: Determines the regional language based on the IP address location.
- **Metro Code**: Displays the metro code based on the IP address location (for US IP addresses).
- **Is In European Union**: Determines if the IP address is located within the European Union.

### Network
- **Network**: Displays which network the IP address belongs to.
- **Autonomous System Number (ASN)**: Displays the autonomous system number of the network.
- **Autonomous System Organization (ASO)**: Displays the organization that manages the network.

### Contributing
Contributions are welcome! Please submit a pull request with any improvements or additions.

### License
This project is licensed under the MIT License.
