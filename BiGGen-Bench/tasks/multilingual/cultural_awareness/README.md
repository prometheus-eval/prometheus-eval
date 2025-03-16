# Cultural Awareness

Tasks that require to understand the culture of the country that uses the target language.

**Authors:** Jinkyung Jo

## Example

A sample query in a zero-shot setting:

```
Input:
আমি বাংলাদেশী বন্ধুর বাড়িতে আমন্ত্রিত হলে তাদের মা-বাবাকে আদরের প্রতি শ্রদ্ধার্ঘ্য হিসেবে আমি হাত মিলাতে পারি কি না?

Output:
বাংলাদেশে, মহিলাদের সাথে হাত মিলাতে হওয়া সাধারিতভাবে অনুমোদিত নয়। বাংলাদেশ একটি ইসলামিক দেশ হিসেবে, এখানে ইসলামিক শৈলী অনুসারে মহিলাদের সাথে শারীরিক সংলঙ্গ্ন কমাতে প্রয়াস করা হয়। খুবই স্পষ্টভাবে এবংছে যে, পুরুষ আগমনকারীদের মধ্যে মহিলাদের সাথে সরাসরি শারীরিক যোগাযোগ এড়ানো হওয়া আরও অধিক নিষিদ্ধ হয়।
```

## What is the task trying to measure?

The purpose is to measure how well it generates culturally appropriate responses tailored to the culture of a country that uses a specific language.

## Motivation

The language model should generate natural language taking into account cultural differences. When the model considers cultural differences, users feel understood and respected in terms of their cultural background, enabling more effective communication. Additionally, what may be considered appropriate in one culture might be inappropriate in another, potentially leading to generating content that is inappropriate for some users.

## Related work

[COPAL-ID: Indonesian Language Reasoning with Local Culture and Nuances](https://arxiv.org/abs/2311.01012)

[Multilingual Language Models are not Multicultural: A Case Study in Emotion](https://arxiv.org/abs/2307.01370)
