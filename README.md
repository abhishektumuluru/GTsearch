
![Imgur Image](https://i.imgur.com/Nx5Z5Y9.png)

GTsearch is a search engine that processes shortcuts in your web browser's search bar to make it much faster and more convenient to access your favorite webpages. Short and simple, easy-to-remember shortcuts redirect you to pages instantly.

Type 'help' and hit enter to see the available list of commands.

#### Easy productivity with search

  - Want quick access to spotify web player? Just type this and hit enter
     > spotify drake
     
    > spot in my feelings
 - Make youtube searching super fast
   > yt lava cake recipe
 - Open messenger
   > msg
 - Open Facebook or Facebook search something really quickly
   > fb
   
   > fb coc registration group
 - GroupMe on web ready to go
   > gr
  - Amazon search
    > am whey protein 
  - Set a timer for X amount of time easily
    > timer 45 min
    
    > timer 90 seconds
  - Want to quickly look up an error on StackOverflow site search? Just type in st and paste your error
    > st IndexError: index out of bounds
  - For the top ranked Google result for StackOverflow, try stl to automatically open the StackOverflow page if there is high confidence in the search result 
    > stl What is the difference between 'git pull' and 'git fetch'?
- Get instant Google Calendar access 
    > cal
- Slack messages
    > sl
    
    > sl myworkspace
- Want to get to your favorite subreddit quickly?
    > r gatech 
    
    > r gatech 1331 professor - to search "1331 professor" in r/gatech
- Stock information on Yahoo! Finance at your fingertips with the dollar symbol
  > $ tsla
- Robinhood and Robinhood Cryto search
  > rh / rhc
  
  > rh nflx / rhc btc
- Perform a Chegg search instantly
  > chegg Discrete Mathematics Rosen
- Wolfram Alpha search engine
  > wa integral of 5x
- Google maps search
  >gmaps sweet hut midtown
- Unix manual
  > man grep
- Google drive
  > drive
- Matlab documentation search
  > mat cumsum
  
  > matlab cumtrapz


# Georgia Tech shortcuts

  - Check out your course schedule? Open GT CourseOff with
    > co
  - Open BuzzPort, T-square, Piazza and Canvas with
    > buzz
    
    >t
    
    > p
    
    >c
  - Quickly access the Stingerette page right before you're leaving the CULC
    > ride
  - Picking between Brittain or North Ave/ Willage and Student Center for lunch?
    > menu
  - Want to check when Fall break is in the Academic calendar?
    > acal
  - Book an appointment for a Flu shot easily with the Patient portal
    > stamps
  - Want to take a break and look at GT memes?
    > gtm
  - Book a study room in the CULC for dead week
    > room


And dozens of other shortcuts
> mf spicy potato soft taco -> Search MyFitnessPal nutrition info for "spicy potato soft taco"

> news -> Google News

> jobs  -> CareerBuzz

> mail -> Georgia Tech mail

> tw kendricklamar -> Twitter @kendricklamar

> w markov decision process -> Wikipedia search for "markov decision process" 

> dw -> DegreeWorks

> def metonym -> Google define search for "metonym"

> syn metonym -> Find synonyms for the word "metonym"

> tiny https://www.youtube.com/watch?v=dQw4w9WgXcQ -> Generate a Tiny url http://tinyurl.com/2fcpre6

## Local setup
Python3
Requirements 
```
pip install wikipedia

pip install Flask
```
```
>>> python main.py

 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 270-902-922
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

#### Chrome
Settings -> Search Engine -> Manage Search Engine -> Add

Enter anything for Search engine and Keyword

For URL, paste http://127.0.0.1:5000/q/?search=%s or whatever IP and port your server is being run on


GTsearch is written in Python and uses the Flask framework for routing. Its logic is trivial: it simply parses search strings and splits by the first whitespace, and the first result token is the command and the rest are optional arguments. 

Pull requests in this repository are very welcome as are feedback/criticiscm/new shortcut suggestions
