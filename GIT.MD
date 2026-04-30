### WHEN A PROJECT IS NEW
- On github.com - create a repository
a. Provide the repository name
b. Set the privacy 
c. Get your repo url on creation
- Start Git processes from project terminaL
- Start  git processes from project terminal
1. initilize the git folder : git init
2. connect local project to repo url:
git remote add origin<url>
3. initial adding of files :git add
4. make commit:git commit -m "write a commit msg"
5. Ensure you have a password token to allow push
6. push using token via this command
git push origin master
where master is referencing the default branch where 
work will be saved


AFTER LOGIN PROCEED TO DO PUSH

### to get project on a new device
- select project saving location - open terminal gere
- git clone linktorepo
###  to update project repo
- git add .
- git commit -m "commit msg here"
- git push -u origin master/main