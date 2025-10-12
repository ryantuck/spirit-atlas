# ssh

Fire up `ssh-agent` if it's not running:

```
eval "$(ssh-agent)"
```

Add your key:

```
ssh-add -K ~/.ssh/id_rsa
```

List keys:

```
ssh-add -l
```
