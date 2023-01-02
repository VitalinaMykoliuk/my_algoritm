def babble_sorted(sec: list):
    changed = True
    while changed:
        changed = False
        for i in range(len(sec) -1):
            if sec[i] > sec[i + 1]:
                sec[i], sec[i + 1] = sec[i + 1], sec[i]
                changed = True
    return sec


print(babble_sorted([3, 9, 58, 43]))
