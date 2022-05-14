Personally, as much as I appreciate the idea of giving as detailed feedback as possible, I think giving lists of options is always going to result in either overwhelming the asker or provide incorrect referrals.

In this specific case, I'd prefer to have a general not about programming or development closure reason, and provide the general list of sites rather than trying to enumerate every possible location they could ask for every type of question (especially given the 500-character limit). I've instead chosen to link to [on-topic](https://stackoverflow.com/help/on-topic) which already covers where to ask many types of questions. This practice is also consistent with our existing closure reasons, and many other communities network wide.


For this reason I propose something along the lines of:

| Field | (Rendered) Markdown | Markdown Length |
|:---|:---|:---|
| Brief Description | Not about programming or software development | 45 |
| Usage guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). It may be on-topic on [another site on the Stack Exchange Network](https://stackexchange.com/sites), but cannot be answered on $SiteName. | 288 |
| Post notice close description | **Closed.** This question is [not about programming or software development](/help/closed-questions). It is not currently accepting answers. | 140 |
| Post owner guidance | This question does not appear to be about a specific programming problem, software algorithm, or tools commonly used by programmers. You can edit the question so it’s [on-topic](/help/on-topic) or see if it can be answered on [another site on the Stack Exchange Network](https://stackexchange.com/sites). | 304 |
| Privileged user guidance | This question does not appear to be about a specific programming problem, software algorithm, or tools commonly used by programmers. If you believe the question is on-topic on [another site on the Stack Exchange Network](https://stackexchange.com/sites) you can leave a comment to explain where the question may be able to be answered. | 335 |

This would make the close dialogue appear as:\
[![Close Dialogue with new closure reasons and no SF or SU close reasons][1]][1]

Post Owners would see the following message:\
[![Post owner guidance][2]][2]

Privileged Users would see the following:\
[![Privileged user guidance][3]][3]

Anonymous Users and <3k users would see the following:\
[![Every user guidance][4]][4]

---

This should be able to support the prior closure reasons as it represents the essence of why "general computing hardware and software" and "professional server or networking-related infrastructure administration" are off topic.

It should also cover many of the custom close reasons currently being used. This new reason could adequantly cover the following custom reasons as well:

|Category| Approx # of Variants<sup>1</sup>| Approx # of posts (last 30 days)<sup>1</sup> |
|:---|:---|:---|
| ML/DL/AI theory and/or methodology | ~8 | ~230 |
| Not about Programming as definied in \[help\] |~34| ~206 |
| Webmasters | ~4 | ~47|
| Mathmatics |~1| ~3|
| DataScience |~1| ~3|



<sup>1</sup> Values were aggregated with the highly accurate and extremely technical method of "by hand" from [question close stats](https://stackoverflow.com/tools/question-close-stats?daterange=last30days). Custom closure reasons are considered distinct unless they match spelling and punctuation _exactly_ so finding all variants and their associated amounts is non-trivial.


  [1]: https://i.stack.imgur.com/sdGdy.png
  [2]: https://i.stack.imgur.com/XdqIkl.png
  [3]: https://i.stack.imgur.com/UiOtkl.png
  [4]: https://i.stack.imgur.com/j9gygl.png
