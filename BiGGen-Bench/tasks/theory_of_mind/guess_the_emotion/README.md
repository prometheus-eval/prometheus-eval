# Guess the Emotion

Tasks designed to assess the model's ability to infer emotion from textual cues in a given scenario. This involves understanding subtle language nuances and context to accurately predict the emotional state of characters in a conversation or a narrative.

**Authors:** Sue Hyun Park (suehyunpark@kaist.ac.kr)

## Example

A sample query in a zero-shot setting:

```
Input:
In the break room at their workplace, Timothy and Dennis are discussing a recent project deadline that was missed.

Timothy: So, about the project deadline. I know we've been swamped, but missing it could really set us back with the client.
Dennis: Yeah, about that. I actually spoke with the client yesterday. Told them we needed more time due to unforeseen issues. They were pretty understanding.
Timothy: Oh, that’s a relief. I didn’t realize you’d already talked to them. What did they say about the new timeline?
Dennis: They said it’s fine as long as we keep the quality high. They’re quite flexible.
A moment passes.
Timothy: It's just that I got an email from the client this morning. They were asking why they hadn't heard from us about the delay.
Dennis: Ah, well, I mean, I didn’t formally email them. It was more of a quick call, just to touch base.
Timothy: I see. We should probably send a follow-up email, just to have everything documented.
Dennis: Great, thanks.

What made Timothy pause in the middle of the conversation? Explain how Timothy and Dennis feel towards the end of the conversation.

Output:
Timothy paused in the middle of the conversation when there seemed to be a discrepancy between Dennis's account of speaking with the client and recent events. Specifically, Timothy mentioned receiving an email from the client inquiring about the project delay, which Dennis had previously stated he handled with a quick call. This discrepancy led Timothy to suggest sending a follow-up email to ensure proper documentation of the situation.

At the end of the conversation, Timothy likely feels a mix of relief (that the client was understanding about the delay) and concern (about the miscommunication and the lack of formal documentation regarding the new timeline). Meanwhile, Dennis is probably feeling grateful for Timothy's suggestion to send a follow-up email, as it can help prevent future misunderstandings with the client. However, Dennis might simultaneously feel a bit embarrassed for not having considered sending a formal email initially. Nonetheless, their conversation demonstrates their ability to collaborate and address issues in a constructive manner.
```

## What is the task trying to measure?
This task measures a language model's capability to recognize and interpret emotions from utterances and/or nonverbal cues in long conversations/narratives.  
This task comprises the following subtasks, designated for each of the 5 instances:

1. **Speaker and listener specific emotion recognition**
    
    `Compare the way {people in the conversation} express emotion (as a speaker) and interpret emotion (as a listener) in the context of the conversation above. How are their speaker/listener profiles different?`

2. **Tracking emotion shift**

    `Describe how {people in the conversation}'s emotion change throughout the conversation and what invoked the change.`

3. **Disentangling stance and emotion**: on the same stance but expressing it through different emotions

    `Determine the stance on the {topic of conversation} of each person and describe how each of them express it through emotions.`

4. **Emotion reasoning**

    `What made {character} pause in the middle of the conversation? Explain how {characters} feel towards the end of the conversation.`

5. **Emotion recognition from nonverbal cues**

    `(Given a story) Describe {character}'s emotions in the sequence of his actions.`


## Motivation

Emotion recognition can be interpreted as:

> inferring an emotional state from observations of emotional expressions and behavior, and through reasoning about an emotion-generating situation[^1]

A machine capable of recognizing emotion can effectively interact with humans, as understanding emotion is integral in nourishing interpersonal relationshps and emphathetic machines can enrich the experience they provide to human beings.   
Since one's emotion can be expressed through natural language, emotion recognition has been a growing field of study in NLP, useful for a wide range of applications such as opinion mining and recommender systems. Note that sentiment analysis and emotion recognition are established on different bases, despite looking similar; emotion is a psychological state while sentiment is the mental attitude created through the existence of emotion[^2].  
Emotion recognition in conversation (ERC) focuses on conversational data, which requires context modeling of the individual utterances beyond recognizing emotion in sentences or utterances[^3]. In order to succeed in ERC, a model should be aware of conversation-specific factors including presence of contextual cues, temporality in speakers' turns, speaker- or listener-specific information, sarcasm, discrepancy in explicit and implicit cues, etc.. Also, conversations can display complex emotional dynamics where emotional influences can be placed on oneself or other interlocutors and is difficult to reason out or track them without comprehensive understanding of the conversation flow.  
In light of this, we construct several conversations and narratives involving a mixture of emotions and diverse methods of expressing them. We explore whether a model can correctly infer emotions in real-life scenarios and provide reasonable interpretations using social intelligence. 


## Data source
For each subtask, we prompt GPT-4 to create a natural-sounding, human-like, commonsense-grounded conversation/narrative that tests emotion recognition, given a description of the subtask provided in Section II of [[2]]. A list of fine-grained emotions in real-world provided in Appendix A of [[4]] is appended to help incorporate specific emotion in the conversation.

## Related work

[^1]: Picard, R. W. (2000). Affective computing. MIT press.

[^2]: Pereira, P., Moniz, H., & Carvalho, J. P. (2022). Deep Emotion Recognition in Textual Conversations: A Survey. arXiv preprint arXiv:2211.09172.

[^3]: Poria, S., Majumder, N., Mihalcea, R., & Hovy, E. (2019). Emotion recognition in conversation: Research challenges, datasets, and recent advances. IEEE Access, 7, 100943-100953.

[^4]: Demszky, D., Movshovitz-Attias, D., Ko, J., Cowen, A., Nemade, G., & Ravi, S. (2020). GoEmotions: A dataset of fine-grained emotions. arXiv preprint arXiv:2005.00547.


