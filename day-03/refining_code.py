import requests
import json


api_url = "https://jsonplaceholder.typicode.com/todos"

#for extracting meaningful data from json

def process_todo_data(todos):
    processed = []

    for todo in todos[:10]:

        processed.append({
            "id": todo.get("id"),
            "userId": todo.get("userId"),
            "title": todo.get("title"),
            "completed": todo.get("completed")
        })
        
    return processed  

# Add try/except in fetch_todos() (API failure handling)

def fetch_todos(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # handles 4xx/5xx
        return response.json()
    except requests.exceptions.Timeout:
        print("ERROR: Request timed out. Please check your internet and try again.")
        return []
    except requests.exceptions.RequestException as e:
        print(f"ERROR: API request failed: {e}")
        return []
    except ValueError:
        print("ERROR: Response was not valid JSON.")
        return []
    
#Add try/except for file saving (file/permission handling)

def save_to_json(data, filename="output.json"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
        return True
    except OSError as e:
        print(f"ERROR: Could not write to {filename}: {e}")
        return False
# Update main() to use the safe flow (no crashes)
    
def main():
   
    todos = fetch_todos(api_url)
    if not todos:
        print("No todo data received. Exiting safely.")
        return

    processed_todos = process_todo_data(todos)

    print("\nProcessed Todo:\n")
    for todo in processed_todos:
        print(f"- [{todo['completed']}] {todo['title']}")

    if save_to_json(processed_todos):
        print("\nData saved to output.json")


if __name__ == "__main__":
    main()


