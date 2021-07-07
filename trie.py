class Trie(object):
    """Simple trie implementation using python dictionary.

    Args:
        object (List[str]): List of words to build trie with

    Returns:
        Trie: Trie object
    """
    root = dict()
    def __init__(self, words):
        current_dict = self.root
        for w in words:
            for letter in w: 
                current_dict = current_dict.setdefault(letter, {})
            current_dict['_end'] = 'end'
            current_dict = self.root
    
    def search(self, text):
        """[summary]

        Args:
            text (str): Input word to search on the trie.

        Returns:
            [Boolean]: True if word is in trie, else False.
        """
        current_dict = self.root
        letter_found = False
        for letter in text:
            if letter in current_dict:
                letter_found = True
                current_dict = current_dict[letter]
            else:
                letter_found = False
        if '_end' in current_dict and letter_found:
            return True
        else:
            return False

t = Trie(['cart', 'cat', 'cabs'])
print(t.search('cart')) #returns True
print(t.search('cab')) #returns False
print(t.search('cat')) #returns True