# Billboard 100 to Spotify Generator
This Python script generates a Spotify playlist based on the Billboard Hot 100 songs for a specified year. It uses web scraping to extract song names from the Billboard website for a given date and then search for these songs on Spotify to create a personalized playlist.

# Prerequisites
Before running the script, make sure you have the required Python packages installed. 

# Getting Started

1. To create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/

2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
3. Copy the Client ID and Client Secret into the PyCharm Python project after creating a Spotify app.
4. Update the script with your Spotify credentials:
   
    Replace SHOPIFY_CLIENT_ID with your Spotify Client ID.
  
    Replace SHOPIFY_CLIENT_SECRET with your Spotify Client Secret.
5. Run the script:
   
    Execute the script in a Python environment.
    Enter the travel date in the format YYYY-MM-DD when prompted.

    You should see the page below show up automatically (be sure to click Agree):
   
    <img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-29-07-8ba3fc5c277b107461713b02e4258407.png" />

   Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:
   
   <img src="https://img-c.udemycdn.com/redactor/raw/2020-08-12_15-32-02-17be790a8783bf4fdc4eeff77b497044.png" />

   Finally, you need to paste the URL into the prompt in PyCharm. 
   The next time the script is run, authentication will no longer be necessary. Simply enter the date and the script will run.
7. Playlist Creation:

   The script will generate a private Spotify playlist titled <travel_date> Billboard 100.
   It will add tracks to the playlist based on the Billboard Hot 100 songs for the specified year.

Author 
samotop
