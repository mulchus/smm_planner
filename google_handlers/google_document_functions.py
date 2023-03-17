import json
from urllib.parse import urlparse

import gdown
from bs4 import BeautifulSoup


def get_post_text(link_google_document):
    document_name = 'temp_post_file'
    gdown.download(url=link_google_document, output=document_name, fuzzy=True, quiet=True)
    text = get_google_document_text(document_name)
    return text


def get_google_document_text(document_name):
    with open(document_name, 'r', encoding='UTF-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        scripts = soup.find_all({'script': 'nonce'})
        text = ''
        for script in scripts:
            if script.text.startswith('DOCS_modelChunk ='):
                text = script.text.replace('DOCS_modelChunk = ', '')
                excess_text_part_char = text.find('; DOCS_modelChunkLoadStart')
                text = text[:excess_text_part_char]
                text = json.loads(text)[0]['s']
                break
    return text
