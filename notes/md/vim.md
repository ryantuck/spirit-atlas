# vim

## Reference

- `q:` - command line history
- `q/` - search history
- `:sort u` - sort the file
- `:set tw=80` for soft word wrap, and works with outlines
- `gU` converts selection to ALL CAPS
- `gu` converts selection to lowercase
- `gf` goes to file under cursor
- `:! <command>` - run commands in vim
- `g_` goes to last non-blank character
- `P` pastes before cursor
- `:let` shows all vars
- `:set linebreak` allows for soft line wraps
- `:set columns=80` will limit the maximum number of columns to display to 80. This works nicely with `:set linebreak` to create a nice UI for writing text.
- `:g/=/d` will delete all lines that contain `=`
- `Ctrl+N/P` provides autocompletion for words already defined in your file.
- `:! <command>` to run commands from a vim window
- `:set suffixesadd+=.md` to allow for interpreting `my_file` as `my_file.md` when using `gf`
- `<C-O>` goes back to the last file you jumped from
- `*` and `#` searches for same word forward and backward
- `:PluginInstall` will ask for your github password if you define the repo name incorrectly

## Window Management

Would be interesting to explore vim windows instead of [[tmux]] panes.

- `<C-w>f` opens file under cursor in new vim window (not tmux window)
- `<C-w><C-w>` switches between vim windows
- `:split` and `:vsplit` for splitting windows
- `<C-w>[hjkl]` to navigate between windows. More [here](https://vi.stackexchange.com/questions/64/is-it-possible-to-split-vim-window-to-view-multiple-files-at-once)


## Spell Check

[Setting up spellcheck in vim](http://thejakeharding.com/tutorial/2012/06/13/using-spell-check-in-vim.html)

- `:setlocal spell` to turn on spell check in a file
- `]s` to go to next misspelled word
- `[s` to go to previous misspelled word
- `zg` to add word under cursor to `spellfile`

## Folding

- `zo` opens fold
- `zc` closes fold
- `zj` and `zk` for nav
- `zO` opens all folds at cursor
- `zm` closes all folds

For markdown, add this to your `~/.vimrc`:

```
let g:markdown_folding=1
```

Within a vim session, your fold settings will be saved for each file, so you can swap back and forth between things.

## Links

- https://shapeshed.com/vim-netrw/ has great stuff about `netrw` and navigating files
- https://andrew.stwrt.ca/posts/vim-ctags/ ctags seem like they could be cool, should experiment with these more.
- Macros: https://vim.fandom.com/wiki/Macros
- https://medium.com/hacking-and-gonzo/10-vim-tricks-you-should-know-6393842b3537


## Markdown syntax improvements


- Header highlighting
- Link highlighting
- Allow underscore mid-word
- indent bulleted lists
- Default column width to 60-70
- Don't support indent-as-code
- Figure out folding
- File-specific usage of `inoremap`

## Etc

- Possible to use vim in encrypted mode? How could you with .swp functionality?
- Would be cool to keystroke from jira ticket name out to chrome.
- Try out infinite history?
- Try out `youcompleteme` for autocomplete

Fun [[regex]] used to replace anything starting with a plus or hashtag. Uses capture groups. Note the escaped capture group parentheses `\(...\)`:

```
%s/\s[#+]\([a-z-]*\)/ [[\1]]/g
```
