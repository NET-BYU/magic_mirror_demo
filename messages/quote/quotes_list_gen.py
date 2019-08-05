###########################
# Author: Maximilian Warner
# Company: BYU
# Project: Magic Mirror
# Created 8/2/19
###########################

import json

# quotes = {}
# quotes['quotes'] = []
# quotes['quotes'].append({
#     'author': 'Karl G. Maeser',
#     'quote_text': '"I am honest, etc."',
# })
# quotes['quote'].append({
#     'author': 'Colin Powell',
#     'quote_text': '"There are no secrets to success. It is the result of preparation, hard work and learning from failure."',
# })
# quotes['quote'].append({
#     'author': 'Russel M. Nelson',
#     'quote_text': '"We can do better and be better."',
# })
# quotes['quote'].append({
#     'author': 'Winston Churchill',
#     'quote_text': '"Success consists of going from failure to failure without loss of enthusiasm."',
# })
#
# with open('quotes_list.txt', 'w') as outfile:
#     json.dump(quotes, outfile, indent=4)


quotes = []
quote = {
    'author': 'Karl G. Maeser',
    'quote_text': '"I am honest, etc."',
}
quotes.append(quote)
quote = {
    'author': 'Colin Powell',
    'quote_text': '"There are no secrets to success. It is the result of preparation, hard work and learning from failure."',
}
quotes.append(quote)
quote = {
    'author': 'Russel M. Nelson',
    'quote_text': '"We can do better and be better"',
}
quotes.append(quote)
quote = {
    'author': 'Winston Churchill',
    'quote_text': '"Success consists of going from failure to failure without loss of enthusiasm."',
}
quotes.append(quote)
quote = {
    'author': 'Maya Angelou',
    'quote_text': '"My mission in life is not merely to survive, but to thrive; and to do so with some passion, some compassion, some humor, and some style."',
}
quotes.append(quote)
quote = {
    'author': 'Theodore Roosevelt',
    'quote_text': '"To educate a person in the mind but not in morals is to educate a menace to society."',
}
quotes.append(quote)
with open('quotes_list.txt', 'w') as outfile:
    json.dump(quotes, outfile, indent=4)
