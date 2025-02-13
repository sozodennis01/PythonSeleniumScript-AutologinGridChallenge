# Internship Python Selenium Script: Auto-Login Grid Challenge
## Auto login into a client's testing environment that had a tedious grid challenge.
Made during QA Summer Internship 2020.
Created for Prometheus Group's Quality Assurance Engineers.
## SAMS Grid Card Example
![image](https://github.com/user-attachments/assets/2d7f04c2-2e73-4188-985a-322316e67c52)

Example Challenge using Grid Card above: A4-A5-D5 | Answer: TSW  
A real login example is the CDC authentication page: [CDC SAMS Grid Card](https://auth.cdc.gov/siteminderagent/forms/login.fcc?TYPE=33554433&REALMOID=06-2e4e428f-8768-4f65-a66d-911e49413d9e&GUID=&SMAUTHREASON=0&METHOD=GET&SMAGENTNAME=-SM-VfBllSkkIKR6GkMEZgI2o6e2zk%2fxh2fc%2fe5E0N%2fN98H5LsZWkDhX%2fH618YU%2bV1pFG6Dqc8o%2buj7a7BOjbw3l3DbOwJLzWlX7IAOrlseiUBdD9DB45IS4xFtcl%2fRbqrug&TARGET=-SM-https%3a%2f%2fsams%2ecdc%2egov%2f).
Its common for companies to have Multi-Factor Authentication methods. An *uncommon one for me* was a Grid Card! 
Basically given a row & column, find the key value in the Grid card. 
## Situation
For QA, I often had to login to a client's system to get their configs and test their bug/feature request tickets. 
I had to login enough times to find the Grid challenge annoying (or maybe I was lazy?). I had to find the Grid card in the Teams directory, keep it open, use the brain to find the key, etc. If it was annoying to me, it'll probably be annoying for someone else too.
## Task
Attempt to automate a tedious login process to increase testing productivity. All the team needed was Python, Selenium, and Chrome installed.
## Action
1. Translate the Grid Card into a data structure (2D Array)
2. Use Selenium to drive Chrome actions.
3. Read HTML code with Inspector to find key ID & classes for Selenium.
4. Grab the challenge string and clean it up.
5. Create a function to find the key, based on the challenge.
6. Submit the answer.
7. Login and enter the client's testing system.
## Result
I could successfully login into the client's testing system with my automation script! I could now login in less than a minute vs 2-3 minutes which involved finding the Grid Card & using my monkey brain for the easy, but tedious challenge.
