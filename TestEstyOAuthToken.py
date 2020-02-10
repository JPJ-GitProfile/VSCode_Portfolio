
import webbrowser
import requests
import requests_oauthlib
from requests_oauthlib import OAuth1Session
from requests_oauthlib import OAuth1
from urllib.parse import urlencode

#1) Request Token >> 2) Authorize >> 3) Access Token

# This is the flow. A sample in Python




def requestToken(etsy):
    scope = urlencode({'scope': 'transactions_r transactions_w'})
   # request_token_url = f'https://openapi.etsy.com/v2/oauth/request_token?{scope}'
    #requestTokenResponse = etsy.fetch_request_token("https://openapi.etsy.com/v2/oauth/request_token", realm='listings_r')
   # requestTokenResponse = etsy.fetch_request_token(request_token_url)
    requestTokenResponse = etsy.fetch_request_token("https://openapi.etsy.com/v2/oauth/request_token?scope=profile_w")

    token = requestTokenResponse.get('oauth_token')
    secret = requestTokenResponse.get('oauth_token_secret')
    loginURL = requestTokenResponse.get('login_url')
    
    print ('login url: ' + loginURL + '; token: ' + token + '; secret: ' + secret)

    return (token, secret, loginURL)

def authorize(etsy, token, loginURL):
    authUrl = etsy.authorization_url(loginURL, token)
    print (authUrl)

    #########
    # THIS IS WHERE YOU NEED THE BROWSER. 
    # You visit authUrl and login with your Username and Password. 
    # This will complete Authorization

    return authUrl

def accessToken(etsy, myVerifier):
    accessTokenResponse = etsy.fetch_access_token("https://openapi.etsy.com/v2/oauth/access_token", verifier=myVerifier)

    print (accessTokenResponse) 

    #########
    #accessTokenResponse contains your actual token
    #

etsy = OAuth1Session('mr9qhz59w4mmuvm4ofozkq67', 'lbkjrsl5xx')
(myToken, mySecret, myAuthURL) = requestToken(etsy)
webbrowser.open(myAuthURL)
verifier = input('Paste confirm code:')
accessToken(etsy, verifier)

