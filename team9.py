

team_name = 'Clueless' 
strategy_name = 'Operation CCB'
strategy_description = 'The strategy works in a pattern of CCB'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'b'  
    '''

   
    
    return 'b'

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, depending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            'c','b'.join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
   
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
            print ('Test passed')
     
    test_move(my_history='bcc',
              their_history='cbb', 
             
              my_score=0, 
              their_score=0,
              result='b')      
