import re

def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def remove_words(text, words_to_remove):
    pattern = r'\b(' + '|'.join(map(re.escape, words_to_remove)) + r')\b'
    cleaned_text = re.sub(pattern, '', text)
    return re.sub(r'\s+', ' ', cleaned_text).strip()

def replace_words(text, words_to_replace):
    pattern = re.compile(r'\b(' + '|'.join(map(re.escape, words_to_replace.keys())) + r')\b')
    replaced_text = pattern.sub(lambda match: words_to_replace[match.group()], text)
    return replaced_text

path = "C:/Users/lukas/Downloads/plik.txt"
text = read_file(path)
print(f"\n{text}\n")

words_to_remove = ["skryptu"]
print(remove_words(text, words_to_remove))

words_to_replace = {"test": "próba", "skryptu": "działania"}
print(replace_words(text, words_to_replace))