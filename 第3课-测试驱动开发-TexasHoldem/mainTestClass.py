import unittest  #python自动单元测试框架

from TexasHoldem import pokers       #导入pokers类
from TexasHoldem import pokersCmp    #导入pokersCmp类


class mainTest(unittest.TestCase):
    def setUp(self):
      self.pokersCmp = pokersCmp()

    def test_Case1(self):
      Input = 'Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH'
      output = self.pokersCmp.mainCmp(Input)
      self.assertEqual(output,'White wins')

    def test_Case2(self):
      Input = 'Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S'
      output = self.pokersCmp.mainCmp(Input)
      self.assertEqual(output,'White wins')

    def test_Case3(self):
      Input = 'Black: 2H 3H 5H 9H KH White: 2C 3H 4S 5C 6H'
      output = self.pokersCmp.mainCmp(Input)
      self.assertEqual(output,'Black wins')
    def test_Case4(self):
      Input = 'Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH'
      output = self.pokersCmp.mainCmp(Input)
      self.assertEqual(output,'Tie')




if __name__=="__main__": 
   unittest.main()
