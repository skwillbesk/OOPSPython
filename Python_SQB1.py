
#Title : Discount on Train Ticket:
#Create a class Train with the below attributes: 
#trainNo  of type Number 
#trainName of type String 
#tktCost of type Number 

class Train:
#Create the __init__ method which takes all parameters in the above sequence. 
# The method should set the value of attributes to parameter values .

    def __init__(self,tNo,tName,tCost):
        self.trainNo = tNo
        self.Name    = tName
        self.tktCost = tCost

    
    #Create a method inside the class with the name getTktCostAfterDiscount.  
    #This method takes a Number value as argument which is the discount by which the train ticket should be decremented 
    #and decreases the ticket cost of the train  by the given discount amount. 
    #e.g. If the train ticket cost is  900 and the given discount is 10, then the updated ticket cost of the train  
    #should be 810.0  and return the same.

    def getTktCostAfterDiscount(self,discount):
        reduced_ticket_price = self.tktCost - discount
        return reduced_ticket_price



#Create another class Railway  with the below attributes:
#zone of type String 
#train_list of type List having Train objects
class Railway:

    #Create the __init__ method which takes all parameters in the above sequence. 
    #The method should set the value of attributes to parameter values inside the method.
     
    def __init__(self,tzo,tlist):
        self.zone = tzo
        self.train_list = tlist 


    #Create another method inside the class with the name getTrainTktCostAfterDiscount. 
    #The method takes the trainNo as first  argument and discount  as the second argument . 
    #The method should find the respective Train, whose trainNo  is given as  in the argument , 
    #decrement the ticket cost as per the given discount and 
    #return the respective Train  object with the decremented ticket cost.
    #If the Train  with given trainNo  is not found , then the method returns  None .
    #Note: In Python None means NULL Object , Accordingly default mail will display the message 
    #'No Train Exists '  
    #Use the method getTktCostAfterDiscount defined in the Train  class
    #to calculate the decremented ticket cost of the Train .

    def getTrainTktCostAfterDiscount(self,tNo,discount):
        flag = 0                    #flag to check whether the train with the give number 'tNo' exits 
        tlist = self.train_list
        for train in tlist:
            if train.trainNo == tNo:
                flag = 1    #train with number tNO exists
                train.tktCost = train.getTktCostAfterDiscount(discount)
                return train

        if flag == 0:
            print("Train with train number ",tNo,"in zone ",self.zone,"does not exist !!")
            return None
            

'''
Validation Code

def get_railway_info(robj):
    tlist = robj.train_list
    for train in tlist:
        print(train.trainNo,train.Name,train.tktCost)

#Create 2 Train Objects in each Railway zone "A" and "B" 
#First Create train objects and then create Railway object
#Zone A

train_a_1 = Train(1,"TrainA1",10)
train_a_2 = Train(2,"TrainA2",20)

train_list_a = [train_a_1,train_a_2]

railway_a = Railway("A",train_list_a)

#Zone B
train_b_1 = Train(3,"TrainB1",30)
train_b_2 = Train(4,"TrainB2",40)

train_list_b = [train_b_1,train_b_2]

railway_b = Railway("B",train_list_b)

get_railway_info(railway_a)
get_railway_info(railway_b)

railway_a.getTrainTktCostAfterDiscount(1,1)
railway_b.getTrainTktCostAfterDiscount(1,1)

get_railway_info(railway_a)
get_railway_info(railway_b)

'''






