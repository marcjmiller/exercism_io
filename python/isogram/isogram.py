def is_isogram(string):
    string = string.casefold()
    return (
        len(string) == 0 or max([string.count(i) for i in string if i.isalpha()]) == 1
    )
