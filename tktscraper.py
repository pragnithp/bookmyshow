import requests
from bs4 import BeautifulSoup
import smtplib
from pushbullet import Pushbullet

# Function to send an email notification
def send_email(subject, body):
    sender_email = "thevectorspace314@gmail.com"  # Your email address
    receiver_email = "thevectorspace314@gmail.com"  # Receiver's email
    password = "Pragnith3105!"  # Your email password (use App Password if 2FA is enabled)

    message = f"Subject: {subject}\n\n{body}"

    # Set up the server and send the email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("thevectorspace314@gmail.com", "Pragnith3105!")
        server.sendmail(sender_email, receiver_email, message)

# Function to send a Pushbullet notification
def send_push_notification(title, message):
    pb = Pushbullet("o.k7pBLxnqH4EZoV8jzbUyyIugE2vHbSEe")  # Your Pushbullet API key
    push = pb.push_note(title, message)

# Function to scrape BookMyShow page and check for ticket availability
def check_tickets():
    url = "https://in.bookmyshow.com/buytickets/pushpa-the-rule-part-2-hyderabad/movie-hyd-ET00356724-MT/20241205"  # Replace with the URL of the movie/show page
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Example: Check if a specific element indicates availability
        tickets_available = soup.find("div", {"class": "__name"})  # Update the class here

        if tickets_available:
            print("Tickets are available!")
            send_email("Ticket Alert", "Tickets are available for booking!")
            send_push_notification("Ticket Alert", "Tickets are available for booking!")
        else:
            print("Tickets are not available.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Call the function to check for tickets
check_tickets()
