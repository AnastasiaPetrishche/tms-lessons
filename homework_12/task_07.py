import re


def generate_words(string: str):
    for world in re.findall(r'[а-яА-Яa-zA-Z]+', string):
        yield world


if __name__ == '__main__':
    text = 'Мама. мыла? раму! мама, мыла- Милу'

for w in generate_words(text):
    print(w)
