import ipaddress
from urllib.parse import urlparse


def analyze_url(url):
    features = {
        "score": 0,
        "reasons": []
    }

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname or ""

    # IP address: +3
    try:
        ipaddress.ip_address(hostname)
        features["score"] += 3
        features["reasons"].append(
            "URL uses an IP address instead of a domain."
        )
    except ValueError:
        pass

    # Long URL: +1
    if len(url) > 75:
        features["score"] += 1
        features["reasons"].append("URL is unusually long.")

    # @ symbol: +3
    if "@" in url:
        features["score"] += 3
        features["reasons"].append("URL contains '@'.")

    # Excessive subdomains: +2
    if hostname.count(".") >= 4:
        features["score"] += 2
        features["reasons"].append(
            "Hostname contains 4 or more dots."
        )

    # No HTTPS: +2
    if parsed_url.scheme.lower() != "https":
        features["score"] += 2
        features["reasons"].append(
            "URL does not use HTTPS."
        )

    # Determine verdict
    if features["score"] <= 2:
        verdict = "LOW"
    elif features["score"] <= 4:
        verdict = "MEDIUM"
    else:
        verdict = "HIGH"

    features["verdict"] = verdict

    return features


url = input("Enter a URL to analyze: ")

result = analyze_url(url)

print(f"\nURL: {url}")
print(f"Score: {result['score']}")
print(f"Verdict: {result['verdict']}")
print("Reasons:")

for reason in result["reasons"]:
    print(f"- {reason}")