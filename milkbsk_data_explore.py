'''
This code is intended to find data insights of Milk Basket Sale Data
author : Darshan Shah , Darshit
date : 3rd Aug 19
'''
#import python libraries
import pandas as pd
import numpy as np

#import plotting libraries
import matplotlib.pyplot as plt
import seaborn as sns

#read csv and load the data
def load_sale_data():
    sales_dataframe = pd.read_csv('hackathon_data.csv')
    print(sales_dataframe.head())
    print(sales_dataframe.shape)
    return sales_dataframe

#check for data quality
def check_data_quality(sales_dataframe):
    print(sales_dataframe['product_quantity'].isnull())
    print(sales_dataframe['product_quantity'].isnull().value_counts())

def quantity_of_product_purchased(sales_dataframe):
    #sales_dataframe = sales_dataframe.reset_index(drop=True)
    results = sales_dataframe['product_quantity'].groupby(sales_dataframe['customer_id']).sum()
    results = results.to_frame()
    results.to_csv('family_size.csv')
    results.reset_index(inplace=True)
    #results.reset_index('customer_id','product_quantity')
    print(results.head())

    #Count
    results = results['customer_id'].groupby(results['product_quantity']).count()
    #results = results.value_counts()
    #out = pd.cut(results.value_counts(), bins=[1, 20, 40, 60,80,100], include_lowest=True)
    #print(out)
    out = pd.cut(results, bins=[0, 10,20,30,100,200,300], include_lowest=True)
    ax = out.value_counts(sort=False).plot.bar(rot=0, color="b", figsize=(6,4))
    #ax.set_xticklabels([c[1:-1].replace(","," to") for c in out.cat.categories])
    plt.show()

    results = results.to_frame()
    results.reset_index(inplace=True)
    fig = plt.figure()
    fig,ax = plt.subplots()
    sns.barplot(x='product_quantity',y='customer_id',data=results,ax=ax,ci=20)
    #sns.catplot(x='product_quantity', hue='customer_id', data=results,kind="count",ax=ax)
    #print(ax)
    plt.show()
    print(results.shape)

def highest_selling_manufacturer(sales_dataframe,column_name):
    results = sales_dataframe['product_quantity'].groupby(sales_dataframe['manufacturer_id']).sum().reset_index()
    print(results.keys())
    results=results.sort_values(by=['product_quantity'],ascending=[False])
    results = results.nlargest(5,'product_quantity')
    print(results.shape)
    ax = results.plot.bar(x='manufacturer_id', y='product_quantity', figsize=(15, 10))
    plt.xticks(fontsize=7, rotation=35)
    plt.show()

def common_subscribedprods():
    subscribed = sales_dataframe[(sales_dataframe['subscription']==1)]
    subscribed_products = subscribed[['product_id','subscription']].groupby('product_id').count()
    unsubscribed = sales_dataframe[(sales_dataframe['subscription']==0)]
    unsubscribed_products=unsubscribed[['product_id','subscription']].groupby('product_id').count()
    merged = pd.merge(left=subscribed_products,right=unsubscribed_products,left_on='product_id',right_on='product_id',how='inner')
    print(merged.shape)
    print(merged)
    merged.to_csv('common_products.csv')

def price_change_product(sales_dataframe):
    #print(sales_dataframe.selling_price_per_unit.nunique())
    price_change = sales_dataframe.groupby(['product_id','order_id'])['selling_price_per_unit'].apply(np.unique)
    #price_change.to_csv('price_change.csv')
    price_change = price_change.to_frame()
    price_change.reset_index(inplace=True)
    print(price_change.head())
    price_change.to_csv('test_price.csv')
    price_change_load = pd.read_csv('test_price.csv')
    count_by_ordernprice = price_change_load.groupby(['product_id','selling_price_per_unit']).size()
    count_by_ordernprice.to_csv('count_by_ordernprice.csv')
    print(count_by_ordernprice)
    #print(price_change.to_csv('test_price.csv'))

def factor_subscrip_pricechange(sales_dataframe):
    df = sales_dataframe[['product_id','selling_price_per_unit','subscription']][sales_dataframe['subscription']==1].groupby(['product_id','selling_price_per_unit']).count()
    #df = df.count().to_frame()
    df.reset_index()
    #df.to_csv('subscribedgrp.csv')
    print(df.shape)
    dfs = sales_dataframe[['product_id','selling_price_per_unit','subscription']][sales_dataframe['subscription']==0].groupby(['product_id','selling_price_per_unit']).count()
    #dfs = dfs.to_frame()
    dfs.reset_index()
    #dfs.drop(['customer_id','manufacturer_id','society_id','city_id','route_id','store_id','order_id','order_date'category_id	subcategory_id	product_id	product_quantity	selling_price_per_unit	total_cost	subscription	product_addedtobasket_on])
    print(dfs.head())
    print(dfs.shape)
    #dfs.to_csv('unsubscrioedgrp.csv')

    #plot
    #data = pd.read_csv('unsubscrioedgrp.csv')
    data = pd.read_csv('subscribedgrp.csv')
    data = data.sort_values("product_id",axis=0,ascending=True)
    print(data.head())
    print('***************')
    #print(data[data['product_id'==1121568]])
    fig, ax = plt.subplots()
    count = 1
    for key,grp in data[213:224].groupby(['product_id']):
        count = count+10
        print(grp)
        grp.reset_index()
        #print(grp[['selling_price_per_unit']])
        ax = grp.plot(ax=ax, kind='line', x='selling_price_per_unit', y='subscription', label=key,marker='o')
        #ax = grp.plot(ax=ax,kind='line',x=grp)
    plt.legend(loc='Subscription change based on price')
    plt.show()

    #print(dfs.filter['product_id','selling_price_per_unit','subscription'])
def product_trending_cities(sales_dataframe):
    trending_prod = sales_dataframe[['city_id','product_id','product_quantity']].groupby(['city_id','product_id'])['product_quantity'].sum().sort_values(ascending=False)
    trending_prod[0:10].plot.bar(grid=True,color='#D7BDE2')
    plt.grid(axis='y', alpha=0.75)
    plt.xticks(fontsize=7, rotation=35)
    plt.show()
    #trending_prod.reset_index()
    #trending_prod.to_csv('trending_prod.csv')
    print(trending_prod)

def time_analysis(sales_dataframe):
    sales_dataframe['time_added_to_cart'] = pd.to_datetime(sales_dataframe['product_addedtobasket_on'])
    time_based_group = sales_dataframe[['order_id','time_added_to_cart','route_id']].groupby(['time_added_to_cart','route_id'])['order_id'].count().reset_index(name='count').sort_values(by=['count'],ascending=False)
    print(time_based_group.head())
    plt.scatter(x=time_based_group['route_id'],y=time_based_group['count'],alpha=0.5)
    plt.ylabel('counts')
    plt.xlabel('routes')
    plt.show()
    
def run_data_analysis():
    sales_dataframe = load_sale_data()
    #check_data_quality(sales_dataframe)
    #quantity_of_product_purchased(sales_dataframe)
    #highest_selling_manufacturer(sales_dataframe,'manufacturer_id')
    #price_change_product(sales_dataframe)
    #factor_subscrip_pricechange(sales_dataframe)
    #product_trending_cities(sales_dataframe)
    time_analysis(sales_dataframe)

run_data_analysis()