package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	conferenceName := "Go Conference"
	const conferenceTickets = 50
	var remainingTickets uint = 50

	greetUsers(conferenceName)

	fmt.Printf("Welcome to our %v booking app.\n", conferenceName)
	fmt.Println("We have total of", conferenceTickets, "tickets and", remainingTickets, "available tickets.")
	fmt.Println("Get your tickets here to attend.")

	for {
		//an array => var bookings = [50]string{}
		// var bookings [50]string //array type
		// bookings[0] = "Nana"
		var bookings = make([]map[string]string, 0) // list of maps, 0 = initial size
		// var bookings =[]string{} // slice
		// bookings :=[]string{} // slice

		var firstName string
		var lastName string
		var email string
		var userTicket uint
		// ask for user input
		fmt.Println("Enter your first name:")
		fmt.Scan(&firstName) // & pointer - variable that points to the memory adress

		fmt.Println("Enter your last name:")
		fmt.Scan(&lastName)

		fmt.Println("Enter your email adress:")
		fmt.Scan(&email)

		fmt.Println("Enter number of tickets:")
		fmt.Scan(&userTicket)

		isValidName := len(firstName) >= 2 && len(lastName) >= 2
		//var isValidName bool = len(firstName) >= 2 && len(lastName) >= 2
		isValidEmail := strings.Contains(email, "@")
		isValidUserTicket := userTicket > 0 && userTicket <= remainingTickets

		// if userTicket > remainingTickets {
		// 	fmt.Printf("We have only %v tickets.\n", remainingTickets)
		// 	continue
		// }

		if isValidName && isValidEmail && isValidUserTicket {

			remainingTickets = remainingTickets - userTicket
			// bookings[0] = firstName + " " + lastName // gets value from array

			// a map for a user
			var userData = make(map[string]string)
			userData["firstName"] = firstName
			userData["lastName"] = lastName
			userData["email"] = email
			userData["numberOfTickets"] = strconv.FormatUint(uint64(userTicket), 10)

			bookings = append(bookings, userData) //append value to list of maps

			fmt.Printf("The whole slice: %v \n", bookings)
			fmt.Printf("The first value: %v \n", bookings[0])
			fmt.Printf("Slice type: %T \n", bookings)
			fmt.Printf("Slice length: %v \n", len(bookings))

			fmt.Printf("Thank you %v %v for booking %v tickets. You will recive a confirmation email at %v. \n", firstName, lastName, userTicket, email)
			fmt.Printf("%v tickets remaining.\n", remainingTickets)

			firstNames := []string{}
			for _, booking := range bookings {
				// var firstName = names[0]
				firstNames = append(firstNames, booking["firstName"])
				return firstName
			} // "booking" is a random variable name,
			// blank identifier "_" is in "index" pleace to ignore variable which we don't want to use (it causes a syntax error)

			fmt.Printf("The first names of booking are: %v.\n", firstNames)
			fmt.Printf("All bookings: %v.\n", bookings)

			// var noTicketsRemainig bool = remainingTickets == 0
			noTicketsRemaining := remainingTickets == 0
			if noTicketsRemaining {
				fmt.Println("Conference is booked out.")
				break
			}
		} else {
			if !isValidName {
				fmt.Println("Invalid first or last name")
			}
			if !isValidEmail {
				fmt.Println("Invalid email")
			}
			if !isValidUserTicket {
				fmt.Println("Invalid ticet number")
			}

		}

	}

	// city := "London"

	// switch city {
	// case "New York":
	// case "Singapore", "Hong Kong":
	// case "London", "Berlin":
	// case "Mexico City":
	// default:
	// 	fmt.Println("No valid city selected")

}

func greetUsers(confName string) {
	fmt.Printf("Welcome to %v. \n", confName)
}
