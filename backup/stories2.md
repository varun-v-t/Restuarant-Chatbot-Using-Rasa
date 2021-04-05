## complete + happy path
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
    - utter_goodbye
    - export

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

## location specified
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
* affirm{"check_op":true}
    - utter_goodbye
    - export
    
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
    
## first price and then valid location specified
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
* goodbye
    - utter_goodbye
    - export
        
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
    
## complete path location specified valid city delhi cusine north indian
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
    - utter_goodbye

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
* goodbye
    - utter_goodbye

## complete path location specified valid city delhi
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
* restaurant_search{"price": "medium"}
    - slot{"price": "medium"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export

## complete path location first price , then cuisine and location specified
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
    - export
    
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
* stop

## complete path location first price and cuisine, then valid location specified
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
    - export
* stop

## complete path location first price and location, then cuisine  specified
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
    - export

## complete path price and location and cuisine specified
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - export
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
* stop

## complete path location first price and valid location and cuisine specified
* greet
    - utter_greet
* restaurant_search{"price": "medium","location": "delhi","cuisine": "chinese"}
    - slot{"price": "medium"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - check_location
    - slot{"check_op":true}
    - action_search_restaurants
    - export
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
* stop
     
## interactive_story_1 location specified valid city
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
* stop

## interactive_story_3 complete italian cusine
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

## interactive_story_4 cuisine and location specified
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
* affirm
    - utter_goodbye

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
    
## happy_path cuisine and valid location specified
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
* affirm
    - utter_goodbye


## interactive_story_6 first cusine and then location
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
* affirm
    - utter_goodbye
    
## interactive_story_6 first price, cusine and then valid location
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
* affirm
    - utter_goodbye

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
    - export
* stop

## interactive_story_7 first cuisine and then location
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - check_location
    - slot{"check_op":false}
    - utter_donot_operate
* affirm
    - utter_goodbye

## interactive_story_8 first invalid location and then valid location
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
    - slot{"location": "mumbai"}
* goodbye
    - utter_goodbye

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
    - slot{"location": "ahmedabad"}
* goodbye
    - utter_goodbye
    
## interactive story
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
* affirm
    - utter_goodbye


