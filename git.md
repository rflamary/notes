## GIT tricks


#### Set url origin

This can be usefull for ssh commit with no password.

For this repository: 

```bash
$ git remote set-url origin git@github.com:rflamary/notes.git

```

#### Pull from master into another branch
You are working on a branch, but you want the commits made on master.
```bash
$ git checkout myBranch # Switch to "myBranch"
$ git fetch origin # Gets you up to date with origin
$ git merge origin/master # Merge with master
```
