print("Welcome to the QA Decision Helper!")
print("What would you like help deciding?\n")
print("1. How much testing should I run for this requirement?")
print("2. Is this bug severe enough to block the release?")
print("3. Where should I focus my testing effort for this release requirement?")

choice = input("\nEnter your choice (1, 2, or 3): ")

if choice not in ["1", "2", "3"]:
    print("Invalid choice. Please run the program again and enter 1, 2, or 3.")

if choice == "1":
    print("\n--- Testing Level Recommendation ---")

    while True:
        feature_type = input("Is this a new or existing requirement? (new/existing): ")
        if feature_type in ["new", "existing"]:
            break
        print("Please enter new or existing.")

    while True:
        high_risk = input("Is this requirement high risk? (yes/no): ")
        if high_risk in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        broken_before = input("Has this area broken before? (yes/no): ")
        if broken_before in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        release_candidate = input("Is this a release candidate? (yes/no): ")
        if release_candidate in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    if feature_type == "new" and high_risk == "yes":
        print("\nRecommendation: Run a FULL test suite.")
        print("Reason: New requirement with high risk requires maximum coverage.")
    elif broken_before == "yes" or release_candidate == "yes":
        print("\nRecommendation: Run a REGRESSION test suite.")
        print("Reason: History of failures or release candidate requires thorough validation.")
    else:
        print("\nRecommendation: Run a SMOKE test suite.")
        print("Reason: Low risk requirement with no history of failures.")

elif choice == "2":
    print("\n--- Bug Severity Assessment ---")

    while True:
        affects_core = input("Does this bug affect core functionality? (yes/no): ")
        if affects_core in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        workaround = input("Is there a workaround available? (yes/no): ")
        if workaround in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        affects_data = input("Does this bug affect data integrity or security? (yes/no): ")
        if affects_data in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        customer_facing = input("Is this bug visible to the customer? (yes/no): ")
        if customer_facing in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    if affects_data == "yes" or (affects_core == "yes" and workaround == "no"):
        print("\nRecommendation: BLOCK the release.")
        print("Reason: Critical impact with no acceptable workaround.")
    elif customer_facing == "yes" and workaround == "no":
        print("\nRecommendation: BLOCK the release.")
        print("Reason: Customer facing bug with no workaround is not acceptable for release.")
    elif workaround == "yes":
        print("\nRecommendation: DO NOT BLOCK the release.")
        print("Reason: A workaround exists. Log the bug and monitor closely post-release.")
    else:
        print("\nRecommendation: USE JUDGMENT.")
        print("Reason: Borderline case. Escalate to the team for a final decision.")

elif choice == "3":
    print("\n--- Testing Focus Recommendation ---")

    while True:
        recent_changes = input("Were there recent changes to the codebase? (yes/no): ")
        if recent_changes in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        high_traffic = input("Is this a high traffic area of the application? (yes/no): ")
        if high_traffic in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        third_party = input("Does this requirement involve third party integrations? (yes/no): ")
        if third_party in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    while True:
        user_reported = input("Have users reported issues in this area before? (yes/no): ")
        if user_reported in ["yes", "no"]:
            break
        print("Please enter yes or no.")

    if third_party == "yes" and user_reported == "yes":
        print("\nRecommendation: Focus on INTEGRATION and REGRESSION testing.")
        print("Reason: Third party integrations with a history of user reported issues require thorough validation.")
    elif recent_changes == "yes" and high_traffic == "yes":
        print("\nRecommendation: Focus on REGRESSION and PERFORMANCE testing.")
        print("Reason: Recent changes to a high traffic area carry significant risk.")
    elif user_reported == "yes":
        print("\nRecommendation: Focus on REGRESSION testing.")
        print("Reason: User reported issues indicate this area needs thorough validation.")
    else:
        print("\nRecommendation: Focus on SMOKE testing.")
        print("Reason: No significant risk indicators. Basic validation is sufficient.")