'''
先记录所有的字符和意思
tax         : 遗产税
money_first : 一代的基础累积财富
money_add   : 银行累积过的财富
money_end   : 经过遗产税的财富
sakura_bag  : 是否有樱包
residens    : 是否有高等居民身份
word_tree   : 世界树等级
time2       : 二代丢在银行内的时间
time3       : 三代至少需要的存放在银行的时间
min_rates   : 最低的利率
base_rates  : 中间的利率
max_rates   : 最高的利率
rates       : 需要的利率
'''

# 初始化变量
word_tree = 0  # 世界树等级 (0-100)
residens = "no"
sakura_bag = "no"
min_rates = 0.000
max_rates = 0.005
base_rates = None
persion = 1e-6
tax = 0.3
money_first = 0  # 初始化为0，将在主函数中设置

def change(word_tree, residens, sakura_bag):
    global tax, min_rates, max_rates
    # 根据世界树等级调整税率 (0-100级)
    # 保持最大减免为60级的10%
    if word_tree >= 60:
        tax -= 0.10  # 60级及以上减税10%
    elif word_tree >= 40:
        tax -= 0.06  # 40级减税6%
    elif word_tree >= 20:
        tax -= 0.04  # 20级减税4%
    elif word_tree >= 10:
        tax -= 0.02  # 10级减税2%
    
    # 确保税率不低于0
    tax = max(tax, 0)
    
    if residens.lower() == "yes":
        tax -= 0.10
        tax = max(tax, 0)
    
    if sakura_bag.lower() == "yes":
        min_rates += 0.004
        max_rates += 0.004
    
    return tax, min_rates, max_rates

# 计算累积过的财富
def wealth_add(money_first, base_rates, time2):
    money_add = money_first
    t = time2
    while t > 0:
        money_add += money_add * base_rates
        t -= 1
    return money_add

# 计算财富在利率下恢复所需时间
def wealth_again(money_end, money_add, base_rates):
    time3 = 0
    current = money_end
    while current < money_add:
        current = wealth_add(current, base_rates, 1)  # 计算一年的增长
        time3 += 1
        if time3 > 200:  # 设置最大年限
            break
    return time3

# 计算每年需要注入的金额
def calculate_injection(money_end, target_wealth, base_rates, years):
    """
    计算每年需要注入的金额
    :param money_end: 初始税后财富
    :param target_wealth: 需要恢复到的目标财富
    :param base_rates: 利率
    :param years: 恢复年限
    :return: 每年需要注入的金额
    """
    if base_rates == 0:
        # 利率为0时，简单平均
        return (target_wealth - money_end) / years
    
    # 计算年金终值系数
    annuity_factor = ((1 + base_rates) ** years - 1) / base_rates
    # 计算现值系数
    present_value_factor = (1 + base_rates) ** years
    
    # 需要注入的金额 = (目标财富 - 初始财富的终值) / 年金终值系数
    injection = (target_wealth - money_end * present_value_factor) / annuity_factor
    return max(injection, 0)  # 确保非负

# 计算恢复时间和实际填补金额
def calculate_recovery_time(money_end, target_wealth, rate, annual_injection, max_years=100):
    """
    计算恢复时间和实际填补金额
    :param money_end: 初始税后财富
    :param target_wealth: 目标财富
    :param rate: 利率
    :param annual_injection: 每年注入金额
    :param max_years: 最大计算年限
    :return: 恢复所需年数, 总注入金额
    """
    current = money_end
    total_injection = 0
    recovery_year = 0
    
    for year in range(1, max_years + 1):
        # 应用利率增长
        interest = current * rate
        current += interest
        
        # 添加年度注入
        current += annual_injection
        total_injection += annual_injection
        
        # 检查是否恢复
        if current >= target_wealth:
            recovery_year = year
            break
    
    # 如果未在最大年限内恢复
    if recovery_year == 0:
        recovery_year = max_years
        # 计算未恢复时的总注入金额
        total_injection = annual_injection * max_years
    
    return recovery_year, total_injection

# 计算三种利率方案下的填补资金
def calculate_injection_scenarios(money_end, target_wealth, min_rate, max_rate, years):
    """
    计算三种利率方案下的填补资金
    :param money_end: 初始税后财富
    :param target_wealth: 目标财富
    :param min_rate: 最低利率
    :param max_rate: 最高利率
    :param years: 恢复年限
    :return: 三种方案结果
    """
    # 计算三种利率方案
    low_rate = min_rate
    mid_rate = (min_rate + max_rate) / 2
    high_rate = max_rate
    
    # 计算每种利率下的年注入金额
    low_injection = calculate_injection(money_end, target_wealth, low_rate, years)
    mid_injection = calculate_injection(money_end, target_wealth, mid_rate, years)
    high_injection = calculate_injection(money_end, target_wealth, high_rate, years)
    
    # 计算每种方案的实际恢复时间和总注入金额
    low_recovery, low_total = calculate_recovery_time(money_end, target_wealth, low_rate, low_injection)
    mid_recovery, mid_total = calculate_recovery_time(money_end, target_wealth, mid_rate, mid_injection)
    high_recovery, high_total = calculate_recovery_time(money_end, target_wealth, high_rate, high_injection)
    
    # 返回结果
    return {
        "low_rate": {
            "rate": low_rate,
            "annual_injection": low_injection,
            "recovery_time": low_recovery,
            "total_injection": low_total
        },
        "mid_rate": {
            "rate": mid_rate,
            "annual_injection": mid_injection,
            "recovery_time": mid_recovery,
            "total_injection": mid_total
        },
        "high_rate": {
            "rate": high_rate,
            "annual_injection": high_injection,
            "recovery_time": high_recovery,
            "total_injection": high_total
        }
    }

# 手动调整参数
def manual_adjustment():
    print("\n===== 手动调整参数 =====")
    print("1. 调整利率范围")
    print("2. 调整恢复时间")
    print("3. 调整世界树等级")
    print("4. 调整高等居民身份")
    print("5. 调整樱包状态")
    print("6. 调整一代基础财富")
    print("7. 返回主菜单")
    
    choice = input("请选择要调整的参数 (1-7): ")
    return choice

# 主函数
def main():
    global word_tree, residens, sakura_bag, min_rates, max_rates, tax, money_first
    
    # 获取用户输入
    print("===== 财富传承计算器 =====")
    money_first = float(input("输入一代的基础累积财富: "))
    time2 = int(input("输入二代丢在银行内的时间: "))
    
    # 获取世界树等级 (0-100)
    while True:
        try:
            word_tree = int(input("输入世界树等级 (0-100): "))
            if 0 <= word_tree <= 100:
                break
            else:
                print("请输入0-100之间的整数")
        except ValueError:
            print("请输入数字")
    
    residens = input("是否有高等居民身份?(yes/no): ").strip().lower()
    sakura_bag = input("是否开启樱包?(yes/no): ").strip().lower()
    
    # 根据用户选择调整税率和利率
    tax, min_rates, max_rates = change(word_tree, residens, sakura_bag)
    
    # 初始化变量
    base_rates = min_rates
    money_add = wealth_add(money_first, base_rates, time2)
    money_end = money_add * (1 - tax)
    injection = 0
    time3 = 0
    
    # 主循环
    while True:
        if sakura_bag == "yes":
            # 开启樱包模式 - 使用二分法寻找合适利率
            low, high = min_rates, max_rates
            best_rate = (low + high) / 2
            money_add = wealth_add(money_first, best_rate, time2)
            money_end = money_add * (1 - tax)
            time3 = wealth_again(money_end, money_add, best_rate)
            
            print("\n===== 财富恢复分析 (开启樱包) =====")
            print(f"遗产税: {tax:.2%}")
            print(f"利率范围: {min_rates:.6f} ~ {max_rates:.6f}")
            print(f"当前利率: {best_rate:.6f}")
            print(f"一代累积财富: {money_first:.2f}")
            print(f"二代存放{time2}年后财富: {money_add:.2f}")
            print(f"税后财富: {money_end:.2f}")
            print(f"三代恢复所需时间: {time3}年")
            print(f"三代恢复后财富: {money_add:.2f}")
            
        else:
            # 不开启樱包模式 - 计算需要注入的金额
            money_add = wealth_add(money_first, base_rates, time2)
            money_end = money_add * (1 - tax)
            
            # 获取恢复时间
            if time3 <= 0:
                time3 = 60  # 默认恢复时间
            new_time = input(f"输入期望的恢复时间 (默认 {time3} 年): ")
            if new_time.strip():
                time3 = int(new_time)
            
            # 计算三种利率方案下的填补资金
            scenarios = calculate_injection_scenarios(money_end, money_add, min_rates, max_rates, time3)
            
            print("\n===== 财富恢复分析 (不开启樱包) =====")
            print(f"遗产税: {tax:.2%}")
            print(f"一代累积财富: {money_first:.2f}")
            print(f"二代存放{time2}年后财富: {money_add:.2f}")
            print(f"税后财富: {money_end:.2f}")
            print(f"三代恢复目标财富: {money_add:.2f}")
            print(f"恢复年限: {time3}年")
            
            # 输出三种方案
            print("\n===== 资金填补方案 =====")
            print("方案一: 最低利率方案")
            print(f"  利率: {scenarios['low_rate']['rate']:.6f}")
            print(f"  每年需填补: {scenarios['low_rate']['annual_injection']:.2f}")
            print(f"  实际恢复时间: {scenarios['low_rate']['recovery_time']}年")
            print(f"  总填补金额: {scenarios['low_rate']['total_injection']:.2f}")
            
            print("\n方案二: 中等利率方案")
            print(f"  利率: {scenarios['mid_rate']['rate']:.6f}")
            print(f"  每年需填补: {scenarios['mid_rate']['annual_injection']:.2f}")
            print(f"  实际恢复时间: {scenarios['mid_rate']['recovery_time']}年")
            print(f"  总填补金额: {scenarios['mid_rate']['total_injection']:.2f}")
            
            print("\n方案三: 最高利率方案")
            print(f"  利率: {scenarios['high_rate']['rate']:.6f}")
            print(f"  每年需填补: {scenarios['high_rate']['annual_injection']:.2f}")
            print(f"  实际恢复时间: {scenarios['high_rate']['recovery_time']}年")
            print(f"  总填补金额: {scenarios['high_rate']['total_injection']:.2f}")
        
        # 提供手动调整选项
        adjust = input("\n是否对结果满意? (yes/no): ").lower()
        if adjust == "yes":
            break
        
        choice = manual_adjustment()
        
        if choice == "1":
            # 调整利率范围
            new_min = float(input(f"输入新最低利率 (当前: {min_rates:.6f}): "))
            new_max = float(input(f"输入新最高利率 (当前: {max_rates:.6f}): "))
            min_rates = new_min
            max_rates = new_max
        
        elif choice == "2":
            # 调整恢复时间
            if sakura_bag == "yes":
                print("开启樱包模式下无法直接调整恢复时间，请调整利率")
            else:
                new_time = int(input(f"输入新恢复时间 (当前: {time3}): "))
                time3 = new_time
        
        elif choice == "3":
            # 调整世界树等级
            while True:
                try:
                    new_level = int(input(f"输入新世界树等级 (当前: {word_tree}): "))
                    if 0 <= new_level <= 100:
                        word_tree = new_level
                        tax, min_rates, max_rates = change(word_tree, residens, sakura_bag)
                        break
                    else:
                        print("请输入0-100之间的整数")
                except ValueError:
                    print("请输入数字")
        
        elif choice == "4":
            # 调整高等居民身份
            new_residens = input(f"是否有高等居民身份?(当前: {'是' if residens == 'yes' else '否'} yes/no): ").strip().lower()
            residens = new_residens
            tax, min_rates, max_rates = change(word_tree, residens, sakura_bag)
        
        elif choice == "5":
            # 调整樱包状态
            new_sakura = input(f"是否开启樱包?(当前: {'是' if sakura_bag == 'yes' else '否'} yes/no): ").strip().lower()
            sakura_bag = new_sakura
            tax, min_rates, max_rates = change(word_tree, residens, sakura_bag)
        
        elif choice == "6":
            # 调整一代基础财富
            new_wealth = float(input(f"输入新的一代基础财富 (当前: {money_first:.2f}): "))
            money_first = new_wealth
        
        elif choice == "7":
            # 返回主菜单
            continue

if __name__ == "__main__":
    main()
