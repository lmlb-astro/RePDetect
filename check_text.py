#This is an example text. It shows that the program works. It verifies whether there are consecutive repeating sentences. This program checks wether a sentence repeats a previous sentence. This is a test.

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
            inps = self.tokenizer(sent1, sent2, return_tensors = "pt")
    
            ## evaluate the input
            output = self.id_model(**inps)
            #print(output)
    
    
    ## Obtains the input text, splits it into sentences and then calls the function to find the repeating sentences
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



## main function: calls the repetition identifier
def main():
    IDer = repetition_identifier()
    IDer.return_repetitions()

if __name__ == "__main__":
    main()