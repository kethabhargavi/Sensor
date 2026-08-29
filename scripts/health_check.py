import urllib.request
import sys

URL = "http://localhost:8501"

try:
    response = urllib.request.urlopen(URL, timeout=5)

    if response.status == 200:
        print("Application is healthy.")
        sys.exit(0)

    print(f"Application returned status: {response.status}")
    sys.exit(1)

except Exception as error:
    print(f"Health check failed: {error}")
    sys.exit(1)
