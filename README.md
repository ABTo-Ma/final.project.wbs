# final.project.wbs
This repository is the final project for the Data Science Course at WBS-Coding School. The aim of the project is to showcase some of the learned tools as well as implementation in a project. The topic of the project is health, specially diseases, vaccinations and prevention. In a course of about two weeks I worked together with Nuria Amezaga Sole.  
# Implemented tools and libraries
The information was stored and updated in a MySQL database. This allowed an efficient storage and continous communication between the interface and the database. The connection was build with **sqlalchemy** and of course visualized with **pandas**
For web-scrapping I used **BeautifulSoup** to gather additional information. 
For the plots I used **plotly** because *,,plotly enables Python users to create beautiful interactive web-based visualizations that can be displayed in Jupyter notebooks, saved to standalone HTML files, or served as part of pure Python-built web applications using Dash."* 
After acquiering the needed data and having a running database itwas time to create an environment for the user to interact with the data. For this purpouse we used **streamlit** mainly because it is the only tool we have learned so far and it is easy to implement. 
# Results
The project was succesfully created in the given two weeks with the main goals achieved. The app visualizes reported cases of different diseases aroung the world in different time-spans, it contains information on needed vaccinations for different groups by contry and it possible to predict bases on symptoms a possible disease. It also gives usefull recommendation and has explanatory videos. 
