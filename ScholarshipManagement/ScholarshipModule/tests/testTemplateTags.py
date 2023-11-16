from django.test import TestCase
from ScholarshipModule.templatetags import add1
from ScholarshipModule.templatetags import sub1
from ScholarshipModule.templatetags import index
from ScholarshipModule.templatetags import replaceType
from ScholarshipModule.templatetags import getFromDict
from ScholarshipModule.templatetags import replaceType

class testTemplateTags(TestCase):

    def testAdd1(self):
        num1 = 1
        
        assert add1.add1(num1) == 2
        
    
    def testSub1(self):
        num1 = 1
        
        assert sub1.sub1(num1) == 0
    
    def testIndex(self):
        a = list({1, 2, 3, 4, 5})
        
        self.assertEquals(index.index(a,0), 1)
        self.assertEquals(index.index(a,1), 2)
        self.assertEquals(index.index(a,2), 3)
        self.assertEquals(index.index(a,3), 4)
        self.assertEquals(index.index(a,4), 5)
    
    def testReplaceType(self):
        a = 0
        b = 1
        
        self.assertEquals(replaceType.replaceType(a), 'Porcentaje')
        self.assertEquals(replaceType.replaceType(b), 'Dinero')
    
    def testGetFromDict(self):
        a = {'1':1,'2':2,'3':3,'4':4,'5':5}
        
        self.assertEquals(getFromDict.get(a,'1'),1)
        self.assertEquals(getFromDict.get(a,'2'),2)
        self.assertEquals(getFromDict.get(a,'3'),3)
        self.assertEquals(getFromDict.get(a,'4'),4)
        self.assertEquals(getFromDict.get(a,'5'),5)
        
        
        



    

