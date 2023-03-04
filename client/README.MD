# Submission Management Client

### This is a command line REPL client to be used by the insurance broker.

## Run 
```
python3 app/main.py
```
Please make sure that the server is up and running

## Supported operations
- CREATE SUBMISSION “<company_name>” “<physical_address>” <annual_revenue>
- UPDATE SUBMISSION “<submission_id>” “<company_name>” “<physical_address>”
<annual_revenue>
- GET SUBMISSION “<submission_id>”
- BIND SUBMISSION “<submission_id>” “<signed_application_path>”
- LIST SUBMISSIONS “only_bound”
- HISTORY
- EXIT
 