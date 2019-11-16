class Substitution:

    def __init__(self, alphabet, key):
        self.alphabet_len = len(alphabet)
        self.alphabet = alphabet
        self.key = key
        self.atk = dict()
        self.kta = dict()
        for i in range(self.alphabet_len):
            self.atk[alphabet[i]] = key[i]
            self.kta[key[i]] = alphabet[i]

    def encrypt(self, text):
        cypher = ''.join(self.atk[c] for c in text)
        return cypher

    def decrypt(self, cypher):
        text = ''.join(self.kta[c] for c in cypher)
        return text
