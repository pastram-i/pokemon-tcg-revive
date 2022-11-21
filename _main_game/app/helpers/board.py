class Player:

    class Prize:
        count = 0
        #Max 6
        #0; Win
        pass

    class Bench:
        count = 0
        #Max 5
        #(bench and active) == 0; Win
        pass

    class Active:
        #Max 1
        #(bench and active) == 0; Win
        #Required 1 to start
        pass

    class Hand:
        count = 0
        pass

    class Deck:
        count = 0
        #Max 60
        #0; Lose
        pass

    class Focus:
        #Inspect
        pass

    class Stadium:
        pass