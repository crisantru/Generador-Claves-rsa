#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Enviar correo Gmail con Python

 
import smtplib
 
fromaddr = 'crisantru@gmail.com'
toaddrs  = 'crisantru@gmail.com'
msg = 'Correo enviado utilizano Python '
 
 
# Datos
username = 'crisantru@gmail.com'
password = 'Itwaslondon2802@'
 
# Enviando el correo

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()