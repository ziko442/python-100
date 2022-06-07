import smtplib


my_email = "from@example.com"
with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.starttls()
    server.login(user="d09a1bfff1a321", password="578b5ce7b572f0")
    server.sendmail(from_addr=my_email,
                    to_addrs="to@example.com",
                    msg='\nhelooo'
                    )
