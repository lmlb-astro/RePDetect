#This is an example text. It shows that the program works. It verifies whether there are consecutive repeating sentences. This program checks wether a sentence repeats a previous sentence. This is a test.

from transformers import AutoModel

class repetition_identifier:
    def __init__(self):
        self.id_model = "test"# LOAD MODEL
    
    def __inds_repetitive_sentences(self, sentences):
        ## loop over all sentences
        for idx in range(0, len(sentences) - 1):
            sent1, sent2 = sentences[idx], sentences[idx+1]
    
            ## RUN THEM THROUGH THE MODEL : FIRST LOAD THE MODEL (DO THIS ONCE)
    
    def __get_repetitions(self):
        # get text from terminal and split into sentences
        text = input("Please input the message:")
        sentences = self.__text_to_sentences(text)
        print(sentences)
    
        rep_inds = self.__inds_repetitive_sentences(sentences) # CONTINUE HERE
    
        ## store the indices and the sentences
    
    ## basic implementation to split the sentence
    def __text_to_sentences(self, text):
        return text.split(".")
    
    
    ## retuns the phrases that repeat the same content
    def return_repetitions(self):
        reps = self.__get_repetitions()

## main function: calls
def main():
    IDer = repetition_identifier()
    IDer.return_repetitions()

if __name__ == "__main__":
    main()