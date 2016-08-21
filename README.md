# sparkbot-google  
  
**What it does**  
This project is one of three components making up the Cisco Shipped/Sparkbot demo. This component listens for requests from sparkbot-watcher, then retreives contextually relevant information for a user based on their location and passes it to the sparkbot-flask service. This project requires the sparkbot-google and sparkbot-watcher components to function, and is designed to be containerized and run on the Cisco Shipped platform  
  
**How to Use (With Cisco Shipped)**  
1. Fork the repository, as well as sparkbot-flask and sparkbot-watcher  
2. Configure your Cisco Shipped project to point at the new repository.  
3. In your service configuration, set up the API_KEY environment variable as your Google Maps API key.  
4. In your service configuration, change the Python image to 2.7  
5. Build and deploy your service on shipped.  
  
**How it works**  
1. sparkbot-watcher polls for room messages every two seconds, and then parses them looking for keywords.  
2. If it spots a keyword _in a message that it has not yet seen_, it adds that message to parsed_kw_messages[] and then makes a call to sparkbot-google to get a result.  
3. Upon receiving a request, sparkbot-google finds contextually relevant location data. For demo purposes, a location is hardcoded.  
4. sparkbot-google sends the resulting data to sparkbot-flask, which posts the message to the spark room.  