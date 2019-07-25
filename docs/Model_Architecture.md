Models Architecture Design
----Beta Version----
Accounts
-user
	-username
	-email
	-first_name
	-last_name
	-gender
	-type (admin,staff,tanod,regUser)
-Add_User
	-username
	-email
	-first_name
	-last_name
	-password
	-gender
	-type (admin,staff,tanod,regUser)

Pages
-Posts
-Send_notification

Services - user side
Recieved_complaint,requested documents, suggestions
-Complaints
	-user (foreignkey to Accounts)
	-Complaint Description
	-Date sent
-Requested_documents
	-user (foreignkey to Accounts)
	-type of document
	-Requested document Description
	-Date sent
-Suggestions
	-user (foreignkey to Accounts)
	-Suggestion Description
	-Date sent

Notification
-Sent_notification
	-* searched * user (Foreignkey to Accounts)
	- type of concern
	-Content
	-date sent
------------------------
Analysis (visualization)
-Complaints
-Requested_documents
-Suggestions