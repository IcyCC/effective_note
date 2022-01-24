
from datetime import datetime, date


template = """
#猪猪攒钱史# Day {days} {today}
已花费总计：👸🏼 {girl_total}元   🐷 {boy_total}元
🌸🌸🌼🌼🌻🌻🌸🌸🌼🌼🌻🌻
👸🏼：
{girl_cost_text}
———————————
💰： {girl_today_total}

🐷：
{boy_cost_text}
——————————
💰： {boy_today_total}
"""

today = date.today()
start_day = date(year=2022, month=1, day=18)
days = (today - start_day).days + 1

def get_emoji_day(num):
    res = ""
    emoji_list = ["0️⃣","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣"]
    for i in str(num):
        res = res + emoji_list[int(i)]
    return res

def stand_str(s):
    return s.replace(":", ",").replace(" ","").replace("，", ",")

gril_bill = """
早餐，2.5
交通, 3
Vintage耳饰，399
咖啡, 22
晚饭, 吃了筑底食堂(日料）,120
草莓🍓, 13.5
房租,2990
"""
gril_pre= 635.8

boy_bill = """
早饭,馒头片, 1
今天公司调休,午饭晚饭免费,0
剪头发,35
"""
boy_pre = 3548

def pareser(bill:str, pre_total):
    bill = stand_str(bill)
    result = []
    total = 0
    bill_lines = bill.splitlines()
    for line in bill_lines:
        if not line:
            continue
        blocks = line.split(",")
        if len(blocks) == 2:
            (name, cost) = blocks
            total = total + float(cost)
            result.append("{name}:{cost} 元".format(name=name, cost=cost))
        if len(blocks) == 3:
            (name, note, cost) = blocks
            total = total + float(cost)
            result.append("{name}: {note} {cost}元".format(name=name, cost=cost, note=note))
    return {
        "today_total": total,
        "total": pre_total + total,
        "cost_text": "\n".join(result)
    }

girl = {"girl_"+k:v for k,v in pareser(gril_bill, gril_pre).items()}
boy =  {"boy_"+k:v for k,v in pareser(boy_bill, boy_pre).items()}
print(days)
print(template.format(
    today=today.strftime("%Y.%m.%d"),
    days=get_emoji_day(days),
    **girl, **boy))
