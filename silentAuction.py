from replit import clear
    
auctionData={}
affirmative=["y","Y","yes","Yes"]
continueBidding=True
while continueBidding == True:
    name=input("Enter your name: ")
    bid=int(input("What is your bid?"))
    auctionData[name]=bid
    clear()
    condition=input("Are there any more bidders?")
    if condition not in affirmative :
        continueBidding=False
        print(auctionData)
        
        
maxPlayer=max(auctionData, key=auctionData.get)
maxVal=max(auctionData.values())
print(f"{maxPlayer} has won the bidding with a bid of {maxVal}")