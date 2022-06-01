# Class Hedgehog
Evening Python Fullstack bootcamp.
May 23 - Sep 23

Instructor:
- Anthony Wallace
- anthony@pdxcodeguild.com

<hr>

### Rough Timeline
- Weeks 1, 2, 3, 4, 5: Python
- Weeks 6, 7: HTML/CSS/Flask
- Weeks 8, 9, 10, 11: Django
- Weeks 12, 13, 14, 15: Javascript
- Weeks 16, 17, 18: Capstone project

<hr>

### Scheduled Holidays (no class)
- May 30 - Memorial Day
- July 4 - Independence Day
- Sept 5 - Labor Day

<hr>

### Assigned Labs:

<details open>
  <summary>Python</summary>

| Lab Number | Title | Due Date |
| ---------- | ----- | -------- |
| Lab 01     | Code Folder | 07 JUN |
| Lab 02a    | Madlib | 08 JUN |
| Lab 02b    | Make Change | 08 JUN |
| Lab 5      | Palindrome Checker | 10 JUN |

</details>

<hr>

## Submitting your work

Make sure all labs are located within `class_hedgehog/code/<YOUR_NAME>`, where `<YOUR_NAME>` is your first name in all lowercase letters.

To emulate a more professional Git workflow, we're going to start creating new branches for each lab starting in the HTML/CSS section.

<h2>Creating a new branch:</h2>
<details>
<summary>Click to expand</summary>

- `git branch` to check that you're on the main branch, use `git checkout main` to go to the main branch if needed.

- `git status` to check if your local main branch is up to date with origin/main on Github.
- `git pull` if needed to pull any recent changes to your local repository

- Create a new branch and switch to it.

  - Option 1:

    - `git branch <YOUR_NAME-SECTION-LAB_NUMBER>`
    - `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

  - Option 2:

    The `-b` flag can be used after the `checkout` command to combine these two steps:

    `git checkout -b <YOUR_NAME-SECTION-LAB_NUMBER>`

  **e.g.** My branch for the **"Lab 01 - Bio"** in the **HTML/CSS** section would be named: `anthony-htmlcss-lab01`. The name can vary a bit from this example, but please keep the chosen formatting consistent from one lab to another.

- `git add <FILENAME>` to add a specific file or `git add .` to add everything in the current dicrectory
- `git commit -m "your commit message"` to commit your work

- A remote branch will need to be created for each new local branch. Git will usually display the proper command to do this when a new branch is pushed for the first time.

  The command is:

  `git push --set-upstream origin <BRANCH_NAME>`

  **OR**

  `git push -u origin <BRANCH_NAME>`

  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/set_upstream_message.png" width=800>
  </details>

- After successfully pushing your new branch to Github, you should see the option to create a Pull Request for your branch on the main repo page.

  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/pull_request_button.png" width=800>
  </details>

- If you don't see that message, you'll have to navigate to your new remote branch
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/switch_branch.gif" width=800>
  </details>

- Once you've navigated to your individual branch, you'll find the option to create a Pull Request in the "Contribute" dropdown.
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/open_pull_request_alternative.gif" width=800>
  </details>

- Click the "Open Pull Request" button. Add a comment to your Pull Request like "Submitting Lab 00" and click "Create Pull request"
  <details>
    <summary>Screenshot</summary>
    <img src="images/screenshots/create_pull_request.png" width=800>
  </details>
</details>

## Updating a branch

<details>
<summary>Click to expand</summary>
After a Pull Request is submitted, the code on that branch will be checked.

Necessary corrections or adjustments will be posted as comments on the Pull Request on Github and the Pull Request will be closed. When the corrections are made, submit the Pull Request again for checking.

Corrections will be made only to that particular branch.

- `git checkout <YOUR_NAME-SECTION-LAB_NUMBER>`

- Add and commit updated files.

- `git push` to push your changes up to the remote repository on GitHub

- Only one Pull Request is allowed per branch.

  - If a Pull Request is already open for the branch, a message will be added to the current Pull Request for the new commits.
  - If a Pull Request is not already open for the branch a new Pull Request will need to be created.

- Once a lab is complete, its branch will be merged into the `main` branch.
</details>

---
