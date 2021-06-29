import itertools
import numpy as np
from scipy.spatial import distance


def create_vector_dict(vectors):
    
    vectors_dict = {}
    
    with open(vectors, "r") as vectors:
        
        for line in vectors:
            
            line = line.strip('\n')
            
            word = line.split(' ', 1)[0]
            
            vector_list = line.split(' ')[1:]
            
            vector = [float(v) for v in vector_list if v != '']
                        
            np.set_printoptions(suppress=True)
            
            vector_array = np.array(vector)
            
            if word not in vectors_dict.keys():
                
                vectors_dict[word] = vector
                
    return vectors_dict
            
            
def calc_cosine(vectors):
    
    vectors_dict = create_vector_dict(vectors)
    
    key_pairs = list(itertools.combinations(create_vector_dict(vectors), 2))
    
    print(key_pairs)
    
#    for word, vector in vectors_dict.items():
#        
#        for key_pair in key_pairs:
    
#    return vector_cosine


vectors = "test_en_wiki.txt.phrases.lang.vec3"

create_vector_dict(vectors)

calc_cosine(vectors)






































































