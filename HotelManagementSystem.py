
class Hotel:

    def __init__(self, name, rooms, location, rating, price):
        self.name = name
        self.rooms = rooms
        self.location = location
        self.rating = rating
        self.price = price


class User:

    def __init__(self, username, user_id, booking_cost):
        self.username = username
        self.user_id = user_id
        self.booking_cost = booking_cost

class Operation:

    def print_hotel(self, hotels_list):
        for hotel in hotels_list:
            print("Name : ", hotel.name)
            print("Location : ", hotel.location)
            print("Rooms : ", hotel.rooms)
            print("Rating : ", hotel.rating)
            print("Price : ", hotel.price)
            print()

    def sort_hotel_rating(self, hotels_list):
        hotels_list_sort = sorted(hotels_list, key = lambda hotel: hotel.rating, reverse = True)
        print("Sorted list by rating : ")
        self.print_hotel(hotels_list_sort)

    def sort_hotel_price(self, hotels_list):
        hotels_list_sort = sorted(hotels_list, key = lambda hotel: hotel.price)
        print("Hotels sorted from cheapest → most expensive : ")
        self.print_hotel(hotels_list_sort)    

    def filter_by_city(self, hotels_list, city):
        hotels_list_filter = []
        for hotel in hotels_list:
            if hotel.location.lower() == city.lower():
                hotels_list_filter.append(hotel)
        if hotels_list_filter == []:
            print("No hotel found")
        else:
            self.print_hotel(hotels_list_filter)

    def filter_by_rooms(self, hotels_list, min_rooms):
        hotels_list_filter = []
        for hotel in hotels_list:
            if hotel.rooms > min_rooms:
                hotels_list_filter.append(hotel)
        if hotels_list_filter == []:
            print("No hotel found")
        else:
            self.print_hotel(hotels_list_filter)
        
class Booking:

    def book_hotel(self, hotels_list, users_list):
        user_id = int(input("Enter your user ID : "))

        # flags
        user_found = None
        hotel_found = None

        # finding user ID
        for users in users_list:
            if user_id == users.user_id:
                user_found = users
                break

        if user_found:
            print("User found : ", user_found.username)
            
            # finding hotel name
            hotel_name = input("Enter hotel name to search : ")
            for hotel in hotels_list:
                if hotel_name.lower() in hotel.name.lower():
                    hotel_found = hotel
                    break
            if hotel_found:
                print("Hotel found : ", hotel_name)
            else:
                print("Hotel not found")
        else:
            print("User not found")

        if hotel_found and user_found:
            try:
                rooms_needed = int(input("Enter number of rooms to book : "))
            except ValueError:
                print("Invalid room number")
                return
    
            # check availability
            if rooms_needed <= 0:
                print("Invalid number of rooms")
                return
    
            if rooms_needed > hotel_found.rooms:
                print("Not enough rooms available")
                return
    
            # update system
            hotel_found.rooms -= rooms_needed
            cost = rooms_needed * hotel_found.price

            if cost > user_found.booking_cost:
                print("Insufficient balance")
                return

            user_found.booking_cost -= cost

    
            # confirmation
            print("\nBooking Successful!")
            print("Hotel:", hotel_found.name)
            print("Rooms booked:", rooms_needed)
            print("Remaining balance:", user_found.booking_cost)
            print("Remaining rooms:", hotel_found.rooms)


            


def menu():
    print("--- Hotel Management System ---")
    print("1 Show Hotels")
    print("2 Sort by Rating")
    print("3 Sort by Price")
    print("4 Filter by City")
    print("5 Filter by Rooms")
    print("6 Exit")
    print("--- Booking System ---")
    print("7 Book a hotel")
    print("8 Exit")

hotel_Raj = Hotel("Raj",20,"mumbai",4.2,2000)
hotel_Mani = Hotel("Mani",13,"pune",4.6,5000)
hotel_Taj = Hotel("Taj",8,"mumbai",4.8,8000)

user_Max = User("Max",1005,3000)
user_Jay = User("Jay",1006,8000)

hotels_list = [hotel_Raj,hotel_Mani,hotel_Taj]
users_list = [user_Max,user_Jay]

op = Operation()
bk = Booking()

while True:
    menu()

    try:
        user_input = int(input("Enter your choice : "))
        
        if user_input == 1:
            op.print_hotel(hotels_list)

        elif user_input == 2:
            op.sort_hotel_rating(hotels_list)

        elif user_input == 3:
            op.sort_hotel_price(hotels_list)

        elif user_input == 4:
            city = input("Enter the city you want to filter : ")
            op.filter_by_city(hotels_list, city)

        elif user_input == 5:
            try:
                min_rooms = int(input("Enter the number of rooms you require : "))
                op.filter_by_rooms(hotels_list, min_rooms)
            except ValueError:
                print("Please enter valid number")

        elif user_input == 6:
            print("Exiting Program...")
            break

        elif user_input == 7:
            bk.book_hotel(hotels_list,users_list)

        elif user_input == 8:
            print("Exiting Program...")
            break

        else:
            print("Invalid option please select again")

    except ValueError:
        print("Invalid Input")