from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import pandas as pd

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from zomatopy import zomatopy
import json
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
places = [i.strip().lower() for i in config['location']['places'].split(',')]
z_config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
zomato = zomatopy.initialize_app(z_config)
# Check if the place name passed is among the places where Foodie is operating
# Input: place_name: location
# Output: True/False
global email_response
email_response=""
def validate_location(place_name):
	if place_name.lower() in places:
		return True
	else:
		return False
def send_email(email_address):
	gmail_user = 'zomatorestaurantbot@gmail.com'
	part2 = MIMEText(email_response, 'html')
	msg = MIMEMultipart('alternative')
	msg['Subject'] = 'Upgrad Case Study Restaurants Results'
	msg['From'] = gmail_user
	msg['To'] = email_address
	msg.attach(part2)
	print("sending email to",email_address)
	try:
		smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
		smtpserver.ehlo()
		smtpserver.starttls()
		smtpserver.ehlo()
		smtpserver.login(gmail_user, "zomato123")
		smtpserver.sendmail(gmail_user, email_address, msg.as_string())
		smtpserver.close()
		print('Email sent!')
	except Exception as e:
		print('Something went wrong while sending email...')
		print(e)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
	def get_cuisines(self,city_id):
		#location_details = response_json["location_suggestions"][0]
		try:
			#print("Location specified",loc)
			#city_id = zomato.get_city_ID(loc)
			cuisines_dict = zomato.get_cuisines(city_id)
			cuisines_dict = {v.strip().lower(): k for k, v in cuisines_dict.items()}
		except Exception as e:
			cuisines_dict = {'american': 1, 'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73,
							 'south indian': 85}
		return cuisines_dict
	def filter_by_budget(self, results, budget):
		output_df = pd.DataFrame(columns=['name', 'location', 'average_cost_for_two', 'rating'])
		resto_re = {}
		if budget == 'high':
			budg_range = (701, 999999)
			print("finding high budget resto")
		elif budget == 'low':
			budg_range = (1, 299)
			print("finding low budget resto")
		elif budget == 'medium':
			budg_range = (300, 700)
			print("finding medium budget resto")
		else:
			budg_range = (1, 999999)
			print("finding default budget resto")
		print("total number of resto found",len(results))
		for restaurant in results['restaurants']:
			if restaurant['restaurant']['average_cost_for_two'] >= budg_range[0] and restaurant['restaurant']['average_cost_for_two'] <= budg_range[1]:
				print("Found restaurant withing budget", restaurant['restaurant']['name'])
				resto_re['name'] = restaurant['restaurant']['name'].encode('utf-8').decode('ascii')
				resto_re['address'] = restaurant['restaurant']['location']['address'].encode('utf-8').decode('ascii')
				resto_re['average_cost_for_two'] = restaurant['restaurant']['average_cost_for_two']
				resto_re['rating'] = restaurant['restaurant']['user_rating']['aggregate_rating']
				output_df = output_df.append(resto_re, ignore_index=True)
		return output_df.sort_values('rating',ascending=False).head(10)

	def run(self, dispatcher, tracker, domain):

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		checkop = tracker.get_slot('check_op')
		price = tracker.get_slot('price')
		print("check_op",checkop)
		print("price", price)
		global email_response
		if checkop is not None and checkop==True:
			print("Location specified", loc)
			location_detail=zomato.get_location(loc, 1)
			try:
				d1 = json.loads(location_detail)
				lat=d1["location_suggestions"][0]["latitude"]
				lon=d1["location_suggestions"][0]["longitude"]
				city_id = d1["location_suggestions"][0]["city_id"]
				city_name = d1["location_suggestions"][0]["city_name"]
				print("city_name found in zomato response",city_name)
				print("city_id found in zomato response", city_id)
				cuisines_dict = self.get_cuisines(city_id)
				results=zomato.restaurant_search_new("", lat, lon, str(cuisines_dict.get(cuisine.strip().lower())), 1000)
				d = json.loads(results)
				df = self.filter_by_budget(d,price)
				response="Found "
				email_response = "We found the below Top 10 restuarants according to your choice, Enjoy eating!! <br><br> <table><tr><th>Restaurant Name</th><th>Restaurant locality address</th><th>Average budget for two people</th><th>Zomato user rating</th></tr>"
				if df.size==0:
					response= "no results"
				else:
					for index,restaurant in df.iterrows():
						if index<5:
							response=response+ "\n"+ restaurant['name']+ " in "+ restaurant['address']+ " has been rated "+str(restaurant['rating'])+"\n"
						email_response = email_response + "<tr><td>"+restaurant['name']+ " </td><td> "+ restaurant['address'] \
										 + " </td><td> "+str(restaurant['average_cost_for_two'])+ " </td><td>" + str(restaurant['rating'])+ "</td></tr>"
				dispatcher.utter_message(response)
				email_response = email_response +"</table>"
				return [SlotSet('location',loc),SlotSet('email_response',email_response)]
			except Exception as e:
				import traceback
				traceback.print_exc()
				dispatcher.utter_message("Sorry, we did not find any restaurant in the specified location,"+loc)
				return []
		else:
			dispatcher.utter_message("We do not operate in that area yet")
			return [SlotSet('check_op', False)]

class CheckLocation(Action):
	def name(self):
		return 'check_location'
		
	def run(self, dispatcher, tracker, domain):

		loc = tracker.get_slot('location')
		if validate_location(loc):
			return [SlotSet('check_op',True)]
		else:
			return [SlotSet('check_op',False)]

class SendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		mail = tracker.get_slot('email')
		send_email(mail)
		print('sending email...',mail)
		return []