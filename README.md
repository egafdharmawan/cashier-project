# Cashier Simple Project With Python

## A. Background

Given the case of giant supermarket manager who wants to make their own self service cahsier system. This system is designed so every customer can make their own purchase everywhere.

## B. Requirements

Tools used in this project :
- Python 3.9

## C. Objectives

Create a simple self service cashier system with python. Here are all the features.
- Add Item
- Update Item
- Delete Item
- Check Cart
- Reset Transaction
- Check Promo
- Checkout

## D. FlowChart

This is the flowchart on how the machine works :

![Cashier System ERD](https://user-images.githubusercontent.com/49968948/217165701-c4476164-b392-4579-9860-a6532824615f.png)

## E. Program Guide

This section will feature explanation of every function on the system
1. Create_Transaction() :

   Trigger when used enter the main menu, followed by asking an input for the user name
   
   <img width="455" alt="image" src="https://user-images.githubusercontent.com/49968948/217168346-c555e46d-eba6-4246-944d-9a9b857c0294.png">

2. Add_Item():
   
   Add new item into the cart.
   
   <img width="188" alt="image" src="https://user-images.githubusercontent.com/49968948/217168731-a2628eb8-c5c8-4c78-9b4d-734448b5870b.png">
   
3. Update_Item():
   
   Update the item on the cart.
   
   <img width="387" alt="image" src="https://user-images.githubusercontent.com/49968948/217168879-d2f39271-c482-4cbb-9e43-05d452d636e3.png">
   
4. Delete_Item():
   
   Delete an item on the cart.
   
   <img width="379" alt="image" src="https://user-images.githubusercontent.com/49968948/217169043-842f1dc7-6373-4d53-a190-44132bc556d9.png">
   
5. Reset_Transaction():
   
   Reset all item added to cart / empty the cart.
   
   <img width="349" alt="image" src="https://user-images.githubusercontent.com/49968948/217169107-05394f98-5f62-4bdf-8eeb-b715ea5f47aa.png">
   
6. Check_Item():
   
   Check all available item on cart.
   
   <img width="558" alt="image" src="https://user-images.githubusercontent.com/49968948/217169527-4380d63c-2e60-4558-a7b3-040b60033713.png">
   
7. Checkout():
   
   Preview on all item added, their price (promo included).
   
   <img width="568" alt="image" src="https://user-images.githubusercontent.com/49968948/217169797-3641e6bc-b677-441e-a536-e1ac8244d7a0.png">
     
## F. Test Guide

Test Case
1. Add item
  - Fried Chicken, Qty: 2, Price: 20.000
  - ToothPaste, Qty: 3, Price: 15.000
  
  <img width="224" alt="image" src="https://user-images.githubusercontent.com/49968948/217170597-8f95a4e3-bccc-44e1-adcf-3d283133ea99.png">
  <img width="576" alt="image" src="https://user-images.githubusercontent.com/49968948/217170648-51160a41-1f0b-4720-9ebf-b787b823b66c.png">

2. Delete Item
  - ToothPaste

  <img width="576" alt="image" src="https://user-images.githubusercontent.com/49968948/217170794-0d32479e-b550-4f58-9916-1bcaacb5c801.png">

3. Reset The Transaction
  
  <img width="354" alt="image" src="https://user-images.githubusercontent.com/49968948/217170918-3df9b477-bfe5-4967-8f61-ab28bf278ef8.png">

4. Add some item and Checkout.
  
  <img width="581" alt="image" src="https://user-images.githubusercontent.com/49968948/217171089-1e312c2c-29ab-4b01-b313-5112c6760ebe.png">

## G. Conclusion

The system has proven to be work successfully, since this is only a simple system there are a lot of ways we can improve it's performance such as adding other feature for the system.
