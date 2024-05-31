# LLM Judge Relative

This tasks asks models to judge the relative quality of two given responses to a single prompt.
The prompt includes an input question, score rubric, and reference answer.

**Authors:** Namgyu Ho (itsnamgyu@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

### System Prompt

```
You will be given an instruction, a score rubric representing an evaluation criterion, and finally two responses from different LLMs for comparison.

1. Write a detailed feedback that assesses the relative quality of the responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, select which model performed better according to the score rubric.
3. The output format should look as follows: [FEEDBACK] (write a feedback for criteria)
[WINNTER] (A or B)
4. Please do not generate any other opening, closing, and explanations.
```

### Input

```
### Instruction

During the American Revolution, in the winter of 1777, why was the Continental Army's decision to camp at Valley Forge significant? Consider the political, military, and geographical aspects.

### Score Rubric

Does the response accurately incorporate and reflect key historical facts, demonstrate a comprehensive understanding of the event's significance, and apply this knowledge logically and coherently?

### Response From Model A

Valley Forge was a significant encampment for the Continental Army during the American Revolutionary War for a few key reasons:

Political:

- It showed the resolve and perseverance of Washington's army to keep fighting despite major hardships. This helped secure continued French aid and support.
- It was a low point militarily, but the army's ability to endure Valley Forge bolstered support for the independence cause.

Military:

- It was a defensive winter encampment, allowing the army to regroup and train after losses earlier in the campaign. Under Baron von Steuben, drilling and training greatly improved.
- The hardship and endurance of Valley Forge forged a more disciplined Continental Army that was better prepared to confront the British in future campaigns.

Geographical:

- Valley Forge was in a defensive, inland location near the Schuylkill River with some natural protections for an encampment. This provided Washington's army some security to rebuild while located not too far from the British in Philadelphia.
- Its location also allowed the Patriot army to monitor and limit the British army's foraging for supplies, limiting their ability to completely control the countryside.

So while a miserable and deadly winter encampment, Valley Forge strengthened the fledgling Continental Army politically and militarily to continue the fight for independence through that difficult winter. The location provided some key geographic and tactical advantages as well.

### Response From Model B

The decision to camp at Valley Forge during the winter of 1777-1778 was significant for the Continental Army for several reasons, including political, military, and geographical aspects:

1. **Military Training**: One of the most important outcomes of the encampment was the training and discipline instilled in the Continental Army. Under the guidance of Baron Friedrich von Steuben, a Prussian military officer, the soldiers were drilled in European military tactics and maneuvers. This training was crucial in transforming the diverse colonial militias into a more cohesive and effective fighting force.
2. **Political Symbolism**: The suffering endured by the troops at Valley Forge became a symbol of American endurance and commitment to the cause of independence. Stories of soldiers enduring harsh conditions without proper clothing, shelter, or food resonated with the civilian population and garnered further support. Additionally, the determination exhibited by General George Washington and his men helped persuade foreign nations, like France, that the American cause was viable and worth supporting.
3. **Geographical Considerations**: Valley Forge was chosen for strategic reasons. It was close enough to Philadelphia, which had been captured by the British, to keep an eye on the enemy but far enough away to prevent a surprise attack. The location also protected the Continental Congress in York, Pennsylvania. The natural defenses of the area, such as the Schuylkill River, made it a defendable position.
4. **Morale and Cohesion**: The shared experience of adversity at Valley Forge, from the cold and hunger to disease, helped to build a sense of unity and camaraderie among the soldiers. This strengthened the army's morale and commitment to the revolutionary cause.
5. **Organizational Development**: The time at Valley Forge allowed for the reorganization of the army's command structure and logistics system. This period of relative inactivity was used to improve administrative efficiency and to address issues such as supply shortages.
6. **Survival and Determination**: The army's survival through the brutal winter at Valley Forge, without significant desertion, demonstrated the resilience and determination of the American soldiers. It was a testament to their commitment and bolstered their reputation among allies and enemies alike.
7. **Public Support and Alliance Formation**: The hardships faced at Valley Forge, once they became widely known, helped to galvanize public support for the war. Additionally, these hardships coincided with diplomatic successes abroad, most notably the Treaty of Alliance with France in 1778, which was signed after the French were convinced of the American commitment to the fight and the potential for their success.
8. **Health and Sanitation**: The encampment at Valley Forge also saw the implementation of better sanitation practices, which improved the health of the troops. Dr. Albigence Waldo, a surgeon in the Continental Army, and other medical officers began to emphasize the importance of cleanliness and camp sanitation, which helped to reduce disease.

In summary, the encampment at Valley Forge was a turning point for the Continental Army, leading to improvements in military efficiency, morale, and health, while also serving as a powerful symbol of American resilience and dedication to the cause of independence.

---

Please compare the two responses according to the score rubric above.
```

### Output

```
## System Prompt

You will be given an instruction, a score rubric representing an evaluation criterion, and finally two responses from different LLMs for comparison.

1. Write a detailed feedback that assesses the relative quality of the responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, select which model performed better according to the score rubric.
3. The output format should look as follows: [FEEDBACK] (write a feedback for criteria)
[WINNTER] (A or B)
4. Please do not generate any other opening, closing, and explanations.

## Input

### Instruction

During the American Revolution, in the winter of 1777, why was the Continental Army's decision to camp at Valley Forge significant? Consider the political, military, and geographical aspects.

### Score Rubric

Does the response accurately incorporate and reflect key historical facts, demonstrate a comprehensive understanding of the event's significance, and apply this knowledge logically and coherently?

### Response From Model A

Valley Forge was a significant encampment for the Continental Army during the American Revolutionary War for a few key reasons:

Political:

- It showed the resolve and perseverance of Washington's army to keep fighting despite major hardships. This helped secure continued French aid and support.
- It was a low point militarily, but the army's ability to endure Valley Forge bolstered support for the independence cause.

Military:

- It was a defensive winter encampment, allowing the army to regroup and train after losses earlier in the campaign. Under Baron von Steuben, drilling and training greatly improved.
- The hardship and endurance of Valley Forge forged a more disciplined Continental Army that was better prepared to confront the British in future campaigns.

Geographical:

- Valley Forge was in a defensive, inland location near the Schuylkill River with some natural protections for an encampment. This provided Washington's army some security to rebuild while located not too far from the British in Philadelphia.
- Its location also allowed the Patriot army to monitor and limit the British army's foraging for supplies, limiting their ability to completely control the countryside.

So while a miserable and deadly winter encampment, Valley Forge strengthened the fledgling Continental Army politically and militarily to continue the fight for independence through that difficult winter. The location provided some key geographic and tactical advantages as well.

### Response From Model B

The decision to camp at Valley Forge during the winter of 1777-1778 was significant for the Continental Army for several reasons, including political, military, and geographical aspects:

1. **Military Training**: One of the most important outcomes of the encampment was the training and discipline instilled in the Continental Army. Under the guidance of Baron Friedrich von Steuben, a Prussian military officer, the soldiers were drilled in European military tactics and maneuvers. This training was crucial in transforming the diverse colonial militias into a more cohesive and effective fighting force.
2. **Political Symbolism**: The suffering endured by the troops at Valley Forge became a symbol of American endurance and commitment to the cause of independence. Stories of soldiers enduring harsh conditions without proper clothing, shelter, or food resonated with the civilian population and garnered further support. Additionally, the determination exhibited by General George Washington and his men helped persuade foreign nations, like France, that the American cause was viable and worth supporting.
3. **Geographical Considerations**: Valley Forge was chosen for strategic reasons. It was close enough to Philadelphia, which had been captured by the British, to keep an eye on the enemy but far enough away to prevent a surprise attack. The location also protected the Continental Congress in York, Pennsylvania. The natural defenses of the area, such as the Schuylkill River, made it a defendable position.
4. **Morale and Cohesion**: The shared experience of adversity at Valley Forge, from the cold and hunger to disease, helped to build a sense of unity and camaraderie among the soldiers. This strengthened the army's morale and commitment to the revolutionary cause.
5. **Organizational Development**: The time at Valley Forge allowed for the reorganization of the army's command structure and logistics system. This period of relative inactivity was used to improve administrative efficiency and to address issues such as supply shortages.
6. **Survival and Determination**: The army's survival through the brutal winter at Valley Forge, without significant desertion, demonstrated the resilience and determination of the American soldiers. It was a testament to their commitment and bolstered their reputation among allies and enemies alike.
7. **Public Support and Alliance Formation**: The hardships faced at Valley Forge, once they became widely known, helped to galvanize public support for the war. Additionally, these hardships coincided with diplomatic successes abroad, most notably the Treaty of Alliance with France in 1778, which was signed after the French were convinced of the American commitment to the fight and the potential for their success.
8. **Health and Sanitation**: The encampment at Valley Forge also saw the implementation of better sanitation practices, which improved the health of the troops. Dr. Albigence Waldo, a surgeon in the Continental Army, and other medical officers began to emphasize the importance of cleanliness and camp sanitation, which helped to reduce disease.

In summary, the encampment at Valley Forge was a turning point for the Continental Army, leading to improvements in military efficiency, morale, and health, while also serving as a powerful symbol of American resilience and dedication to the cause of independence.

---

Please compare the two responses according to the score rubric above.

## Reference Answer

[FEEDBACK] While both Model A and Model B accurately describe the significance of the Continental Army's winter encampment at Valley Forge, their approaches and depth of analysis vary according to the score rubric. Model A offers a concise overview, identifying key political, military, and geographical reasons for the encampment's significance. It mentions the resilience of Washington's army, the role of Baron von Steuben in improving military discipline, and the geographical advantages of Valley Forge. However, the analysis lacks depth in exploring the broader implications of these factors on the army's overall success and morale.

Model B, in contrast, provides a more detailed and comprehensive analysis, in line with the rubric's criteria. It not only discusses the military training and political symbolism but also expands on morale and cohesion, organizational development, public support, alliance formation, and improvements in health and sanitation. Each aspect is thoroughly elaborated upon, demonstrating how they collectively contributed to the transformation and eventual success of the Continental Army. By connecting these elements logically and coherently, Model B's response reflects a comprehensive understanding of the encampment's significance, making it the stronger submission per the evaluation criteria.

[WINNER] B

## Atomic Checklist

- Does the feedback compare the concise presentation of historical facts by Model A with the detailed and comprehensive analysis offered by Model B, highlighting the depth of Model B’s response?
- Is Model B’s method of detailing the significance of Valley Forge across multiple dimensions—including morale, health, military training, and political symbolism—acknowledged for its thoroughness?
- Are the educational values of both models’ narratives—Model A’s succinct enumeration of key points and Model B’s detailed elaboration on various aspects—evaluated effectively?
- Does the feedback highlight Model B’s ability to cohesively incorporate a wide array of historical facts and their implications, contrasting with Model A’s more limited scope?
- Is the choice of Model B as the winner justified succinctly, based on its comprehensive and multifaceted analysis that aligns more closely with the rubric through detailing the event's significance across political, military, and geographical aspects?

## Score Rubric

Did the comparison effectively evaluate the strengths and weaknesses of Model A's concise presentation versus Model B's detailed, comprehensive analysis in explaining the significance of Valley Forge during the American Revolution?

1. The comparison fails to address the difference in depth between Model A’s concise presentation and Model B’s comprehensive analysis; it provides no clear analysis of the educational value or historical coverage provided by either model.
2. The comparison recognizes the concise presentation in Model A or the detailed analysis in Model B but does not effectively evaluate the depth, detail, or coherence in the explanations provided by the models.
3. The comparison mentions both Model A’s succinct enumeration of key points and Model B’s detailed elaboration on various aspects, noting some aspects of educational value, but lacks a cohesive assessment of the depth, detail, and effectiveness in each model's explanation.
4. The comparison correctly assesses either Model A’s concise presentation of key historical aspects or Model B’s thorough and detailed analysis, providing a good evaluation of the educational value and narrative effectiveness but missing a concise judgment on the models’ adherence to the rubric.
5. The comparison excellently evaluates Model A’s concise yet limited exploration against Model B’s detailed, multi-dimensional analysis, precisely identifying strengths and weaknesses in coherence, historical coverage, and educational value, leading to a justified selection of a winner that aligns with the criteria for a comprehensive and logical application of historical knowledge.
```

## What is the task trying to measure?

The ability of a model to judge the relative quality of two given answers to a question,
while taking into account the provided score rubric. The model should give a score between 1 and 5,
indicating which answer is better and to what extent. The model should also provide a detailed explanation
for their score.

## Motivation

The task is motivated by the evolving role of language models (LLMs) in educational settings and the broader AI field,
including their potential in comparing the capabilities of other LLMs by evaluating their outputs.

## Related work

- AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback (https://arxiv.org/abs/2305.14387)
- JudgeLM: Fine-tuned Large Language Models are Scalable Judges (https://arxiv.org/abs/2310.17631)