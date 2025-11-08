class HashTable:
   def __init__(self,size = 10):
      self.size = size
      self.table = [[] for _ in range(size)]
   def hash_function(self,key):
      return key % self.size
   def insert(self,key):
      index = self.hash_function(key)
      if key not in self.table[index]:
         self.table[index].append(key)
   def search (self,key):
      index = key in self.hash_function(key)
      return key in self.table[index]
   def delete (self,key):
      index = self.hash_function(key)
      if key in self.table[index]:
         self.table[index].remove(key)
         return True
      return False
   def display(self):
      for i ,bucket in enumerate(self.table):
         print(f"Index{i}: {bucket}")
   def menu(self):
    while True:
     print("===Menu===")
     print("1.Insert")
     print("2.Search")
     print("3.Delete")
     print("4.Display")
     print("5.Exit")
     choice = int(input("Enter the choice :"))
     if choice == 1:
       key = int(input("Enter key to be insert : "))
       self.insert(key)
     elif choice == 2:
       key = int(input("Enter key to be search : "))
       res = self.search(key)
       if res:  
          print("key found")
       else:
          print("key not found")
     elif choice==3:
       key = int(input("Enter key to be deleted : "))
       res = self.delete(key)
       if res:  
          print("key deleted")
       else:
          print("key not found")
     elif choice == 4:
       self.display()
     elif choice == 5:
       print("Exit")
     else:
       print("Enter a valid choice.")
h1 = HashTable()
h1.menu()
     
     

        
        

        
        



