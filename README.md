# Example application to query weather conditions from [OpenWeatherMap](http://openweathermap.org/)

To use it:
* Sign up to OpenWeatherMap, you will get APIKEY. When looking at your account details, copy API key to your clipboard.
* Export it as environment variable:

    export APIKEY=your_key_here
    
* Launch app: 

    python main.py

## Testing

To test this application using Hoverfly, export administration endpoint (to import data):

    export HOVERFLY_ADMIN=http://hoverfly-address:8888/
    
and also provide proxy endpoint:
    
    export HOVERFLY=http://hoverfly:8500/
    
Having these variables set, test cases will automagically populate Hoverfly with test data.