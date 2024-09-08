
def main():
    # abs関数は引数の絶対値を返す
    print(abs(4))
    print(abs(-4))
    
    # abs関数は引数が浮動小数点数の場合も使える
    print(abs(4.5))
    print(abs(-4.5))
    
    # abs関数は引数が複素数の場合も使える
    print(abs(complex(3, 4)))
    
    # abs関数が定義されたクラスの場合、__abs__関数が呼び出される
    meter = Meter(7)
    print(abs(meter))
    
# __abs__関数を定義するクラス
class Meter:
    
    def __init__(self, value):
        self.value = value
        
    def __abs__(self):
        return self.value + 10
    
    
if __name__ == '__main__':
    main()