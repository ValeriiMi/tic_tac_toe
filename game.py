
def mytictactoe(val):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[0], val[1], val[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(val[3], val[4], val[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(val[6], val[7], val[8]))
    print("\t     |     |")
    print("\n")

    return "\n\t     |     |\n\t  " + str(val[0]) + "  |  " + str(val[1]) + "  |  " + str(val[2]) + "\n" \
        "\t_____|_____|_____\n\t     |     |\n\t  " + str(val[3]) + "  |  " + str(val[4]) + "  |  " + str(val[5]) + \
        "\n\t_____|_____|_____\n\t     |     |\n\t  " + str(val[6]) + "  |  " + str(val[7]) + "  |  " + str(val[8]) \
           + "\n\t     |     |\n"


def check_Tie(playerpos):
    if len(playerpos['X']) + len(playerpos['O']) == 9:
        return True
    return False


def check_Victory(playerpos, curplayer):
    # All probable winning combinations
    solution = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check whether any winning combination is satisfied or not
    for i in solution:
        if all(j in playerpos[curplayer] for j in i):
            # Return True if any winning combination is satisfied
            return True
            # Return False if no combination is satisfied
    return False
