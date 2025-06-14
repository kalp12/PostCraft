import pandas as pd
import json
from db import get_db

class FewshotPosts:
    def __init__(self, file_path = "data/processed_posts.json"):
        self.db = get_db()
        self.df = None
        self.unique_tags = None
        self.load_posts(file_path)
        
    def load_posts(self, file_path, db=True):  
        if not db:
            with open(file_path, 'r', encoding='utf-8') as raw_file:
                raw_data = json.load(raw_file)
                self.df = pd.json_normalize(raw_data)
                self.df['length'] = self.df['line_count'].apply(self.categorize_length)
                all_tags = self.df['tags'].apply(lambda x: x).sum()
                self.unique_tags = list(set(all_tags))
        else:
            print("Loading posts from MongoDB...")
            collection = self.db['posts']
            self.df = pd.DataFrame(list(collection.find()))
            self.df['length'] = self.df['line_count'].apply(self.categorize_length)
            all_tags = self.df['tags'].apply(lambda x: x).sum()
            self.unique_tags = list(set(all_tags))

    def get_filtered_posts(self, length='short', language='english', tag='jobseekers', creator=None):
        if self.df is None:
            raise ValueError("Posts data not loaded. Please check the file path.")
        print(f"Filtering posts with length: {length}, language: {language}, tag: {tag}, creator: {creator}")
        filtered_df = self.df[
            (self.df['length'] == length) &
            (self.df['language'] == language) &
            (self.df['tags'].apply(lambda x: any(tag.lower() == t.lower() for t in x))) &
            (self.df['creator'] == creator if creator else True) 
        ]
        
        return filtered_df.to_dict(orient='records')
    
    def categorize_length(self, line_count):
        if line_count < 5:
            return 'Short'
        elif 5 <= line_count < 10:
            return 'Medium'
        else:
            return 'Long'
    
    def get_tags(self):
        return self.unique_tags

    def get_creator(self):
        return self.df['creator'].unique().tolist() if 'creator' in self.df.columns else []
    
if __name__ == "__main__":
    fs = FewshotPosts()
    # posts = fs.get_filtered_posts('Short','Hinglish','Scams')
    posts = fs.get_filtered_posts('Long','English','Job Search')
    print(posts)