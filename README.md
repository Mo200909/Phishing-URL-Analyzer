# Phishing URL Analyzer

**TL;DR:** Paste a URL, get a risk score (LOW / MEDIUM / HIGH) and the reasons why. Offline, standard library only.

## Run it (3 steps, ~1 min)

1. Open a terminal in this folder.
2. Run `python Phishing_Analyzer.py`
3. Paste a URL that starts with `http://` or `https://`

Example:

```
Enter a URL to analyze: http://192.168.1.1/login

URL: http://192.168.1.1/login
Score: 5
Verdict: HIGH
Reasons:
- URL uses an IP address instead of a domain.
- URL does not use HTTPS.
```

## The 5 checks

| Check | Points |
|---|---|
| Hostname is a raw IP address | 3 |
| URL contains `@` | 3 |
| 4+ dots in hostname | 2 |
| Not HTTPS | 2 |
| URL longer than 75 characters | 1 |

## Verdict

| Score | Result |
|---|---|
| 0-2 | LOW |
| 3-4 | MEDIUM |
| 5+ | HIGH |

## Tested (5 of 5 passed)

| URL | Score | Verdict |
|---|---|---|
| `https://example.com/page` | 0 | LOW |
| `https://docs.python.org/3/` | 0 | LOW |
| `http://192.168.1.1/login` | 5 | HIGH |
| `https://paypal.com@evil.example/verify` | 3 | MEDIUM |
| `http://secure.login.verify.account.example.com/update` | 4 | MEDIUM |

A 5-URL sanity check, not an accuracy measurement.

## Limits (read before trusting it)

1. Weights are hand-picked, not validated on real data.
2. Long legitimate URLs and `@` in query strings give false positives.
3. Clean short HTTPS phishing URLs score 0, with no reputation or domain-age data.
4. URLs without `http://` or `https://` skip the IP and subdomain checks.
5. Lookalike (punycode) domains, shorteners, and redirects are not covered.

Learning project. Not a security control.

## Build note

Code written by me. AI (Claude) provided the spec, suggested `ipaddress` for IP validation, and gave debugging feedback.
