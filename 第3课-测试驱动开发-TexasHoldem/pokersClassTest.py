import unittest  #python自动单元测试框架

from TexasHoldem import pokers       #导入pokers类

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
pokersCol ={ 'S':4, #黑桃
             'H':3, #红桃
             'D':2, #方片
             'C':1  #梅花 
            }
'''
#测试pokers类
class pokersTest(unittest.TestCase):
   def setUp(self):
      self.pokers = pokers()
   
   def test_sortCardsCase1(self):
      cards = '2H 4D 3C 6S 5H'
      self.assertEqual(self.pokers.sortCards(cards),[(2,3),(3,1),(4,2),(5,3),(6,4)])

   def test_sortCardstCase2(self):
      cards = '2H 2D 3C 3S 5H'
      self.assertEqual(self.pokers.sortCards(cards),[(2,2),(2,3),(3,1),(3,4),(5,3)])

   def test_sortCardsCase3(self):
      cards = '2H 2D 2C 2S 5H'
      self.assertEqual(self.pokers.sortCards(cards),[(2,1),(2,2),(2,3),(2,4),(5,3)])
    

   #同花顺
   def test_straightFlush(self):
      cards = '2H 3H 4H 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),7)

   #同花
   def test_suit(self):
      cards = '2H 7H 4H 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),6)
   #顺子
   def test_straight(self):
      cards = '3D 7H 4H 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),5)
   #三条
   def test_threeOfAKindCase1(self):
      cards = '2H 2D 2S 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),4)

   #三条
   def test_threeOfAKindCase2(self):
      cards = '2H 2D 2S 2C 6H'
      self.assertEqual(self.pokers.getCardsType(cards),4)
   #两对
   def test_twoPairs(self):
      cards = '2H 2D 4H 4D 6H'
      self.assertEqual(self.pokers.getCardsType(cards),3)
   #对子
   def test_onePairs(self):
      cards = '2H 2D 4H 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),2)
   #散牌
   def test_card(self):
      cards = '2H 7H 4D 5H 6H'
      self.assertEqual(self.pokers.getCardsType(cards),1)        
 

if __name__=="__main__": 
   unittest.main()
