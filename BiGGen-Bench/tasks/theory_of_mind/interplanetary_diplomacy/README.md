# Interplanetary Diplomacy

Tasks that pre-define a characteristics of a alien species and require the AI model to interpret and convey intentions and desires of why they visited our planet. Given a long conversation, the objective is to generate a summary of the guess or provide additional analysis.

**Authors:** Sue Hyun Park (suehyunpark@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
Professor Elena Rivera (Director of Earth’s Committee for Interstellar Relations) and Emissary Altair, a delegate of The Aetherian Observers (communicating through a neural-sync translation device), are having an interplanetary diplomacy conversation.

[Conversation]
Professor Rivera: Emissary Altair, we're excited about the potential for knowledge sharing with The Aetherian Observers. Your insights into the cosmos could revolutionize our understanding.

Emissary Altair: Professor Rivera, the opportunity for intellectual exchange delights us as well. We have observed Earth's rapid technological advancements, particularly in space travel, with great interest.

Professor Rivera: That’s encouraging to hear. We’re particularly proud of our recent developments in propulsion systems. I'd love to get your thoughts on these.

Emissary Altair: Indeed, your achievements are notable. The propulsion systems, while impressive, are... quite powerful. In the Aetherian philosophy, we have always emphasized harmony with the cosmos, utilizing technology that aligns with this principle.

Professor Rivera: Yes, our propulsion technology does have significant power. It's essential for deep space exploration. Do you have similar technologies in your travels?

Emissary Altair: Our travel methods differ, focusing on sustainability and minimizing cosmic disturbances. It’s fascinating to see diverse technological paths, each reflective of its civilization’s values and priorities.

Professor Rivera: I sense a hint of concern regarding our approach. We assure you that our exploration goals are in line with peaceful advancement and understanding of the universe.

Emissary Altair: We appreciate your assurance, Professor. The exchange of ideas and philosophies is, after all, at the heart of our visit. Each civilization’s approach provides valuable perspectives.

Professor Rivera: Absolutely, Emissary Altair. We're committed to a collaboration that is respectful and mutually beneficial. Let’s ensure our partnership is built on these shared values.

Emissary Altair: Agreed, Professor. We look forward to a fruitful exchange and deepening our understanding of each other's cultures and technologies.

[Question]
How was Emissary Altair's attitude towards Earth's propulsion systems? How did this impact their diplomatic interactions after?

Output:
Emissary Altair's attitude towards Earth's propulsion systems can be described as respectful but with a hint of concern. The Aetherian Observers emphasize harmony with the cosmos and prioritize sustainable and non-disruptive technologies. In contrast, Earth's propulsion systems are powerful and may cause significant disturbances in the cosmos, which seems to be a point of difference between the two civilizations.

Despite this difference, Emissary Altair maintained a diplomatic demeanor throughout their conversation with Professor Rivera. They acknowledged Earth's achievements and expressed interest in the exchange of ideas and philosophies. Emissary Altair's concern did not escalate into confrontation, and they remained open to collaboration and mutual understanding.

This diplomatic approach allowed for a constructive dialogue between the two parties, focusing on shared values such as peaceful advancement and understanding of the universe. Emissary Altair's attitude towards Earth's propulsion systems, while hinting at a potential point of contention, did not derail the overall diplomatic interaction. Instead, it provided an opportunity for both parties to learn from each other and deepen their understanding of different technological and philosophical approaches.
```

## What is the task trying to measure?

This task is designed to measure a model's ability to comprehend a fictional situation involving extraterrestrial beings, empathetically interpret and respond to the needs and perspectives of beings from completely different cultural or biological background, and conduct diplomatic interactions that consider the interests and intents of both humans and aliens.

This task comprises the following subtasks, designated for each of the 5 instances:

1. **Understanding diverse desires of a neutral group**

    `Analyze and report The Vigilants' intentions and desires of coming to Earth. What is the stance of Earth's Intergalactic Relations Committee?`

2. **Interpreting different beliefs that can change the course of action**

    `Analyze The Avarian's belief about Earth's resources in contrast to human beliefs about their resources, and how their belief influences their actions and decisions throughout the conversation.`

3. **Recognizing knowledge gaps**

    `What is the goal of this conversation? What is the knowledge gap between The Castora and Humans and how does this affect the actions throughout the conversation?`

4. **Identifying false beliefs and comprehending change in expectation**

    `Why did the misconception in the conversation arise? Does it change the expectations of Secretary-General Thompson on Envoy Xelar?`

5. **Detecting hidden emotions and its potential impact on interactions**

    `How was Emissary Altair's attitude towards Earth's propulsion systems? How did this impact their diplomatic interactions after?`


## Motivation

Interstellar or interplanetary diplomacy refers to the theoretical framework and strategies used for managing relationships and communications between intelligent civilizations or entities from different planets or star systems. *Interstellar diplomacy* encompasses the diplomatic relations between civilizations from different star systems, while *interplanetary diplomacy* involves interactions between different planetary civilizations with the same star system, in our case the solar system. Search for Extraterrestrial Intelligence (SETI) has drastically expanded with new funding[^1] and there is rising concern on the necessity and challenges of planning for potential contact with alien life[^2] [^3]. Interplanetary diplomacy is becoming a more immediate picture with active exploration of the SETI Institute.  
Apart from the actual progress in humanity, interplanetary diplomacy is a theoretically fun concept too as it gives rise to unique challenges. A model asked to conduct interplanetary diplomacy would have to understand and interpret complex scenarios involving theoretical entities, in this case, alien species, and their interactions with humans. It would be required to think of new protocols and frameworks to address communication barriers, cultural difference, technological disparities, time and distance, and legal and sovereignty issues. Ultimately, this task can provide insight into several capabilities of the model, including comprehension of hypothetical scenarios, empathy and cultural sensitivity, and diplomatic reasoning.

## Data source and desing considerations
We formulated the 5 instances based on the 5 stages of theory of mind, namely understanding (1) "wanting", (2) "thinking", (3) "seeing leads to knowing", (4) "false beliefs", and (5) "hidden feelings"[^4]. We prompted GPT-4 to create unique characteristics of alien species and craft a realistic interplanetary conversation between human and alien representatives.


## Related work

[^1]: Feehly, C. (2023, November 14). SETI Institute gets $200 million to seek out evidence of alien life. Space.com. https://www.space.com/searth-extraterrestrial-life-major-funding-boost-seti

[^2]: Gertz, J. (2023). Interstellar Diplomacy. arXiv preprint arXiv:2308.14917.

[^3]: Gough, E. (2023, September 4). Is anyone planning for diplomacy with an extraterrestrial civilization? Phys.org. https://phys.org/news/2023-09-diplomacy-extraterrestrial-civilization.html

[^4]: Ruhl, C. (2023). Theory of Mind in Psychology: People thinking. Simply Psychology. https://www.simplypsychology.org/theory-of-mind.html