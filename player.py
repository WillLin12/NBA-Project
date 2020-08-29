class Player:

    def __init__(self, p_id, name, pts, reb, ast, stls, blks, tpm, fgm, ftm, tov, fga, fta):
        self.id = p_id 
        self.name = name
        self.pts = pts
        self.reb = reb
        self.ast = ast 
        self.stls = stls
        self.blks = blks
        self.tpm = tpm
        self.fgm = fgm
        self.fga = fga
        self.ftm = ftm 
        self.fta = fta
        self.tov = tov
        self.fantasy = 0

    def calculate_pct(self):
        if self.fga == 0:
            return 0 
        return self.fgm / self.fga

    def calculate_ftpct(self):
        if self.fta == 0:
            return 0 
        return self.ftm / self.fta

    def get_id(self):
        return self.id

    def set_fta(self, p_id):
        self.id = p_id

    def get_fta(self):
        return self.id

    def set_fga(self, p_id):
        self.id = p_id

    def get_fga(self):
        return self.id  

    def set_id(self, p_id):
        self.id = p_id
        
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_pts(self):
        return self.pts

    def set_pts(self, pts):
        self.pts = pts

    def get_reb(self):
        return self.reb

    def set_reb(self, pts):
        self.reb = reb

    def get_ast(self):
        return self.ast

    def set_ast(self, pts):
        self.ast = ast
    
    def get_stls(self):
        return self.stls

    def set_stls(self, pts):
        self.stls = stls
    
    def get_blks(self):
        return self.blks

    def set_blks(self, pts):
        self.blks = blks
    
    def get_tpm(self):
        return self.tpm

    def set_tpm(self, pts):
        self.tpm = tpm
        
    def get_fgm(self):
        return self.fgm

    def set_fgm(self, pts):
        self.fgm = fgm

    def get_ftm(self):
        return self.ftm

    def set_ftm(self, pts):
        self.ftm = ftm

    def get_tov(self):
        return self.tov

    def set_tov(self, pts):
        self.tov = tov