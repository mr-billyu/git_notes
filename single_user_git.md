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

Show branches:
    git branch

Create branch:
    git branch develop

Change branch:
    First:
        git commit -a
            This saves work in current branch
    Then:
        git checkout branch

Delete branch:
    git branch -d branch

Configure difftool:
    git config --global diff.tool gvimdiff
    git config --global difftool.prompt false
    git config --global alias.d difftool

Show file differences:
    Note: 'd' is an alias for difftool.
    git d filename
        Show differences between working directory and index.
    git d --cached filename
        Show differences between index and last commit.
    git d HEAD filename
        Show differences between working directory and last commit.
    git d master develop filename
        Compare files from two different branches.

Show specified version of file:
    git show SHA:file

Merge develop branch to master:
    Commit all files in develop branch. See Stage and Commit above.
    Then:
        git checkout master
        git merge develop

Undo merge
    git reset --merge ORIG_HEAD

Update branch with changes from master:
    Commit all files in branch.
    Then:
        git checkout branch
        git merge master

Rename file or directory:
    git mv 'original file/dir' 'renamed file/dir'
        Changes the file name and prepares it for
        commit.

Remove file:
    git rm file
        Removes the file from the working directory and
        stages the deletion.

Git tags:
    git tag
        List all tags.
    git tag -a v1.0 -m "v1.0 of file|project|etc"
        Adds tag to current commit. 
    git tag -a v1.0 -m "v1.0 of file|project|etc" SHA
        Adds tag to SHA commit.
    git show v1.0
        Displays detail about tag v1.0.
    git tag -d v1.0
        Deletes tag v1.0.

List git configuration:
    git config -l

========= REMOTE =========
Remote can be another server, cloud server, GitHub, etc

GitHub:
    Sign on GitHub and create repository for git_notes.

    Associate local repository with GitHub repository:
        git remote add server https://github.com/mr-billyu/git_notes.git

    View existing remotes
        git remote -v

    Rename remote
        git remote rename old_name new_name
        Example: git remote rename origin server

    Push local branches to GitHub repository:
        git push server master
        git push server develop

Clone a repository:
    Change to the directory that will be the parent of the clone.
    ie. ~/Applications

        git clone url

    The clone directory will have been created under the parent 
    directory.  ie. ~/Applications/clone_dir



