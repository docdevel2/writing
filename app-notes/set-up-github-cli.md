# Set up GitHub CLI

(See notes on LM5430)

## Install GitHub CLI

* sudo apt install gitsome
* Command: $ gh ...

### Command syntax 

* Usage:  gh \<command> \<subcommand> [flags]
* Read the manual at  [https://cli.github.com/manual](https://cli.github.com/manual) 
* Useful gh commands  
	* auth:        Authenticate gh and git with GitHub
	* browse:      Open the repository in the browser
	* codespace:   Connect to and manage codespaces
	* config:      Display or change configuration settings for gh
	* repo:        Manage repositories

* SSH commands  
	* ssh: Provides secure encrypted communications between two untrusted hosts
	* ssh-keygen: Generates key for specified algorithm
	* ssh-keyscan: Reports all known public(?) keys for specified host

### Examples

```
$ gh auth login
$ gh auth login --hostname <string> --git-protocol <string>
$ gh auth login -h <string> -p <string>
$ gh auth logout
$ gh auth status
$ gh browse
$ gh config
$ gh repo clone `git@github.com:docdevel2/writing.git`
```

## Authenticate

This section describes the process of generating and verifying the authentication key.

### Create ECDSA Authentication Key

* Note: Elliptic Curve Digital Signature Algorithm (ECDSA) is an upgrade from RSA
* $ ssh-keygen -t ed25519 -C "your_email@example.com"
	* Note: -t option selects algorithm, -C is comment option
	* [Source GitHub doc page](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

### Add github.com known hosts

* $ ssh-keyscan github.com >> ~/.ssh/known_hosts
	* Source unknown; result of Google search

### Set port visibility

* $ gh codespace ports visibility 8000:public
	* 	Port 8000 must be visible else clone, fetch, and push will fail 
	* 	This API operation needs the "codespace" scope. To request it, run:  gh auth refresh -h  [github.com](http://github.com)  -s codespace

## Enable clone

* $ gh browse  
	* 	Opening  [github.com/docdevel2/writing](http://github.com/docdevel2/writing)  in your browser.
	* Click `Code<>` button
	* Click `Local` tab
	* Copy URI text under SSH: `git@github.com:docdevel2/writing.git`
* $ gh repo clone `git@github.com:docdevel2/writing.git`
	* 	Cloning into 'writing'...
	* 	Permanently added the ECDSA host key for IP address '192.30.255.113' to the list of known hosts.

### Test Authentication Key
* $ gh auth status
* $ gh auth status -h  [github.com ](http://github.com) 
	* -h option verifies authentication for specified host (github site) 
* $ ssh -T git@github.com
	* Response: Hi docdevel2! You've successfully authenticated, but GitHub does not provide shell access. (This is a positive response, even with the shell access warning.)

## Git remotes documentation 
(`https://www.git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes`)

## Test steps in gitdir/writing repo 
* 	Inspect .git dir 
* 	git status 
* 	git remote -v 
* 	git log 
* 	git pull (response: Already up to date) 
* 	git fetch  (ls -la reveals that 1 file in .git directory was updated; “FETCH_HEAD”)
* 	git add
* 	git ignore (.gitignore)
* 	git config - -global core.editor xed 

## Actions
* 	Verify port 8000 vs. 443
* 	Investigate GitWeb
	* 	simple web-based visualizer
	* 	Automatically runs by invoking Instaweb, a light weight git web server 
	* 	Invoke:  $ `git instaweb` 



### End