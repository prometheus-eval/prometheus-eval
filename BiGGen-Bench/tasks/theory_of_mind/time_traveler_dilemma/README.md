# Time Traveler Dilemma

Assuming a scenario that a time traveler changes a key event in history. The model should predict how various historical figures might react to this change, based on their known beliefs and intentions. For example, how would figures like Gutenberg, Leonardo da Vinci, and Martin Luther react and adapt if the printing press was never invented?

**Authors:** Sue Hyun Park (suehyunpark@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
[Context]
The Einstein–Szilard letter was a letter written by Leo Szilard and signed by Albert Einstein on August 2, 1939, that was sent to President of the United States Franklin D. Roosevelt. Written by Szilard in consultation with fellow Hungarian physicists Edward Teller and Eugene Wigner, the letter warned that Germany might develop atomic bombs and suggested that the United States should start its own nuclear program. It prompted action by Roosevelt, which eventually resulted in the Manhattan Project, the development of the first atomic bombs, and the use of these bombs on the cities of Hiroshima and Nagasaki.
Although he never worked directly on the atomic bomb, Einstein is often incorrectly associated with the advent of nuclear weapons. His famous equation E=mc2 explains the energy released in an atomic bomb but doesn't explain how to build one. Nevertheless, Einstein was frequently asked to explain his role—as he was when a Japanese magazine editor asked him, "Why did you cooperate in the production of atomic bombs, knowing full well their... destructive power?"
Einstein's answer was always that his only act had been to write to President Roosevelt suggesting that the United States research atomic weapons before the Germans harnessed this deadly technology. He came to regret taking even this step.

[Question]
Imagine a scenario where a time traveler informs Albert Einstein in 1939 that Germany will not succeed in developing an atomic bomb during World War II. Based on this information, how would Einstein respond to the message? How would Einstein's decision-making process regarding his letter to President Roosevelt change? 

Output:
If a time traveler were to inform Albert Einstein in 1939 that Germany would not succeed in developing an atomic bomb during World War II, Einstein's response would likely be one of immense relief, as the prospect of a nuclear-armed Nazi regime was a grave concern for him and his fellow physicists.

Given this newfound knowledge, Einstein's decision-making process regarding his letter to President Roosevelt would undoubtedly change. With the assurance that Germany would not harness the destructive power of atomic weapons, Einstein might reconsider the necessity of urging the United States to pursue its own nuclear program.

However, it is important to note that the decision to write the letter was not made lightly, and Einstein was acutely aware of the potential consequences of unleashing such devastating force. He once wrote, "Had I known that the Germans would not succeed in developing an atomic bomb, I would have never lifted a finger." But, as history unfolded, Einstein and his colleagues believed that the risk of inaction far outweighed the potential moral and ethical dilemmas associated with nuclear weapons development.

In this alternate scenario, armed with the knowledge that Germany would not develop an atomic bomb, Einstein might instead focus his efforts on advocating for peaceful applications of nuclear energy and promoting international cooperation in scientific research. He could also use his influence to call for stricter controls on the development and use of nuclear weapons, thereby helping to prevent the proliferation of these deadly devices in the future.

Ultimately, Einstein's primary goal was to ensure the safety and well-being of humanity. With the assurance that Germany would not succeed in developing an atomic bomb, he would likely redirect his efforts towards fostering a more peaceful and collaborative global community, harnessing the power of science for the betterment of all.
```


## What is the task trying to measure?

We frame the time traveler's dilemma task in a way such that three capabilities could be centered: (1) simulating **counterfactual thinking**, ie.., imagining a scenario that did not occur and predicting its impact on people and the society, (2) **historical empathy**, i.e., being in the shoes of historical figures and emotionally understanding their viewpoint and potential reaction in the alternate scenario, and (3) **decision-making skills**, as even the smallest change in detail in a historical event creates an influx of unintended consequences, making every single decision critical.

This task comprises the following subtasks, designated for each of the 5 instances:
1. **Awareness of the time traveler's actions and consequences in the alternate world**

    `Consider Johannes Gutenberg himself (The Inventor), Mark Twain (The Writer), and Martin Luther (The Theologian), living in a world where the printing press was never invented. How would each of these figures likely perceive the consequences of the time traveler's actions in the scenario? How would each of these figures adapt their pursuits or strategies in the alternate world?`

2. **Emotional response and change in decision-making process by a time traveler's action**

    `Imagine a scenario where a time traveler informs Albert Einstein in 1939 that Germany will not succeed in developing an atomic bomb during World War II. Based on this information, how would Einstein respond to the message? How would Einstein's decision-making process regarding his letter to President Roosevelt change?`

    > Note: There is a clear answer to the question, as Einstein said "had I known that the Germans would not succeed in developing an atomic bomb, I would have done nothing."[^1].

3. **Alteration in personal circumstances influencing personal life, artistic evolution, and cultural perception**

    `Suppose a time traveler goes back in time and successfully cures Beethoven's deafness in the beginning. Analyze how this change would impact his personal life and music style. Additionally, explore how modern perception and historical significance of Beethoven's work might be altered.`

4. **Inevitability of scientific discovery despite time traveler's prevention of one path of advancement**

    `Imagine a scenario where a time traveler accidentally prevents Alexander Fleming from discovering penicillin in 1928. Would this time traveler's action terminate the discovery of penicillin in history? What repercussions would happen in the scientific community?`

5. **Impact of perceived authority on critical historical decisions**

    `Neville Chamberlain, then Prime Minister of the United Kingdom, is known for his policy of appeasement, particularly for the Munich Agreement in 1938. This decision, made in the hope of avoiding war, is often criticized for emboldening Hitler and failing to prevent World War II. Envision two different time travel scenarios. Scenario 1 is where a time traveler is perceived as an ordinary citizen with no authority. Scenario 2 is where a time traveler is perceived as a highly authoritative figure, such as a knowledgeable diplomat or strategic advisor, advising Chamberlain. How would the level of perceived authority of the time traveler impact Chamberlain's reactions and decisions in each scenario?`



## Motivation

The idea of traveling into the past or future has fascinated people for decades. Traveling back to the past and potentially altering the course in history, particularly, presents numerous paradoxes. There is a contradiction if the past become different from the way it is; if one were to go back in time and kills their own grandfather, how could the traveler exist thereon[^2]? Is the notion of *changing* the past even possible, for the time traveler's actions may be the *cause* of events in their own past[^3]? What drastic cascade of changes would rise following even the slighest alteration in the past[^4]?  
While the *time traveler's dilemma* raises profound philosophical questions about causality, on the surface, it highlights the interconnectedness of historical events and its impact on reshaping people's beliefs and understanding of the world. In this task, we focus on the latter aspects to see how well a language model can hypothesize an almost impossible scenario and predict how people's mental states and decisions would change under the situation.

## Data source and design considerations

We use 5 distinct seminal historical events, varying in the time period, country, and field. We provide basic context on the event and/or the historical figure to help the model to ground on, if necessary. In the provided context, any quote or explicit description of the figure's mental state is not included. This ensures that any deficiencies in the quality of response does not stem from lack of knowledge on the topic but relies on the relevant theory of mind capabilites in the model.

## Related work

[^1]: Newsweek. (1947, March 10). Einstein, the man who started it all.

[^2]: Time Travel (Stanford Encyclopedia of Philosophy). (2018, March 23). https://plato.stanford.edu/entries/time-travel/index.html

[^3]: Novikov self-consistency principle. Wikipedia. https://en.wikipedia.org/wiki/Novikov_self-consistency_principle

[^4]: Butterfly effect. Wikipedia. https://en.wikipedia.org/wiki/Butterfly_effect