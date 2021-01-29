# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 10:07:24 2020

@author: Razer Blade
"""

def book2hist(textfile,n):
    import string
    import matplotlib.pyplot as plt
    import numpy as np

    count_words=dict()
    text= open(textfile)
    text = text.read().lower().translate(str.maketrans('', '', string.punctuation))
    text_list = text.split()
    text_set = set(text_list)
    for i in text_set:
        count_words[i] = text_list.count(i)

    sorted_dict = sorted(count_words.items(), key=lambda x: x[1], reverse=True)
    sorted2 = sorted_dict[:n]

    word = []
    value = []
    for i in sorted2 :
        a,b = i
        word.append(a)
        value.append(b)
  
    y= np.arange(len(word))
    plt.style.use('ggplot')
    plt.xticks(y,word)
    plt.title("Zipf's Law")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.bar(y,value,edgecolor="black")
  