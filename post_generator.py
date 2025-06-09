from llm_helper import llm
from few_shots import FewshotPosts

few_shot = FewshotPosts()

def get_length(length):
    if length == 'Short':
        return '1 to 5 lines'
    elif length == 'Medium':
        return '6 to 10 lines'
    else:
        return '11 to 20 lines'

def generate_posts(title, length, language, creator):
    prompt = get_prompt(title, length, language, creator)
    response = llm.invoke(prompt)
    return response.content

def get_prompt(title, length, language,creator):
    length_str = get_length(length)
    prompt = f'''
    Generate a LinkedIn post using the below information. No preamble.

    1) Topic: {title}
    2) Length: {length_str}
    3) Language: {language}
    4) Writing Style: Match the tone and writing style of {creator}
    This includes their typical sentence structure, voice (personal/professional/motivational/etc.), and use of emojis or storytelling.
    
    If Language is Hinglish then it means it is a mix of Hindi and English. 
    The script for the generated post should always be English.
    '''
    examples = few_shot.get_filtered_posts(length, language, title,creator)
    if len(examples) > 0:
        prompt += "5) Use the writing style as per the following examples."

    for i, post in enumerate(examples):
        post_text = post['text']
        prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        if i == 1: 
            break
    
    return prompt

if __name__ == "__main__":
    print(generate_posts("Job Seekers", "Short", "English"))

