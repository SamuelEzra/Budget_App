class Budget:
    def __init__(self, category):
        self.category = category
        

    def deposit(self, amount):
        self.amount = amount

        return amount


    def withdrawal(self, amount):
        self.amount = amount
       
        return amount


    def transfer(self, amount):
        self.amount
        
        return amount
        

category_1 = Budget('Food')
category_2 = Budget('Clothing')
category_3 = Budget('Entertainment')

foodBalance = 0
clothingBalance = 0
entertainmentBalance = 0

foodDeposit = category_1.deposit(int(input('How much are you depositing for Food? If NO enter "0" \n')))
foodWithdrawal = category_1.withdrawal(int(input('How much are you withdrawing for Food? If NO enter "0" \n')))
foodToClot = category_1.transfer(int(input('How much are you transfering from Food to Clothing? If NO enter "0" \n')))
foodToEnt = category_1.transfer(int(input('How much are you transferin from Food to Entertainment? If NO enter "0" \n')))

clothingDeposit = category_2.deposit(int(input('How much are you depositing for Clothing? If NO enter "0" \n')))
clothingWithdrawal = category_2.withdrawal(int(input('How much are you withdrawing for Clothing? If NO enter "0" \n')))
clotToFood = category_2.transfer(int(input('How much are you transfering from Clothing to Food? If NO enter "0" \n')))
clotToEnt = category_2.transfer(int(input('How much are you transfering Clothing to Entertainment? If NO enter "0" \n')))

entertainmentDeposit = category_3.deposit(int(input('How much are you depositing for Entertainment? If NO enter "0" \n')))
entertainmentWithdrawal = category_3.withdrawal(int(input('How much are you withdrawing for Entertainment? If NO enter "0" \n')))
entToClot = category_3.transfer(int(input('How much are you transfering from Entertainment to Clothing? If NO enter "0" \n')))
entToFood = category_3.transfer(int(input('How much are you transfering from Entertainment to Food? If NO enter "0" \n')))


foodBalance += (foodDeposit - foodWithdrawal - foodToClot - foodToEnt + clotToFood + entToFood)
clothingBalance += (clothingDeposit - clothingWithdrawal - clotToFood - clotToEnt + foodToClot + entToClot)
entertainmentBalance += (entertainmentDeposit - entertainmentWithdrawal - entToClot - entToFood + clotToEnt + foodToEnt)


print(f'Your Food Budget balance is: {foodBalance} \n')
print(f'Your Clothing Budget balance is: {clothingBalance} \n')
print(f'Your Entertainment Budget balance is: {entertainmentBalance} \n')