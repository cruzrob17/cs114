print("how much change do u need")
change= input()
coins_in_quarters= change//25
change_left_quarters= change - (coins_in_quarters * 25)
coins_in_dimes = change// 10
change_left_dimes= change - (coins_in_dimes * 10)
change_in_nickels= change//5
change_left_nickels= change- (coins_in_nickels * 5)
change_in_pennies= change//1
change_left_pennies= 
