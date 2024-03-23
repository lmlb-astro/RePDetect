#This is an example text. It shows that the program works. It verifies whether there are consecutive repeating sentences. This program checks wether a sentence repeats a previous sentence. This is a test.

# PUT IN CLASS FORMAT
# USE ML TO IDENTIFY SENTENCES?




def get_repetitions():
    # get text from terminal and split into sentences
    text = input("Please input the message:")
    sentences = text_to_sentences(text)
    print(sentences)

    rep_inds = inds_repetitive_sentences(sentences) # CONTINUE HERE

## basic implementation to split the sentence
def text_to_sentences(text):
    return text.split(".")


## retuns the phrases that repeat the same content
def return_repetitions():
    reps = get_repetitions()

## main function: calls
def main():
    #print("hello world!")
    return_repetitions()

if __name__ == "__main__":
    main()