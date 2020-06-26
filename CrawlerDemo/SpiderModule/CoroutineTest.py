import  asyncio
import aiohttp  # 支持asyncio的request模块

# 定义一个协程函数, 里面io操作必须是特殊指定的才有协程效果, 否则没有任何效果
async def get_request(url):
    async with await aiohttp.ClientSession() as session:  # aiohttp中的session
        # with session.get(url, headers = {}, params, proxy) 有headers params和proxy效果
        async with await session.get(url) as response: # 发送网页请求
            page_text = response.text()  # 执行

    return page_text
    # await asyncio.sleep(1)  # C#中的 yield return new WaitForSeconds(2)

    return "it's "
# 协程函数结束后执行的回调函数
def callback(task):
    print('我是回调函数', task.result())  # task.result用于接受协程函数的返回值



coroutine1 = get_request(1)  # 声明了一个协程对象(任务对象)
task = asyncio.ensure_future(coroutine1)  # 封装了协程对象
task.add_done_callback(callback)  # 给协程对象添加回调函数,

coroutine2 = get_request(2)  # 声明第二个)
task2 = asyncio.ensure_future(coroutine2)

tasks = [task, task2]

loop = asyncio.get_event_loop()  # 创建一个事件循环对象

loop.run_until_complete(task)  # 执行单个任务对象  C#中的 StartCoroutine()
loop.run_until_complete(asyncio.wait(tasks))  # 协程同时执行多个任务对象

