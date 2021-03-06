from texting.chars import RT, SP

from aryth.bound.vector.duobound import duobound

paramsList = {
    'one_zero': [0],
    'one_nan': [None],
    'asc_4': [0, 1, 2, 3],
    'desc_4': [3, 2, 1, 0],
    'misc': [False, 101, True, 103],
    'misc2': [1, 't', None, 4, 'f', ' 3.5'],
    'tx_nums': ['244', 200, '306', '...', 'ant', 400, ],
    'tx_strs': 'comprehend how it\'s driven by animal spirits'.split(' '),
}


def test():
    for key, vec in paramsList.items():
        tag_list_x, tag_list_y = duobound(vec)
        print(key)
        print(SP, tag_list_x, vars(tag_list_x))
        print(SP, tag_list_y, vars(tag_list_x))


test()
