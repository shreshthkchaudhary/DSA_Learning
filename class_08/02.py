# User define datatype
# linkdlist

# # a2=[2,"ii","b"]
# # a3=[3,"iii","c"]
# # a4=[4,"iv","d"]

class serial:
    # number
    # roman_number
    # alphabet
    def __init__(self, number, roman_number, alphabet):
        self.number=number
        self.roman_number=roman_number
        self.alphabet=alphabet
        # return [self.number,self.roman_number,self.alphabet]
    
a1=serial(1,"i","a")
print(a1.alphabet)