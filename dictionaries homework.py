restaurantrestaurant_menu["Main Course"]["Steak"] = 17.99
_menu["Beverages"] = {"Coffee": 2.50, "Soda": 1.99}
del restaurant_menu["Starters"]["Bruschetta"]

class TicketSystem:
    def __init__(self):
        self.service_tickets = {}

    def open_ticket(self, ticket_id, customer, issue):
        self.service_tickets[ticket_id] = {"Customer": customer, "Issue": issue, "Status": "open"}

    def close_ticket(self, ticket_id):
        if ticket_id in self.service_tickets:
            self.service_tickets[ticket_id]["Status"] = "closed"
        else:
            print(f"Ticket {ticket_id} not found.")

    def display_tickets(self):
        for ticket_id, ticket_info in self.service_tickets.items():
            print(f"Ticket {ticket_id}: Customer: {ticket_info['Customer']}, Issue: {ticket_info['Issue']}, Status: {ticket_info['Status']}")

# Initialize the ticket system
ticket_system = TicketSystem()

# Example usage
ticket_system.open_ticket("Ticket001", "Alice", "Login problem")
ticket_system.open_ticket("Ticket002", "Bob", "Payment issue")
ticket_system.close_ticket("Ticket002")

# Display all tickets
ticket_system.display_tickets()

