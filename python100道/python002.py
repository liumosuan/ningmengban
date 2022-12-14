"""
低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成。
从键盘输入当月利润I，求应发放奖金总数？
"""
try:
    profit = float(input("输入当月利润，单位(万元):"))
    if profit <= 10:
        print(f"应发放奖金总数为{profit * 0.1}万元")
    elif profit <= 20:
        print(f"应发放奖金总数为：{10 * 0.1 + (profit - 10) * 0.075}万元")
    elif 20 < profit <= 40:
        print(f"应发放奖金总数为：{10 * 0.1 + 10 * 0.075 + (profit - 20) * 0.05}万元")
    elif 40 < profit <= 60:
        print(f"应发放奖金总数为：{10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (profit - 40) * 0.03}万元")
    elif 60 < profit <= 100:
        print(f"应发放奖金总数为：{10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (profit - 60) * 0.015}万元")
    else:
        print(
            f"应发放奖金总数为：{10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (profit - 100) * 0.01}万元")
except Exception as e:
    print("输入的不是正确利润！")
