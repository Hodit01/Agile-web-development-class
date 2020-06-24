#cards = '2H 4D 3C 6S 5H'
'''
pokers类的作用
整理手牌顺序、判断手牌类型
四个数字相同的牌按三条处理
'''
class pokers():
  def __init__(self,name=None,cards=None):
    self.pokersType = {'散牌':1,'对子':2,'两对':3,
                       '三条':4,'顺子':5,'同花':6,
                       '同花顺':7}
    self.pokersNum = {'2':2,'3':3,'4':4,'5':5,
                      '6':6,'7':7,'8':8,'9':9,
                      'T':10,'J':11,'Q':12,'K':13,
                      'A':14}
    self.pokersCol ={ 'S':4, #黑桃
                      'H':3, #红桃
                      'D':2, #方片
                      'C':1  #梅花 
                    }

    self.name = name #持牌者名称
    self.cards = self.sortCards(cards) #所持手牌
    self.cardsNumList= []
    self.cardsColList = []
    self.cardsNumSet = {}
    self.cardsNumSetLen = 0
    self.cardsColSet = {}
    self.cardsColSetLen = 0
    
    self.cardsType = self.getCardsType(cards)  #所持手牌类型



  def sortCards(self,cards):
    cardsList = cards.split(' ')
    cards = []
    for card in cardsList:
      cardTuple = (self.pokersNum[card[0]],self.pokersCol[card[1]])
      cards.append(cardTuple)
    cards.sort( key = lambda x : (x[0], x[1]) )
    self.cards =cards
    return cards
  
  def getCardsType(self,cards):
    cards = self.sortCards(cards)
    cardsNumList= []
    cardsColList = []
    cardsType = None
    
    for  card in cards:
      cardsNumList.append(card[0])
      cardsColList.append(card[1])
    
    self.cardsNumList = cardsNumList
    self.cardsColList = cardsColList
    cardsNumSet = set(cardsNumList)
    cardsColSet = set(cardsColList)

    self.cardsNumSet = cardsNumSet
    self.cardsColSet = cardsColSet

    cardsNumSetLen = len(cardsNumSet)
    cardsColSetLen = len(cardsColSet)
    self.cardsNumSetLen = cardsNumSetLen
    self.cardsColSetLen = cardsColSetLen


    if cardsColSetLen == 1:
      isStraigh = True
      i = 0
      while i < 4:
        if cardsNumList[i+1] - cardsNumList[i] != 1:
          isStraigh = False
          break
        i += 1
      if isStraigh and cardsColSetLen==1:  #同花顺
        cardsType = 7
      else:
        cardsType = 6 #同花

    else:
      #set长度为5可能为 散牌、顺子
      if cardsNumSetLen==5:
        isStraigh = True
        i = 0
        while i < 4:
          if cardsNumList[i+1] - cardsNumList[i] != 1:
            isStraigh = False
            break
          i += 1
        if isStraigh: #顺子
          cardsType = 5
        else:
          cardsType = 1 #散牌

      elif cardsNumSetLen== 4: #对子
        cardsType = 2
      
      else: #cardsNumSetLen==3 or 2 可能为两对或三条
        isTwoPairsTest = True
        for i in cardsNumSet:
          if cardsNumList.count(i) >= 3:  #四个数字相同的牌按三条处理
            isTwoPairsTest = False
            break
        if isTwoPairsTest:  #两对
          cardsType = 3   
        else:          #三条
          cardsType = 4
    
    self.cardsType = cardsType
    return cardsType
  
    
'''
pokersCmp类的作用
比较两手牌的大小
'''
class pokersCmp():
  def cmp_ReturnWinnerName(self,B_pokers,W_pokers):
    if B_pokers.cardsType > W_pokers.cardsType:
      return B_pokers.name
    elif B_pokers.cardsType < W_pokers.cardsType:
      return W_pokers.name
    else:
      cardsType = B_pokers.cardsType
      if cardsType == 7:
        return self.straightFlushCmp(B_pokers,W_pokers)
      elif cardsType == 6:
        return self.suitCmp(B_pokers,W_pokers)
      elif cardsType == 5:
        return self.straightCmp(B_pokers,W_pokers)
      elif cardsType == 4:
        return self.threeOfAKindCmp(B_pokers,W_pokers)
      elif cardsType == 3:
        return self.twoPairsCmp(B_pokers,W_pokers)
      elif cardsType == 2:
        return self.onePairsCmp(B_pokers,W_pokers)
      elif cardsType == 1:
        return self.cardCmp(B_pokers,W_pokers)
  

  def mainCmp(self,Input):
    B_name = Input[0:5]
    W_name = Input[22:27]
    B_cards = Input[7:21]
    W_cards = Input[29:43]
    output = 'Tie'

    B_pokers = pokers(B_name ,B_cards)
    W_pokers = pokers(W_name,W_cards)
    winner = self.cmp_ReturnWinnerName(B_pokers,W_pokers)
    if winner != 'Tie':
      output = winner + " wins"
    return output
      


      


  def straightFlushCmp(self,B_pokers,W_pokers):
    return self.cardCmp(B_pokers,W_pokers)

  def suitCmp(self,B_pokers,W_pokers):
    return self.cardCmp(B_pokers,W_pokers)
  def straightCmp(self,B_pokers,W_pokers):
    return self.cardCmp(B_pokers,W_pokers)

  def threeOfAKindCmp(self,B_pokers,W_pokers):
    B_cardsNumSet =  B_pokers.cardsNumSet
    B_cardsNumList = B_pokers.cardsNumList
    B_num = None

    for i in B_cardsNumSet:
      if B_cardsNumList.count(i) >=3:
        B_num = i
        break
    
    W_cardsNumSet =  W_pokers.cardsNumSet
    W_cardsNumList = W_pokers.cardsNumList
    W_num = None

    for i in W_cardsNumSet:
      if W_cardsNumList.count(i) >=3:
        W_num = i
        break
    
    if B_num > W_num:
      return B_pokers.name
    elif B_num < W_num:
      return W_pokers.name
    else:
      return 'Tie'
      

  def twoPairsCmp(self,B_pokers,W_pokers):
    return self.pairsCmp(B_pokers,W_pokers)
  def onePairsCmp(self,B_pokers,W_pokers):
    return self.pairsCmp(B_pokers,W_pokers)

  def pairsCmp(self,B_pokers,W_pokers):
    winner = None
    B_cardsNumSet =  B_pokers.cardsNumSet
    B_cardsNumList = B_pokers.cardsNumList
    B_cardsNumCountDic = {}
  
    for i in B_cardsNumSet:
      B_cardsNumCountDic[i] = B_cardsNumList.count(i)

    W_cardsNumSet =  W_pokers.cardsNumSet
    W_cardsNumList = W_pokers.cardsNumList
    W_cardsNumCountDic = {}

    for i in W_cardsNumSet:
      B_cardsNumCountDic[i] = B_cardsNumList.count(i)
    
    if B_pokers.cardsType == 4:
      B_num = None
      W_num = None
      for i in B_cardsNumSet:
        if B_cardsNumCountDic[i] >=3:
          B_num = i
          break
      for i in W_cardsNumSet:
        if W_cardsNumCountDic[i] >=3:
          W_num = i
          break
      if B_num > W_num:
        winner = B_pokers
      elif B_num < W_num:
        winner = W_pokers
      else:
        pass

    elif B_pokers.cardsType == 3 or B_pokers.cardsType == 2:
      B_paris = []
      B_one_cards = []

      for i in B_cardsNumSet:
        if B_cardsNumList.count(i) == 2:
          B_paris.append(i)
        else:
          B_one_cards.append(i)
      W_paris = []
      W_one_cards = []
      for i in W_cardsNumSet:
        if W_cardsNumList.count(i) == 2:
          W_paris.append(i)
        else:
          W_one_cards.append(i)
      
      B_paris.sort(reverse = True)
      W_paris.sort(reverse = True)
      B_one_cards.sort(reverse = True)
      W_one_cards.sort(reverse = True)

      
      for i in range(len(B_paris)):
        if B_paris[i] > W_paris[i]:
          winner = B_pokers
          break
        elif B_paris[i] < W_paris[i]:
          winner = W_pokers
          break
        else:
          pass
   
      if winner == None:
        for i in range(len(B_one_cards)):
          if B_one_cards[i] > W_one_cards[i]:
            winner = B_pokers
            break
          elif B_one_cards[i] < W_one_cards[i]:
            winner = W_pokers
            break
          else:
            pass
    else:
      pass

    if winner == None:
      return 'Tie'
    else:
      return winner.name

 


  def cardCmp(self,B_pokers,W_pokers):

    B_cardsNumList = B_pokers.cardsNumList
    W_cardsNumList = W_pokers.cardsNumList

    winner = 'Tie'
    i = 4
    while i >= 0:
      if B_cardsNumList[i] < W_cardsNumList[i]:
        winner = W_pokers.name
        break
      elif B_cardsNumList[i] > W_cardsNumList[i]:
        winner = B_pokers.name
        break
      else:
        i -= 1
    return winner

    



'''
pokers = pokers()
print(pokers.showPokersType(cards = '2H 3H 4H 5H 6H'))

B_pokers =pokers('Black','2H 3H 6H 4H 5H')
W_pokers =pokers('White','3D 7D 5D 6D 4D')
pokersCmp = pokersCmp()
winner = pokersCmp.cmp_ReturnWinnerName(B_pokers,W_pokers)
print(winner)

'''



