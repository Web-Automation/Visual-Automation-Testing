# Visual-Automation-Testing
Use this code to automate visual regression testing when need to compare web pages in bulk.

## Getting started
Along with the Selenium web driver, percy-selenium packages and percy.io application provided by Python & BrowserStack, we can run visual automation testing.
Need to install nodejS to run Percy.

## Usage
Install dependencies: (Python Packages)
- pip install selenium
- pip install percy-selenium
- pip install webdriver_manager

Install dependencies: (nodejS Packages)
- Install nodejS package in your desktop first.
- npm install --save-dev @percy/cli

**Configuration:**
- Set the Percy token in the environment variable like this: export PERCY_TOKEN="<your token here>" 
- Token will be generated while you create your project on percy.io
- While creating the project use 'Percy' instead of 'Automate' in "Browser Selection to be handled by" which will be asked in percy.io while creating the project
- export PERCY_BUILD_TAG=<your build tag> [It can be live, uat or anything based on your preference]
- While creating the project use 'Git' instead of 'Visual Git' in "Baseline management" which will be asked in percy.io while creating the project
- When opting for 'Git' the build(it will be inside the Percy project shown in your dashboard) made each time will use the previous build to compare the next build.
Example: There are 5 builds; Build-1, Build-2, Build-3, Build-4 & Build-5. Now Build-1 will be used by Build-2 for visual comparison. Suppose in Build-1 you send the stagging changes and in Build-2 will have current production data, then Build-2 will be compared by Build-1.
- If opted for 'Visual Git' then the build made in the first instance will be used to compare across all the builds.
Example: There are 4 builds; Build-1, Build-2, Build-3 & Build-4. Now Build-1 will be used across all the builds i.e. 2, 3 & 4 for visual comparison. Suppose in Build-1 you send the stagging changes and in Build-2 will have current production data, then Build-2 will be compared by Build-1.

**Notes:**
- Generate $percy_token from percy.io
- Percy dashboard will compare the screenshot on its own, you just need to send the screenshot using the script and proper naming convention so that images can be compared properly.
- If using 'Git' in "Baseline Management" then remember that every new build which will be created compare with previous build, so first prepare the build of live webpage then build the stagging webpage. 
