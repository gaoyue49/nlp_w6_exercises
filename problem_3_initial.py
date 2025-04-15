# -*- coding: utf-8 -*-
"""problem_3_initial.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NEBdolccu-oAIP_aeavEO1FUIUbGNgk0
"""

# 의존성 설치
!pip install nltk

import numpy as np
from nltk.tokenize import word_tokenize
import nltk

# NLTK 데이터 다운로드
nltk.download('punkt')
nltk.download('punkt_tab')

# 기술 주제 말뭉치
tech_corpus = [
    "artificial intelligence powers modern computers",
    "machine learning algorithms process big data",
    "neural networks drive ai innovation"
]

# 토큰화
tech_tokenized = [word_tokenize(s.lower()) for s in tech_corpus]
tech_vocab = sorted(set(word for s in tech_tokenized for word in s))
tech_word2idx = {word: idx for idx, word in enumerate(tech_vocab)}

# 동시출현 행렬 생성 함수
def build_cooc_matrix(tokenized_corpus, vocab, window_size):
    cooc_matrix = np.zeros((len(vocab), len(vocab)))
    for sentence in tokenized_corpus:
        for i, word in enumerate(sentence):
            start = max(0, i - window_size)
            end = min(len(sentence), i + window_size + 1)
            for j in range(start, end):
                if i != j:
                    cooc_matrix[tech_word2idx[word]][tech_word2idx[sentence[j]]] += 1
    return cooc_matrix

# 행렬 생성
tech_matrix = build_cooc_matrix(tech_tokenized, tech_vocab, window_size=3)