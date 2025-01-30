class TLogElements:
    def __init__(self):
        self.__in1=0
        self.__in2=0
        self._res=0
        if not hasattr(self,'_calc'):
            raise NotImplementedError('Нельзя создать такой объект!')
    def __setIn1(self,newIn1):
        if newIn1 in (0,1):
            self.__in1=newIn1
            self._calc()
    def __setIn2(self,newIn2):
        if newIn2 in (0,1):
            self.__in2=newIn2
            self._calc()
    In1 =property(lambda x:x.__in1,__setIn1)
    In2=property(lambda x:x.__in2,__setIn2)
    Res=property(lambda x:x._res)
class TNot(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)

    def _calc(self):
        self._res=int(not(self.In1))

class TAnd(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)

    def _calc(self):
        self._res=self.In1 * self.In2

class wor(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)
    def _calc(self):
        if self.In1==self.In2==1:
            self._res=1
        else:
            self._res=self.In1+self.In2
class ue(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)
    def _calc(self):
        if self.In1==self.In2:
            self._res=1
        else:
            self._res=0
class Txor(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)
    def _calc(self):
        if self.In1==self.In2:
            self._res=0
        else:
            self._res=1
class TImp(TLogElements):
    def __init__(self):
        TLogElements.__init__(self)
    def _calc(self):
        if self.In1==self.In2==1:
            self._res=1
        elif self.In1==self.In2==0:
            self._res=1
        else:
            self._res=int(not self.In1)*self.In2