#Git Notes

##Local

###Create repository

To create a git repository, switch to the parent directory and run `git init project-name`. The following example creates a git_notes repository under the parent directory ~/Applications.

        cd ~/Applications
        git init git_notes

To create a git repository for an existing directory, switch to the directory and run `git init`. This will create the `.git` file.

        cd ~/Applications/Project_x
        git init

###Display status of repository

        git status

###Display files tracked by git

        git ls-files

###Ignore files

Instruct git to ignore a file, enter the file name into `.gitignore`. The .gitignore file should be committed.

###Stage files to be commited

        git add file

###Unstage file

Change file back to untracted status.

        git reset HEAD file

###Get fresh copy of file

Change file back to last commit.

        git checkout file

###Add file to git

        git add file

###Commit files

It is wise to run `git status` before and after a commit.

        git commit 
        git commit file

###Display commit messages for current branch

        git log
        git log --oneline

###Display commit messages for file

        git log file
        git log --oneline file

###Display branches

        git branch

###Create branch

        git branch develop

###Change branch

        git commit -a   # Save work in current branch
        git checkout branch-name

###Delete branch

        git branch -d branch-name

###Merge develop branch to master

        git commit -a          # Save work in develop branch
        git checkout master   
        git merge develop

###Update branch with changes from master

        git checkout branch
        git commit -a          # Save work in branch
        git merge master 

###Show file differences

**Note:** `d` is an alias for `difftool`.

Display differences between working directory and index.

        git d filename

Display differences between index and last commit.

        git d --cached filename

Display differences between working directory and last commit.

        git d HEAD filename

Display differences between two branches.

        git d master develop filename

###Display specified version of file

        git show SHA:file

###Undo merge

        git reset --merge ORIG_HEAD

###Rename file or directory

Change the file name and prepare it for commit.

        git mv 'original file/dir' 'renamed file/dir'

###Remove file

Remove the file from the working directory and stages the deletion.

        git rm file

###Git tags

List all tags.

        git tag

Add tag to current commit.

        git tag -a v1.0 -m "v1.0 of file|project|etc"

Add tag to SHA commit.

        git tag -a v1.0 -m "v1.0 of file|project|etc" SHA

Displays detail about tag v1.0.
 
        git show v1.0

Delete tag v1.0.

        git tag -d v1.0

###List git configuration

        git config -l

###Configure difftool

        git config --global diff.tool gvimdiff
        git config --global difftool.prompt false
        git config --global alias.d difftool

##Remote

Remote can be another server, cloud server, GitHub, etc

###View existing remotes

        git remote -v

###Rename remote

Rename remote origin to server.

        git remote rename origin server

###GitHub

Sign on GitHub and create repository for git_notes.

####Associate local repository with GitHub repository.

        git remote add server https://github.com/mr-billyu/git_notes.git

####Push local branches to GitHub repository.

        git push server master
        git push server develop

####Clone a repository

Change to the directory that will be the parent of the clone.  ie. ~/Applications

        git clone url

The clone directory will have been created under the parent directory.  ie. ~/Applications/clone_dir

##Git Reference

<https://git-scm.com/docs/>

