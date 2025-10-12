# git

Related: [[code]]

Random `git` notes.

### Wanna rebase, but have already merged, oh fuck

Create a new branch off of master, then do:

```
git checkout master
git checkout -b new-clean-branch
git read-tree -u -m old-fucked-up-branch
```

from this [SO answer](https://stackoverflow.com/questions/6248231/git-rebase-after-previous-git-merge/6258664#6258664)


### Set upstream branch on forked repo

```
git remote add upstream git@github.com:official/repo.git
```

### Update origin url

```
git remote set-url origin git@github.com:my/origin.git
```



### Push an empty commit

to trigger a build or something

```
git commit --allow-empty -m 'changing nothing'
```
