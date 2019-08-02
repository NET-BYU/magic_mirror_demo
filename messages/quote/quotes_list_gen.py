###########################
# Author: Maximilian Warner
# Company: BYU
# Project: Magic Mirror
# Created 8/2/19
###########################

import json

quotes = {}
quotes['quote'] = []
quotes['quote'].append({
    'author': 'Karl G. Maeser',
    'quote_text': '"I\'m honest, etc."',
})
quotes['quote'].append({
    'author': 'Colin Powell',
    'quote_text': '“There are no secrets to success. It is the result of preparation, hard work and learning from failure.”',
})
quotes['quote'].append({
    'author': 'Russel M. Nelson',
    'quote_text': '"We can do better and be better."',
})
quotes['quote'].append({
    'author': 'Winston Churchill',
    'quote_text': '"Success consists of going from failure to failure without loss of enthusiasm."',
})

with open('quotes_list.txt', 'w') as outfile:
    json.dump(quotes, outfile)
