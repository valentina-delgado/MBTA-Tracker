import requests
import time
from datetime import datetime

# Get your free API key from: https://api-v3.mbta.com/
API_KEY = "90066ccdb48844b49afbd0ce275cd03e"
BASE_URL = "https://api-v3.mbta.com"

def get_predictions(stop_id, route_id=None):
    """Get real-time predictions for a stop."""
    url = f"{BASE_URL}/predictions"
    params = {
        "api_key": API_KEY,
        "filter[stop]": stop_id,
        "include": "route,trip"
    }
    if route_id:
        params["filter[route]"] = route_id
    
    response = requests.get(url, params=params)
    return response.json()

def format_time(arrival_time):
    """Format arrival time to minutes from now."""
    if not arrival_time:
        return "Arriving"
    
    arrival = datetime.fromisoformat(arrival_time.replace('Z', '+00:00'))
    now = datetime.now(arrival.tzinfo)
    diff = (arrival - now).total_seconds() / 60
    
    if diff < 1:
        return "Arriving"
    return f"{int(diff)} min"

def display_predictions(stop_id, stop_name):
    """Display predictions for a stop."""
    print(f"\n🚌 {stop_name}")
    print("=" * 50)
    
    data = get_predictions(stop_id)
    
    if not data.get('data'):
        print("No upcoming arrivals")
        return
    
    for prediction in data['data'][:5]:  # Show next 5
        route = prediction['relationships']['route']['data']['id']
        direction = prediction['attributes']['direction_id']
        arrival = prediction['attributes']['arrival_time']
        
        print(f"{route:8} → {format_time(arrival):>12}")

def main():
    # Popular Boston stops
    stops = {
        "1": ("place-north", "North Station"),
        "2": ("place-harsq", "Harvard Square"),
        "3": ("place-knncl", "Kenmore"),
        "4": ("place-rugg", "Ruggles")
    }
    
    print("\n🚇 MBTA Tracker")
    print("Select a stop:")
    for key, (_, name) in stops.items():
        print(f"{key}. {name}")
    
    choice = input("\nEnter number: ")
    
    if choice in stops:
        stop_id, stop_name = stops[choice]
        while True:
            display_predictions(stop_id, stop_name)
            time.sleep(30)  # Refresh every 30 seconds
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()