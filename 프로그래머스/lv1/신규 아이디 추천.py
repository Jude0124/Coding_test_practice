import re
def solution(new_id):
    level4 = re.sub(r"^\.|\.$","",re.sub(r"\.+",".",re.sub(r"[^a-z0-9-_\.]","",new_id.lower())))
    if len(level4) == 0: level4 += "a"
    if len(level4) >= 16: 
        level4 = level4[:15]
        if level4[14] == ".": level4 = level4[:14]
    if len(level4) <= 2: level4 = level4.ljust(3,level4[-1]) 

    return level4