import pandas as pd 
import datetime

data = pd.read_json('trips_gdrive.json')
def retail_affinity(focus_brand):
    result = data.groupby(["brand","retailer"])["qty"].sum().reset_index().sort_values(["brand","qty"],ascending = False).set_index(["brand","retailer"]).reset_index()
    focus = (list(result[result.brand==focus_brand].retailer)[0])
    return focus


def count_hhs(retailer,brand,start_date,end_date):
    household_transactions_dates = data.date
    start_date
    try:
        if start_date & end_date is not None:
            hh_query = 1 and (data.retailer == retailer) & (data.brand == brand) & (data.date > start_date) & (data.date <= end_date)
    except:
        hh_query = 1 and (data.retailer == retailer) & (data.brand == brand) & (data.date < datetime.datetime.today().strftime('%Y-%m-%d') )
    filter_hh_transactions = data[hh_query]
    unique_hh = filter_hh_transactions.userId.unique()
    

    print(filter_hh_transactions)

    print("These are the unique transactions:", len(unique_hh))


#Find out how much money each customer(userId) spent for a given brand

def top_buying_brand():
    data.amount = data.amount.str.replace("$", "")
    data.amount = data.amount.astype(float)

    data.amount = data.amount * data.qty

    total_amount_per_household = data.groupby(["brand", "userId"])["amount"].sum()
    top_selling_brand = total_amount_per_household.idxmax()[0]
    print(top_selling_brand)


# print(retail_affinity("Rockstar"))
# count_hhs(start_date = "2014-01-11", end_date = "2014-01-25")

top_buying_brand()


