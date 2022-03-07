class Molecula():

    def __init__( self,n,w,KE,PE,hits,minimumw, minimumPE, minimumhits, Z, valid ):
        self.n=n
        self.w=w
        self.KE=KE
        self.PE=PE
        self.hits=hits
        self.minimumw = minimumw
        self.minimumPE = minimumPE
        self.minimumhits = minimumhits
        self.Z = Z
        self.valid = valid

    def toString(self):
        return "{ n: %s, PE: %.16f, KE: %.16f, Z: %.16f }" % (str(self.n), float(self.PE), self.KE, self.Z)