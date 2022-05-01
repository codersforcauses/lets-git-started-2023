# git-tute


Please ensure that you have git installed  before continuing

---

## Setup


1. Open Terminal / Power Shell and change directory into where you would like to store project

Run:
```
git clone https://github.com/codersforcauses/lets-git-started.git
```

Please nominate one person from your group to do steps 2-5

2. Create a new branch for your group by running (please create branch with the same name as your group):
```
git branch <name of branch>
```

3. To view all branches available (not on github), Run:
```
git branch
```

Now that we have created our branch, it is time we checkout(switch to) that branch so we can edit code!

4. to change to the branch created, Run:
```
git checkout <name of your branch>
```

5. Let push your newly created branch to github by running:

(name of remote will be origin for today)

```
git push <name of remote> <name of branch>
```

---

## Checkpoint!

Now that your group has created the branch, we need to update the repositories of other group members by running:
```
git pull
```

Once everyone in your group has updated their repository, please checkout to the branch created by your group

We will be running this command several times to 'pull' in changes made by our group members!

---

## Exercise

Please ensure that you are on the branch your group has created before continuing further!

1. Now that you are on your branch, you are free to do whatever you like with the code! For the excercise, create a copy of the template folder and rename it to the name of your group. Run:
```
cp -r ./template/ ./<name of group>
```






