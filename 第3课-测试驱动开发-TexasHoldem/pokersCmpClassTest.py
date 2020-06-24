import unittest  #python自动单元测试框架

from TexasHoldem import pokers       #导入pokers类
from TexasHoldem import pokersCmp    #导入pokersCmp类


'''
#手牌类型对应的数值
pokersType = {'散牌':1,'对子':2,'两对':3,
              '三条':4,'顺子':5,'同花':6,
              '同花顺':7
}

pokersNum = {'2':2,'3':3,'4':4,'5':5,
             '6':6,'7':7,'8':8,'9':9,
             'T':10,'J':11,'Q':12,'K':13,
             'A':14
}
pokersCol ={ 'D':1, #方片
             'S':2, #黑桃
             'H':3, #红桃
             'C':4  #梅花
}
'''



#测试pokersCmp类
class pokersCmpTest(unittest.TestCase):
   def setUp(self):
      self.pokersCmp = pokersCmp()

   def test_cmpCase1(self):
      B_pokers =pokers('Black','2H 3D 5S 9C KD')
      W_pokers =pokers('White','2C 3H 4S 8C AH')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')

   def test_cmpCase2(self):
      B_pokers =pokers('Black','2H 4S 4C 2D 4H')
      W_pokers =pokers('White','2S 8S AS QS 3S')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')

   def test_cmpCase3(self):
      B_pokers =pokers('Black','2H 3H 5H 9H KH')
      W_pokers =pokers('White','2C 3H 4S 5C 6H')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Black')

   def test_cmpCase4(self):
      B_pokers =pokers('Black','2H 3D 5S 9C KD')
      W_pokers =pokers('White','2D 3H 5C 9S KH')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Tie')
   
   def test_straightFlushCmpCase1(self):
      B_pokers =pokers('Black','2H 3H 6H 4H 5H')
      W_pokers =pokers('White','3D 7D 5D 6D 4D')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')
   
   def test_straightFlushCmpCase2(self):
      B_pokers =pokers('Black','2H 3H 6H 4H 5H')
      W_pokers =pokers('White','2H 4H 6H 3H 5H')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Tie')

   def test_straightCmpCase1(self):
      B_pokers =pokers('Black','2D 3H 6S 4H 5H')
      W_pokers =pokers('White','3D 7H 5S 6D 4D')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')
   
   def test_straightCmpCase2(self):
      B_pokers =pokers('Black','2H 3D 6H 4H 5H')
      W_pokers =pokers('White','2H 3S 6H 4H 5H')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Tie')

   def test_threeOfAKindCmpCase1(self):
      B_pokers =pokers('Black','2D 2H 2S 4H 5H')
      W_pokers =pokers('White','3D 5C 5S 5D 4D')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')
   
   def test_threeOfAKindCmpCase2(self):
      B_pokers =pokers('Black','2H 2D 2S 2C 5H')
      W_pokers =pokers('White','7H 3S 3H 3C 5C')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')

   def test_twoPairsCmpCase1(self):
      B_pokers =pokers('Black','4D 4H 3S 3H 5H')
      W_pokers =pokers('White','3D 3C 2S 2S 4D')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Black')
   
   def test_twoPairsCmpCase2(self):
      B_pokers =pokers('Black','2D 2H 3S 3H 5H')
      W_pokers =pokers('White','3D 3C 2S 2S 5S')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Tie')
   
   def test_onePairsCmpCase1(self):
      B_pokers =pokers('Black','4D 4H 2S 3H 5H')
      W_pokers =pokers('White','3D 3C 9S 2S 4D')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Black')
   
   def test_onePairsCmpCase2(self):
      B_pokers =pokers('Black','2D 2H 8S 3H 5H')
      W_pokers =pokers('White','4D 8C 2S 2C 5S')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')
   
   def test_cardCmpCase1(self):
      B_pokers =pokers('Black','2D 7H 8S 3H 5H')
      W_pokers =pokers('White','3D 8C 7S 2C 5S')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'Tie')
   def test_cardPairsCmpCase2(self):
      B_pokers =pokers('Black','2D 5H 8S 3H 6H')
      W_pokers =pokers('White','6D 8C 9S 3C 5S')
      winner = self.pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
      self.assertEqual(winner,'White')



if __name__=="__main__": 
   unittest.main()