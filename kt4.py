class InvestmentOptimizer:
    def max_profit_1d(self, stocks, budget):
        dp = [0] * (budget + 1)
        selected = [[] for _ in range(budget + 1)]
        for i, (cost, profit) in enumerate(stocks):
            for amount in range(budget, cost - 1, -1):
                new_profit = dp[amount - cost] + profit
                if new_profit > dp[amount]:
                    dp[amount] = new_profit
                    selected[amount] = selected[amount - cost] + [i + 1]
        return dp[budget], selected[budget]

    def max_profit_2d(self, stocks, bonds, total_budget, risk_limit):
        if not 0 <= risk_limit <= 100:
            raise ValueError("Риск должен быть от 0 до 100 процентов")
        limit = int(total_budget * risk_limit / 100)
        dp = [[float("-inf")] * (limit + 1) for _ in range(len(stocks) + 1)]
        dp[0][0] = 0
        for i in range(1, len(stocks) + 1):
            cost, profit = stocks[i - 1]
            for amount in range(limit + 1):
                dp[i][amount] = dp[i - 1][amount]
                if amount >= cost:
                    dp[i][amount] = max(dp[i][amount], dp[i - 1][amount - cost] + profit)
        best_profit = float("-inf")
        stocks_amount = 0
        for amount in range(limit + 1):
            profit = dp[len(stocks)][amount] + (total_budget - amount) * bonds
            if profit > best_profit:
                best_profit = profit
                stocks_amount = amount
        return round(best_profit, 2), stocks_amount, total_budget - stocks_amount


def main():
    stocks = [(100, 10), (200, 30), (150, 20)]
    optimizer = InvestmentOptimizer()
    profit, selected = optimizer.max_profit_1d(stocks, 300)
    print("Одномерное ДП")
    print("Прибыль:", profit)
    print("Номера акций:", selected)
    print("Затраты:", sum(stocks[i - 1][0] for i in selected))
    profit, stocks_amount, bonds_amount = optimizer.max_profit_2d(stocks, 0.05, 300, 50)
    print("Двумерное ДП")
    print("Прибыль:", profit)
    print("В акции:", stocks_amount)
    print("В облигации:", bonds_amount)


if __name__ == "__main__":
    main()
