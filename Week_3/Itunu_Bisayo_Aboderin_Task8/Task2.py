# **Task2**
# - Comment the code below appropriately, and using doctring, explain what the code is doing.
# -  Adapt the code to the case below.

# - Federal Government Scholarship Key Eligibility Requirements:
#   - Citizenship:
#     - Applicant must be a citizen of Nigeria. 
#   - Enrollment:
#     - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
#   - Other Scholarships:
#     - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
#   - Academic Qualification:
#     - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.


citizenship = input("Country of citizenship: ").title()                 #Asks the user to enter your country of citizen      
enrollment = input("Are you a registered full-time undergraduate student in a recognized Nigerian_university Yes or No: ")     # Asks the user to enter your enrollment status
other_scholarship = input("Are you a current recipient of Oil and Gas industry, whether national or international? Yes or No:  ")       # Asks the user to enter other scholarship status
academic_qualification = input("Do you have 5 As and Bs in relevants subjects including English and Mathematics? Yes or No: ")             # Asks the user if they are qualified academically

eligibility = ((citizenship == "Nigeria") or (citizenship == "Nigerian")) and (enrollment == "Yes") and (other_scholarship) != "Yes " and (academic_qualification == "Yes") # Defines the eligibility criteria using assignment operators

print(f"\nEligibility Requirements: \nCitizenship: {citizenship}\nEnrollment status: {enrollment}\nOther scholarships: {other_scholarship}\nAcademic Qualification: {academic_qualification}\nEligible: {eligibility}")   # Displays the eligibility requirements using f string and printing on new line

# Output
# Eligibility Requirements:
# Citizenship: Nigeria
# Enrollment status: Yes
# Other scholarships: No
# Academic Qualification: Yes
# Eligible: True


