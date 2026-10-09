import streamlit as st
from scraper.py import get_mobile_data
from calculator.py import calculate_budget, recommend_mobiles

# Page Configuration
st.set_page_config(page_title="Budget Mobile Advisor", page_icon="📱", layout="centered")

st.title("📱 Budget-Based Mobile Advisor")
st.write("Apni monthly income aur savings plan ke hisaab se best mobiles dhoondhein.")

st.divider()

# Input Section
col1, col2 = st.columns(2)

with col1:
    income = st.number_input("Monthly Income (Rs.)", min_value=10000, value=50000, step=5000)
    expenses = st.number_input("Monthly Expenses (Rs.)", min_value=0, value=35000, step=2000)

with col2:
    months = st.slider("Savings Period (Months)", min_value=1, max_value=24, value=6)

# Action Button
if st.button("Find Recommended Mobiles", type="primary"):
    total_budget = calculate_budget(income, expenses, months)
    monthly_savings = income - expenses
    
    if monthly_savings <= 0:
        st.error("Aapke kharche aapki income se ziada ya barabar hain! Savings possible nahi hain.")
    else:
        st.success(f"**Monthly Savings:** Rs. {monthly_savings:,} | **Total Target Budget:** Rs. {total_budget:,}")
        
        # Load Data & Filter
        mobiles_list = get_mobile_data()
        recommended = recommend_mobiles(mobiles_list, total_budget)
        
        st.subheader(f"Recommended Mobiles (Under Rs. {total_budget:,})")
        
        if recommended:
            for item in recommended:
                st.markdown(f"**📱 {item['name']}** — `Rs. {item['price']:,}`")
        else:
            st.warning("Aapke budget ke andar koi mobile match nahi hua. Savings months barhayein ya budget adjust karein.")
