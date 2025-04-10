import requests
import time


def test_google_maps_api_key(api_key):
    """
    Test Google Maps API key functionality with basic requests
    """
    endpoints = {
        "Geocoding": f"https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={api_key}",
        "Places": f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum&inputtype=textquery&key={api_key}",
        "Directions": f"https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal&key={api_key}",
    }

    results = {}
    for name, url in endpoints.items():
        try:
            response = requests.get(url)
            status = response.json().get("status", "")
            results[name] = {
                "status_code": response.status_code,
                "api_status": status,
                "valid": response.status_code == 200 and status != "REQUEST_DENIED",
            }
            # Respect rate limits
            time.sleep(1)
        except Exception as e:
            results[name] = {"error": str(e)}

    return results


def print_results(results):
    print("\nAPI Key Test Results:")
    print("-" * 50)
    for endpoint, result in results.items():
        print(f"\n{endpoint}:")
        for key, value in result.items():
            print(f"  {key}: {value}")


if __name__ == "__main__":
    api_key = input("Enter your Google Maps API key: ")
    results = test_google_maps_api_key("AIzaSyAU9sG696hoKqdoDZNpvCcHU-RdV82AFWo")
    print_results(results)
