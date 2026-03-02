#case of one of lists/ recieved params is empty
def one_empty_params(list_1, list_2, result_list):

#if list one empty
    if(list_1.len < 1): # result should be the contents of the second param
        return (list_2 == result_list)