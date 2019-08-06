###########################
# Author: Maximilian Warner
# Company: BYU
# Project: Magic Mirror
# Created 8/2/19
###########################

import json


quotes = []
quote = {
    'author': 'Karl G. Maeser',
    'quote_text': '"Be yourself, but always your better self."',
}
quotes.append(quote)
quote = {
    'author': 'Thomas S. Monson',
    'quote_text': '"Choose your love, Love your choice."',
}
quotes.append(quote)
quote = {
    'author': 'Colin Powell',
    'quote_text': '"There are no secrets to success. It is the result of preparation, hard work and learning from failure."',
}
quotes.append(quote)
quote = {
    'author': 'Russel M. Nelson',
    'quote_text': '"We can do better and be better."',
}
quotes.append(quote)
quote = {
    'author': 'Mark Twain',
    'quote_text': '"The two most important days in your life are the day you are born and the day you find out why."',
}
quotes.append(quote)
quote = {
    'author': 'Billy Connolly',
    'quote_text': '"Before you judge a man, walk a mile in his shoes. After that who cares? He\'s a mile away and you\'ve got his shoes!"',
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
    'author': 'Jeffrey R. Holland',
    'quote_text': '"If for a while the harder you try, the harder it gets, take heart. So it has been with the best people who ever lived."',
}
quotes.append(quote)
quote = {
    'author': 'Theodore Roosevelt',
    'quote_text': '"To educate a person in the mind but not in morals is to educate a menace to society."',
}
quotes.append(quote)
quote = {
    'author': 'Thomas S. Monson',
    'quote_text': '"May we ever choose the harder right instead of the easier wrong."',
}
quotes.append(quote)
quote = {
    'author': 'Abraham Lincoln',
    'quote_text': '"Better to remain silent and be thought a fool than to speak out and remove all doubt."',
}
quotes.append(quote)
quote = {
    'author': 'Russel M. Nelson',
    'quote_text': '"Stellar spirits are often housed in imperfect bodies."',
}
quotes.append(quote)
quote = {
    'author': 'C. S. Lewis',
    'quote_text': '"True humility is not thinking less of yourself; it is thinking of yourself less."',
}
quotes.append(quote)
quote = {
    'author': 'Sheri L. Dew',
    'quote_text': '"There is one thing the power of God and the power of Satan have in common: Neither can influence us unless we allow them to."',
}
quotes.append(quote)
quote = {
    'author': 'Andrew Carnegie',
    'quote_text': '"There is little success where there is little laughter."',
}
quotes.append(quote)
quote = {
    'author': 'Laurence J. Peter',
    'quote_text': '"Originality is the fine art of remembering what you hear but forgetting where you heard it."',
}
quotes.append(quote)
quote = {
    'author': 'Socrates',
    'quote_text': '"Education is the kindling of a flame, not the filling of a vessel."',
}
quotes.append(quote)
quote = {
    'author': 'Jeffrey R. Holland',
    'quote_text': '"Some blessings come soon, some come late, and some don\'t come until heaven; but for those who embrace the gospel of Jesus Christ, they come."',
}
quotes.append(quote)
quote = {
    'author': 'Thomas S. Monson',
    'quote_text': '"Faith and doubt cannot exist in the same mind at the same time, for one will dispel the other."',
}
quotes.append(quote)
quote = {
    'author': 'Helen Keller',
    'quote_text': '"The best and most beautiful things in this world cannot be seen or even heard but must be felt with the heart.',
}
quotes.append(quote)
quote = {
    'author': 'Dale G. Renlund',
    'quote_text': '"When God directs us to do one thing, He often has many purposes in mind."',
}
quotes.append(quote)
quote = {
    'author': 'J. R. R. Tolkien',
    'quote_text': '"Not all those who wander are lost."',
}
quotes.append(quote)
quote = {
    'author': 'Karl G. Maeser',
    'quote_text': '"He who cheats others is a knave, but he who cheats himself is a fool."',
}
quotes.append(quote)
quote = {
    'author': 'Russel M. Nelson',
    'quote_text': '"Education is the difference between wishing you could help others and being able to help them."',
}
quotes.append(quote)
quote = {
    'author': 'Dalai Lama',
    'quote_text': '"If you think you are too small to make a difference, try sleeping with a mosquito."',
}
quotes.append(quote)
quote = {
    'author': 'Mark Twain',
    'quote_text': '"The secret of getting ahead is getting started."',
}
quotes.append(quote)
quote = {
    'author': 'Jeffrey R. Holland',
    'quote_text': '"No misfortune is so bad that whining about it won\'t make it worse."',
}
quotes.append(quote)
quote = {
    'author': 'Massimo De Feo',
    'quote_text': '"If you are struggling to find the strength to forgive, don\'t think of what others have done to you, but think of what the Lord has done for you."',
}
quotes.append(quote)
quote = {
    'author': 'Kevin J. Worthen',
    'quote_text': '"You are more capable, more talented, & more faith-filled than you realize.  More important, you are more loved by God than you realize."',
}
quotes.append(quote)
quote = {
    'author': 'Sheri L. Dew',
    'quote_text': '"None of us come to this earth to gain our worth; we brought it with us."',
}
quotes.append(quote)
quote = {
    'author': 'C. S. Lewis',
    'quote_text': '"I believe in Christianity as I believe that the sun has risen: not only because I see it, but because by it I see everything else."',
}
quotes.append(quote)
quote = {
    'author': 'Russel M. Nelson',
    'quote_text': '"Truth is truth! It is not divisible, and any part of it cannot be set aside."',
}
quotes.append(quote)
quote = {
    'author': 'Thomas S. Monson',
    'quote_text': '"Whether it is the best of times or the worst of times, He is with us. He has promised that this will never change."',
}
quotes.append(quote)

with open('quotes_list.txt', 'w') as outfile:
    json.dump(quotes, outfile, indent=4)
