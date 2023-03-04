# Submission Management Server

### This is a FLASK server to be used by the submission management repl client.

## Run 
1. `docker build -t submission-management-server .`
2. `docker run -p 5000:5000 submission-management-server`



## Supported operations
- CREATE SUBMISSION “<company_name>” “<physical_address>” <annual_revenue>
- UPDATE SUBMISSION “<submission_id>” “<company_name>” “<physical_address>”
<annual_revenue>
- GET SUBMISSION “<submission_id>”
- BIND SUBMISSION “<submission_id>” “<signed_application_path>”
- LIST SUBMISSIONS “only_bound”
- HISTORY
- EXIT
 