# coding: utf-8
#Black Jack

class Game:
    def __init__(self):
        self.cards = {1: 4, 2: 4, 3: 4, 4: 4, 5: 4, 6: 4, 7: 4, 8: 4, 9: 4, 10: 4, 11: 4, 12: 4, 13: 4}
        self.player_num = 0

    
    @classmethod
    def new_game(cls):
        
        # プレイヤー人数の設定
        error_count = 0
        while True:
            try:
                num = int(input("プレイヤー人数を入力してください > "))
                print("プレイヤーは" + str(num) + "人でよろしいですか？")
                ans = input("YES or NO? > ").lower()
                print(ans)
                if ans == "yes":
                    print("プレイヤーは" + str(num) + "人です")
                    cls.player_num = num
                    break
                else:
                    pass
            except:
                print("数値を入力してください")
                error_count += 1
                if error_count == 5:
                    print("お帰りくださいませ。")
                    break
        
        # プレイヤーの生成

      
        
        

class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.state = "alive"

if __name__ == "__main__":
    print("New Game!!")
    Game.new_game()