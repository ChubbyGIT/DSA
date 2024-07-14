stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

class HashTable:
    def __init__(self):
        self.MAX =100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()



t.__setitem__("apr 09",33)
t.__setitem__("apr 08",33)
t.__delitem__('march 11')
for i in stock_prices:
    print(t.get_hash(i),':',i, stock_prices[i])