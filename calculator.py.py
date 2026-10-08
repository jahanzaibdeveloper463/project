def calculate_budget(income, expenses, months):
    monthly_savings = income - expenses
    if monthly_savings <= 0:
        return 0
    return monthly_savings * months

def recommend_mobiles(mobiles_list, budget):
    recommended = []
    for mobile in mobiles_list:
        if mobile["price"] <= budget:
            recommended.append(mobile)
    
    # Prices high to low sort hongi
    recommended.sort(key=lambda x: x["price"], reverse=True)
    return recommended