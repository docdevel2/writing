# GitHub Auth Notes
Start date: 3/9/23  
Last rev.: 3/14/23  

I've generated these notes as preparation to respond to a post for a freelance technical writer to write a 1500-2000 word article on GitHub's authorization model. 

## Investigate  
* OAuth2 scope in JWT

## Authentication
Authentication is the process of verifying who a user is 

## Authorization
* authorization is the process of verifying what they have access to
* access is controlled by permissions. 
* A permission is the ability to perform a specific action. For
example, the ability to delete an issue is a permission. 
* A role is a set of permissions you can assign to individuals or teams.
	* Personal accounts
		* Owner access: (Characterize actions)
		* Collaborator access: (Characterize actions)
	* Organization accounts  
		* Repository-level roles
			* Read
			* Triage
			* Write
			* Maintain
			* Admin
		* Team-level roles
		* Organization-level roles
			* Owners	
				* complete administrative access to your organization
			* Members	
				* default
				* non-administrative 
				* can create repositories and project boards
			* Moderators	
				* block and unblock non-member contributors
				* set interaction limits 
				* hide comments in public repositories owned by the organization
			* Billing managers
				* manage the billing settings for your organization
			* Security managers
				* manage security alerts and read permissions for all repositories
				* can limit access of any team member
	* Enterprise accounts

## Authentication vs. Authorization
While often used interchangeably, authentication and authorization represent fundamentally different functions. In this article, we compare and contrast the two to show how they protect applications in complementary ways. [99]

## OAuth2 scope
OAuth is an authentication protocol that allows you to
approve one application interacting with another on your behalf without giving away your password.

Open Authorization is a process through which an application or website can access private data from another website.

Facebook's Graph API only supports OAuth 2.0. Google supports OAuth 2.0 as the recommended authorization mechanism for all of its APIs.[23] Microsoft also supports OAuth 2.0 for various APIs and its Azure Active Directory service, which is used to secure many Microsoft and third party APIs. [3]

## JWT
* Grants access permissions upon login
* Grants access permissions for specified periods of time after login
	* Gets complicated if permissions need to change between login periods
	* Doesn't adapt permissions in real time 

## Summary 
* Authorization is distinct from authentication
* OAuth2 focuses on authentication and adds general authorization features
* GitHub authorization provides more granular authorization than OAuth 

## References
1. [OAuth2](https://oauth.net/2/)
2. JWT
3. Wikipedia
4. [OAuth](https://oauth.net/) 
5. [Auth0](https://auth0.com/docs/get-started/identity-fundamentals/authentication-and-authorization)

## GitHub docs
* Access permissions on GitHub
* OAuth2 Scopes vs Permissions
* Repository roles for an organization
* Scopes for OAuth Apps

### End 