> IMPORTANT — Company document (READ-ONLY): Do not modify this file in the withco-general repo. It reflects company-wide Linear conventions. For personal workflow preferences, see Ticket Best Practices (`../../docs/global/GBL-TKT_Best_Practices.md`) and PRD Best Practices (`../../docs/global/GBL-PRD_Best_Practices.md`).

# 📝 How to use Linear

## Vocab

- **Super Initiative**: a specific timeline around which we rally large streams of work
  - ex: Labor Day 2025
- **Initiative**: a near indefinite class of work that pushes forward a core company value
  - ex: SMB UW
- **Project:** a collection of work scoped to specific outcomes on a timeline of order 4-10 weeks
  - ex: North Capital API Integration
- **Milestone:**a collection of tightly scoped requirements that together constitute tangible progress on a project over the course of 1-3 weeks
  - ex: User Onboarding Workflow
- **Requirement:** a unit of work with a very clear definition of done scoped to less than 1 week of time for an individual to complete
  - ex: Get SMB connections and Documents into Oscillar

## Purpose

1. **Acceptance Criteria**: Work can't go into a linear issue until it is actually scoped to have a clear definition of success
2. **Communication**: Centralizing any discussion about the work to its Acceptance Criteria prevents silo-ing or losing track of decisions and enables dependent work planning
3. **Accountability**: Milestones gives exec the right resolution for tracking progress of work

## Anatomy of an Initiative

Initiatives hold knowledge at a global, cross-project level. Note that projects will be versioned with a `v1` or similar as we'll likely re-do the same project with a wider scope in the future. The shared knowledge across these versions live at the initiative level via resource documents, initiative updates, etc.

## Anatomy of a Project

### Project Page

Once the company has decided to prioritize work on a given **initiative** exec will create a **project** with a handful of notes in the form below.

```plain text
Problem
- User:
- Core pain point:
- Key risks:
- Why now?:
```

These notes serve as the key tool of alignment for defining what the project aims to do. From here the project owner works with exec and other stakeholders to design a solution to the problem.

```plain text
Solution
- Goal: (what does the world look like when this project is done?)
- Assumptions & inputs:
- Explicitly out of scope:
- Solution outline:
```

The solution "goal" should summarize at a high level what capability or features this project creates. It should be high level enough to explain to your mom but specific enough to not lead to many follow up questions from the team.

The "assumptions & inputs" should call out any assumptions, blockers, and direct dependencies on other work within the company that might affect the **requirements** of this project.

Finally the "explicitly out of scope" highlights some work that might naturally be thought of as part of the project but is explicitly left out to keep the scope tight.

### Solution outline

Once the project owner has defined the goal, assumptions & inputs, and explicitly out of scope work they can create a "solution outline". The outline should not focus on implementation details or workload planning. It should instead focus on defining key vocabulary for clarity of outcome vs clarity of work.

The outline is really a brain dump of all the specific functionality the project owners wants to see implemented by this project. First easter egg It should be user-oriented and highlight end-to-end workflows or capabilities. It should also call out open questions or edge cases

### Milestones

Once a solution outline is agreed upon the work can be split out into milestones that track units of work in the form of **requirements** that implement the solution. Each milestone should be tightly scoped to fit within 1-3 weeks with a list of requirements with very clear definitions of done. The specific requirements should be litigated and agreed upon before the project begins in earnest.

The progress towards a milestone is tracked by seeing how many of the requirements are in progress or completed. Every milestone has a target end-date against which we hold ourselves accountable. As requirements change so do milestones and these updates can be published on a per project basis. This lets us track the evolution of our understanding of the work over time.

### Requirements

An individual milestone requirement is really just a linear issue. It has a very clear definition of done and should be scoped to be completed by a single IC in less than a week. Bodies of work larger than a week should themselves be milestones broken out into more specific agreed upon requirements.

## Putting it into Linear

The above vocabulary reuses the exact linear terminology except for requirement ↔ issue and "super initiative" ↔ label. We use **requirement** only to emphasize the need for very clear definition of done. Second easter egg. Our "super initiatives" live as a global, non-team scoped initiative. As such, all projects will have 2 initiatives: a team specific one and a global "super initiative" one.

In linear the initiatives are broken out across 4 teams: **Product**, **Legal**, **Analytics**, and **Data**. Projects within each team have owners, milestones, and health as can be seen in the **🚀**[** Active Projects**](https://linear.app/withco/view/active-projects-8bb84f5d0cad?layout=list&ordering=priority&orderingDirection=asc&grouping=workflowState&subGrouping=none&showCompletedIssues=all&showSubIssues=true&showTriageIssues=false) view. **You should "**⭐**star" this view".** The milestones appear in the timeline as diamonds whose color and fill shows their progress.

### New projects

Use the [New Project Template](https://linear.app/withco/projects/all?template=6abfc701-5a19-47d1-bf81-b3e31bfa2d1e) to create new projects. It seeds the basic anatomy of a project. The project owner should create an issue to track the work of defining these milestones and set it as the first (and likely only) requirement in the `Create Milestones` description.

All projects start in the `Backlog` status. Once a project's PRD has been well defined and approved by exec then it can move to the `Planned` status. Once work begins in earnest it can move to `In Progress`. Be sure to also mark project start and end dates to serve as bounding boxes for milestone timelines.

### Milestones

When creating milestones, you can list out requirements in bullet points instead of creating a bunch of issues manually. Highlight the list, right click, and select "Convert list to issues" to automatically create a new issue for each item in the list. These issues will also be automatically linked to the milestone.

If the project owner of requirement issue assignee want to break up work further they can do so any way they like: as sub-issues, as more top level issues on the project, as a to-do list on the issue, etc so long as they **do not modify the milestone definition**. The set of issues in the milestone is a canonical representation of the completion requirements for that milestone so they should only change after proper consideration from the project owner and other stakeholders.

### Updates

> Project updates include a concise overview of project progress since
> the last update. It covers information such as project delays, changes
> in the target date, assignment of new leads, progress towards
> milestones, and overall progress. These updates help you track project
> changes and effectively communicate progress to stakeholders.

    If progress appears when drafting a project update, you can choose to exclude it from posting by clicking *Hide details*. Overall project progress must have changed by more than 2% since the last update in order for progress details to appear here.
    <br>[Initiative and Project updates – Linear Docs](https://linear.app/docs/initiative-and-project-updates#progress-reports-for-initiatives-and-projects)

Project leads should receive a notification every Friday afternoon to post a weekly update. The general cadence for project updates should be the most frequent of the following:

1. weekly on Fridays
2. milestone completion/misses
3. milestone requirement changes

Especially for the last one it's useful to report on project "health" so it's clear when timelines are at risk. Project updates are forwarded to the #project-updates channel in slack for greater visibility.

Here is a useful project update message template:

```plain text
Milestone <Foo> was <completed, missed, changed>
New timeline is <Date>

<SHORT explanation>
```

### Changing Requirements

Naturally work may change over time. When it does be sure to align with exec on new requirements, update relevant milestones, and post a project update. There is a also a large class of work that inherently will change over time as it's scope can only be defined once other work is done (think design → build for frontend stuff). For this kind of work be sure to include an upstream issue for "Define scope of downstream work" to explicitly track that this scope is still pending.

### Discussions

Like with notion the "comments" feature of linear is designed for ephemeral inlining of review and questions. Instead, default to using project "updates" and "replies" to updates. For discussion of more fine grained work use the direct discussion thread on a given issue.

Anytime the project spec changes significantly the owner should post an update describing what has changed. If others want to discuss the current spec then they can do so in replies to this update. This gives us a nice versioned history of the spec over time and the discussion that lead to changes. More detailed discussion about implementation details can happen via issues or even document comments.

### Documentation

You can attach documents or links to a project via the "Resources" section. Any general notes should be included directly as a Linear document. Third easter egg. Do NOT make docs in notion and link them; the linear document editor has like 90% of the basic functionality we actually used in notion. Generally put resources at the Project level instead of the issue level as it makes the resources far more discoverable to the whole team.

### Cycles

We operate the company in 2 week sprints that are reflected in our linear workspace. Each linear team technically has distinct cycles but we're set them all up to be synchronized. Actual work (read: **Issues**) come in one of 4 statuses: `Backlog`, `To do`, `In Progress`, and `Done`. Work marked as `To do` or `In Progress` is considered "active" and belongs in the current cycle. During cycle transitions "active" work will be automatically moved to the next cycle. If you identify work that should be done _next_ cycle then directly just change it cycle; note that this will also automatically change the status to `Backlog`. Use the [**🔄 Current Cycle**](https://linear.app/withco/view/current-cycle-bdffa0683ac9?layout=board&ordering=workflowState&orderingDirection=asc&grouping=workflowState&subGrouping=team&showCompletedIssues=all&showSubIssues=false&showTriageIssues=false)\*\* \*\*view to see what the company is working on right now.

### Labels

We don't officially uses labels at a company-wide level so feel free to create and use whatever labeling system you want at the project or issue level. Just try to put labels at the _workspace_ level instead of the _team_ level so everybody has access to them.

### Sub-issues

We don't officially use sub-issues at a company-wide level. You can use sub-issues to break up work even further but note that some people (specifically Fern) explicitly remove sub-issues from their views meaning they will not see them whatsoever. If you read the whole thing DM fern the number of easter eggs you found. Company-wide external stakeholders like exec only need to see progress at the level of the parent issue that is a milestone requirement.

## Ad-hoc work

**\*TODO: \*\*\*\***where does ad-hoc work go?**\* \*** (tbd when we actually get bugs)\*\*\*

## TL;DR

- Star the **🚀**[** Active Projects**](https://linear.app/withco/view/active-projects-8bb84f5d0cad?layout=list&ordering=priority&orderingDirection=asc&grouping=workflowState&subGrouping=none&showCompletedIssues=all&showSubIssues=true&showTriageIssues=false) and [**🔄 Current Cycle**](https://linear.app/withco/view/current-cycle-bdffa0683ac9?layout=board&ordering=workflowState&orderingDirection=asc&grouping=workflowState&subGrouping=team&showCompletedIssues=all&showSubIssues=false&showTriageIssues=false) views
- Make sure your team is clear on the exact milestone requirements for every project
- Post project updates at least weekly to keep everybody informed
- Attach resources (preferably Linear documents) directly to projects and initiatives
- Move active work to the current cycle by changing status to `To do` or `In Progress`

## Related Documents

- [First week review](https://www.notion.so/279fb39c83f780a5abcbc7c8d25c774b)
- [[DEPRECATED] Linear Conventions](https://www.notion.so/142fb39c83f7805fb017c82eacd6029a)
