print("=" * 50)
print("  CYBERGUARD v1.0  ")
print("PERSONAL SECURITY MONITORING SYSTEM")
print("=" * 50)

print()
print("Welcome, Security Analyst!")
print()
print("Your mission is to monitor account activity and detect potential threats.")
print("Information and identify potential threats.")
print()
print("Starting security assessment... ")
print()
print("=" * 50)

print("\nUSER INFORMATION")
print("=" * 50)
username = input("Enter your username: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")
age = int(input("Enter your age: "))
ip_address = input("Enter your IP address: ")
failed_attempts = int(input("Enter failed login attempts: "))
account_input = input("Is account Active or Inactive?") 

if account_input == "Active":
    account_status = True
else:
    account_status = False
    print("\nInformation collected successfully!")


    print("\nDATA TYPE VERIFICATION")
print("-" * 50)

print("Username:", type(username))
print("Email:", type(email))
print("Password:", type(password))
print("Age:", type(age))
print("IP Address:", type(ip_address))
print("Failed Attempts:", type(failed_attempts))
print("Account Status:", type(account_status))


print("\nSECURITY THREAT DETECTION")
print("-" * 50)

if failed_attempts == 0:
    print("No failed login attempts detected.")

elif failed_attempts >= 1 and failed_attempts <= 5:
    print("LOW SECURITY ALERT!")
    print("A few failed login attempts detected.")

else:
        print("CRITICAL WARNING!")
        print("Possible brute-force attack detected.")

if account_status == False:
     print("Account access is currently disabled.")


else:
     print("Account is active.") 

    
if failed_attempts < 5:
        print("No critical login threat detected.")

print("\nPASSWORD STRENGTH ASSESSMENT")
print("-" * 50)

password_length = len(password)

print("Password Length:", password_length)

if password_length < 8:
    print("Password Strength: WEAK")

elif password_length >= 8 and password_length <= 11:
    print("Password Strength: MODERATE")

else:
    print("Password Strength: STRONG")


    print("\n")
print("=" * 50)
print("       CYBERGUARD SECURITY REPORT")
print("=" * 50)

print("\nUSER INFORMATION")
print("-" * 50)

print("Username:", username)
print("Email:", email)
print("Age:", age)
print("IP Address:", ip_address)

if account_status == True:
    print("Account Status: ACTIVE")
else:
    print("Account Status: INACTIVE")

print("\nSECURITY ANALYSIS")
print("-" * 50)

print("Password Assessment:", end=" ")

if password_length < 8:
    print("WEAK")
elif password_length <= 11:
    print("MODERATE")
else:
    print("STRONG")

print("Failed Login Attempts:", failed_attempts)

print("\nTHREAT DETECTION")
print("-" * 50)

if failed_attempts >= 5:
    print("[CRITICAL] Multiple failed login attempts!")
    print("[WARNING] Possible brute-force attack detected.")

elif failed_attempts >= 1:
    print("[WARNING] Failed login attempts detected.")

else:
    print("[SAFE] No failed login attempts detected.")

if account_status == False:
    print("[WARNING] Account access is currently disabled.")

print("\nFINAL SECURITY STATUS")
print("-" * 50)

if failed_attempts >= 5:
    print("THREAT LEVEL: HIGH")
    print("\nRECOMMENDATION:")
    print("Investigate the login activity and secure")
    print("the account immediately.")

elif account_status == False:
    print("THREAT LEVEL: ACCOUNT INACTIVE")
    print("\nRECOMMENDATION:")
    print("Verify the account status before allowing access.")

elif failed_attempts >= 1:
    print("THREAT LEVEL: LOW")
    print("\nRECOMMENDATION:")
    print("Monitor the account for unusual activity.")

else:
    print("THREAT LEVEL: LOW")
    print("\nRECOMMENDATION:")
    print("Continue monitoring the account.")

print("\n" + "=" * 50)
print("       END OF SECURITY REPORT")
print("=" * 50)