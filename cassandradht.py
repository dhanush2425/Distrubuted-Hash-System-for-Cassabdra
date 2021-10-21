k=int(input("Enter the number of replicas"))
hash_size=int(input("Enter the hash size"))
ring_size=pow(2,hash_size)
n=int(input("Enter the number of nodes"))
# A single node of a singly linked list
class Node:
  # constructor
  def _init_(self, data = None, next=None,list1=[None]): 
    self.data = data
    self.next = next
    self.list1=[]
    for i in range(0,k):
        self.replicas=[]
    

# A Linked List class with a single head node
class LinkedList:
  def _init_(self):  
    self.head = None
    
 
    
# insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
      
  
    
  
    
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
  def locate(self):
      val=int(input("Enter the value to be searched"))
      curr=self.head
      while(curr!=None):
          if val>=curr.data and val<=curr.next.data:
              return curr.next.data
          else:
              curr=curr.next
  
    
  
  #Add a New Node to the Hash Ring  
  def AddNode(self,data):
      temp=Node(data)
     
      print("Enter the postion of the node to be inserted")
      pos=int(input())
      if(pos==1):
          temp.next=self.head
          self.head=temp
      else:
          ptr=self.head
          for i in range(0,pos-2):
              ptr=ptr.next
          temp.next=ptr.next
          ptr.next=temp
         
 
    
 
    
 #Add Hash Value to the Ring
  def AddData(self):
      data=int(input("Enter the Data to be added"))
      curr=self.head
      while(curr!=None):
          if data>curr.data and data<=curr.next.data:
             curr.next.list1.append(data)
             curr.next.replicas.append(data)
             print("Hash Value added to Node",curr.next.data)
             return curr.next.list1
          else:
              curr=curr.next
              
  
    
  
    #Print the Hash Values of the Node
  def printVal(self):
      data=int(input("Enter the Node Value"))
      curr=self.head
      while(curr!=None):
          if(data==curr.data):
              return curr.list1
          else:
              curr=curr.next
   
              
   
    
   #Function to Add Replicas to the Node
  def showReplicas(self):
      n=int(input("Enter the Node which replicas has to be displayed"))
      curr=self.head
      while(curr!=None):
          if(n==curr.data):
           for i in range(0,k):
            print( curr.replicas)
           return 
          else:
              curr=curr.next
             
    
             
    
    #Funcion to Perform Load Balancing
  def loadBalancing(self):
      n=int(input("Enter the Node to be balanced"))
      curr=self.head
      while(curr!=None):
          if(curr.data==n):
              if(len(curr.list1))>5:
                  k=curr.list1.pop()
                  curr.next.list1.append(k)
                  print(curr.list1)
                  print(curr.next.list1)
                  return
          else:
            curr=curr.next
       
            
       
        
       #Fucntion to Delete a Node from the Ring
  def deleteNode(self):
      n=int(input("Enter the Node to be deleted"))
      curr=self.head
      while(curr!=None):
          if curr.next.data==n:
              curr.next=curr.next.next
              return
          else:
              curr=curr.next
        
      
          
# Singly Linked List with insertion and print methods
LL = LinkedList()
sum=0

for i in range(0,n):
  
  LL.insert(sum)
  sum=int((ring_size/n)+sum)
print("Nodes in the Ring are")
print('')
LL.printLL()
print('')

def addhashvalue():
    val=int(input("Enter the value to be added"))
    if val in LL.data:
        print("Node is present")
        
def switch():
  print("1.Locate the Hash Value")
  print("2.Add Hash Value to the Node")
  print("3.Add a New Node")
  print("4.Display all Hash Value in a Node")
  print("5.Perform Load Balancing")
  print("6.Display Replicas")
  print("7.Delete a Node")
  switcher=int(input("Enter the Input"))
  if switcher==1:
      print("Value is present in Node",LL.locate())
  elif switcher==2:
        
        print(LL.AddData())
        print('')
  elif switcher==3:
      print("Enter the value of the node to be added")
      data=int(input())
      LL.AddNode(data)
      print("New Hash Ring Is")
      LL.printLL()
      print('')
  elif switcher==4:
      print(LL.printVal())
      print('')
  elif switcher==5:
      LL.loadBalancing()
      print('')
  elif switcher==6:
      LL.showReplicas()
      print('')
  elif switcher==7:
      LL.deleteNode()
      print("Node Deleted")
      LL.printLL()
      print('')
while(1):
 switch()