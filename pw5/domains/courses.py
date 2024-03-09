class courses : 
    def __init__(self , courses_id , courses_name):
        self.id = courses_id 
        self.name = courses_name 
        self.scores = {} 
    
    def input_mark ( self , student , mark ) :
        self.scores[student] = mark 
    
    def get_mark( self  , student ): 
        return self.scores.get(student , 0 ) 
