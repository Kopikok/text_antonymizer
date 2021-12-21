<h1 align="center">Text Antonymizer</h1>

<p align="center">
 
<img src="https://img.shields.io/badge/made%20by-kopikok-blue.svg">

<img src="https://img.shields.io/badge/python-3.7-blue.svg">

<img src="https://img.shields.io/badge/pymorphy2-0.9.1-green.svg">
 
</p>

The text antonymizer has a function `antonymize_text(text)` to replace some words in Russian to their antonyms using parsing of [antonymonline](https://antonymonline.ru/) website. You can also get one antonym for one word see usages below.

<h2>Install</h2>

```cmd
git clone https://github.com/Kopikok/text_antonymizer.git
cd text_antonymizer
pip3 install -r requirements.txt
```

<h2>Usages</h2>

In python3 terminal:

```python3
from text_antonymizer import antonymize_text
antonymize_text(YOUR_TEXT)
```
Replace words in Russian for their antonyms in `YOUR_TEXT`, then return changed text.

```python3
from text_antonymizer import find_antonym
find_antonym(YOUR_WORD)
```
Find antonym for YOUR_WORD in Russian, if there is no antonym in [antonymonline](https://antonymonline.ru/) website, return YOUR_WORD without changes.
