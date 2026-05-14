## Project Overview.
Phase 1: Data Collection & Methodology
This project utilizes a custom-built dataset to analyze user sentiment across major Ethiopian fintech applications. Moving away from static, common datasets, this methodology ensures the analysis is based on unique, real-world interactions.

🛠 Scraping Methodology
Source: Google Play Store.

Tooling: google-play-scraper (Python).

Target Applications:

CBE: Commercial Bank of Ethiopia Mobile Banking.

BOA: Bank of Abyssinia Mobile Banking.

Dashen: Dashen Bank Super App.

Strategy: Reviews were scraped using the NEWEST sort filter to prioritize current app performance and user experience.

📅 Dataset Temporal Scope
Start Date: March 9, 2026.

End Date: May 13, 2026.

Total Duration: 65 Days.

Record Count: ~1,500 total reviews (500 per bank).

⚠️ Technical Limitations & Challenges
Multilingual Content: A significant portion of reviews contains a mix of English and Amharic (including Amharic written in Latin script), which presents a challenge for standard NLP sentiment libraries.

Deduplication Needs: Initial scrapes contained duplicate user entries. A robust cleaning pipeline was implemented to remove duplicates based on a combination of user_name and review_text.

Key Errors: During the cleaning phase, the standard review_id key was unavailable in the custom DataFrame schema, requiring a pivot to multi-column uniqueness checks.

Snapshot Constraint: The data is a static snapshot taken on May 14, 2026, and does not account for reviews edited or deleted by users after this date.