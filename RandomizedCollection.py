import random
class RandomizedCollection:
    """
    RandomizedCollection -> new empty RandomizedCollection
    """
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._element_list = []#collection elements
        self._element_to_indicies = {}#collection element to set of inidicies containing that element
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self._element_list.append(val)

        if val not in self._element_to_indicies:
            self._element_to_indicies[val] = set()

        self._element_to_indicies[val].add(len(self._element_list)-1)
        
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self._element_to_indicies:
            return False

        val_ind = self._element_to_indicies[val].pop()
        
            
        self._element_list[val_ind] = self._element_list[-1]
        self._element_to_indicies[self._element_list[-1]].add(val_ind)
        self._element_to_indicies[self._element_list[-1]].remove(len(self._element_list)-1)
        
        
        self._element_list.pop()
        
        if len(self._element_to_indicies[val])==0:
            del self._element_to_indicies[val]
            
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self._element_list)
		

