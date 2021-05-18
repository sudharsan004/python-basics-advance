class bike():
    def __init__(self,model,price,condition='New',kms=0):
        self.model =model
        self.price =price
        self.condition =condition
        self.kms =kms
    
    def say_details(self,showKms=False):
        print(f'{self.model} costs {self.price} and it is a {self.condition}bike {("it ran "+str(self.kms)+"kms.") if showKms else ""}')
       
honda = bike('honda Shine',95000)
honda.say_details()
honda.say_details(True)
