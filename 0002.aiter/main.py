# このコードは、Python 3.10以降で利用できるコードです。
import asyncio


# 非同期イテレータを使って、非同期for文を実行する
async def asyncMain():
    async_iterable = AsyncIterable(5)
    async for i in async_iterable:
        print(i)

class AsyncIterable:
        def __init__(self, count):
            self.count = count
            
        def __aiter__(self):
            self.current = 0;
            return self
        
        # __anext__関数を定義することで、非同期イテレータを作成できる
        async def __anext__(self):
            if self.current < self.count:
                self.current += 1
                return self.current
            else:
                raise StopAsyncIteration

## 用途1 ファイルの非同期読み込み
async def async_line_reader(file_path):
    with open(file_path, 'r') as file:
        while True:
            line = await file.readline()
            if not line:
                break
            yield line.strip()

class AsyncFileIterable:
    def __init__(self, file_path):
        self.file_path = file_path

    async def __aiter__(self):
        return aiter(async_line_reader(self.file_path))
## 用途2 ネットワーク通信

## 用途3 データベースアクセス


if __name__ == '__main__':
    asyncio.run(asyncMain())