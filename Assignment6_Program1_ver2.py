"""ASS6 PROG1
Program 1: Number Sorter
Create a program that ask 4 numbers. 
Print the 4 numbers from highest to lowest using only if-else statement."""

#Ass6 Prog1, 1st try,   
#            2nd try,   changed int to float

def AskInput():
    print("\nMorning!! Give me four numbers and I'll arrange them in descending order for you!\n")
    FirstNum = float(input("1st input/number:  "))
    SecNum = float(input("2nd input/number:  "))
    ThirdNum = float(input("3rd input/number:  "))
    FourthNum = float(input("4th input/number:  "))
    return FirstNum, SecNum, ThirdNum, FourthNum

def Solve(FirstNumF, SecNumF, ThirdNumF, FourthNumF):
    #solve highest, midhigh, midlow, lowest 

   #To solve for the highest:
   # compare 1st and 2nd, compare 3rd and 4th. then compare higher1 to the higher2
 
    #compare 1st and 2nd, higher will be higher1 (equate the lower to lower1 as it is need to find the lowest)
    if FirstNumF > SecNumF:
        Higher1 = FirstNumF
        Lower1 = SecNumF
    else: 
        Higher1 = SecNumF
        Lower1 = FirstNumF
    #compare 3rd and 4th, higher will be higher2
    if ThirdNumF > FourthNumF:
        Higher2 = ThirdNumF
        Lower2 = FourthNumF
    else: 
        Higher2 = FourthNumF
        Lower2 = ThirdNumF
    #compare higher1 and higher2, higher will be the highestnum overall  (equate the lower to lowbuthigh as it is needed to solve midhigh n midlow)
    if Higher1 > Higher2:
        HighestNum = Higher1
        LowButHigh = Higher2
    else: 
        HighestNum = Higher2
        LowButHigh = Higher1
    
    #to solve lowest:
    # compare lower1 and lower2, lower will be lowestnum overall (equate the higher to highbutlow as it is needed to solve midhigh n midlow)
    if Lower1 < Lower2:
        LowestNum = Lower1
        HighButLow = Lower2
    else:
        LowestNum = Lower2
        HighButLow = Lower1
    
    #to solve midhigh and midlow:
    if HighButLow > LowButHigh: 
        MidHigh = HighButLow
        MidLow = LowButHigh
    else:
        MidHigh = LowButHigh
        MidLow = HighButLow

    return HighestNum, MidHigh, MidLow, LowestNum


def Display(HighestF, MidHighF, MidLowF, LowestF):
    #para d na ilagay ung .0 kapag integer nmn initial input
    if HighestF - int(HighestF) == 0:
        HighestF = int(HighestF)
    if MidHighF - int(MidHighF) == 0:
        MidHighF = int(MidHighF) 
    if MidLowF - int(MidLowF) == 0:
        MidLowF = int(MidLowF) 
    if LowestF - int(LowestF) == 0:
        LowestF = int(LowestF) 

    print(f"\nThe order of numbers from highest to lowest is:\n{HighestF} ,   {MidHighF} ,   {MidLowF} ,   {LowestF}\n")


#1 Ask 4 numbers
Final1stNum, Final2ndNum, Final3rdNum, Final4thNum = AskInput()

#2 find the highest using if-else statements
FinalHighestNum, FinalMidHighNum, FinalMidLowNum, FinalLowestNum = Solve(Final1stNum, Final2ndNum, Final3rdNum, Final4thNum)

#3 print the highest number
Display(FinalHighestNum, FinalMidHighNum, FinalMidLowNum, FinalLowestNum)
