# Contributing and Adapting
The Hudson Republic is a sovereign entity, but it also acts as a global governance standard known as the **“Beaver Standard.”**  
This document outlines how to contribute to the project or adapt it for independent use.

## Contribution Workflow
Due to legislative restrictions, contributions follow an issue-based process:

1. Fork the repository (optional for drafting changes).  
2. Prepare your proposed change, amendment, or addition.  
3. Open an Issue describing:
   - The proposal or concern  
   - Affected files or acts  
   - Suggested changes (if applicable)  
4. Authorized legislative members review the submission.  
5. Approved changes are formalized and merged by elected officials.  

Direct pull requests from non-authorized contributors are not accepted.

## Notes About Forking

### Pull Request Support
Pull requests are restricted to authorized collaborators. Only elected officials may submit pull requests for their respective legislative house. This preserves the integrity of the legislative process.  

See the **[Legislative Framework Act](https://github.com/usrmusicman/hudson_republic_main/blob/master/laws/docs/CA/CA_LEGISLATIVEFRAMEWORK_20260401.md)** and **[Legislative Document Classification and Naming Convention Act](https://github.com/usrmusicman/hudson_republic_main/blob/master/laws/docs/CA/CA_NAMINGCONVENTION_20260401.md)** for details.

### Assets, Culture, Language
Use of beaver imagery is permitted, but independent projects are encouraged to adopt their own cultural symbols, legislative structures, and assets. The Hudson Republic provides a working governance model built on DVCS principles.

## Forking (Other Projects)
Forking creates a derivative repository for independent development, experimentation, or drafting proposals prior to Issue submission.

### GUI Creation (Web Interface)

**Create a fork**:

**1.** Navigate to the **[Hudson Republic Official Repository](https://github.com/usrmusicman/hudson_republic_main)**.  
**2.** Click the **Fork** button.  
**3.** Choose your account as the owner and give the forked repository a name.  
**4.** Create a brief memorable description.  
**5.** Choose to copy only the main branch or the whole repository (including all branches).  
**6.** Click **Create fork**.

**Optional (local setup)**:

**7.** `git clone https://github.com/<fork-owner>/hudson_republic_main.git`  
**8.** `git remote -v`  
**9.** `git remote add upstream https://github.com/usrmusicman/hudson_republic_main.git`

See **[Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)** for more details.

**Create an issue**:

**Make sure to include**
- Purpose of the proposal or concern.
- Relevant files or acts.
- Suggested changes or rationale.

**1.** Navigate to the **[Hudson Republic Official Repository](https://github.com/usrmusicman/hudson_republic_main)**.  
**2.** Under your repository name, click **Issues**.  
**3.** Click **New Issue**.  
**4.** Add a title and a description.  
**5.** Click **Create**.

See **[Quickstart for GitHub Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/quickstart)** for more details.

### CLI Creation (Terminal Application)

Follow these steps to create a fork:

**1.** Install the GitHub CLI package and make sure bash is the default shell.  
**2.** `gh repo fork <fork owner>/hudson_republic_main --remote-name <your repository's name> --clone`

Updating from upstream:

**1.** `git pull upstream master`  
**2.** `git push <your repository's name> <branch name>`

Create an issue:

**Make sure to include**
- Purpose of the proposal or concern.
- Relevant files or acts.
- Suggested changes or rationale.

**Type**:  
`gh issue create --title "Subject of Concern --body "Proposed Change or Concern --web`
