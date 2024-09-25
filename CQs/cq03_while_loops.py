__author__ = "730749520"

"""Return the numbers of characters in a sentence"""

def num_instances(phrase:str, search_char:str) -> int:
    count:int=0
    index:int=0
    while index < len(phrase):
        if phrase[index].lower() == search_char.lower():
            count +=1
        index +=1

    return count
num_instances(phrase="HelloHeLloHello", search_char="e")
