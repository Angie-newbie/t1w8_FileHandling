from file_operation import load_matches, save_matches
from match_operation import display_matches

spam = load_matches('matches.json')
display_matches(spam)
# spam[0]['Score A'] = 3
# save_matches('debug.json', spam)