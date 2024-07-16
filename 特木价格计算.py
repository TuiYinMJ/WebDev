def supply_price_cny():
    # Given values
    gross_margin_coefficient = float(input("请输入毛利率0-1:"))
    product_weight_kg = float(input("请输入产品重量(kg):"))  # 应该输入千克
    display_price_usd = float(input("请输入产品售价(美元):"))

    # Convert the display price from USD to CNY
    display_price_cny = display_price_usd * 7  # 假设汇率为1美元兑换7人民币

    # Calculate the supply price in CNY
    # 供货价 = (前端显示价格 * 7 - 运费) / (1 + 毛利系数)
    supply_price_cny = ((display_price_cny * 7) - (120 *
                        product_weight_kg)) / (1 + gross_margin_coefficient)
    print('实际供货价格RMB:' + str(supply_price_cny))


def supply_price_usd():
    # Given values
    gross_margin_coefficient = float(input("请输入毛利系数0-1:"))
    supply_price_cny = float(input("请输入供货价RMB:"))
    product_weight_kg = float(input("请输入产品重量(kg):"))  # 应该输入千克

    # Calculate the front-end display price in USD
    # 前端显示价格 = (供货价 * (1 + 毛利系数) + 运费) / 7
    display_price_usd = (
        supply_price_cny * (1 + gross_margin_coefficient) + (120 * product_weight_kg)) / 7
    print('前端展示价$:' + str(display_price_usd))


if __name__ == '__main__':
    while (True):
        n = int(input("请输入计算前端售价(1)，还是逆推供货价(2),退出系统(0)"))
        if n == 1:
            supply_price_usd()
        elif n == 2:
            supply_price_cny()
        elif n == 0:
            break
