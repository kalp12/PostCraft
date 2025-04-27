import json

def process_posts(raw_file_path,processed_file_path):
    with open(raw_file_path, 'r', encoding='utf-8') as raw_file:
        raw_data = json.load(raw_file)
        for post in raw_data:
            print(post['text'].encode('utf-8', errors='ignore').decode('utf-8'))

if __name__ == "__main__":
    process_posts('data/raw_posts.json', 'data/processed_posts.json')