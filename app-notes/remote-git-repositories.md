# Remote Git Repositories 

## Highlights 

* 	[Protocols] [1]
	* 	Remotes can use a variety of protocols
	* 	https:// (http protocol)
	* 	git:// (git protocol)
	* 	git@github.com:// (ssh protocol)
* 	[git clone] [1]
	* 	Default shortname for cloned repo is “origin”
	* 	This command implicitly adds the origin remote
	* 	Shortname can be used in future git commands
	* 	e.g.
		* $ git remote origin
* 	[git remote -v] [1]
	* 	Shows list of shortnames and URL	
* 	git remote add [1]
	* 	To add a new remote Git repository as a shortname you can reference easily, run git remote add \<shortname> \<url>
* 	git push \<remote> \<branch> [1]
	* 	works only if you cloned from a server to which you have write access and if nobody has pushed in the meantime
		* 	e.g. $ git push origin master
	* 	to push your master branch to your origin server
		* 	$ git push origin master
* 	git fetch [1]
	* 	fetches any new work that has been pushed to that server since you cloned (or last fetched from) it
	* 	only downloads the data to your local repository — it doesn’t automatically merge it with any of your work or modify what you’re currently working on
	* 	You have to manually merge fetched data into your work
* 	git ignore [2]
	* 	Files in .gitignore file are ignored by git
	* 	Wildcard can be used, e.g. *.backup
* 	git reset HEAD to undo [2]
	* 	git reset HEAD \<file> 
* 	git pull [2]
	* 	automatically fetch and then merge that remote branch into your current branch.

## Basic Git workflow

The basic Git workflow goes something like this: 

1. You modify files in your working tree. 
2. You selectively stage just those changes you want to be part of your next commit, which adds only  those changes to the staging area. 
3. You do a commit, which takes the files as they are in the staging area and stores that snapshot permanently to your Git directory.

## Staging  

The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit. Its technical name in Git parlance is the “index”, but the phrase “staging area” works just as well.

Staging command: git add \<file> ...

To begin tracking a new file, you use the command  
`$ git add`

## References  

[1] [Scott Chacon & Ben Straub, *Pro Git*, sec. 2.5, Working with Remotes]([1]: https://www.git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

[2] [Scott Chacon & Ben Straub, *Pro Git*, sec. 2.1, Git Basics](https://www.git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)

---
[0]: Hidden-reference-links

[1]: https://www.git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes

[2]: https://www.git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository 


### End