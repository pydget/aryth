from texting.chars import RT, SP

from aryth.bound.matrix.duobound import duobound

paramsList = {
    'row': [[5, 7, 9, 10, 6]],
    'column': [[5], [7], [9], [10], [6]],
    'simple': [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    'tx_mx': [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']],
    'mixed': [['1', '2', 3], ['4', '...', '6'], ['7', '8', 'else']],
    'w_none': [[None, None, None], [4, None, 6], [7, 8, 9]],
    'empty': [],
    'empty2': [[]],
}


def test():
    for key, mx in paramsList.items():
        print(key)
        tagged_x, tagged_y = duobound(mx)
        print(SP, tagged_x, vars(tagged_x))
        print(SP, tagged_y, vars(tagged_y))


test()
