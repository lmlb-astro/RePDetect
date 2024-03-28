#This is an example text. It shows that the program works. It verifies whether there are consecutive repeating sentences. This program checks wether a sentence repeats a previous sentence. This is a test.

# PCCW 's chief operating officer , Mike Butcher , and Alex Arena , the chief financial officer , will report directly to Mr So . Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So .

# According to the federal Centers for Disease Control and Prevention ( news - web sites ) , there were 19 reported cases of measles in the United States in 2002 . The Centers for Disease Control and Prevention said there were 19 reported cases of measles in the United States in 2002 .

import numpy as np

## Need model "ForSequenceClassification"
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class repetition_identifier:
    ## Initializes the repetition identifier
    def __init__(self):
        ## Need model "ForSequenceClassification", a simple Automodel would not work
        self.id_model = AutoModelForSequenceClassification.from_pretrained('./tautology_BERT_v0p1')
        self.tokenizer = AutoTokenizer.from_pretrained('./tautology_BERT_v0p1')
    
    
    #### PRIVATE FUNCTIONS OF THE CLASS ####
    
        
    ## Determine the indices of the repetitive sentences with the language model
    ## returns a list with the indices of the first sentence that is then repeated in the next sentence
    def __inds_repetitive_sentences(self, sentences):
        ## initialize the array
        rep_id_list = []
        
        ## loop over all sentences
        for idx in range(0, len(sentences) - 1):
            ## get the two sentences
            sent1, sent2 = sentences[idx], sentences[idx+1]

            ## create tokenized data input for the model
            inps = self.tokenizer(sent1, sent2, return_tensors = "pt") ## tokenizes both sentences
    
            ## evaluate the input with the model
            output = self.id_model(**inps)

            ## use the output to determine whether the sentence repeat the same thing
            ## i.e. if the second sentence has higher output than the first sentence
            if (output.logits[0][0] < output.logits[0][1]):
                rep_id_list.append(idx)
        
        return rep_id_list
    
    
    ## basic implementation to split the sentence
    def __text_to_sentences(self, text):
        ## split the text into sentences and remove the last part of the split() function which does not return an actual sentence of the text
        sentences = text.split(".")[:-1]

        ## make sure every sentence ends with a "."
        for idx in range(0, len(sentences)):
            sentences[idx] = "{sentence}.".format(sentence = sentences[idx])

        return sentences


    
    #### PUBLIC FUNCTIONS OF THE CLASS ####
    
    
    ## Obtains the input text, splits it into sentences and then calls the function to find the repeating sentences
    def print_repetitions(self):
        # get text from terminal and split into sentences
        text = input("Please input the message:")
        sentences = self.__text_to_sentences(text)
    
        ## get the indices of the sentences that are being repeated
        rep_inds = self.__inds_repetitive_sentences(sentences)
    
        ## print the repeating indices
        if(len(rep_inds) > 0):
            print("The following sentences are repeated in by the sentence text:\n")
            for idx in rep_inds:
                print("Sentence No. {idx}: {sentence} \n".format(idx = idx+1, sentence = sentences[idx]))
        else:
            print("There are no repeated sentences in the text.")




