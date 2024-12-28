def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    recommend_id = ""
    for str in new_id:
        if str.islower() or str.isnumeric() or str == '-' or str == '_' or str == '.':
            recommend_id += str
    # 3
    new_id = ""
    before = ''
    for str in recommend_id:
        if not (before == '.' and str == '.'):
            new_id += str
        before = str
    # 4
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5
    if len(new_id) == 0:
        new_id = 'a'
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    # 7
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id
