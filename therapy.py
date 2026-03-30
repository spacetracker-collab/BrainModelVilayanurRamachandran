
def mirror_therapy(left, right, enable=True):
    if enable:
        return right, left
    return left, right
