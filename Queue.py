class Node:
    def __init__(self, key):
       self.key = key
       self.left = None
       self.right = None
class BST:
    def __init__(self):
       self.root=None
    def insert(self,root,key):
       if root is None:
           return Node(key)
       if key < root.key:
           root.left = self.insert(root.left, key)
       elif key > root.key:
           root.right = self.insert(root.right, key)
       return root         
    def inorder(self, root):
        if root:
           self.inorder(root.left)
           print(root.key, end=' ')                                
           self.inorder(root.right)
           
    def preorder(self, root):
        if root:
           print(root.key, end=' ')
           self.preorder(root.left)
           self.preorder(root.right) 
    def postorder(self,root):
        if root:
           self.postorder(root.left)
           self.postorder(root.right)
           print(root.key, end=' ') 
    def search(self,root,key):
        if root is None or root.key == key:
           return root
        if key < root.key:
           return  self.search (root.left, key)
        return self.search(root.right, key)
    def delete(self,root,key):
        if root is None:
            return root
        if key < root.key:
            root.left=self.delete(root.left,key)
        elif key > root.key:
            root.right=self.delete(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            temp = self_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right,temp.key)
        return
    def min_value_node(self,node):
        current = node
        while current.left is not None:
                     current = current.left
        return current                             
    def menu(self):
       while True:
        print("\n---Menu---")
        print("1.Insert")
        print("2.Inorder")
        print("3.Preorder") 
        print("4.Postorder")
        print("5.Search")
        print("6.Delete")
        print("7.Exit")     
        choice = int(input("Enter your choice:"))
        if choice==1:
           keys= input("Enter the keys:").split()
           for key in keys:
             self.root=self.insert(self.root, int(key))
        elif choice==2:
           print("Inorder Traversal of BST:")
           self.inorder(self.root)
        elif choice==3:
           print("Pre-order Traversal of BST:")
           self.preorder(self.root)
        elif choice==4:
           print("Post-order Traversal of BST:")
           self.postorder(self.root)
        elif choice==5:
           key_to_search = input("Enter Key to be searched:")
           result = self.search  
        elif choice==6:
           key_to_delete = int(input("Enter key to be delete:"))
           self.root = self.delete (self.root,key_to_delete)
           print(f"In-order after deleting{key_to_delete}:")
           self.inorder(self.root)
           print()
        elif choice==7:
           print("Exit")    
           break
        else:
           print("Invalid option. Try again!")
tree = BST()
tree.menu()      
     

        
        

        
        



