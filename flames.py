# To eliminate common charcters
def flames(name1,name2) :  
    for i in range(len(name1)) :  
        for j in range(len(name2)) :  
            if name1[i] == name2[j] :  
                c = name1[i]  
                name1.remove(c)  
                name2.remove(c)  
                name3 = name1 + ["*"] + name2  
                return [name3, True]  
  
    name3 = name1 + ["*"] + name2  
    return [name3, False]  
  
  
if __name__ == "__main__" :  
    playerOne = input("First Player Name : ")  
    playerOne = playerOne.lower()  
    playerOne.replace(" ", "")  
    playerOneList = list(playerOne)  
  
    playerTwo = input("Second Player Name : ")  
    playerTwo = playerTwo.lower()  
    playerTwo.replace(" ", "")  
    playerTwoList = list(playerTwo)  
  
    proceed = True  
      
    while proceed :  
        retList = flames(playerOneList, playerTwoList)  
        conList = retList[0]  
        proceed = retList[1]  
        starIndex = conList.index("*")  
  
        playerOneList = conList[ : starIndex]  
        playerTwoList = conList[starIndex + 1 : ]  
  
    theCount = len(playerOneList) + len(playerTwoList)  
  
    # list of FLAMES acronym  
    res = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]  
  
    while len(res) > 1 :  
        splitIndex = (theCount % len(res) - 1)  
        if splitIndex >= 0 :  
            right = res[splitIndex + 1 : ]  
            left = res[ : splitIndex]  
            res = right + left  
        else :  
            res = res[ : len(res) - 1]  
  
    # print final result  
    print("Relationship Status :", res[0]) 
    if res[0]=="Friends":
        print("\nNATPU🙂🙂")
    elif res[0]== "Lovers":
        print("\nSONAMUTHA POCHA 🤣😂")
    elif res[0]== "Affection":
        print("\nNO EXPLANATION🙃🙃")
    elif res[0]== "Marriage":
        print("\nNO COMMENTS SIMPLY WASTE🫡🫡")
    elif res[0]== "Enemies":
        print("\nALL THE BEST 😵‍💫😵")
    else:
        print("🤩🤩🤩🤩") 
