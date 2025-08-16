import streamlit as st
import pandas as pd
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",       # change as per your setup
        user="root",            # your MySQL username
        password="Sweetdreams2007@",    # your MySQL password
        database="food_management"      # your database name
    )

# -------------------------------
# Predefined Queries
# -------------------------------
queries = {
    "1. Total Food Receivers by City": 
        "SELECT city, COUNT(*) AS total_food_receivers FROM receivers_data GROUP BY city ORDER BY total_food_receivers DESC",

    "2. Total Food Providers by City": 
        "SELECT city, COUNT(*) AS total_food_providers FROM providers_data GROUP BY city ORDER BY total_food_providers DESC",

    "3. Top food provider": 
        "SELECT Type, COUNT(*) AS top_food_providers FROM providers_data GROUP BY Type ORDER BY top_food_providers DESC",

    "4. Top food receiver":
        "SELECT Type,COUNT(*) AS top_food_receivers FROM providers_data GROUP BY Type ORDER BY top_food_receivers DESC",

    "5. Contact information of food providers":
        "SELECT Contact, Type, Name FROM providers_data",

    "6. Total quantity of food available":
        "Select sum(Quantity) AS total_quantity FROM food_listings_data",

    "7. Cities having highest number of food listings":
        "SELECT Location, COUNT(*) AS top_citiesforlistings FROM food_listings_data GROUP BY Location ORDER BY top_citiesforlistings DESC",

    "8. Most commonly available food type":
        "SELECT Food_Type, COUNT(*) AS top_food_types FROM food_listings_data GROUP BY Food_Type ORDER BY top_food_types DESC",


    "9. Food claims made for each food item":
        "SELECT food_listings_data.Food_Name, COUNT(*) AS total_claims FROM food_listings_data JOIN claims_data ON food_listings_data.Food_ID=claims_data.Food_ID GROUP BY food_listings_data.Food_Name ORDER BY total_claims DESC",


    "10. Providers having highest number of completion":
         "SELECT food_listings_data.Provider_Type, COUNT(*) AS top_provider FROM food_listings_data JOIN claims_data ON food_listings_data.Food_ID=claims_data.Food_ID WHERE claims_data.Status='Completed' GROUP BY food_listings_data.Provider_Type ORDER BY top_provider DESC",


    "11. Percentage of completed,pending and cancelled status":
         "SELECT Status, COUNT(*) AS total_claims, ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM claims_data), 2) AS percentage_of_total FROM claims_data GROUP BY Status ORDER BY percentage_of_total DESC", 



    "12. Average quantity of food claimed":
         "SELECT AVG(Quantity) AS average_quantity FROM food_listings_data",


    "13. Meal type claimed most":
         "SELECT Meal_Type, COUNT(*) AS top_meal FROM food_listings_data GROUP BY Meal_Type ORDER BY top_meal DESC" ,



    "14. Total quantity of food donated":
         "SELECT Provider_Type, SUM(Quantity) AS Provider_quantity FROM food_listings_data GROUP BY Provider_Type ORDER BY provider_quantity DESC",

    
}

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="SQL Query Dashboard", layout="wide")
st.title("📊 SQL Query Dashboard")

# Dropdown to select query
query_name = st.selectbox("Choose a query to run:", list(queries.keys()))

# Show selected SQL query
st.code(queries[query_name], language="sql")

# Run query button
if st.button("Run Query"):
    try:
        conn = get_connection()
        df = pd.read_sql(queries[query_name], conn)
        conn.close()

        st.success("✅ Query executed successfully!")
        st.write("### Results:")
        st.dataframe(df, use_container_width=True)


    except Exception as e:
        st.error(f"❌ Error: {e}")
