# TypeMaster  
### Table of contents:  
* [Overview](https://github.com/sak345/TypeMaster/edit/main/README.md#overview)
* [Features](https://github.com/sak345/TypeMaster/edit/main/README.md#features)
* [How to run the application](https://github.com/sak345/TypeMaster/edit/main/README.md#how-to-run-the-application)
* [Future Improvements](https://github.com/sak345/TypeMaster/edit/main/README.md#future-add-ons)
### Overview:  
TypeMaster is an interactive and user-friendly application designed to help users evaluate and improve their typing speed and accuracy. It offers an array of features to enhance the typing test experience.
### Features:  
* TypeMaster is crafted using Python's powerful Tkinter library, ensuring a sleek and intuitive graphical user interface (GUI) for an exceptional user experience.
* It is equipped with a built-in performance feedback system, providing users with valuable statistics, including word count, accuracy, omissions, and elapsed time, enabling users to track their progress over time.
* It allows users to store and access their historical performance data using MySQL Database. Reviewing past typing test results fosters a sense of achievement and serves as a motivation for improvement.
### How to run the application:  
#### Requirements:  
* Python must be installed in the system. (Python-3 or above)
* MySQL should be set-up and configured
#### Follow the below setups after ensuring the above requirements are met:  
* Open Typing_speed_test.py file and change to your actual MySQL user and password on line 53
* Open the command prompt and go the directory where application is installed
* Type the following command in the cmd - `py -m pip install ttkthemes keyboard mysql-connector-python requests`
* After the above libraries have been successfully installed, type - `py typing_speed_test.py` to start the application

### Future add-ons:  
* **Deploying:** Deploy the application on a hosted server to improve accessibility, reliability and scalability.
* **User Profiles:** Implement user profiles with login functionality to enable multiple users to track their individual progress
* **Difficulty Levels:** Introduce varying difficulty levels for typing tests, catering to users with different skill levels. This could include easy, medium, and hard mode tests.
* **Real-time Leaderboard:** Create a competitive edge by adding a real-time leaderboard that displays the highest typing speeds achieved by users, fostering friendly competition and motivation.
* **Social Sharing:** Add social media integration for users to share their typing achievements and challenge friends to typing competitions, making the app more engaging.
