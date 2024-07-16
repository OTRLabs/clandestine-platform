## Projects, tasks, issues, etc

Fundamentally, the real benefit comes from the quality of the information logged in the database. So it is critical we have strong foundations for how we segment anything related to “planning” 

Some things we want to 

projects are the base “unit” of planning measurement. Projects can contain:

- name
- Description
- Scope: target assets. Infrastructure, people, etc
- Out of scope: assets the target has clarified are not the target objective. Scanners should ignore them.
- milestones: Markers for reaching a “level of progress”
- Components: key elements of a project. Infrastructure, software, planned capabilities, features of your projects capabilities
- tasks: an individual action that can generally be thought of as comparable to a GitHub issue. They include the ability to have markdown content, tags, etc.

They can have the following entities linked:

- repositories in a Git provider

We will create “template” projects. For instance based off of:

- mitre Att&ck framework
- Cyber kill chain
- Malware development timeline
- Bug bounty
- Penetration test
- Red team engagement
- Purple team engagement