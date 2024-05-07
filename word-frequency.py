import re

#split sentence based on punctuation and whitespace using regex
def count_words(sentence):
    freq_dict = {}
    sentence = re.split('\W+', sentence)
    print(sentence)
    for i in sentence:
        if i in freq_dict:
            freq_dict[i] += 1
        else:
            freq_dict[i] = 1    
    
    print(freq_dict)

#use for loop over len of sentence and manually check for punct/spaces
def count_words_slicing(sentence):
    freq_dict = {}
    punct_spaces = [' ', ',', '!', '.', '?']
    start_index = 0
    for i in range(len(sentence)):
        if sentence[i] in punct_spaces:
            if sentence[start_index:i] in freq_dict:
                freq_dict[sentence[start_index:i]] += 1
            else:
                freq_dict[sentence[start_index:i]] = 1
            start_index = i+1

    print(freq_dict)
    

if __name__ == "__main__":
    count_words_slicing("This is an example sentence. example, sentence, the dog, the dog, i love my cat, dogs, dog, Dog, this, This")

