import time
import sys
import random

all_time = int(input("这次需要计时多少秒？1h=60min=3600sec\n"))
end_time = all_time
bar_length = 40  # 进度条长度
library_list=[
    "✝︎ 少女祈祷中。。。。。。",
    "岂不闻，天无绝人之路！",
    "只要我想走，路就在脚下!",
    "正在装填弹药中。。。",
    "既然你诚心诚意的发问了。。。",
    "☣︎英雄可不能临阵脱逃啊！！！"
]

print("---强制娱乐时间---", end='\r', flush=True)  # 初始标题，会被后续内容覆盖
print(f"{random.choice(library_list)}")
while end_time >= 0:
    # 计算进度百分比和进度条
    progress = 1 - end_time / all_time
    filled_length = int(bar_length * progress)
    bar = '■' * filled_length + '□' * (bar_length - filled_length)
    
    # 计算剩余时间
    minutes = end_time // 60
    seconds = end_time % 60
    
    # 格式化输出（覆盖上一行）
    sys.stdout.write(f"\r{bar} 剩余时间为{minutes}分{seconds:02d}秒")
    sys.stdout.flush()
    
    if end_time > 0:
        time.sleep(1)  # 最后1秒不等待
    end_time -= 1

# 结束后显示消息
print("\n\n^_^== 娱乐时间结束了，可以学习啦==^_^")
