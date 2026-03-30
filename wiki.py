import requests

headers = {"User-Agent" : "wiki-cli-project/1.0 (learning project)"}
while True:
    topic = input("Enter a topic to retrieve from wiki: (or 'quit' to exit): ")
    print("="*50)
    if topic == 'quit':
        break
    topic = topic.replace(" ", "_")
    response = requests.get(f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}", headers=headers)
    data = response.json()
    if response.status_code == 200 and 'extract' in data:
        print(data['extract'])
        print("="*50)
        with open(f"{topic}.txt", "w") as f:
            f.write(data['title'] + "\n\n")
            f.write(data['extract'])
        print(f"Saved to {topic}.txt ✅")
    else:
        print(f"Topic '{topic}' not found on Wikipedia. Try a different search term.")

