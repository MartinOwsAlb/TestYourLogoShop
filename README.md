# YourLogo

User acceptance test suite for buy products in shop 

-------
### Env vars

It is required to choose `RUN_PLATFORM` in `test_env.sh` 

For local run with preview you will need to download two drivers:
- geckodriver - `https://github.com/mozilla/geckodriver/releases`
- chromedriver - `https://chromedriver.chromium.org/downloads`

and create a local directory for them named `Local_drivers` after that 
set extra `MAIN_LOCAL_PATH` in `test_env.sh` for drivers that will run from the `Local_drivers`


-------
### How to run

####Locally docker     
1. Set required env vars   
2. Set PYTHONPATH: `export PYTHONPATH=/path/to/yourlogo`
3. Deploy Selenium grid: `docker-compose up`   
4. Run: from terminal `source your_logo/test_env.sh; python -m pytest`

####Locally with preview
1. Set PYTHONPATH: `export PYTHONPATH=/path/to/yourlogo`
2. Install `requirements.txt`
3. Set all required env vars in debug configuration
   1. ACCEPTOR_MAIN_LOCAL_PATH=`/.here you need to set your local path/shoptest`;
   2. ACCEPTOR_SELENIUM_URL=`http://0.0.0.0:4444/wd/hub`;
   3. ACCEPTOR_RUN_PLATFORM=`local`
