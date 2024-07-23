# AIRCRAFT on-board computer AIRBUS A320-200 FMS

import math
import random
from geopy.distance import great_circle
from datetime import datetime

#READ TIME
current_datetime=datetime
day=current_datetime.day
year=current_datetime.year


page=1
def layout():
    global page
    #NUMBER OF PAGE AND NAME OF AIRPLANE
    print("          ----------------AIRBUS A320 A320-200 FMS----------------")
    print("page ", page)
    page=page+1

    #FUNCTION TO READ GEOGRAPHICAL COORDINATES
move='false'
def read_coordinates(airport_A,airport_B,airport_C):
    global distance
    global alt_distance
    global move
    coordinates_dict = {
        "KRK": (50.0461, 19.9423),  # Kraków, Poland - John Paul II International Airport Kraków-Balice
        "WAW": (52.1657, 20.9675),  # Warsaw, Poland - Warsaw Chopin Airport
        "NCE": (43.6653, 7.2154),  # Nice, France - Nice Côte d'Azur Airport
        "CDG": (49.0097, 2.5479),  # Paris, France - Charles de Gaulle Airport
        "FCO": (41.8003, 12.2389),  # Rome, Italy - Leonardo da Vinci–Fiumicino Airport
        "VIE": (48.1103, 16.5697),  # Vienna, Austria - Vienna International Airport
        "PRG": (50.1008, 14.2632),  # Prague, Czech Republic - Václav Havel Airport Prague
        "ZRH": (47.4647, 8.5492),  # Zurich, Switzerland - Zurich Airport
        "AMS": (52.3105, 4.7683),  # Amsterdam, Netherlands - Amsterdam Airport Schiphol
        "FRA": (50.0379, 8.5622),  # Frankfurt, Germany - Frankfurt Airport
        "MUC": (48.3538, 11.7861),  # Munich, Germany - Munich Airport
        "BCN": (41.2974, 2.0833),  # Barcelona, Spain - Barcelona-El Prat Airport
        "MAD": (40.4917, -3.5695),  # Madrid, Spain - Adolfo Suárez Madrid-Barajas Airport
        "LIS": (38.7742, -9.1355),  # Lisbon, Portugal - Humberto Delgado Airport
        "ATH": (37.9364, 23.9445),  # Athens, Greece - Athens International Airport
        "BRU": (50.9010, 4.4844),  # Brussels, Belgium - Brussels Airport
        "DUB": (53.4213, -6.2701),  # Dublin, Ireland - Dublin Airport
        "CPT": (-33.9692, 18.5975),  # Cape Town, South Africa - Cape Town International Airport
        "LED": (59.7999, 30.2625),  # Saint Petersburg, Russia - Pulkovo Airport
        "HEL": (60.3172, 24.9633),  # Helsinki, Finland - Helsinki-Vantaa Airport
        "OSL": (60.1975, 11.1004),  # Oslo, Norway - Oslo Gardermoen Airport
        "SVO": (55.9726, 37.4146),  # Moscow, Russia - Sheremetyevo International Airport
        "IST": (41.2753, 28.7519),  # Istanbul, Turkey - Istanbul Airport
        "SOF": (42.6949, 23.3930),  # Sofia, Bulgaria - Sofia Airport
        "BUD": (47.4333, 19.2619),  # Budapest, Hungary - Budapest Ferenc Liszt International Airport
        "VNO": (54.6367, 25.2878),  # Vilnius, Lithuania - Vilnius Airport
        "RIX": (56.9236, 23.9710),  # Riga, Latvia - Riga International Airport
        "TIA": (41.4147, 19.7206),  # Tirana, Albania - Tirana International Airport
        "SKG": (40.5197, 22.9706),  # Thessaloniki, Greece - Thessaloniki Airport
        "ARN": (59.6519, 17.9186),  # Stockholm, Sweden - Stockholm Arlanda Airport
        "CPH": (55.6179, 12.6554),  # Copenhagen, Denmark - Copenhagen Airport
        "TXL": (52.5597, 13.2877),  # Berlin, Germany - Berlin Tegel Airport
        "DUS": (51.2895, 6.7668),  # Düsseldorf, Germany - Düsseldorf Airport
        "MRS": (43.4396, 5.2218),  # Marseille, France - Marseille Provence Airport
        "NAP": (40.8846, 14.2908),  # Naples, Italy - Naples International Airport
        "GVA": (46.2381, 6.1089),  # Geneva, Switzerland - Geneva Airport
        "LJU": (46.2266, 14.4550),  # Ljubljana, Slovenia - Ljubljana Jože Pučnik Airport
        "BEG": (44.8194, 20.3072),  # Belgrade, Serbia - Belgrade Nikola Tesla Airport
        "OTP": (44.5711, 26.0850),  # Bucharest, Romania - Henri Coandă International Airport
        "ZAG": (45.7429, 16.0682),  # Zagreb, Croatia - Franjo Tuđman Airport
        "TLL": (59.4133, 24.8325),  # Tallinn, Estonia - Tallinn Airport
        "GOT": (57.6628, 12.2797),  # Gothenburg, Sweden - Gothenburg Landvetter Airport
        "EDI": (55.9508, -3.3615),  # Edinburgh, Scotland - Edinburgh Airport
        "BRS": (51.3836, -2.7184),  # Bristol, England - Bristol Airport
        "LGW": (51.1537, -0.1821),  # London, England - Gatwick Airport
        "BHX": (52.4525, -1.7435),  # Birmingham, England - Birmingham Airport
        "LHR": (51.4700, -0.4543),  # London, England - London Heathrow Airport
        "MAN": (53.3650, -2.2728),  # Manchester, England - Manchester Airport
    }

    if airport_A in coordinates_dict and airport_B in coordinates_dict and airport_C in coordinates_dict:
        coord1 = coordinates_dict[airport_A]
        coord2 = coordinates_dict[airport_B]
        coord3 = coordinates_dict[airport_C]
        # calculating the distance between airports
        distance = great_circle(coord1, coord2).kilometers
        alt_distance = great_circle(coord2, coord3).kilometers
        move='true'
    else:
        print("ERROR: AIRPORT CODE IS INVALID---TRY AGAIN---")
        move='false'

#function to calculate the mass of fuel
def fuel_mass(distance):
    #fuel_consumption_per_km=3.8
    litres_of_fuel=distance*3.8
    mass_of_fuel=litres_of_fuel*0.8
    return mass_of_fuel
#function to READ airlines_codes
airline_name="blabla"
move2='false'
def airlines_codes(flight_number):
    global airline_name
    global move2
    first_3_letters=flight_number[0:3]
    airlines_icao = {
        "LOT": "LOT Polish Airlines",
        "WZZ": "Wizz Air",
        "DLH": "Lufthansa",
        "AFR": "Air France",
        "BAW": "British Airways",
        "AZA": "Alitalia",
        "SAS": "SAS Scandinavian Airlines",
        "KLM": "KLM Royal Dutch Airlines",
        "EIN": "Aer Lingus",
        "IBE": "Iberia"
    }
    if first_3_letters in airlines_icao:
        airline_name = airlines_icao[first_3_letters]
        move2 = 'true'
    else:
        print("ERROR: AIRLINE CODE IS INVALID---TRY AGAIN---")

#page1
layout()
print("--FLIGHT INIT--")

while move2 =='false':
    flight_number=input("FLIGHT NBR: ").upper()
    airlines_codes(flight_number)

#the pilot must enter the airport from which he departs, to which he flies and an alternative airport for landing. Additionaly he must to enter tempereture on airport he/she is right now.
while move=='false':
    airport_A=input("FROM: ").upper()
    airport_B=input("TO: ").upper()
    airport_C=input("ALT: ").upper()
    read_coordinates(airport_A, airport_B, airport_C)


#cruise flight level (feets) (FL360=36000 feets)
move3='false'
while move3=='false':
    flight_level=int(input("CRZ/FL: "))
    if flight_level==300 or flight_level==320 or flight_level==340 or flight_level==360 or flight_level==380 or flight_level==400:
        move3='true'
    else:
        print("ERROR: FLIGHT CODE MUST BE 300 or 320 or 340 or 360 or 380 or 400 ---TRY AGAIN---")


#degrees Celsius are the standard
temperature=int(input("TEMP: "))

#page2
layout()
print("--PAYLOAD--")

#PAX is number of passengers
move3='false'
while move3=='false':
    pax=int(input("PAX: "))
    if(pax>=20 and pax<181):
        move3 = 'true'

    else:
        print("ERROR: PAX MUST BE BETWEEN (20-180)---TRY AGAIN---")

#extra fuel in kilograms
move3='false'
while move3=='false':
    extra=int(input("EXTRA: "))
    if(extra>=0 and extra<=500):
        move3 = 'true'
    else:
        print("ERROR: EXTRA (MIN 0 MAX 500)---TRY AGAIN---)")

move3='false'
while move3=='false':
    TAXI=int(input("TAXI:")) #fuel for plane taxiing
    if(TAXI>=50 and TAXI<=200):
        move3='true'
    else:
        print("ERROR: TAXI (MIN 50 MAX 200)---TRY AGAIN---")


TRIP_FUEL=fuel_mass(distance)
alt_fuel=fuel_mass(alt_distance)
MIN_T_OFF_FUEL=TRIP_FUEL+605.0+alt_fuel
T_OFF_FUEL=extra+MIN_T_OFF_FUEL+TAXI
passengers_weight=pax*84
TOW=45700+ T_OFF_FUEL +passengers_weight #TOW- TAKE OFF WEIGHT (FINAL)

#page3
layout()
print("--TAKE OFF PERFORMANCE--")
#pilot must enter the flaps settings
flaps=input("FLAPS(1+F/2): ").upper()
#lenght of runway in meters
move3='false'
while move3=='false':
    length_runway=int(input("RNW/L: "))
    if length_runway>999 and length_runway<6251:
        move3='true'
    else:
        print("ERROR: LENGTH OF RUNWAY MIN 1000 MAX 6250")
#conditions of runway (WET/DRY)
conditions=input("RNW/COND: ").upper()
#v1,vr,v2 - different speeds for take off

#cases for various TOW
if TOW < 47850:
    v1 = 122
    vr = 122
    v2 = 127

elif 47850 <= TOW < 52500:
    v1 = 122
    vr = 122
    v2 = 132

elif 52500 <= TOW < 57500:
    v1 = 126
    vr = 126
    v2 = 137

elif 57500 <= TOW < 62500:
    v1 = 130
    vr = 131
    v2 = 142

elif 62500 <= TOW < 67500:
    v1 = 134
    vr = 135
    v2 = 148

else: #TOW >= 67500
    v1 = 138
    vr = 140
    v2 = 153

#if flaps == 2 , we have to change speeds
if(flaps=="2"):
    v1=0.9*v1
    vr=0.97*vr
    v2=0.92*v2
#depends if runway is WET or DRY
if(conditions=="WET"):
    v1=0.9*v1
    vr=0.96*vr
    v2=0.92*v2

#depend of lenght of runway we have to change speeds

if length_runway < 2250:
    v1 = v1 - 1
    vr = vr - 1

elif 2750 <= length_runway < 3250:
    v1 = v1 + 1
    vr = vr + 1

elif 3250 <= length_runway < 3750:
    v1 = v1 + 2
    vr = vr + 2

elif 3750 <= length_runway < 4250:
    v1 = v1 + 3
    vr = vr + 3

elif 4250 <= length_runway < 4750:
    v1 = v1 + 4
    vr = vr + 4

elif 4750 <= length_runway < 5250:
    v1 = v1 + 5
    vr = vr + 5

elif 5250 <= length_runway < 5750:
    v1 = v1 + 6
    vr = vr + 6

elif 5750 <= length_runway <= 6250:
    v1 = v1 + 7
    vr = vr + 7
#page4
print("----------------")
name_of_pilot=input("PIC (PILOT IN COMMAND) NAME: ")


#FLIGHT PLAN
print("\n")
print("\n")
print("----------------AIRBUS A320 A320-200 FMS----------------")
print("FLIGHT PLAN")
print("----------------")
print(flight_number," ",airport_A," ",airport_B)
print(airline_name)
print("A320-200 / CFM56-5B4\n") #airplane and engine model
print("MAXIMUM    TOW ", 78000," LAW ",66000, " ZFW ",62500)
print("ESTIMATED   TOW ", int(TOW)," LAW ",int(TOW-TRIP_FUEL), " ZFW ",int(passengers_weight+45700)) #Take-Off Weight/ Landing Weight/ Zero-Fuel Weight
print("----------------")
wind1=random.randint(40, 250)
wind2=random.randint(20, 70)
print("----------------")
print("AVG WIND: ",wind1,"/",wind2)
print("----------------")
print("    PLANNED FUEL")
print("----------------")
print("    FUEL/TIME  ")
print("----------------")
time=distance/14
alt_time=alt_distance/14
print("TRIP:    ",int(TRIP_FUEL+alt_fuel),"/", int(time))
print("----------------")
print("CONT 15 MIN:  605/0015 ")   #extra 15 minutes
print("----------------")
print("ALT:  ",int(alt_fuel)," ",extra)
print("----------------")
print("MINIMUM T/OFF FUEL:    ",int(605+TRIP_FUEL+alt_fuel)," ",int(15+time+alt_time))
print("----------------")
print("EXTRA:    ", int(extra))
print("T/OFF FUEL:   ",int(extra+605+TRIP_FUEL+alt_fuel))
print("----------------")
print("TAXI:    ", int(TAXI))
print("----------------")
print("BLOCK FUEL:    ",int(TAXI+extra+605+TRIP_FUEL+alt_fuel))
print("----------------")
print("ROUTING")
print("----------------")
first_runway=random.randint(1,10)
second_runway=random.randint(1,10)
print(airport_A,"/",first_runway,"  ","FL "," ",flight_level," ",airport_B,"/",second_runway) #it generates random number for runway
print("----------------")
print("DEPARTURE")
print("----------------")
print(airport_A,"/",first_runway, " RNW ",conditions )
print("WIND ",random.randint(40, 250),"/",random.randint(20, 70))
print("----------------")
print("ARRIVAL")
print("----------------")
print(airport_B,"/",second_runway, " RNW ",conditions )
print("----------------")
print("T/OFF SPEEDS")
print("----------------")
print("V1:    ",round(v1,2))
print("VR:    ",round(vr,2))
print("V2:    ",round(v2,2))
print("----------------")
print("I HEREWITH CONFIRM THAT I HAVE PERFORMED A")
print("THOROUGH SELF BRIEFING ABOUT THE DESTINATION")
print("AND ALTERNATE AIRPORTS OF THIS FLIGHT")
print("INCLUDING THE APPLICABLE INSTRUMENT APPROACH")
print("PROCEDURES, AIRPORT FACILITIES, NOTAMS AND")
print("ALL OTHER RELEVANT PARTICULAR INFORMATION.")
print("PIC NAME: ",name_of_pilot)
print("----------------")
PIC_SIGNATURE=input("PIC SIGNATURE:    ")
print("----------------")
print("HAVE A SAFE FLIGHT !")
print("----------------")



