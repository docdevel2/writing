# github-notes-v2.md

## GitHub Notes v2.0 
Last revision: 11/27/23

## Description
About GitHub: The complete developer platform to build, scale, and deliver secure software.

GitHub runs on Git. What is Git? Git is a version-control system created by programming icon, Linus Torvald. He originally created Git to track changes to source code changes as he was developing the Linux operating system. Git helps programmers collaborate, coordinate work, and work together on complex code and development projects.
(Source: Ref. 1)

My conclusion: GitHub is an online extension of Git that allows multiple developers to collaborate.

## Free account

* 	Best place to start, 
* 	Install Git
* 	Sign up for free account 
* 	To do anything in GitHub, youʼll need to know how to first start a repository. A repository (or repo) is essentially synonymous with the word “project.”


## Install Git

* 	Objective: Study basic Git operations.
* 	Initially practice revision control using markdown documents that I’m currently editing.


## Why use Git?

* 	Get access to unlimited public and private repositories
* 	Get bug tracking and project management
* 	Publish & consume packages
* 	Your GitHub Profile is a great place for recruiters to find you and reach out about potential jobs and projects. Many people strive to gain GitHub followers by writing engaging and helpful blog posts, or even by creating podcasts or YouTube GitHub tutorials.


## First Steps

* 	Install 
* 	Init
* 	Status
* 	Add
* 	Status 
* 	Edit 
* 	Status 
* 	Commit 
* 	Status 


## Stage
The git add command is used to add file contents to the Index (Staging Area). This command updates the current content of the working tree to the staging area. It also prepares the staged content for the next commit.

“git add” is a multipurpose command — you use it to begin tracking new files, to stage files, and to do other things like marking merge-conflicted files as resolved. It may be helpful to think of it more as “add precisely this content to the next commit” rather than “add this file to the project”.

## SDLC
Software Development Life Cycle (SDLC)
* 	Planning
* 	Analysis
* 	Design
* 	Implementation
* 	Maintenance
* 	Repeat from planning step

## GitHub account signup

* 	email address: (gmail)
* 	Password: (gmail)
* 	User name: docdevel2
* 	Launch code: 93651499


# Signup steps
* 	Go to GitHub.com
* 	Click “Sign-up for GitHub”
* 	Enter email address (gmail) *DONE*
* 	Create a password (gmail) *DONE*
* 	Launch code will be sent to your email address 
* 	Enter launch code
* 	You will be asked: “How many team members will be working with you?” or “Are you a student or teacher?” (You can skip this personalization if you choose.)
* 	My answer: “Just me”
* 	You will be asked: “What specific features are you interested in using?” (You can skip this personalization if you choose.)
* 	My answer: “Collaborative coding” and “Automation and CD/CI”
* 	Click “Continue for free”
* 	You will be taken to your personal dashboard 


## The GitHub Flow 

GitHub is designed around a particular collaboration workflow, centered on Pull Requests. This flow works whether you’re collaborating with a tightly-knit team in a single shared repository, or a globally-distributed company or network of strangers contributing to a project through dozens of forks. It is centered on the  Topic Branches  workflow covered in  Git Branching. [3]

Here’s how it generally works: 

	1.	Fork the project. 
	2.	Create a topic branch from  master. 
	3.	Make some commits to improve the project. 
	4.	Push this branch to your GitHub project. 
	5.	Open a Pull Request on GitHub. 
	6.	Discuss, and optionally continue committing. 
	7.	The project owner merges or closes the Pull Request. 
	8.	Sync the updated master back to your fork. 

This is basically the Integration Manager workflow covered in  Integration-Manager Workflow, but instead of using email to communicate and review changes, teams use GitHub’s web based tools.

## Remote flow 

* git clone (If not already done)  
* git remote -v  
* git fetch, or  
* git pull (to automatically fetch and then merge that remote branch into your current branch)  
* git push (to push changes from local repo to GitHub)  

## Comments

* 	Markdown format is used for README, CONTRIBUTING, & ISSUE_TEMPLATE files.


## Repo  URL
https://github.com/docdevel2/repo_name.git
https://github.com/docdevel2/scratch.git

## For writers

* 	HT Geek: ( [https://www.howtogeek.com/438252/how-writers-can-use-github-to-store-their-work/amp/](https://www.howtogeek.com/438252/how-writers-can-use-github-to-store-their-work/amp/) )
* 	Dig Ocean: ( [https://www.digitalocean.com/community/tutorials/how-to-use-git-to-manage-your-writing-project](https://www.digitalocean.com/community/tutorials/how-to-use-git-to-manage-your-writing-project) )


## Tutorials

* 	Intro to GitHub 
* 	( [https://github.com/skills/introduction-to-github](https://github.com/skills/introduction-to-github) )
* 	GitHub Pages tutorial—build web site 
* 	( [https://github.com/skills/github-pages](https://github.com/skills/github-pages) )
## GitHub CITATION
You can add a CITATION.cff file

[https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files)

## References
1. (  [https://devmountain.com/blog/what-is-github-and-how-do-you-use-it/](https://devmountain.com/blog/what-is-github-and-how-do-you-use-it/)  ) 
2. (  [https://en.m.wikipedia.org/wiki/Kanban_board](https://en.m.wikipedia.org/wiki/Kanban_board)  )
3. ProGit, , p.172, (GitHub flow)
4. ProGit, p.50, (Working with Remotes)

## Glossary
* 	docsify: Docsify is **a simple and lightweight documentation generator**. You can start using it without having any knowledge of JavaScript or React. Docsify comes with zero configuration, no statically built HTML files, multiple theme support, inbuilt plugin API, and full-text search support with a plugin.
* 	Kanban board: Kanban boards visually depict work at various stages of a process using cards to represent work items and columns to represent each stage of the process. [2]


###