# Convert ordinal string (like 'first' or '1') to numeric index.
def convert_ordinal_to_index(ordinal: str) -> int:

    word_to_number = {
        'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5,
        'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10
    }
    
    if ordinal.lower() in word_to_number:
        return word_to_number[ordinal.lower()]
    
    try:
        return int(ordinal)
    except ValueError:
        raise ValueError(f"Invalid ordinal number: {ordinal}") 