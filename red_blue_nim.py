# Importing Sys
import sys

# function for min-max alpha Beta_Value
def Func_Min_Max_Alpha_Beta(Current_Piles, Alpha_Value, Beta_Value, Player_At_Max, Working_Depth):
    # checking the blank state
    if min(Current_Piles) == 0:
        # return statement 
        return (2 * Current_Piles[0] + 3 * Current_Piles[1]) * (1 if Player_At_Max else -1), None
    # initializing the best move to blank
    Next_Best_Move = None
    # varaible posible moves to move possibly
    Moves_Possible = [0, 1]
    # check the player position
    if Player_At_Max:
        # value
        Current_Value = -float('inf')
        # check all the possible moves
        for Loop_Move in Moves_Possible:
            # check if we have the items in pile
            if Current_Piles[Loop_Move] > 0:
                # picking up the current state of pile
                New_Working_Pile = Current_Piles.copy()
                # making a move
                New_Working_Pile[Loop_Move] -= 1
                # finding the min max value
                Loop_Min_Max_Value, _ = Func_Min_Max_Alpha_Beta(New_Working_Pile, Alpha_Value, Beta_Value, False, Working_Depth - 1)
                # checking for the move
                if Loop_Min_Max_Value > Current_Value:
                    # taking one
                    Current_Value = Loop_Min_Max_Value
                    # setting best moves
                    Next_Best_Move = Loop_Move
                # setting Alpha_Values
                Alpha_Value = max(Alpha_Value, Current_Value)
                # checking break condition
                if Alpha_Value >= Beta_Value:
                    break
    # else part
    else:
        # current value
        Current_Value = float('inf')
        # checking all the moves
        for Loop_Move in Moves_Possible:
            # checking the pile
            if Current_Piles[Loop_Move] > 0:
                # copying the pile
                New_Working_Pile = Current_Piles.copy()
                # setting the var
                New_Working_Pile[Loop_Move] -= 1
                # finding min max
                Loop_Min_Max_Value, _ = Func_Min_Max_Alpha_Beta(New_Working_Pile, Alpha_Value, Beta_Value, True, Working_Depth - 1)
                # cheking chances of move
                if Loop_Min_Max_Value < Current_Value:
                    # plying move
                    Current_Value = Loop_Min_Max_Value
                    Next_Best_Move = Loop_Move
                # getting beta value
                Beta_Value = min(Beta_Value, Current_Value)
                # checing alpha beta
                if Alpha_Value >= Beta_Value:
                    break
    # return final solution
    return Current_Value, Next_Best_Move

# main function
def main(Number_Of_Red, Number_Of_Blue, First_Player_m, Working_Depth):
    # setting current pile
    Current_Piles = [Number_Of_Red, Number_Of_Blue]
    # checkign first player
    if First_Player_m not in ('computer', 'human'):
        # invalid condition
        print("Invalid first player! Must be 'computer' or 'human'.")
        return
    # cheking move
    Is_Comp_Turn = First_Player_m == 'computer'
    # playing game
    while min(Current_Piles) > 0:
        # printing pile
        print("Red:",Current_Piles[0],"Blue", Current_Piles[1], "\n")
        # playing computer move
        if Is_Comp_Turn:
            _, Loop_Move = Func_Min_Max_Alpha_Beta(Current_Piles, -float('inf'), float('inf'), True, Working_Depth)
            # changing pile situation
            Current_Piles[Loop_Move] -= 1
            # printing logs
            print(f"Computer removed a marble from the {'red' if Loop_Move == 0 else 'blue'} pile.")
        # plying human move
        else:
            # takign human move 
            Loop_Move = input("Enter the pile to remove a marble from (red/blue): ").lower()
            # plying move
            if Loop_Move == 'red' and Current_Piles[0] > 0:
                Current_Piles[0] -= 1
            elif Loop_Move == 'blue' and Current_Piles[1] > 0:
                Current_Piles[1] -= 1
            else:
                # condition for invalid move
                print("Invalid move or the chosen pile is empty. Try again.")
                continue
        # changing the turn
        Is_Comp_Turn = not Is_Comp_Turn
    # final decision
    Final_Winner = "Computer" if Is_Comp_Turn else "Human"
    Final_Score = 2 * Current_Piles[0] + 3 * Current_Piles[1]
    print(f"{Final_Winner} wins! Final Score: {Final_Score}")

# main run
if __name__ == "__main__":
    # atking args in
    Number_Of_Red = int(sys.argv[1])
    Number_Of_Blue = int(sys.argv[2])
    # making and deciding move
    if len(sys.argv) >= 4 and sys.argv[3].lower() == "human":
        First_Player_m = "human"
    else:
        First_Player_m = "computer"
    if len(sys.argv) >= 5:
        Working_Depth = int(sys.argv[4])
    else:
        Working_Depth = 0
    # running function
    main(Number_Of_Red, Number_Of_Blue, First_Player_m, Working_Depth)
