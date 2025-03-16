# API Generalization

Tasks involving the generalization to previously unseen APIs or tools, using API documentation effectively.

**Authors:** Hanseok Oh

## Example

A sample query in a zero-shot setting:

```
Input:
Plan a trip from New York to Tokyo, including flight, hotel, and activities for 3 days.

Output:
For planning a trip from New York to Tokyo, including flights, hotels, and activities for 3 days, we'll use three of the provided tools: Flight Booking, Hotel Reservation Tool, and Activity Planner Tool. Let's generate the inputs for each tool:

1. **Flight Booking**:
    - **Departure City:** New York
    - **Destination City:** Tokyo
    - **Departure Date:** [Example: 2024-02-15]
    - **Return Date:** [Example: 2024-02-18]
    
    Format:
    
    <flight_booking>
    Departure City: New York | Destination City: Tokyo | Departure Date: 2024-02-15 | Return Date: 2024-02-18
    </flight_booking>
    
2. **Hotel Reservation Tool**:
    - **Destination City:** Tokyo
    - **Check-in Date:** 2024-02-15
    - **Check-out Date:** 2024-02-18
    - **Preferences:** [Example: 4-star hotel]
    
    Format:
    
    <hotel_reservation>
    Destination City: Tokyo | Check-in Date: 2024-02-15 | Check-out Date: 2024-02-18 | Preferences: 4-star
    </hotel_reservation>
    
3. **Activity Planner Tool**:
    - **Destination City:** Tokyo
    - **Start Date:** 2024-02-15
    - **End Date:** 2024-02-18
    - **Interests:** [Example: Cultural Sites, Nature, Dining]
    
    Format:
    
    <activity_planner>
    Destination City: Tokyo | Start Date: 2024-02-15 | End Date: 2024-02-18 | Interests: Cultural Sites, Nature, Dining
    </activity_planner>
    

These formatted inputs will utilize the respective tools to arrange the flight, accommodation, and activities for the trip, ensuring a well-organized and enjoyable experience in Tokyo.

```

## What is the task trying to measure?

The task is attempting to measure a model's ability to generalize their understanding of API documentation principles and effectively apply them to previously unseen APIs or tools. It evaluates their capacity to navigate, interpret, and utilize API documentation in unfamiliar contexts.

## Motivation

The motivation behind this task is to assess a model's competence in adapting to new technologies and APIs by relying on their comprehension of API documentation. It aims to determine their capability to independently learn and utilize different APIs, reflecting their adaptability and proficiency in a rapidly evolving technological landscape.

## Related work

* ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs (https://arxiv.org/abs/2307.16789)
* Tool Documentation Enables Zero-Shot Tool-Usage with Large Language Models (https://arxiv.org/abs/2308.00675)
