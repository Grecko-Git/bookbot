import os

# Get the directory containing the current file (main.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

def main():
    book_path = os.path.join(current_dir, "books", "frankenstein.txt") # Construct the path to the book file
    text = read_book(book_path) # call read_book function and store it in text
    wordcount = count_words(text) # call count_words function and store it in wordcount
    character_count = count_characters(text)
    print(f"--- Begin report of books/frankenstein.txt --- \n{wordcount} words found in the document\n") # printing number of words in the book
    # Get sorted key-value pairs
    sorted_keys = sort_on(character_count)

    # Loop through sorted keys and print them
    for key, value in sorted_keys:
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")


def sort_on(my_dict): # function to sort a dictionary by descending number
    return sorted(my_dict.items(), key=lambda item: item[1], reverse=True) # select the dictionary, lambda = num, what to sort, descending order

def count_characters(text):
    count = {} # define dictionary
    for i in text: # cycle through every character in the book
        c = i.lower() # lowercase character and save it in c
        if c.isalpha(): # checks if c is a letter
            if c in count: # cycle through count as c
                count[c] += 1 # +1 to c if c is in count
            else:
                count[c] = 1 # sets c to 1 if not already in count
    return count # return the dictionary with all the counted characters

def count_words(text): # count the words of a specific file
    words = text.split() # splitting the file into seperate lines
    return len(words) # counting the words and return it

def read_book(path): # reading the book and returning all the words
    with open(path, "r") as f: # open the book
        return f.read() # read the book and return it

if __name__ == "__main__":
    main()