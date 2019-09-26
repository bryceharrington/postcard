from requests_oauthlib import OAuth1Session

# The Trello API supports basic OAuth 1.0; you can use an OAuth library and the following URLs:
#
# https://trello.com/1/OAuthGetRequestToken
# https://trello.com/1/OAuthAuthorizeToken
# https://trello.com/1/OAuthGetAccessToken

def get_access_token(api_key, api_secret, scope, app_name):
    # Get the request token
    session = OAuth1Session(client_key=api_key, client_secret=api_secret)
    response = session.fetch_request_token('https://trello.com/1/OAuthGetRequestToken')
    token_key = response.get('oauth_token')
    token_secret = response.get('oauth_token_secret')

    # Redirect to Trello.com for OAuth token
    print("Open this link in your browser to authorize access to your Trello board:\n")
    print("%s?oauth_token=%s&scope=read,write&expiration=30days&name=%s" %(
        "https://trello.com/1/OAuthAuthorizeToken",
        token_key,
        app_name,
        ))

    # Read the verification code from the user
    reading = True
    while reading:
        try:
            code = input('\n\nEnter the verification code from Trello:\n')
            reading = False
        except:
            print('Invalid entry')
            reading = True

    # Get the access token for the user
    session = OAuth1Session(
        client_key=api_key,
        client_secret=api_secret,
        resource_owner_key=token_key,
        resource_owner_secret=token_secret,
        verifier=code)
    return session.fetch_access_token('https://trello.com/1/OAuthGetAccessToken')
