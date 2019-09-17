# Contributing

In order to get a clean code and a clean git. All contributors should follow this following rules.

[Create an issue](#create-an-issue)

[WorkFlow](#workflow)

[Create a branch](#create-a-branch) 

[Coding](#coding) 

[Push work](#push-work) 

[Commit Rules](#commits-rules) 

[Commit type](#commit-type) 
    
[Commit scope](#commit-scope) 

[Commit subject](#commit-subject) 

[Pull Request](#pull-request) 




## Create an issue
To create an issue:
- Click on Issues' Tab
- Click on new issue
- Click on Get Started
- Give a title to your issue
- Fill the comment' part
- Assign the issue to someone
- Add the good label
- Add the issue on POC_KANBAN' project
- Add a milestone, if needed

## WorkFlow

Here the workFlow to follow:

![alt text](https://leanpub.com/site_images/git-flow/git-flow-nvie.png "WorkFlow")
## Create a branch

```shell
    git pull develop
    git checkout -b <issue name and number>
```
For example for the issue '_Login #1_'

```shell
    git pull develop
    git checkout -b 'Login #1'
```

## Coding

To avoid to be overwhelmed by big feature, split the feature in smalls issues.

For  exemple for _"Login #1"_ 's issue, when can create severals smalls issues
- Create login Page
- Check login data
- Active validation button
- Connect front to back
- Receive answers and treats all return type

## Push work

```shell
    git add <filename>
    git commit -m "<type>(<scope>): <subject>"
    git push origin release
```

### Commits Rules

A good commit have to be self-speaking. We have to know what's change and why but not how.

#### What to commit ?
Every time you finish a small feature or when you fix a bug.
#### When to commit ?
As often as you can. 
#### How to commit ?

##### Commit template
```shell
    <type>(<scope>): <subject>
```

###### Commit type
  - **build** : change concerning build system or extern dependancies(npm, make, ...)
  - **ci** : change about intergration or configuration files and scripts  
  - **feat** : add new feature
  - **perf** :perf amelioration
  - **refactor** : code writting who doesn't who is not a new feature or perf ameliation 
  - **style** : css
  - **test** : everything related to test
  - **revert** : cancel a commit
  - **docs** : documentation
  - **fix** : correction
  - **chores** : any non-relevant task or anything that does'nt fit in the previous types
  ###### Commit scope 
  
  Name of the big feature or of the affected  file
  
  ###### Commit subject 
   1) No more than 50 characters
   2) Use imperative mood like add, remove, change, ...
   3) Explain **WHAT** and **WHY** and no how
   
   ```shell
    perf(database): add caching for better performance
```
For more informations check this website https://buzut.fr/git-bien-nommer-ses-commits/


## Pull Request
When your issue is done, create a pull request. Your issue will be review by other members.
- To create a pull request, click on pull request tab.
- Click on  new pull request's button
- Select develop for base branch 
- Select the branch you want to pull request for compared branch
- Choose a PR template by appending ```&template=feature.md``` to URL query. PR templates are located [here](../PULL_REQUEST_TEMPLATE/feature.md)
- Then click on create pull request

