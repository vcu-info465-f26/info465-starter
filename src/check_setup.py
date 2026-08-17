import sys
import requests

def main():
    print(f"Python {sys.version.split()[0]}")

    response = requests.get("https://api.github.com/zen", timeout=10)
    response.raise_for_status()
    print(f"API call worked: {response.text}")

    print("Setup looks good. We did it!")

if __name__ == "__main__":
    main()