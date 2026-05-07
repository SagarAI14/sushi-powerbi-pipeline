import requests

def extract_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    try:

        print("Calling API...\n")

        response = requests.get(url, timeout=10)

        print(f"Status Code: {response.status_code}")

        # Validate status code
        response.raise_for_status()

        data = response.json()

        print("API data extracted successfully!\n")

        return data

    except requests.exceptions.Timeout:

        print("ERROR: API request timed out")

    except requests.exceptions.HTTPError as err:

        print(f"HTTP ERROR: {err}")

    except requests.exceptions.ConnectionError:

        print("ERROR: Connection failed")

    except requests.exceptions.RequestException as err:

        print(f"REQUEST ERROR: {err}")

    except Exception as err:

        print(f"UNEXPECTED ERROR: {err}")

    return []