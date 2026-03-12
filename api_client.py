import requests

def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for non-200 HTTP status

        users = response.json()

        for i, user in enumerate(users[:num_users]):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"User {i+1}: {name}, {email}, {city}")
            except KeyError as e:
                print(f"Missing expected key in user data: {e}")
                continue

    except requests.exceptions.RequestException as e:
        print(f"Network or HTTP error occurred: {e}")
        return None
    except ValueError as e:
        print(f"Error parsing JSON response: {e}")
        return None


# Example calls
fetch_and_display_users(3)