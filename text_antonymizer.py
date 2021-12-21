"""
Module containing utilities to replace words in russian text with their antonyms.
"""
import re
import requests
import pymorphy2
from bs4 import BeautifulSoup


def find_antonym(word):
    """
    Return antonym for the word, if there is no antonym for such word in antonymonline.ru,
    return this word.

    :param word: word in Russian that we find antonym for.
    :type word: str

    :rtype: str
    :return: antonym, word
    """
    soup = BeautifulSoup(requests.get(f'https://antonymonline.ru/{word[0]}/{word}').text, 'html.parser')
    li_tags = soup.findAll('li')
    for tag in li_tags:
        if tag.findChild('span'):
            return tag.findChild('span').text
    return word


def antonymize_text(text):
    """
    Function that replaces some russian words for their antonyms.

    :param text: text in Russian where we want to change words to their antonyms.
    :type text: str

    :rtype: str
    :return: changed_text
    """
    morph = pymorphy2.MorphAnalyzer(lang='ru')
    words = re.findall(r'([А-я]+)', text)
    words_indexes = [[word.start(), word.end()] for word in re.finditer(r'([А-я]+)', text)]
    words_indexes.append([len(text)])
    changed_text = [text[:words_indexes[0][0]]]

    for i, word in enumerate(words):
        adding_word = word

        analyze = morph.parse(word)[0]
        antonym = find_antonym(analyze.normal_form)
        antonym_analyze = morph.parse(antonym)[0]
        if antonym_analyze.inflect(analyze.tag.grammemes):
            adding_word = antonym_analyze.inflect(analyze.tag.grammemes).word
            if word[0].isupper():
                adding_word = adding_word.capitalize()
        changed_text.extend([adding_word, text[words_indexes[i][1]:words_indexes[i + 1][0]]])
    return ''.join(changed_text)
