# OAuth Notes

https://oauth.net/

## Overview

OAuth stands for Open Authorization.
It’s a process through which an application or website can access private data from another website. It provides applications the
ability for “secure designated access.”

OAuth is a way to get access to protected data from an application. It's safer and more secure than asking users to log in with passwords.

OAuth never shares password data but instead uses authorization tokens to prove an identity between consumers and service providers. OAuth is an authentication protocol that allows you to
approve one application interacting with another on your behalf without giving away your password. [1]

The Authorization Code Grant Type is the most commonly used grant type.

For API developers...

If you're supporting...

    web applications
    mobile applications
    server-side APIs
    mashups


Use OAuth to let application developers securely get access to your users' data without sharing their passwords.

## Getting an Access Token [2]

Your server exchanges the authorization code for an access token by making a POST request to the authorization server's token endpoint:

```
POST https://api.authorization-server.com/token
	grant_type=authorization_code&
	code=AUTH_CODE_HERE&
	redirect_uri=REDIRECT_URI&
	client_id=CLIENT_ID&
	client_secret=CLIENT_SECRET
```

* grant_type=authorization_code - The grant type for this flow is authorization_code
* code=AUTH_CODE_HERE - This is the code you received in the query string
* redirect_uri=REDIRECT_URI - Must be identical to the redirect URI provided in the original link
* client_id=CLIENT_ID - The client ID you received when you first created the application
* client secret=CLIENT_SECRET - Since this request is made from server-side code, the secret is included

The server replies with an access token and expiration time

```
{
	"access_token":"RsT5OjbzRn430zqMLgV3Ia",
	"expires_in":3600
}
```

or if there was an error

```
{
	"error":"invalid_request"
}
```

Security: Note that the service must require apps to pre-register their redirect URIs.


## References
1. [Getting Started with OAuth 2.0](https://blog.loginradius.com/engineering/oauth2/)
2. [OAuth 2 Simplified](https://aaronparecki.com/oauth-2-simplified/)
3. [OAuth](https://oauth.net/)

###
