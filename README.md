# fotgb
Welcome to the fellowship of the Ghostbusters. Here be Ghosts in the Machine.

## Getting started
Follow this step by step guide for installing git locally and cloning the repository

**1. Download Git**

The [Git Manual](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) has OS
specific instructions for how to download git. Find the section for your OS and follow
the guide.

**2. Clone the Repository**

Open your terminal (git-bash on Windows) and execute the following command
```
git clone https://github.com/ezzy1337/fotgb.git
```
This creates a folder named `fotgb` on your computer. Inside that folder is all of the
code we work on as a group.


## Contributing

Ok so you've cloned the repo and now you want to contribute some code to it. Heres how you
keep your local version of the repository in sync with the master copy located on Github.

The general workflow is, pull changes from the origin, commit changes, and push changes to
the origin. The following is an example of pulling, committing, and pushing changes.

```bash
git pull origin main
# Inbetween this command and the next command is when you make changes to the code
git status
git add <path to changed files>
git commit -m "A detailed message stating what changes you made"
git pull origin main # At this point you might hit merge conflicts if you do good luck
git push origin main
```
__NOTE: I setup a folder for each of you so if you limit your changes to your folder the likelihood of getting merge conflicts is minimal.__


## Questions?
You know how to get a hold of me.
