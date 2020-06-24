
``` tree
├── 第3课-测试驱动开发-TexasHoldem
    ├── mainTestClass.py
    ├── pokersClassTest.py
    ├── pokersCmpClassTest.py
    ├── TexasHoldem.py
    ├── taskContent.md
    └── README.md

```

# mainTestClass.py
按照如下case进行测试
输入: Black: 2H 3D 5S 9C KD White: 2C 3H 4S 8C AH 输出: White wins  
输入: Black: 2H 4S 4C 2D 4H White: 2S 8S AS QS 3S 输出: White wins  
输入: Black: 2H 3H 5H 9H KH White: 2C 3H 4S 5C 6H 输出: Black wins  
输入: Black: 2H 3D 5S 9C KD White: 2D 3H 5C 9S KH 输出: Tie  
# pokersClassTest.py  
测试 pokers 类  
pokers 类 作用是 判断手牌类型
# pokersCmpClassTest.py  
测试 pokersCmp 类  
pokersCmp 类 作用是 判断相同类型手牌的大小
# TexasHoldem.py  
在里面定义了pokers 和 pokersCmp 类
# taskContent.md
作业内容