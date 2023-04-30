# Hackathon. Code Crusaders (C+)

## Table of contents 
[1. Our team](https://github.com/ekaterinatao/hackathon_Code_Crusaders#team)   
[2. Description](https://github.com/ekaterinatao/hackathon_Code_Crusaders#description)   
[3. Aim](https://github.com/ekaterinatao/hackathon_Code_Crusaders#aim)  
[4. Datasets and code](https://github.com/ekaterinatao/hackathon_Code_Crusaders#datasets-and-code)  
[5. Launch interactive interface](https://github.com/ekaterinatao/hackathon_Code_Crusaders#launch-interactive-interface)    

## Team
[Ekaterina Tao](https://github.com/ekaterinatao) - project manager  
Ilia Beliakov - data engineer   
Alexander Zhuravlev - data analyst  
Bogdan Kostyuk - data engineer  
Anna Rybakova - data analyst   
Danila Lyulya - data analyst  

## Description
Here is our team project for hackaton. We have parsed some data about startups from kaggle (more than 20 datasets) and theorg.com (more than 300 thousand companies), preprocessed this data and created SQLite database with interactive interface.  

## Aim
To create database containing information about startups with interactive interface.  

## Datasets and code
Parsing code from [kaggle](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/main/parsing_kaggle.ipynb) and [theorg.com](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/main/parsing_theorg.ipynb).  

You can find parsed data in the project folder [raw_data](https://github.com/ekaterinatao/hackathon_Code_Crusaders/tree/main/raw_data).  

Data preprocessing code is [here](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/main/database_to_sql.ipynb).  

Code creating SQLite database is [here](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/main/preprocessing.ipynb).
  
Merged and preprocessed dataset is [here](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/master/final_dataset.rar).  

**Columns of the final dataset:**  
  
* `name_x`, `name_norm` - company name, and normalized name  
* `Website` of the company  
* `country_code`, `city`, `state_code` (only for USA) - location of the company  
* `status` - current status of the company  
* `founded_at`, `closed_at`, `first_investment_at`, `last_investment_at`, `first_funding_at`, `last_funding_at`, `first_milestone_at`, `last_milestone_at` - dates related to major events of the company  
* `description`, `long_description` of the company  
* `category_code`, `INDUSTRY` - company's basic industry  
* `SUB-INDUSTRY` - company's additional industries  
* `tag_list`  
* `valuation_billion_usd` - company's capitalization  
* `funding_total_usd` - total funding amount  
* `ROI` - return on investment  
* `created_by` - name of the creator  
* `funding_stage` - current funding stage  
* `Fund structure` - company's capital structure  
* `investment_rounds` - the number of investment round  
* `invested_companies` - the number of invested companies  
* `funding_rounds` - the number of funding rounds  
* `milestones` - the number of achieved milestones  
* `relationships` - the number of relationships  
* `twitter_username`, `Crunchbase Url`, `Unicorn Nest website link` - other different links related to the company  
* `Investors` - list of company's investors  
* `Fund that most often invests in previous rounds`, `Fund that most often invests together`, `Fund that most often invests in following rounds` - names of given funds  
* `TOP_novelty_companies`, `TOP_companies_at_peak_activity` `TOP_key_persons`, `TOP_lead_investments`, `TOP_unicorn_amount`, `TOP_avg_rounds_per_year`, `TOP_avg_round_size`, `TOP_avg_startup_valuation`, `TOP_decision_makers_strategy_diversity_index`, `TOP_avg_multiplicator`, `TOP_success_strategy_diversity_index`, `TOP_follow_on_index`, `TOP_readiness_take_younger_startups` - company's best rank category  
* `team_size`, `employeeRange` - absolute and categorical number of employee  
* `followerCount` in Twitter  
* `positionCount` - the number of permanent full time equivalent positions  
* `stage` - company's stage  
* `best_company` - whether the company is listed in the best companies list or not  

## Launch interactive interface
To launch interactive SQLite database click [here](http://45.8.248.146:8000/).  

**To launch database on your server follow next steps:**  
1. [Gradio_prod.py](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/master/Gradio_prod.py) should be hosted on the server (`0.0.0.0` port `8000`) to launch the app. This code reads the data and constructs the interface using gradio.  
2. [StartUps_DB.db](https://github.com/ekaterinatao/hackathon_Code_Crusaders/blob/master/StartUps_DB.db) is the SQLite database containing the table `StartUps_DB`. The database should be in the root folder (otherwise the path in Gradio_prod.py should be changed).  
3. To run in the background **screen** should be installed via linux command:  
    `sudo apt-get install screen`  
4. Create new session:  
    `screen -S gradio`  
5. Run python file:  
    `python3 Gradio_prod.py`  
6. Follow the link.  