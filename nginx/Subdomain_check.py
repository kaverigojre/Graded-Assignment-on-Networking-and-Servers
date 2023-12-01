import requests
from tabulate import tabulate
import time


subdomains = ["awesomeweb", "subdomain1", "subdomain2"]

def check_subdomains(subdomains):
    results = []

    for subdomain in subdomains:
        url = f"http://{subdomain}"

        try:
            response = requests.get(url, timeout=5)
            status = response.status_code
        except requests.ConnectionError:
            status = "Connection Error"

        results.append((subdomain, status))

    return results

def display_results(results):
    headers = ["Subdomain", "Status"]
    table = tabulate(results, headers=headers, tablefmt="pretty")
    print(table)

def main():
    while True:
        print("Checking subdomains...")
        results = check_subdomains(subdomains)
        display_results(results)
        time.sleep(60)  

if __name__ == "__main__":
    main()