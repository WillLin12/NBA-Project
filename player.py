class Player:

    def __init__(self, p_id, name, pts, reb, ast, stls, blks, tpm, fgm, ftm, tov):
        self.__id = p_id 
        self.__name = name
        self.__pts = pts
        self.__reb = reb
        self.__ast = ast 
        self.__stls = stls
        self.__blks = blks
        self.__tpm = tpm
        self.__fgm = fgm
        self.__ftm = ftm 
        self.__tov = tov

	def get_id(self):
        return self.__id
        
    def get_x(self):
        return self.__x
    
