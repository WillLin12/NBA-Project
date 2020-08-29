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

    def set_id(self, p_id):
        self.__id = p_id
        
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_pts(self):
        return self.__pts

    def set_pts(self, pts):
        self.__pts = pts

    def get_reb(self):
        return self.__reb

    def set_reb(self, pts):
        self.__reb = reb

    def get_ast(self):
        return self.__ast

    def set_ast(self, pts):
        self.__ast = ast
    
    def get_stls(self):
        return self.__stls

    def set_stls(self, pts):
        self.__stls = stls
    
    def get_blks(self):
        return self.__blks

    def set_blks(self, pts):
        self.__blks = blks
    
    def get_tpm(self):
        return self.__tpm

    def set_tpm(self, pts):
        self.__tpm = tpm
        
    def get_fgm(self):
        return self.__fgm

    def set_fgm(self, pts):
        self.__fgm = fgm

    def get_ftm(self):
        return self.__ftm

    def set_ftm(self, pts):
        self.__ftm = ftm

    def get_tov(self):
        return self.__tov

    def set_tov(self, pts):
        self.__tov = tov