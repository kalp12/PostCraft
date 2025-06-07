import json

def process_posts(raw_file_path,processed_file_path = 'data/processed_posts.json'):
    enriched_posts = []
    with open(raw_file_path, 'r', encoding='utf-8') as raw_file:
        raw_data = json.load(raw_file)
        for post in raw_data:
            # print(post['text'].encode('utf-8', errors='ignore').decode('utf-8'))
            metadata = extract_metadata(post['text']) 
            post_with_metadata = post | metadata       
            enriched_posts.append(post_with_metadata)
    for epost in enriched_posts:
        print(epost)
                
def extract_metadata(post):
    return {
        'line_count': post.count('\n') + 1,
        'word_count': len(post.split()),    
        'language': 'english', 
        'tags' : ['mental health', 'wellness'] 
    }

if __name__ == "__main__":
    process_posts('data/raw_posts.json', 'data/processed_posts.json')