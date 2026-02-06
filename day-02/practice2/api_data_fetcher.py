import requests
import json


api_url = "https://jsonplaceholder.typicode.com/todos"


def fetch_todos():
    response = requests.get(url=api_url)
    if response.status_code == 200: 
        #print(response.json())
        return response.json()

todos = fetch_todos()
     
#for extracting meaningful data from json

def process_todo_data():
    processed = []

    for todo in todos[:10]:

        processed.append({
            "id": todo["id"],
            "userId": todo["userId"],
            "title": todo["title"],
            "completed": todo["completed"]
        })
        
    return processed  

def save_to_json(data, filename="output.json"):
    """Save processed data to JSON file"""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def main():
    todos = fetch_todos()
    processed_todo = process_todo_data()

    print("\nProcessed Todo:\n")
    for t in processed_todo:
        print(f"- [{t['completed']}] {t['title']}")

    save_to_json(processed_todo)
    print("\nData saved to output.json")


if __name__ == "__main__":
    main()


