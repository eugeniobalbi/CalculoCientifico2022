# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 11:57:38 2022

@author: eugen
"""

def add_time(start, duration, starting_day=""):
    # Separa el inicio en horas y minutos.
    pieces = start.split()
    time = pieces[0].split(":")
    end = pieces[1]

    # Calcular formato de reloj de 24 horas
    if end == "PM" :
        hour = int(time[0]) + 12
        time[0] = str(hour)
    
    # Separar la duración en horas y minutos.
    dur_time = duration.split(":")

    # Agregar horas y minutos
    new_hour = int(time[0]) + int(dur_time[0])
    new_minutes = int(time[1]) + int(dur_time[1])

    if new_minutes >= 60 :
        hours_add = new_minutes // 60
        new_minutes -= hours_add * 60
        new_hour += hours_add

    days_add = 0
    if new_hour > 24 :
        days_add = new_hour // 24
        new_hour -= days_add * 24
    
    # Encuentra AM y PM
    if new_hour > 0 and new_hour < 12 :
        end = "AM"
    elif new_hour == 12 :
        end = "PM"
    elif new_hour > 12 :
        end = "PM"
        new_hour -= 12
    else :
        end = "AM"
        new_hour += 12

    if days_add > 0 :
        if days_add == 1 :
            days_later = " (next day)"
        else :
            days_later = " (" + str(days_add) + " days later)"
    else :
        days_later = ""

    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if starting_day :
        weeks = days_add // 7
        i = week_days.index(starting_day.lower().capitalize()) + (days_add - 7 * weeks)
        if i > 6 :
            i -= 7
        day = ", " + week_days[i]
    else :
        day = ""
    
    new_time= str(new_hour) + ":" + \
        (str(new_minutes) if new_minutes > 9 else ("0" + str(new_minutes))) + \
        " " + end + day + days_later
    
    return new_time
