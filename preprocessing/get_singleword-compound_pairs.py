import numpy as np
from check_if_food_in_corpus import get_food_words, food_data
from scipy.spatial import distance

def get_norm_food_vectors(food_data, vectors):    
    norms_vectors = {}
    norms = get_food_words(food_data)
    with open(vectors, "r", encoding="ISO-8859-1") as vectors:        
        for line in vectors: 
            line = line.strip('\n')
            word = line.split(' ', 1)[0] 
            vector_list = line.split(' ')[1:]
            if word in norms:
                # Make sure vectors are floats
                vector = [float(v) for v in vector_list if v != '']
                norms_vectors[word] = vector
#    print(norms_vectors)
    
# Get ascending dict
                
    asc_sorted_norm_food_vectors = {}
    for key in sorted(norms_vectors.keys()):
        asc_sorted_norm_food_vectors[key] = norms_vectors[key]
        
# Write    
    with open('asc_sorted_norm_food_vectors.txt', 'w', encoding='utf-8') as out:
        for k, v in asc_sorted_norm_food_vectors.items():
            out.write(k + ': ' + str(v) + '\n')

# Get descending dict
        
    desc_sorted_norm_food_vectors = {}
    for key in sorted(norms_vectors.keys(), reverse=True):
        desc_sorted_norm_food_vectors[key] = norms_vectors[key]    

# Write     
    with open('desc_sorted_norm_food_vectors.txt', 'w', encoding='utf-8') as out:
        for k, v in desc_sorted_norm_food_vectors.items():
            out.write(k + ': ' + str(v) + '\n')
    
    all_vector_cosines = {}
    string_to_write = ""
    for asc_norm, asc_vector in asc_sorted_norm_food_vectors.items():
        for desc_norm, desc_vector in desc_sorted_norm_food_vectors.items():
            if asc_norm != desc_norm:
                vector_cosine = 1 - distance.cosine(asc_vector, desc_vector)
                compared_targets = str(asc_norm) + ', ' + str(desc_norm)
                string_to_write += compared_targets + ', ' + str(vector_cosine) + '\n'
                all_vector_cosines[compared_targets] = vector_cosine
# Write (unsorted)     
#    with open("all_vector_cosines_list.txt", 'w') as out:
#        out.write(string_to_write)
# Write    
#    with open("all_vector_cosines.txt", 'w') as out:
#        out.write(str(all_vector_cosines))
                    
    removed_duplicates = {}           
    sorted_all_vector_cosines = sorted(all_vector_cosines.items(), key=lambda kv: kv[1])
    for k, v in dict(sorted_all_vector_cosines).items():
        if v not in removed_duplicates.values():
            removed_duplicates[k] = v
# Write             
    with open("all_vector_cosines_sorted.txt", 'w') as out:
        for k, v in removed_duplicates.items():
            out.write(k + ' : ' + str(v) + '\n')    
            
                
def get_similar_norms(cosine_corpus, food_data):
        
    norms = get_food_words(food_data)
    split_norms = {}                                                # Format: {kidney_bean : ('kidney', 'bean')...}
    single_word_norms = []                                          # List of single_word norms
    for norm in norms:
        if "_" in norm:
            split_norm = tuple(norm.split("_"))
            split_norms[norm] = split_norm
        else:
            single_word_norms.append(norm)
    compound_foods_dict = {}                                        # Format: {black_bean : bean, bread_stick : bread...}
    for split_norm, compound_norm in split_norms.items():
        for single_word_norm in single_word_norms:
            if single_word_norm in compound_norm:
                compound_foods_dict[split_norm] = single_word_norm
    norms_to_find = {}                                              # Need the vectors, format = {veal_meat ('veal', 'meat')...}
    for split_norm, included_norms in split_norms.items():
        if split_norm not in compound_foods_dict.keys():
            norms_to_find[split_norm] = included_norms
#    included_norms_list = []
#    for included_norms in norms_to_find.values():
#        for norm in included_norms:
#            included_norms_list.append(norm)

    return norms_to_find


        

         
            

#vectors = "test_en_wiki.txt.phrases.lang.long.vec3"

vectors = "en_wiki_clean_lemmatized.txt.phrases.lang.vec3"
norms_vectors = "norm_food_vectors.txt"
cosine_corpus = "all_vector_cosines_sorted.txt"
included_norms_list = "included_norms_list.txt"


if __name__ == "__main__":
    
#    get_norm_food_vectors(food_data, vectors)
#    get_similar_norms(cosine_corpus, food_data)
#    get_norm_food_vectors(food_data, vectors)
