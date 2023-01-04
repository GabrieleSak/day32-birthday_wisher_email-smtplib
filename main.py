import smtplib
from secrets import *

# connection = smtplib.SMTP("smtp.gmail.com", port=587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs=email, msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()


with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg="Subject:Hello\n\nThis is the body of my email.\n\nHave a nice day!"
    )
