from email.mime.text import MIMEText
import smtplib

my_email = "yatintest117@gmail.com"
password = "shuf dyap txmo lybq"
to_addr = "yatintyagi2425@gmail.com"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(my_email, password)
server.sendmail(my_email, to_addr, msg="Subject:Helloworld\n\n This is the body")
server.quit()


