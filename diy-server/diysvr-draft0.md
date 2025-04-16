# diysvr-draft0.md  

## DIY Token Server Article Notes  

This article is intended as a basic tutorial on how authorization tokens are used in REST APIs. To model the authorization flow, I will use JavaScript to create a simple token server to demonstrate the flow.  

In this article, you will learn how to create a token server in JavaScript. The token server will be a local http server that will send a token to a client-side REST API.  

## Cloud APIs  

Many cloud-based applications today use REST APIs [DIYSVR-11] to authenticate user identities and control access. Authentication and authorization protocols are required to ensure that data and privacy security. Authentication focuses on verifying identity, while authorization focuses on access to resources. This article focuses on authorization, however, it is worth taking a moment to how authentication and authorization work together as complementary security processes.  

Cloud applications typically require a login and password to access private resources like secure databases. If you deploy multiple applications to access your databases, you use your login ID and password for each application.  Authentication servers are responsible for verifying your identity. They don’t automatically authorize permission to access your database. That is the role of an authorization server.  

In an authorization flow, your authorization server checks with your authentication server to verify your identity before granting database access. That verification is frequently done with authentication tokens.

In this article, you will learn about the principles of token servers with code snippets of a simple JavaScript token server.  

## Authorization tokens  

Security is a critical issue in cloud computing. It is necessary to ensure two critical factors when accessing resources. Those factors are: identity and permission. Identity is confirmed by authentication servers. Permission is confirmed by authorization servers. Authorization servers grant permissions via tokens.  

Authorization tokens specify which resources the web application can access, what read, write, and execute permissions are allowed.  Authentication servers typically send JSON web tokens to you, which you then send to your authentication server.  

The OAuth authentication protocol allows you to approve one application interacting with another on your behalf without exposing your password.  

OpenID Connect authentication functionality is built on top of the  OAuth 2.0 protocol.  

## Single sign-on  

Cloud computing has given rise to a proliferation of web applications that require users to create IDs and passwords for each. Single sign-on (SSO) providers offer a solution to this dilemma. SSO technology allows the user to establish their identity via sign-on (login and password), then enable registered apps to verified the user's identity with the SSO provider. The user is not required to create a new sign-on with each app. Instead, the authorization server returns a token that the application uses to access the user's resources.  

Based on  OAuth 2.0, OpenID Connect is a protocol standard that enables SSO providers to offer authentication and authorization services for cloud applications. It is used by many SSO providers, including names like Apple, Google, and Microsoft.  

## Authorization flow demonstration code  

We can create a local server model of an authentication server response to a user request for a token, then  



Below is an example of a simple token server implemented in JavaScript code. This code will simulate the client application flow.  

**Objective:** Set up nodejs as a token server that can be called from a browser.  

* Set up nodejs server to serve token then use token for a REST API  
* Token will be passed to browser as a variable in localStorage  

## The process  

* Create nodejs server “tkserver.js”.  
* Put token in secret file.  
* Browser requests token from server.  
* Browser uses token for another API.  

```

## Source ENV variable  


# Script name: token-setup.src
# This script sets and exports a token value in an ENV variable.
# Source the scripts from the command line.
# Import the ENV var into JS with the process.env.VARIABLE_NAME property.

myToken=myCode123xyz
export myToken
```


Run server  

`node token_server.js`  

```
http.createServer(function (request, response) {
    // Send the HTTP header
    // HTTP Status: 200 : OK
    // Content Type: text/plain
    // 'Access-Control-Allow-Origin': 'http://127.0.0.1:8081/'
    response.writeHead(200, {
        'Content-Type': 'text/plain', 
        'Origin': 'http://127.0.0.1:8081/',
        'Access-Control-Allow-Origin': '*',
        'Vary': 'Origin'
    });
    response.end(jsonStr);
}).listen(8081);
```


## Fetch token  

```
async function postBlob() {
  const url = "http://localhost:8081/"; 
  // Access requires local token server header {'Access-Control-Allow-Origin': '*'}

  console.log('Running getToken()');

  try {
    const response = await fetch(url); // No header
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const jsonResp = await response.json();
    var myKey = jsonResp.myKey;
    var bearer_auth = 'Bearer ' + myKey

  } catch (error) {
    console.error(error.message);
  }

```

(Insert image of result in console.)  

## Conclusion  

JSON web tokens offer a secure way to manage access authorization over a REST API. Our JavaScript code snippets demonstrate a client authorization flow where a local authentication server responds to a fetch request for a token.  

Delivering tokens by SSO providers benefits both users and developers. Users are relieved of the burden of sending login IDs and passwords to multiple applications without compromising security. Developers are relieved of the security risks associated with managing and storing IDs and passwords for multiple accounts.  

# Background  

## DIY Token Server Article Notes  

This article is intended as a basic tutorial on how authorization tokens are used in REST APIs. To model the authorization flow, I will use JavaScript to create a simple token server to demonstrate the flow.  

In this article, you will learn how to create a token server in JavaScript. The token server will be a local http server that will send a token to a client-side REST API.  

## Key points  

* Secure access to tokens and passwords  
* Automate the entry process  
* Tutorial on 3rd party authorization  
* JavaScript implementation  
* Experiment with creating a narrative of a specific “application scenario”

## Outline  

* Why?  
  * API token security  
  * Control access  
  * Current solutions?  
    * 3rd party  
* What?  
  * Authorization server  
  * Similar solution, OAuth 2  
  * Reference HubSpot REST API article  
* How?  
  * ￼￼Client-server model implementation  
  * Write server code in JS  
  * Write fetch code in JS  
* Show me  
  * JS server code  
  * JS app fetch code  
  * Output results to console  
* Conclusion?  
  * Keep API JWTs secure  
  * Automate JWT entry  

## Why is this important  

Many web-based applications today use REST APIs [DIYSVR-11] to authenticate user identities and control access. Authentication and authorization protocols are required to ensure that data and privacy security. This article will focus on authorization.  

One of the more popular authentication protocols is OAuth 2, which allows secure authorization in a simple and standard method from web, mobile and desktop applications.  

There are a variety of methods used to prove authority. Tokens are the most common.  

In this article, you will learn about the principles of token servers with code snippets of a simple JavaScript token server.  


## What is authorization?  

OAuth stands for Open Authorization.

It’s a process through which an application or website can access private data from another website. It provides applications the ability for “secure designated access.”   

The Authorization Code Grant Type is the most commonly used grant type.  

For API developers...  

If you're supporting...  

* web applications  
* mobile applications  
* server-side APIs  
* mashups  

## DigitalOcean authorization steps  

There are 4 parties involved and 3 exchanges that take place.  

* Client and resource owner  
  * Client requests authorization from resource owner   
  * Resource owner sends authorization grant code to client
* Client and authorization server exchange  
  * Client sends authorization grant code to authorization server  
  * Authorization server sends access token to client  
* Client and resource server exchange  
  * Client sends token to resource server  
  * Resource server sends requested resource to client  

DigitalOcean references: [DIYSVR-8]  

## DigitalOcean app registration  

* Name  
* Homepage URL  
* Description  
* Callback URL  

## Application scenario  

* Manage my music database  

## Benefits  

* Get access to protected data from an application.  
* Safer and more secure than asking users to log in with passwords.  
* Never shares password data  
* Uses authorization tokens to prove an identity between consumers and service providers.  
* Allows you to approve one application interacting with another on your behalf without giving away your password.  

## Getting an Access Token [DIYSVR-2]  
Your server exchanges the authorization code for an access token by making a POST request to the authorization server's token endpoint:  

```
POST https://api.authorization-server.com/token
	grant_type=authorization_code&
	code=AUTH_CODE_HERE&
	redirect_uri=REDIRECT_URI&
	client_id=CLIENT_ID&
	client_secret=CLIENT_SECRET
```

## Example  

Below is an example of a simple token server implemented in JavaScript code. This code will simulate the client application flow.  

**Objective:** Set up nodejs as a token server that can be called from a browser.  

* Set up nodejs server to serve token then use token for a REST API  
* Token will be passed to browser as a variable in localStorage  

## The process  

* Create nodejs server “tkserver.js”.  
* Put token in secret file.  
* Browser requests token from server.  
* Browser uses token for another API.  

```

## Source ENV variable  


# Script name: token-setup.src
# This script sets and exports a token value in an ENV variable.
# Source the scripts from the command line.
# Import the ENV var into JS with the process.env.VARIABLE_NAME property.

myToken=myCode123xyz
export myToken
```


Run server  

`node token_server.js`  

```
http.createServer(function (request, response) {
    // Send the HTTP header
    // HTTP Status: 200 : OK
    // Content Type: text/plain
    // 'Access-Control-Allow-Origin': 'http://127.0.0.1:8081/'
    response.writeHead(200, {
        'Content-Type': 'text/plain', 
        'Origin': 'http://127.0.0.1:8081/',
        'Access-Control-Allow-Origin': '*',
        'Vary': 'Origin'
    });
    response.end(jsonStr);
}).listen(8081);
```


## Fetch token  

```
async function postBlob() {
  const url = "http://localhost:8081/"; 
  // Access requires local token server header {'Access-Control-Allow-Origin': '*'}

  console.log('Running getToken()');

  try {
    const response = await fetch(url); // No header
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const jsonResp = await response.json();
    var myKey = jsonResp.myKey;
    var bearer_auth = 'Bearer ' + myKey

  } catch (error) {
    console.error(error.message);
  }

```

(Insert image of result in console.)  

## How OpenID Connect Works  

OpenID Connect enables an Internet identity ecosystem through easy integration and support, security and privacy-preserving configuration, interoperability, wide support of clients and devices, and enabling any entity to be an OpenID Provider (OP). [DIYSVR-17]  

OpenID is an easy and safe way for people to reuse an existing account and user profile from an identity provider, for example Apple, Google, or Microsoft to sign-in to any OpenID-enabled applications and websites without creating a new registration and password. You choose the provider, such as Google and enter your Gmail address and password to sign-in. [DIYSVR-18]  

OpenID Connect is an interoperable authentication protocol based on the OAuth 2.0 framework of specifications (IETF RFC 6749 and 6750). It simplifies the way to verify the identity of users based on the authentication performed by an Authorization Server and to obtain user profile information in an interoperable and REST-like manner. [DIYSVR-18]  

OpenID Connect enables application and website developers to launch sign-in flows and receive verifiable assertions about users across Web-based, mobile, and JavaScript clients. And the specification suite is extensible to support a range of optional features such as encryption of identity data, discovery of OpenID Providers, and session logout. [DIYSVR-18]  

For developers, it provides a secure and verifiable answer to the question “What is the identity of the person currently using the browser or mobile app that is connected?” Best of all, it removes the responsibility of setting, storing, and managing passwords which is frequently associated with credential-based data breaches. [DIYSVR-18]  

OpenID Connect uses the JSON Web Token (JWT) and JSON Object Signing and Encryption (JOSE) specifications. [DIYSVR-19]  

## JSON Web Token (JWT)

Abstract

JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties.  The claims in a JWT are encoded as a JSON object that is used as the payload of a JSON Web Signature (JWS) structure or as the plain text of a JSON Web Encryption (JWE) structure, enabling the claims to be digitally signed or integrity protected with a Message Authentication Code (MAC) and/or encrypted. [DIYSVR-19]  


## OIDC Authorization Code Flow [DIYSVR-14]  

More recently, however, the use of the ~[OAuth2 Authorization Code Grant](https://medium.com/@robert.broeckelmann/saml2-vs-jwt-understanding-oauth2-4abde9e7ec8b)~ (or ~[OIDC Authorization Code Flow](https://medium.com/@robert.broeckelmann/saml2-vs-jwt-understanding-openid-connect-part-2-f361ca867baa)~) with a Public Client has been on the rise. Identity Provider (IdP) vendors and bloggers have expressed varying opinions over using the OIDC Authorization Code Flow with a Public Client for SPAs, but this approach—with the proper safeguards—is viable and brings several benefits to the table, including:  
 
* Use of refresh tokens. (This is a big one.)  
* Greater control over the user session timeout via spec-defined mechanisms.  
* Consistency across various use cases (SPA, native mobile apps, native desktop apps, web applications, etc).  

## Authorization Code Flow Steps  
[DIYSVR-15]  

The Authorization Code Flow goes through the following steps.  

1. Client prepares an Authentication Request containing the desired request parameters.  
2. Client sends the request to the Authorization Server.  
3. Authorization Server Authenticates the End-User.  
4. Authorization Server obtains End-User Consent/Authorization.  
5. Authorization Server sends the End-User back to the Client with an Authorization Code.  
6. Client requests a response using the Authorization Code at the Token Endpoint.  
7. Client receives a response that contains an ID Token and Access Token in the response body.  
8. Client validates the ID token and retrieves the End-User's Subject Identifier.  


## OAuth Authentication  

**Documentation and Registration**  
[OAUTH-1], sec. 4  

OAuth includes a Consumer Key and matching Consumer Secret that together authenticate the Consumer (as opposed to the User) to the Service Provider. Consumer-specific identification allows the Service Provider to vary access levels to Consumers (such as un-throttled access to resources).  [OAUTH-1]  

Service Providers SHOULD NOT rely on the Consumer Secret as a method to verify the Consumer identity, unless the Consumer Secret is known to be inaccessible to anyone other than the Consumer and the Service Provider. The Consumer Secret MAY be an empty string (for example when no Consumer verification is needed, or when verification is achieved through other means such as RSA). [OAUTH-1]  

**WWW-Authenticate Header**  
[OAUTH-1], sec. 5.4.2 

Service Providers MAY indicate their support for the extension by returning the OAuth HTTP WWW-Authenticate header upon Consumer requests for Protected Resources. As per **~[RFC2617]~** such a response MAY include additional HTTP WWW-Authenticate headers:

### Authenticating with OAuth  

OAuth authentication is the process in which Users grant access to their Protected Resources without sharing their credentials with the Consumer. OAuth uses Tokens generated by the Service Provider instead of the User's credentials in Protected Resources requests. The process uses two Token types:  

* Request Token:  
  - Used by the Consumer to ask the User to authorize access to the Protected Resources. The User-authorized Request Token is exchanged for an Access Token, MUST only be used once, and MUST NOT be used for any other purpose. It is RECOMMENDED that Request Tokens have a limited lifetime.  

* Access Token:  
  - Used by the Consumer to access the Protected Resources on behalf of the User. Access Tokens MAY limit access to certain Protected Resources, and MAY have a limited lifetime. Service Providers SHOULD allow Users to revoke Access Tokens. Only the Access Token SHALL be used to access the Protect Resources.  

OAuth Authentication is done in three steps:  

1. The Consumer obtains an unauthorized Request Token.  
2. The User authorizes the Request Token.  
3. The Consumer exchanges the Request Token for an Access Token.  

## Obtaining User Authorization  
[OAUTH-1] sec.6.2  

The Consumer cannot use the Request Token until it has been authorized by the User. Obtaining User authorization includes the following steps:  

### 6.2.1.  Consumer Directs the User to the Service Provider  

In order for the Consumer to be able to exchange the Request Token for an Access Token, the Consumer MUST obtain approval from the User by directing the User to the Service Provider. The Consumer constructs an HTTP GET request to the Service Provider's User Authorization URL with the following parameter: …  

### 6.2.2. Service Provider Authenticates the User and Obtains Consent  

The Service Provider verifies the User's identity and asks for consent as detailed. OAuth does not specify how the Service Provider authenticates the User. However, it does define a set of REQUIRED steps: …  

**6.2.3.  Service Provider Directs the User Back to the Consumer**  

After the User authenticates with the Service Provider and grants permission for Consumer access, the Consumer MUST be notified that the Request Token has been authorized and ready to be exchanged for an Access Token. If the User denies access, the Consumer MAY be notified that the Request Token has been revoked.  

To make sure that the User granting access is the same User returning back to the Consumer to complete the process, the Service Provider MUST generate a verification code: an unguessable value passed to the Consumer via the User and REQUIRED to complete the process.  

## Doodles  

Note: I have replaced the term “Consumer” with the term “[App]”.  

Example:  

* Service Provider is a web application that allows access via OAuth.  
* AWS, Google, HubSpot, Snowflake, etc.  

Tokens:  

* Request tokens get exchanged for access tokens 

Request URLs: Who sends & receives?  

* Request token URL: SP > [App]  
  - SP > request token > [App]  
  - Token is unauthorized until User approves  
* User authorization URL: [App] directs user to SP for authorization  
  - [App] constructs an HTTP GET request to the Service Provider's User Authorization URL  
* Access token URL: The [App] exchanges the Request Token for an Access Token capable of accessing the Protected Resources  
  - To request an Access Token, the [App] makes an HTTP request to the **Service Provider's** Access Token URL.  
  - HTTP POST is RECOMMENDED.  
  - SP > Access Token > App   

## OAuth 2  
[DIYSVR-16]  

OAuth 2 is an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications. 

OAuth stands for Open Authorization. It’s a process through which an application or website can access private data from another website. It provides applications the ability for “secure designated access.”  

OAuth is a way to get access to protected data from an application. It's safer and more secure than asking users to log in with passwords.  [DIYSVR-16]  


The Authorization Code Grant Type is the most commonly used grant type. [DIYSVR-4]

## Role of authorization  

* Add: It [OpenID/OAuth 2] allows applications to access user information such as databases. 
* Add edited version of "JSON Web Token (JWT) is a compact, URL-safe means of representing claims to be transferred between two parties."  

## Definition  

Open authorization (OAuth) is an open protocol to allow secure authorization in a simple and standard method from web, mobile and desktop applications.[1]  

OAuth is a way to get access to protected data from an application. It's safer and more secure than asking users to log in with passwords.  

## OIDC  
[DYISVR-15]  

OpenID Connect 1.0 is a **simple identity layer on top of the OAuth 2.0 protocol**. It enables Clients to verify the identity of the End-User based on the authentication performed by an Authorization Server, as well as to obtain basic profile information about the End-User in an interoperable and REST-like manner.  

This specification defines the core OpenID Connect functionality: authentication built on top of OAuth 2.0 and the use of Claims to communicate information about the End-User. It also describes the security and privacy considerations for using OpenID Connect.  


## Authentication vs. Authorization  

While often used interchangeably, authentication and authorization represent fundamentally different functions. In this article, we compare and contrast the two to show how they protect applications in complementary ways. (From GitHub Auth Notes in Bear; original source, check references from Upwork GitHub post)  

Comment: The OAuth authentication protocol allows you to approve one application interacting with another on your behalf without exposing your password.  

(From Wiki)  
The crucial difference is that in the OpenID *authentication* use case, the response from the identity provider is an assertion of identity; while in the OAuth *authorization* use case, the identity provider is also an API provider, and the response from the identity provider is an access token that may grant the application ongoing access to some of the identity provider's APIs, on the user's behalf. The access token acts as a kind of "valet key" that the application can include with its requests to the identity provider, which prove that it has permission from the user to access those APIs.  

## Authentication libraries  
[DIYSVR-20]


> Here are links to some of the library recommendations for IdPs that I commonly use.  
> 
> 		[Red Hat SSO](https://access.redhat.com/documentation/en-us/red_hat_single_sign-on/7.0/html/securing_applications_and_services_guide/overview#what_are_client_adapters)  
> 		~[KeyCloak](https://www.keycloak.org/docs/3.1/securing_apps/topics/overview/supported-platforms.html)~  
> 		Azure Active Directory, https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries  
> 		~[ADFS](https://github.com/AzureAD)~ (~[this](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/overview/ad-fs-scenarios-for-developers)~ link mentions that the Microsoft ~[ADAL libraries](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-authentication-libraries)~ can be used with ADFS)  
> 		~[PingONE](https://www.pingidentity.com/content/developer/en/code.html)~  
> 		~[Ping Federation](https://www.pingidentity.com/content/developer/en/code.html)~  
> 		~[AWS Cognito](https://aws.amazon.com/cognito/dev-resources/)~ (tends to steer developers towards SDKs that use proprietary interfaces. Check out the A~[WS Cognito Auth SDK](https://github.com/aws/amazon-cognito-auth-js)~ for Javascript as an example of a library that uses the OIDC interface).  
> 		~[Okta](https://developer.okta.com/code/android/)~  
> 		~[Auth0](https://auth0.com/docs/libraries)~  


The OpenID Foundation (https://openid.net/)~ has an authentication library called AppAuth (https://github.com/openid) that supports Javascript/node.js, iOS, Android, and other platforms. The benefit (and limitation) of this library is adherence to the spec. This means it can be used with any OIDC compliant IdP (OpenID Provider to be accurate), but it also complicates using proprietary IdP features. 

## AppAuth libraries  

AppAuth for JavaScript is a client SDK for [public clients](https://tools.ietf.org/html/rfc6749#section-2.1) for communicating with [OAuth 2.0](https://tools.ietf.org/html/rfc6749) and [OpenID Connect](http://openid.net/specs/openid-connect-core-1_0.html) providers following the best practice [RFC 8252 - OAuth 2.0 for Native Apps](https://tools.ietf.org/html/rfc8252). The library is designed for use in Web Apps, Node.js CLI applications, Chrome Apps and applications that use Electron or similar frameworks.  

It strives to directly map the requests and responses of those specifications, while following the idiomatic style of the implementation language.  

## OIDC Authentication Request  
(https://openid.net/specs/openid-connect-core-1_0.html#Authentication) [DIYSVR-15]  

An Authentication Request is an OAuth 2.0 Authorization Request that requests that the End-User be authenticated by the Authorization Server.  

Authorization Servers MUST support the use of the HTTP GET and POST methods defined in **RFC 7231** [RFC7231] at the Authorization Endpoint. Clients MAY use the HTTP GET or POST methods to send the Authorization Request to the Authorization Server. If using the HTTP GET method, the request parameters are serialized using URI Query String Serialization, per **Section 13.1**. If using the HTTP POST method, the request parameters are serialized using Form Serialization, per **Section 13.2**.  

## Red Hat SSO  
[DIYSVR-21]  

Open ID Connect (OIDC) is an authentication protocol that is an extension of OAuth 2.0. While OAuth 2.0 is only a framework for building authorization protocols and is mainly incomplete, OIDC is a full-fledged authentication and authorization protocol. OIDC also makes heavy use of the Json Web Token (JWT) set of standards. These standards define an identity token JSON format and ways to digitally sign and encrypt that data in a compact and web-friendly way.  

There is really two types of use cases when using OIDC. The first is an application that asks the Red Hat Single Sign-On server to authenticate a user for them. After a successful login, the application will receive an identity token and an access token. The identity token contains information about the user such as username, email, and other profile information. The access token is digitally signed by the realm and contains access information (like user role mappings) that the application can use to determine what resources the user is allowed to access on the application.  

The second type of use cases is that of a client that wants to gain access to remote services. In this case, the client asks Red Hat Single Sign-On to obtain an access token it can use to invoke on other remote services on behalf of the user. Red Hat Single Sign-On authenticates the user then asks the user for consent to grant access to the client requesting it. The client then receives the access token. This access token is digitally signed by the realm. The client can make REST invocations on remote services using this access token. The REST service extracts the access token, verifies the signature of the token, then decides based on access information within the token whether or not to process the request.  

## Example SSO providers 

* Auth0  
* AWS 
* Okta  
* Ping Identity 

[DIYSVR-22] For software to qualify as an SSO, it must fulfill the following criteria:  

* Allows users to sign into multiple databases, servers, or applications via a single portal.
* Provide secure and unrestrained access to data and applications.
* Run [automated authentication](https://cloudinfrastructureservices.co.uk/best-freeradius-gui-to-manage-wifi-authentication/) to avoid multiple logins.
* Feature centralized authentication servers for applications
* Integrate login access into business centric applications.

Interestingly [SSO solutions](https://cloudinfrastructureservices.co.uk/wordpress-sso-single-sign-on/) can be offered in various forms, some run on the cloud, some On Prem, and some combine both. 

## Single sign-on  

[DIYSVR-23] **Benefits:** 

Benefits of using single sign-on include:  

* Mitigate risk for access to 3rd-party sites ("federated authentication")[5] because user passwords are not stored or managed externally
* Reduce [password fatigue](https://en.m.wikipedia.org/wiki/Password_fatigue) from different username and password combinations
* Reduce time spent re-entering passwords for the same identity[5]
* Reduce IT costs due to lower number of IT [help desk](https://en.m.wikipedia.org/wiki/Help_desk) calls about passwords[6]
* **Simpler administration.** SSO-related tasks are performed transparently as part of normal maintenance, using the same tools that are used for other administrative tasks.
* **Better administrative control.** All network management information is stored in a single repository. This means that there is a single, authoritative listing of each user's rights and privileges. This allows the administrator to change a user's privileges and know that the results will propagate network wide.
* **Improved user productivity.** Users are no longer bogged down by multiple logons, nor are they required to remember multiple passwords in order to access network resources. This is also a benefit to Help desk personnel, who need to field fewer requests for forgotten passwords.
* **Better network security.** Eliminating multiple passwords also reduces a common source of security breaches—users writing down their passwords. Finally, because of the consolidation of network management information, the administrator can know with certainty that when he disables a user's account, the account is fully disabled.
* **Consolidation of heterogeneous networks.** By joining disparate networks, administrative efforts can be consolidated, ensuring that administrative best practices and corporate security policies are being consistently enforced.

SSO shares centralized [authentication servers](https://en.m.wikipedia.org/wiki/Authentication_server)that all other applications and systems use for authentication purposes and combines this with techniques to ensure that users do not have to actively enter their credentials more than once.

## OpenID Connect SSO providers  
[Google AI search results]

Several SSO providers utilize OpenID Connect, including Google, Microsoft Azure AD (including Azure AD B2C), Okta, Auth0, Salesforce, Facebook, Twitter, Keycloak, OneLogin, GitLab, and Apple; essentially, any identity provider that adheres to the OpenID Connect standard can be considered an OpenID Connect SSO provider. 

## AWS IAM Identity Center   
[DIYSVR-24] [UPD-3]

AWS IAM Identity Center OpenID Connect (OIDC) is a web service that enables a client (such as AWS CLI or a native application) to register with IAM Identity Center. The service also enables the client to fetch the user’s access token upon successful authentication and authorization with IAM Identity Center.  

## Single sign-on  

Narrative: 

[DIYSVR-23] **Benefits:** 

Q: What is history of OIDC?

> OpenID is an easy and safe way for people to reuse an existing account and user profile from an identity provider, for example Apple, Google, or Microsoft to sign-in to any OpenID-enabled applications and websites without creating a new registration and password. [DIYSVR-18]  

> OpenID Connect is an interoperable authentication protocol based on the OAuth 2.0 framework of specifications (IETF RFC 6749 and 6750). It simplifies the way to verify the identity of users based on the authentication performed by an Authorization Server and to obtain user profile information in an interoperable and REST-like manner. [DIYSVR-18]  

Cloud computing has given rise to a proliferation of web applications that require users to create IDs and passwords for each.

Benefits of using single sign-on include:  
[DIYSVR-26]

* Developers must register their application](https://cloud.digitalocean.com/account/api/applications/new to use OAuth. 
* A registered application is assigned a client ID and client secret. 
* The client secret should be kept confidential, and only used between the application and the authorization server
* OpenID is an easy and safe way for people to reuse an existing account and user profile from an identity provider, for example Apple, Google, or Microsoft to sign-in to any OpenID-enabled applications and websites without creating a new registration and password. 
* OpenID Connect enables application and website developers to launch sign-in flows and receive verifiable assertions about users across Web-based, mobile, and JavaScript clients. 


## Questions  

* Follow up OIDC authorization code flow mentioned in both references above.  
* Identity provider (IdP) to handle authentication  


## Conclusion  

* Token is secure way to control authorization over a REST API.  
* Principles of Client authorization flow were explained.  
* JavaScript code illustrates implementation of token server.  
* Fetch code illustrates how to retrieve token.  

## Glossary  

* IdP: identity provider (IdP)  
* OIDC: OpenID Connect  
* SAML: Security Assertion Markup Language) [DIYSVR-25]  


### End  