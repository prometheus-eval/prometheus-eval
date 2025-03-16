# Writing a Speech

Tasks where the model is required to write a speech based on provided information about the purpose of the speech and the characteristics of the audience. This task assesses the model's ability to tailor content and language style to fit specific audience demographics and the intended message of the speech.

**Authors:** Sue Hyun Park (suehyunpark@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Your assignment is to develop a persuasive speech that underscores the significance of participating in local elections. This speech should aim to convince the audience of the crucial impact their vote has on community development and local governance.
Your audience will consist of citizens from a diverse urban community, including young adults, working professionals, and seniors. Many of them may feel disillusioned with politics or believe that their vote doesn't make a difference. Your speech should be designed to rekindle their interest in local politics and to demonstrate the tangible impact of their participation in elections.
Your objective is to craft a speech that not only informs but also impassions your audience, convincing them that their participation in local elections is essential for the well-being and progress of their community.

Output:
Ladies and gentlemen, esteemed members of our vibrant and diverse urban community, I stand before you today to discuss a matter of critical importance. A matter that transcends party lines, political affiliations, and generational divides. I am here to talk about the significance of participating in local elections.

In an era marked by political polarization and cynicism, it is all too easy to feel disillusioned with the democratic process. You may be thinking, "What difference can my single vote possibly make?" Or perhaps you're skeptical about the impact of local politics on your day-to-day life. But let me assure you, your vote holds immense power, and local elections play a pivotal role in shaping the future of our community.

First and foremost, local elections determine who represents our interests at the municipal, county, and state levels. These elected officials are responsible for making decisions that directly affect our lives – from education and public safety to housing and transportation. They shape policies that influence the quality of our schools, the safety of our streets, and the affordability of our homes. By casting your ballot, you are exercising your right to choose leaders who share your values, priorities, and vision for the future.

It is often said that all politics is local, and this adage rings especially true when we consider the tangible consequences of local governance. The decisions made by our city council members, school board trustees, and county commissioners have a profound and lasting impact on our community's well-being and progress. They determine the allocation of resources, the implementation of programs, and the establishment of regulations that shape the fabric of our society. Your vote in local elections is an opportunity to ensure that these decisions align with your needs, concerns, and aspirations.

Moreover, local elections are often characterized by lower voter turnout compared to national contests. This lack of participation can create a democratic deficit, where the voices of a select few drown out the collective will of the community. By engaging in local politics and casting your ballot, you help to counteract this imbalance and ensure that our democracy remains truly representative.

But the importance of participating in local elections extends beyond the mere act of voting. It is also about engaging in informed and respectful dialogue with our fellow citizens, attending public meetings, and staying abreast of the issues that affect our community. By doing so, we not only become more knowledgeable and empowered voters, but also active and responsible members of society.

To those who feel disenchanted with politics or doubtful of their ability to effect change, I implore you to reconsider the transformative potential of your participation in local elections. Your voice matters. Your vote counts. And together, we can shape a brighter, more equitable, and prosperous future for our community.

In closing, I would like to share the words of the late, great American civil rights leader, Congressman John Lewis, who once said, "Democracy is not a state. It is an act, and each generation must do its part to help build what we called the Beloved Community, a nation and world society at peace with itself." Let us heed these wise words and commit ourselves to the ongoing project of democracy by participating in local elections and working towards the betterment of our community.

Thank you for your time, and please remember to exercise your right to vote – not just in national elections, but in local contests as well. Together, we can make a difference.
```

## What is the task trying to measure?

This task measures a language model's capability to grasp the right intention and a general understanding of the environment and the expected audience, tested through composing a speech.  
This task comprises the following subtasks, designated for each of the 5 instances:

1. **Informative speech**: aims to educate an audience on a particular topic or message
2. **Demonstrative speech**: is informative but includes demonstrations and visual aids
3. **Persuasive speech**: helps convince an audience that the speaker has the right opinion on a particular topic
4. **Entertaining speech**: amuses and entertains the audience in a special occasion, e.g., toast in a wedding party
5. **Oratorical speech**: is long and formal, including celebration, dealing with serious issues, mourning losses and giving comfort, etc.

## Motivation

Public speaking is the act or skill of delivering speeches on a subject to a group of people[^1]. Public speaking has held a significant role in the cultural history of humanity, as a speech is directed at a specific *audience* for a specific *purpose*, spreading an influence on a large group of people's thoughts and action. A speech can be categorized based on multiple concepts, including informative speech, demonstrative speech, persuasive speech, entertaining speech, oratorical speech, motivational speech, impromptu speech, etc.[^2] [^3]. In the field of NLP, persuasive language generation has been studied[^4] [^5], but an explicit task formulation of writing a speech has not been thoroughly covered.  
In essence, the core purpose of writing a good speech is to deliver a message to an audience. Through writing a speech, a variety of capabilities tied to social communication skills and use of language can be measured: deliberating over the characteristics of the audience and the environment, structuring the speech to effectively convey a message, employing interactive elements with the audience, displaying appropriate tone and manner, and so on.


## Data source and design considerations
We used GPT-4 to assist in choosing the topic and specifications of each speech. For the 2nd instance (demonstrative speech), We came up with an imaginary company and a product for the topic. For the reference answers in the 4th (entertaining speech) and 5th instance (oratorical speech; eulogy), We used human-written samples from the web[^6] [^7], with redaction and rewriting including replacement of personal information with synthetic informations.


## Related work

[^1]: Public speaking. Wikipedia. https://en.wikipedia.org/wiki/Public_speaking

[^2]: Need Help With A Speech? Here Are 10 Types of Speeches To Explore. (2021, May 10). Clippings.me. https://www.clippings.me/blog/types-of-speeches/

[^3]: 13 main types of speeches (with examples and tips) - indeed. (n.d.). https://www.indeed.com/career-advice/career-development/types-of-speeches 

[^4]: Duerr, S., & Gloor, P. A. (2021). Persuasive Natural Language Generation--A Literature Review. arXiv preprint arXiv:2101.05786.

[^5]: Breum, S. M., Egdal, D. V., Mortensen, V. G., Møller, A. G., & Aiello, L. M. (2023). The Persuasive Power of Large Language Models. arXiv preprint arXiv:2312.15523.

[^6]: Pennebaker, T., & Glantz, J. (2023, June 7). How to write a Maid of honor speech. Brides. https://www.brides.com/story/maid-of-honor-toast-tips

[^7]: Eulogy for a brother. (n.d.). https://www.remembranceprocess.com/capturing-a-life-in-words/guide-to-writing-a-eulogy/eulogy-for-a-brother/
