import re
def cap(match):
    return match.group(1).upper()
def snake_to_camel(snake_case):
    return re.sub(r'_([a-z])', cap, snake_case)
snake = "ia_zmeia_i_dovolen_etim"
camel = snake_to_camel(snake)
print(camel)
