import streamlit as st
from PIL import Image
class Restaurant():


     def __init__(self,Menu):
         # Initialize the menu and total_amount as instance attributes
         self.total_amount = 0
         self.menu=Menu


     def disp_menu(self):
         st.subheader("MENU")
         for food, price in self.menu.items():
             # the items() method: gets you both the keys and values in a dictionary.
            st.write(f"{food}-->{price}")


     def take_order(self):
         order_count = 1  # Counter to generate unique keys for text_input widgets as they always take unique value
         rest_pic = Image.open("An-image-of-Alberto-and-Luca-eating-Trenette-al-Pesto.jpg")
         st.image(rest_pic, caption="WELCOME TO RESTAURANT")
         self.order = st.radio("do you want to order something ?", options=["yes", "no"])

         while self.order=="yes":
             self.disp_menu()
             order_count += 1
             food_key = f"food_order{order_count}"
             food_choice = st.text_input("please tell your order", key=food_key).lower()
             # Process the order only if the user entered something
             if food_choice:
                 if food_choice in self.menu:
                     self.total_amount = self.total_amount + self.menu[food_choice]
                 else:
                     st.write("sorry we don't have this item")
             order_count += 1  # Increment to ensure a new key next time
             repeat_key = f"repeat_order{order_count}"
             self.order = st.text_input("do you want to order something else?", key=repeat_key).lower()

         if self.order == "no":
             self.show_total()

     def show_total(self):
         st.write(f"Your Total Amount is Rs.{self.total_amount}")

         thank_pic = Image.open("thanku.jpeg")
         col1, col2, col3 = st.columns([1, 6, 1])

         with col1:
             st.write("")

         with col2:
             st.image(thank_pic, caption="Thank You")

         with col3:
             st.write("")


         st.write("Thanks for visiting ,Please Come Again!!!")
      #main method to process the order flow:
     #1. process_order by calling with object
     #2. take order
     #3. if yes, call disp_order
     #4  if no  ,show_total
     def process_order(self):
         self.take_order()

Menu={"tea":50,"hot chocolate":350,"coffee":200,"juice":80,"muffin":50,"fries":75,"strawberry pastry":120,"mango mousse":90,"sandwich":50 }
restaurant=Restaurant(Menu)
restaurant.process_order()
