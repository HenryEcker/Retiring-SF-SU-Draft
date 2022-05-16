Personally, as much as I appreciate the idea of giving as detailed feedback as possible, I think giving lists of options is not the correct approach as:
- any list will eventually go out of date as new sites are added (or removed) from the network
- we are limited to 500-characters and standard(ish) markdown rules

For this reason, I'd prefer to have a general "not about programming or development" closure reason, and provide the general list of sites rather than trying to enumerate every possible location for every type of question. I've instead chosen to link to [on-topic](https://stackoverflow.com/help/on-topic) which already covers where to ask many types of questions. This practice is also consistent with our existing closure reasons and the closure reasons of many other communities network wide.


This is the proposed guidance:

<!-- 
    PLEASE DO NOT EDIT THIS TABLE 

If there are issues that need to be addressed please leave a comment so the character length and images can be updated
-->
| Field | (Rendered) Markdown | Markdown Length |
|:---|:---|:---|
| Brief Description | Not about programming or software development | 45 |
| Usage guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). It _may_ be able to be answered on [another Stack Exchange site](https://stackexchange.com/sites) but is not on-topic for $SiteName. | 283 |
| Post notice close description | **Closed.** This question is [not about programming or software development](/help/closed-questions). It is not currently accepting answers. | 140 |
| Post owner guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). You can edit the question so it’s [on-topic](/help/on-topic) or see if it can be answered on [another Stack Exchange site](https://stackexchange.com/sites), but be sure to read the on-topic page for the site you choose before posting. | 385 |
| Privileged user guidance | This question does not appear to be about [a specific programming problem, software algorithm, or tools commonly used by programmers](/help/on-topic). If you believe the question is on-topic on [another site on the Stack Exchange Network](https://stackexchange.com/sites) you can leave a comment to explain where the question may be able to be answered. | 353 |

---

As I was working on these reasons, I realised it was dificult for me to conceptualise what these reasons would feel like in situ so I have created a mock closure dialogue and some mock close banners.

The close dialogue would look something like:\
[![Close Dialogue with new closure reasons and no SF or SU close reasons][1]][1]

Post Owners would see the following message:\
[![Post owner guidance][2]][2]

Privileged Users would see the following:\
[![Privileged user guidance][3]][3]

Anonymous Users and users with less than 3000 reputation would see the following:\
[![Every user guidance][4]][4]

---

This should be able to support the prior closure reasons as it represents the essence of why "general computing hardware and software" and "professional server or networking-related infrastructure administration" are off topic.

It should also cover many of the custom close reasons currently being used. For Example:

|Category| Approx # of Variants<sup>1</sup>| Approx # of posts (last 30 days)<sup>1</sup> |
|:---|:---|:---|
| ML/DL/AI theory and/or methodology | ~8 | ~230 |
| Not about Programming as definied in \[help\] |~34| ~206 |
| Webmasters | ~4 | ~47|
| Mathmatics |~1| ~3|
| DataScience |~1| ~3|



<sup>1</sup> Values were aggregated with the highly accurate and extremely technical method of "by hand" from [question close stats](https://stackoverflow.com/tools/question-close-stats?daterange=last30days). Custom closure reasons are considered distinct unless they match spelling and punctuation _exactly_ so finding all variants and their associated amounts is non-trivial.


---

I would like to acknowledge that these reasons are the derivied from many different users network wide. My hope was to create reasons with guidance and links that were consistent with our existing reasons, help center, and MSO. I also pulled the current community-specific closure reasons for every community on the Stack Exchange network to see how they handle off-topic questions on their relative sites. My hope is not that this guidance is revolutionary or groundbreaking, but rather something that is familiar and can be easily adopted by our community.

A special thanks to [Oleg Valter](https://meta.stackoverflow.com/users/11407695) and [Ryan M](https://meta.stackoverflow.com/users/208273) for their assistance in getting this proposal into somewhat reasonable form, as well as everyone who participated in the initial [close reasons and guidance project](https://meta.stackoverflow.com/q/417475/15497888) and in [Overhauling our community's closure reasons and guidance](https://meta.stackoverflow.com/q/417008/15497888).


  [1]: ./builders/img_output/mock-close-dialogue-rendered.png
  [2]: ./builders/img_output/mock-private-banner-rendered.png
  [3]: ./builders/img_output/mock-privileged-banner-rendered.png
  [4]: ./builders/img_output/mock-public-banner-rendered.png
