#This is an example text. It shows that the program works. It verifies whether there are consecutive repeating sentences. This program checks wether a sentence repeats a previous sentence. This is a test.

# PCCW 's chief operating officer , Mike Butcher , and Alex Arena , the chief financial officer , will report directly to Mr So . Current Chief Operating Officer Mike Butcher and Group Chief Financial Officer Alex Arena will report to So .

# According to the federal Centers for Disease Control and Prevention ( news - web sites ) , there were 19 reported cases of measles in the United States in 2002 . The Centers for Disease Control and Prevention said there were 19 reported cases of measles in the United States in 2002 .


import numpy as np
from transformers import AutoModel, AutoTokenizer

class repetition_identifier:
    ## Initializes the repetition identifier
    def __init__(self):
        self.id_model = AutoModel .from_pretrained('./tautology_BERT_v0p1')
        self.tokenizer = AutoTokenizer.from_pretrained('./tautology_BERT_v0p1')
    
    
    ## Determine the indices of the repetitive sentences with the language model
    def __inds_repetitive_sentences(self, sentences):
        
        ## loop over all sentences
        for idx in range(0, len(sentences) - 1):
            sent1, sent2 = sentences[idx], sentences[idx+1]

            ## create tokenized data input for the model
            print(sent1)
            inps = self.tokenizer(sent1, sent2, return_tensors = "pt")
            #inps2 = self.tokenizer(sent2, return_tensors = "pt")
            #if idx == 0: print(inps1)
    
            ## evaluate the input
            output = self.id_model(**inps)

            ## use the output to determine whether the sentence repeat the same thing
            print(np.argmax(output, axis = -1)) # DOES THIS WORK?
    
    
    ## Obtains the input text, splits it into sentences and then calls the function to find the repeating sentences
    def __get_repetitions(self):
        # get text from terminal and split into sentences
        text = input("Please input the message:")
        sentences = self.__text_to_sentences(text)
    
        rep_inds = self.__inds_repetitive_sentences(sentences)
        # CONTINUE HERE
    
        ## store the indices and the sentences
    
    
    ## basic implementation to split the sentence
    def __text_to_sentences(self, text):
        ## split the text into sentences
        sentences = text.split(".")[:-1]

        ## make sure every sentence ends with a "."
        for idx in range(0, len(sentences)):
            sentences[idx] = "{sentence}.".format(sentence = sentences[idx])

        return sentences
    
    
    ## retuns the phrases that repeat the same content
    def return_repetitions(self):
        reps = self.__get_repetitions()



## main function: calls the repetition identifier
def main():
    IDer = repetition_identifier()
    IDer.return_repetitions()

if __name__ == "__main__":
    main()