. what is git and github ?

Git: Git is a version control system that tracks changes to code locally, Developers use Git to manage history and branches.

Github: GitHub is a cloud platform that hosts Git repositories for collaboration. GitHub to share, review, and merge code. 

---

. What is the difference between Git and GitHub?

Git works on your computer, keeping track of changes.

GitHub lives on the internet, letting you upload your Git projects and collaborate with teammates.

Git = tool, GitHub = platform.

----

. What is a repository?

A repository (repo) is just a special folder for your project. Inside it, Git keeps all the history, branches, and commits

----

. What does git push do?

git push : “Send my changes to GitHub”.

----

. What does git pull do?

git pull : “Bring the latest changes from GitHub to my computer.”

----

. What is origin?

Origin → The nickname Git gives to your main online repo (usually GitHub).

----

. What is a branch?

Branch : A separate workspace inside your repo. You can experiment without messing up the main code.

----

. What is a fork?

Fork : Your own copy of someone else’s repo on GitHub. You can play with it freely.

----

. What is a Pull Request?

Pull Request (PR) : A polite way of saying: “Hey, I made changes. Can we merge them into the main project?”

----

. Why do developers use branches?

Developers use branches because they don’t want to break the main project. It’s like working on a draft before publishing. Each feature or bug fix gets its own branch, then later merged when ready.

----

. Explain the complete GitHub workflow from changing code to creating a PR .

GitHub workflow :


. Clone the repo : Copy the project from GitHub to your computer.
(git clone <repo-url>)

. Create a branch : Start fresh for your feature.
(git checkout -b my-feature
)

. Make changes : Edit files, add new code.

. stage changes : Tell Git which files you want to save.(git add file.py)

. Commit changes : Save a snapshot with a message.(git commit -m "Added login feature")

. Push branch to GitHub : Upload your work.(git push origin my-feature)

. Open a Pull Request : On GitHub, ask to merge your branch into main.

. Review & approve : Teammates check your code, suggest fixes.

. Merge PR : Your branch joins the main project.

. Pull updates locally : Sync your computer with the latest version.(git pull origin main)