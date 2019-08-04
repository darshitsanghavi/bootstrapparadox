# Bootstrap Paradox
Code Repository for Bootstrap Paradox Hackathon conducted by Blume at Microsoft Office, Bengaluru on 3rd August 2019 - 4th August 2019

URL:
https://skillenza.com/challenge/bootstrap-paradox/checkpoint/submit/1559

## Problem Statement by Milk Basket

> The goal of the problem is to generate innovative insights from order dataset and also to increase the average order value (AOV). The dataset for this competition is a flat-file describing customers orders over time. The dataset is anonymized and contains a sample of over 6 million grocery orders from more than 30000 Milkbasket users. The only information provided about users is their sequence of orders and the products in those orders. All of the IDs in the dataset are entirely randomized, and cannot be linked back to any other ID For each user, we provide more than 300 of their orders, with the sequence of products purchased in each order. We also provide the time of the day the product was added to the basket and the order was assumed to be created at that time itself.

## Team
### Name: Deburgerz
### Members:
- Darshit Sanghavi
- Darshan Shah

## Design Document

[Design Document](https://github.com/darshitsanghavi/bootstrapparadox/blob/master/DesignDocumentDeburgerz.pdf).

## Tech Stack
- Python
- Pandas
- Numpy
- Matplotlib
- AWS Lambda
- AWS Personalize

## Solution
[Python script to generate graphs](milkbsk_data_explore.py). 
The commented lines at the end can be uncommented one by one to see graphs or insights one by one and uncommenting all will generate all graphs at the same time.

### Insights:
1. Detecting the change in buyers trend when a product price fluctuates for users who has subscription to certain products
> Initially we drilled down to how many times a price of the product is changed. Based on that how is affects the orders with old and new selling rate. On the basis of these order details, the orders are further drilled down to subscribed and unsbscribed. These details are compared with new price of the product to check how many users have moved from subscription to non-subscription and vice versa once there was a price change.

2. Route Delivery
> Listing down the routes with maximum order delivered which can help in predicting how many delivery persons will be required in future.

3. Order Quantity
> Visualizing the total quantity of products being ordered by a user which can help in targetting some prooducts from another region to potential users like a canary deployment.

### Recommendation Engine
The insights generated can be used to train the engine to suggest users relevant products. We were planning to build an engine powered by Reinforcement Learning where it would learn by itself to recommend the user based on click history.
In interest of time, we have leveraged AWS Personalize which helps in building the recommendation engine in 3 ways. One by provinding best recommendation to the user by using HRRN. Another by proving the best recommendation from the past order history using Personalized Ranking and lastly using SIMS one can recommend another item to the user based on the current item viewed. 

### Milkbasket quest to find the name of the city in which it is going to launch?

The city name was encrypted using SHA-256 and was stored in an HTML/Angular tag in the code. On Decoding it was Pune
