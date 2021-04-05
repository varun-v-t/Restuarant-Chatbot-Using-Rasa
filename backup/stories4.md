## complete + happy path + send email 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email 
* affirm
    - utter_ask_email_address
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart
  
## complete + happy path + do not send email 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email 

* deny
    - utter_goodbye
    - export
    - action_restart

## complete path + invalid location
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* goodbye
    - utter_goodbye
    - export
    - action_restart

## location specified + send email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart

## location specified + do not send email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart


    
## first price and then invalid location specified
* greet
    - utter_greet
* restaurant_search{"price":"medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* goodbye
    - utter_goodbye
    - export
    - action_restart
    
## first price and then valid location specified + send email
* greet
    - utter_greet
* restaurant_search{"price":"medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
  
* goodbye
    - utter_goodbye
    - export
    - action_restart

## first price and then valid location specified + do not  send email
* greet
    - utter_greet
* restaurant_search{"price":"medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart
  
        
## location specified in tier3 at start
* greet
    - utter_greet
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* goodbye
    - utter_goodbye
    - export
    - action_restart
    
## complete path location specified valid city delhi cusine north indian + send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian","check_op":true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email

* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart

## complete path location specified valid city delhi cusine north indian + do not send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian","check_op":true}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price":"high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart


## complete path location specified valid city italy
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
    - check_location
    - slot{"check_op":true}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price":"low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - utter_ask_email
  
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart

## complete path location specified valid city delhi + send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export  
    - action_restart


## complete path location specified valid city delhi + do not send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart
  


## complete path location first price , then cuisine and location specified + send email
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "delhi","cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export  
    - action_restart

## complete path location first price , then cuisine and location specified + do not send email
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "delhi","cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart


    
## complete path location first price , then cuisine and invalid location specified
* greet
    - utter_greet
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - utter_ask_location
* restaurant_search{"location": "mirzapur","cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
    - export
    - action_restart
* stop

## complete path location first price and cuisine, then invalid location specified
* greet
    - utter_greet
* restaurant_search{"price": "medium","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "honnnali"}
    - slot{"location": "honnnali"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
    - export
    - action_restart
* stop

## complete path location first price and cuisine, then valid location specified + send email
* greet
    - utter_greet
* restaurant_search{"price": "low","cuisine": "chinese"}
    - slot{"price": "low"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart
* stop

## complete path location first price and cuisine, then valid location specified + do not send email
* greet
    - utter_greet
* restaurant_search{"price": "low","cuisine": "chinese"}
    - slot{"price": "low"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart
* stop


## complete path location first price and location, then cuisine  specified + send email
* greet
    - utter_greet
* restaurant_search{"price": "high","location": "delhi"}
    - slot{"price": "high"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export  
    - action_restart

## complete path location first price and location, then cuisine  specified + do not send email
* greet
    - utter_greet
* restaurant_search{"price": "high","location": "delhi"}
    - slot{"price": "high"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - utter_ask_email 
* deny 
    - utter_goodbye
    - export
    - action_restart
  


## complete path price and location and cuisine specified + send email
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email  
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart
* stop

## complete path price and location and cuisine specified + do not send email
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email  
* deny
    - utter_goodbye
    - action_restart
* stop


## complete path location first price and invalid location and cuisine specified
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "honnali","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "honnali"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
    - export
    - action_restart
* stop

## complete path location first price and valid location and cuisine specified + send email
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart
* stop

## complete path location first price and valid location and cuisine specified + do not send email
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart
* stop



## complete path location first price and invalid location
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "mirzapur"}
    - slot{"price": "medium"}
    - slot{"location": "mirzapur"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
    - action_restart
* stop
     
## interactive_story_1 location specified valid city + send email
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export 
    - action_restart
* stop


## interactive_story_1 location specified valid city + do not send email
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart
* stop



## interactive_story_2 location specified invalid city
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* goodbye
    - utter_goodbye
    - action_restart
* stop

## interactive_story_3 complete italian cusine + send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian","check_op":true}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart

## interactive_story_3 complete italian cusine + do not send email
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian","check_op":true}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email 
* deny
    - utter_goodbye
    - export
    - action_restart


## interactive_story_4 cuisine and location specified + send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart

## interactive_story_4 cuisine and location specified + send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "low","check_op":true}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email 
* deny
    - utter_goodbye
    - export
    - action_restart

## interactive_story_5 cuisine and invalid location specified
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* affirm
    - utter_goodbye  
    - action_restart
    
## happy_path cuisine and valid location specified + send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "medium","check_op":true}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart


## happy_path cuisine and valid location specified + do not send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "medium","check_op":true}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email 
* deny
    - utter_goodbye
    - export  
    - action_restart



## interactive_story_6 first cusine and then location + send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "medium","check_op":true}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - export
    - action_restart
  
## interactive_story_6 first cusine and then location + do not send email
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_price
* restaurant_search{"price": "medium","check_op":true}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* deny
    - utter_goodbye
    - export
    - action_restart


## interactive_story_6 first price, cusine and then valid location + email
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
  

## interactive_story_6 first price, cusine and then valid location + do not email
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese","check_op":true}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email 
* deny
    - utter_goodbye
    - action_restart


## interactive_story_6 first price, cusine and then invalid location
* greet
    - utter_greet
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
    - action_restart
* stop

## interactive_story_7 first cuisine and then location
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_8 first invalid location and then valid location + email
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "calcutta"}
    - slot{"location": "calcutta"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian","check_op":true}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_8 first invalid location and then valid location + do not send email
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "calcutta"}
    - slot{"location": "calcutta"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian","check_op":true}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart



## interactive_story_9 first invalid location then again invalid location and then valid loca
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "thuminakatti"}
    - slot{"location": "thuminakatti"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "ahmedabad","cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "ahmedabad"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email 
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - action_restart  

## interactive_story_9 first invalid location then again invalid location, then valid + no email
* restaurant_search{"location": "honnali"}
    - slot{"location": "honnali"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "thuminakatti"}
    - slot{"location": "thuminakatti"}
    - check_location
    - slot{"check_op": false}
    - utter_donot_operate
* restaurant_search{"location": "ahmedabad","cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "ahmedabad"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_price
* restaurant_search{"price": "high"}
    - slot{"price": "high"}
    - action_search_restaurants
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart


    
## interactive story + send email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
    - slot{"price": "low"}
    - action_search_restaurants  
    - utter_ask_email
* affirm
    - utter_ask_email_address
  
* email_response{"email":"abc@google.com"}
    - slot{"email":"abc@google.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive story + do not send email
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
    - slot{"price": "low"}
    - action_search_restaurants  
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart  

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - slot{"email_response": "We found the below Top 10 restuarants according to your choice, Enjoy eating!! <br><br> <table><tr><th>Restaurant Name</th><th>Restaurant locality address</th><th>Average budget for two people</th><th>Zomato user rating</th></tr><tr><td>Saravana Bhavan </td><td> P-13, Connaught Circus, Connaught Place, New Delhi </td><td> 500 </td><td>4.6</td></tr><tr><td>Carnatic Cafe </td><td> 84-85, Meharchand Market, Lodhi Road, Lodhi Colony, New Delhi </td><td> 600 </td><td>4.5</td></tr><tr><td>Saravana Bhavan </td><td> 50, Atul Grove Road, Janpath, New Delhi </td><td> 500 </td><td>4.5</td></tr><tr><td>Karnataka Food Centre </td><td> Delhi Karnataka Sangha Building, Rao Tula Ram Marg, Sector 12, R K Puram, New Delhi </td><td> 450 </td><td>4.4</td></tr><tr><td>Naivedyam </td><td> Shop 1, Hauz Khas Village, New Delhi </td><td> 500 </td><td>4.4</td></tr><tr><td>Carnatic Cafe </td><td> M-21, M Block Market, Greater Kailash (GK) 2, New Delhi </td><td> 600 </td><td>4.4</td></tr><tr><td>Carnatic Cafe </td><td> Unit 4, Ground Floor, 32nd Milestone, Sector 15, Gurgaon </td><td> 600 </td><td>4.4</td></tr><tr><td>Naivedyam </td><td> H-1A/17, 1st Floor, Near Fortis Hospital, Sector 63, Noida </td><td> 600 </td><td>4.3</td></tr><tr><td>Naivedyam </td><td> F-12, Main Road, Kalkaji, New Delhi </td><td> 600 </td><td>4.3</td></tr><tr><td>Naivedyam </td><td> 2nd Floor, Vipul Square, B Block, Sushant Lok, Gurgaon </td><td> 600 </td><td>4.2</td></tr></table>"}
    - utter_ask_email
* deny
    - utter_goodbye
    - action_restart
