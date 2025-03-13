def word_count(book_text):
    count = len(book_text.split())
    return count

def sort_on(dict):
    return dict["count"]

def sort_dictionary(dict):
    dict_list = []
    for item in dict:
        if item.isalpha():
            dict_list.append({"character": item, "count": dict[item]})
    
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def letter_count(book_text):
    lower_text = book_text.lower()
    count_dict = {}
    for letter in lower_text:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    
    return count_dict