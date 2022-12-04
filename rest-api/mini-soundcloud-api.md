# Mini - SoundCloud API

SoundCloud is a music service that allows musicians to share their music with a community of artists and listeners.

## API

For developers interested in integrating SoundCloud services into their applications, an application programming interface (API) and corresponding documentation are available. An application programming interface allows a client application to interact with a server using a common protocol.

## REST

One such protocol is REpresentational State Transfer (REST). The REST protocol operates in two modes, request and response. The client sends a request to the server for data, and the server responds with a status code, and if appropriate, the requested data. REST is a common protocol used by music API web sites. Web site APIs that employ the REST protocol are referred to as RESTful.

A RESTful API allows the client to retrieve data from the server without the need to details the server backend implementation. There is no need for the client to know which server or database management software is being used. In addition, the API enhances security by restricting who can access data, what data is accessible.

## Request & response

The SoundCloud API is commonly used to retrieve either songs or music metadata such as artist, song title, album name, etc.

API requests are typically some form of an HTTP  request using the GET, POST, PUT, or DELETE methods. If you want to retrieve, for example, a song title, album name, and track number, use the GET method.

(Insert Example)

If the request is successful, you get an HTTP response code indicating success.

## Notes

### API

* SoundCloud for Developers [Ref. 4]

* API Guide [Ref. 5]

* Client Credentials: Your application intends to access public resources only. That implies searching for a track, or a playlist, playback and URL resolution. For these purposes you do not require a user session, just an authorized app. 
* Rate limit: 
	* Please be aware there is a rate limiting on amount of token you can request through the Client Credentials Flow: 50 tokens in 12h per app, and 30 tokens in 1h per IP address. In order to not hit the limit we highly recommend reusing one token between instances of your service and implementing the Refresh Token flow to renew tokens. 

* API usage policies

If you are looking to build an application on top of SoundCloud’s API, you can register your app and find what you need to know from our developer website. There you’ll find a great range of resources from Stack Overflow support, to information around rate limiting, to our API Terms of Use. 


### From web site

[Ref. 2]

* What is SoundCloud?

Founded in 2007, SoundCloud is an artist-first platform powered by a global community of artists and listeners on the pulse of what’s new, now and next in music culture. We empower independent artists with the tools, services and resources they need to help them build and grow their careers. With over 250 million tracks from 30 million artists from 190 countries on SoundCloud, we are the largest audio discovery platform in the world. 
 
* How can you use SoundCloud?

Be an artist. Upload tracks and share them with your social networks. Promote your releases, engage with fans and earn money when you become eligible to monetize. Create an account for free or upgrade to Next Pro to access our best-in-class tools.

* Check out our artist resource center here. 

Be a listener. Find new music and share favorite discoveries with your social networks. Support the artists you love by commenting, reposting and liking their tracks. You can even save unlimited tracks and playlists for ad-free, offline listening with a Go+ subscription.


### iTunes App Store description
Be the first to discover, play and share your favorite tracks from emerging artists

Access the world’s largest music discovery platform

- That’s 300M+ tracks from 30M+ artists in 193 countries

Discover new music, picked just for you

- Play curated mixes and playlists based on the music you love

Listen to exclusive music on SoundCloud

- Hear tracks you can’t find anywhere else

Find and connect with your music community

- Share tracks, reach a global audience, and connect with your favorite artists and fans directly on SoundCloud

Upload your own tracks

- Tap into a global fanbase of millions by sharing your music

Help your favorite independent artists get paid

- Your fan-powered streams put money in the pockets of the artists you want to support

Listen to SoundCloud for free, or subscribe to SoundCloud Go or SoundCloud Go+ for premium features.

SOUNDCLOUD FREE:

- Play your favorite tracks from independent and established artists, with ads

SOUNDCLOUD Go:

- Listen without ads

- Save tracks to listen offline — anywhere, anytime

- Support your favorite independent artists through Fan-Powered Royalties

SOUNDCLOUD Go+:

- Unlock premium Go+ tracks

- Upgrade your DJ sets with exclusive app integrations

- Listen without ads

- Save tracks to listen offline — anywhere, anytime

- Support your favorite independent artists through Fan-Powered Royalties



Need help? Get in touch:

[Ref. 1]https://soundcloudcommunity.com

[Ref. 2]https://help.soundcloud.com

[Ref. 3]https://twitter.com/SCsupport

[Ref. 4]https://developers.soundcloud.com/

[Ref. 5]https://developers.soundcloud.com/docs/api/guide


###