Personally, as much as I appreciate the idea of giving as detailed feedback as possible, I think giving lists of options is always going to result in either overwhelming the asker or producing incorrect referrals.

In this specific case, I'd prefer to have a general "not about programming or development" closure reason, and provide the general list of sites rather than trying to enumerate every possible location for every type of question (especially given the 500-character limit). I've instead chosen to link to [on-topic](https://stackoverflow.com/help/on-topic) which already covers where to ask many types of questions. This practice is also consistent with our existing closure reasons and the closure reasons of many other communities network wide.


For this reason I propose something along the lines of:

| Field | (Rendered) Markdown | Markdown Length |
|:---|:---|:---|
| Brief Description | Not about programming or software development | 45 |
| Usage guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). It _may_ be able to be answered on [another Stack Exchange site](https://stackexchange.com/sites) but is not on-topic for $SiteName. | 283 |
| Post notice close description | **Closed.** This question is [not about programming or software development](/help/closed-questions). It is not currently accepting answers. | 140 |
| Post owner guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). You can edit the question so it’s [on-topic](/help/on-topic) or see if it can be answered on [another Stack Exchange site](https://stackexchange.com/sites), but be sure to read the on-topic page for the site you select prior to posting. | 387 |
| Privileged user guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). If you believe the question is on-topic on [another site on the Stack Exchange Network](https://stackexchange.com/sites) you can leave a comment to explain where the question may be able to be answered. | 353 |

This would make the close dialogue appear something like:\
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


  [1]: ./builders/img_output/mock-close-dialogue-rendered.png
  [2]: ./builders/img_output/mock-private-banner-rendered.png
  [3]: ./builders/img_output/mock-privileged-banner-rendered.png
  [4]: ./builders/img_output/mock-public-banner-rendered.png
