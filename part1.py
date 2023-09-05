#file_name = input("Enter your file name: ")
import string
def count_ngrams(file_name, n=2): 
  with open(file_name, 'r') as file:
    content = file.read()
    for character in string.punctuation:
      content = content.replace(character, "")
    ultimate_list = content.strip().lower().split()
      
    
    n_grams = {}
    num = n
    
    for i in range(0, len(ultimate_list)-1):
      pre_ngram = []
      counter = 0
      while counter < num:
        term_index = i+counter
        if term_index <= len(ultimate_list) - 1:
          pre_ngram.append(ultimate_list[term_index])
        counter += 1
      if len(pre_ngram) == num:
        n_gram = tuple(pre_ngram)
      if n_gram not in n_grams:
        n_grams[n_gram] = 0
      n_grams[n_gram] += 1
    
    return n_grams #return n_grams
    
    
def single_occurences(ngram_count_dict):
    occuring_once = []
    for key,value in ngram_count_dict.items():
        if value == 1:
            occuring_once.append(key)
    return occuring_once #return
    
    
def most_frequent(ngram_count_dict, n = 5): 
    num = n
    list_of_n_grams_items = []
    for key, value in ngram_count_dict.items():
        pair = (value, key)
        list_of_n_grams_items.append(pair)
        sorted_list_of_n_grams_items = sorted(list_of_n_grams_items)

    #creating the list of num ngrams
    list_of_most_occuring_items = sorted_list_of_n_grams_items[len(sorted_list_of_n_grams_items)-1:len(sorted_list_of_n_grams_items)-(num+1):-1]

    #getting the key after sorting
    key_ngrams = []
    list_of_most_occuring_n_grams = []
    for x in range(len(list_of_most_occuring_items)):
        key_ngram = list_of_most_occuring_items[x][1]
        key_ngrams.append(key_ngram)
    return key_ngrams #return


  
def main():
  filename = input("Enter your file name: ")
  n = int(input("Enter n for your n-grams: "))
  ngram_counts = count_ngrams(filename, n)
  print('{}-grams that occur only once:'.format(n))
  print(single_occurences(ngram_counts))
  print('\n')# just to organize output
  most_frequent_k = int(input("How many of the most frequent n-grams do you need?: "))
  print('{} most frequent {}-grams:'.format(most_frequent_k, n))
  print(most_frequent(ngram_counts, most_frequent_k)) 



if __name__ == "__main__":
    main()
    

    
    
    
