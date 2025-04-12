# Start a new git repository  
## Install on Linux  

* apt install git  

## Initialize project  

Your first instinct, when you start to do something new, should be git init. You’re starting to write a new paper, you’re writing a bit of code to do a computer simulation, you’re mucking around with some new data … /anything/: think git init.

## A new repo from scratch  

Say you’ve just got some data from a collaborator and are about to start exploring it.  

* 	Create a directory to contain the project.
* 	Go into the new directory.
* 	Type git init.
* 	Write some code.
* 	Type git add to add the files (see the  [typical use page](https://kbroman.org/github_tutorial/pages/routine.html) ).
* 	Type git commit.

The first file to create (and add and commit) is probably a ReadMe file, either as plain text or with  [Markdown](https://daringfireball.net/projects/markdown/) , describing the project.
Markdown allows you to add a bit of text markup, like  [hyperlinks](https://en.wikipedia.org/wiki/Hyperlink) , *bold*//italics/, or to indicate code with a monospace font. Markdown is easily converted to html for viewing in a web browser, and GitHub will do this for you automatically.

## A new repo from an existing project
Say you’ve got an existing project that you want to start tracking with git.

* Go into the directory containing the project.
* Type git init.
* Type git add to add all of the relevant files.
* You’ll probably want to create a .gitignore file right away, to indicate all of the files you don’t want to track. Use git add .gitignore, too.
* Type git commit.

> **Note: Skip the connect step below.** 

---
# Connect it to github
You’ve now got a local git repository. You can use git locally, like that, if you want. But if you want the thing to have a home on github, do the following.

* Go to  [github](https://github.com/) .
* Log in to your account.
* Click the  [new repository](https://github.com/new)  button in the top-right. You’ll have an option there to initialize the repository with a README file, but I don’t.
* Click the “Create repository” button.

Now, follow the second set of instructions, “Push an existing repository…”

```
$ git remote add origin git@github.com:username/new_repo
$ git push -u origin master
```

Actually, the first line of the instructions will say

`$ git remote add origin https://github.com/username/new_repo`

But I use `git@github.com:username/new_repo` rather than `https://github.com/username/new_repo`, as the former is for use with  [ssh](https://en.wikipedia.org/wiki/Secure_Shell)  (if you set up ssh as I mentioned in “ [Your first time](https://kbroman.org/github_tutorial/pages/first_time.html) ”, then you won’t have to type your password every time you push things to github). If you use the latter construction, you’ll have to type your github password every time you push to github.

> **My Steps below!**

> New directory

```
mkdir gitdir
cd gitdir
git init
(Initialize empty Git repository in /home/docdevel/gitdir/.git/)
git status
git config --global user.email "jcofield2.0@gmail.com"
git config --global user.name "docdevel2"
(Copy files to gitdir)
git add gittest_1.md
git status
(Edit gittest_1.md)
git status
git commit -m 'First edits made to gittest_1.'
```

> Existing directory

```
mkdir gitdir
cd gitdir
git init
(Initialize empty Git repository in /home/docdevel/gitdir/.git/)
git status
git config --global user.email "jcofield2.0@gmail.com"
git config --global user.name "docdevel2"
(Retrieve existing repository)
git clone git clone git@github.com:docdevel2/writing.git 
	(Note: Use SSH link from CODE dropdown menu.)
```
