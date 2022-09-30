
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
