import re
import spacy

nlp = spacy.load('en', disable=['parser', 'ner'])


with open("en_wiki_new.txt", "r", encoding='utf-8') as infile, open("en_wiki_clean_lemmatized.txt", "w", encoding='utf-8') as out:
   
    for line in infile:

        doc = nlp(line)
        
        lemmas = " ".join([token.lemma_ for token in doc])
        
        new_sentences = re.sub('(^.*?\s+)', "", lemmas )
    
        out.write(new_sentences)

