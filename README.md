📖 About The Project
AnimeXind is a high-performance Anime Discovery Engine built to bridge the gap between static datasets and real-time information.

🧩 The Problem
Most anime datasets are static and lack updated visuals or detailed synopses. Searching through 12,000+ records manually is inefficient for users looking for high-quality recommendations based on specific ratings and genres.

💡 The Solution
This project implements a Hybrid Data Approach:

Local Processing: Uses FastAPI and Pandas to instantly filter and sort 12,294 records from the local CSV based on user-defined parameters (Rating, Genre, Pagination).

Live Enrichment: When a user selects an anime, the system performs a real-time handshake with the Jikan v4 API to fetch the latest HD posters and official synopses.

Smart Redirection: Implements dynamic URL encoding to provide direct "Watch Now" search links to external streaming platforms like HiAnimes.se.

💻 Technical Stack
Frontend: HTML5, CSS3, JavaScript (ES6+), Bootstrap 5, AOS Animation Library.

Backend: Python 3.10, FastAPI, Uvicorn ASGI.

Data Handling: Pandas for efficient CSV manipulation and filtering.

API: Jikan API (Unofficial MyAnimeList API).

🌟 Project Milestones

Level 1: Integrated dynamic streaming links using search-query encoding.

Level 2: Refined the UI with a professional "Deep Slate" theme and custom CSS transitions.

Level 3: Implemented scroll-triggered animations (AOS) to enhance user engagement.




IMAGES

 Home Page <img width="1352" height="599" alt="1" src="https://github.com/user-attachments/assets/07fc1404-656c-4d47-b928-a78afe8a548a" />

 Anime Lists <img width="1339" height="589" alt="2" src="https://github.com/user-attachments/assets/c7a628ce-e8a3-4ab5-bc90-63a76325915b" />

 Description and Status of the anime & No.Episodes...etc <img width="848" height="569" alt="3" src="https://github.com/user-attachments/assets/d522c9c0-e7ed-424d-a49f-2b1ca36b8a06" />

 Hianime Website <img width="1343" height="591" alt="4" src="https://github.com/user-attachments/assets/74bea5a6-802f-4bcb-9531-5d46f1bdb7cf" />

DEMO VIDEO



https://github.com/user-attachments/assets/a45ce4ae-fbc6-405b-aabd-f3c43db2cc10







**FOR HOW TO SETUP SEE THE "Setup.txt" FILE** 

