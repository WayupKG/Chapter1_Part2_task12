word = input()
if word.count('w') == 1:
    print(s.find('w'))
elif word.count('w') >= 2:
    print(s.find('w'), s.rfind('w'))