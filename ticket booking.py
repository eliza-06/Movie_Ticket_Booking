movies = {
    "1": {"name": "Avengers: Endgame", "available_seats": 10},
    "2": {"name": "Inception", "available_seats": 8},
    "3": {"name": "The Matrix", "available_seats": 5}}
def display_movies():
    print("\nAvailable Movies:")
    for key, movie in movies.items():
        print(f"{key}. {movie['name']} (Seats Available: {movie['available_seats']})")
def book_ticket():
    display_movies()
    movie_choice = input("\nEnter the number of the movie you want to book: ")
    if movie_choice not in movies:
        print("Invalid movie selection.")
        return
    try:
        num_tickets = int(input("Enter the number of tickets you want to book: "))
        if num_tickets <= 0:
            print("Please enter a valid number of tickets.")
            return
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    movie = movies[movie_choice]
    if num_tickets <= movie['available_seats']:
        movie['available_seats'] -= num_tickets
        print(f"Successfully booked {num_tickets} tickets for '{movie['name']}'. Enjoy the show!")
    else:
        print(f"Sorry, only {movie['available_seats']} tickets are available for '{movie['name']}'.")
def main():
    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. View Movies")
        print("2. Book Ticket")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            display_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            print("Thank you for using the booking system!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
