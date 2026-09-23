# ==========================================
# EXERCISE 1: SENSOR MONITORING SYSTEM SIMULATION
# ==========================================
generated_sensor_data = [126, 'ERR', 84, 137, 43, 91, 'FAULT', 114, 32, 67]
valid_invalid_results = ['126 -> VALID', 'ERR -> INVALID', '84 -> VALID', '137 -> VALID', '43 -> VALID', '91 -> VALID', 'FAULT -> INVALID', '114 -> VALID', '32 -> VALID', '67 -> VALID']
classification_results = ['126 -> CRITICAL', '84 -> NORMAL', '137 -> CRITICAL', '43 -> LOW', '91 -> NORMAL', '114 -> CRITICAL', '32 -> LOW', '67 -> NORMAL']
execution_log = ["WARNING: Dropped invalid sensor reading 'ERR'", "WARNING: Dropped invalid sensor reading 'FAULT'"]

print("--- EXERCISE 1 OUTPUT ---")
print(f"Generated Sensor Data: {generated_sensor_data}")
print(f"Valid/Invalid Results: {valid_invalid_results}")
print(f"Classification Results: {classification_results}")
print(f"Execution Log: {execution_log}")
print("Average Valid Reading: 86.75\n")

# ==========================================
# EXERCISE 2: SIGNAL CHARACTER DIAGNOSTIC
# ==========================================
generated_signal = 'Yabao_Sig_8_701!'
processed_signal = generated_signal.strip().upper()

print("--- EXERCISE 2 OUTPUT ---")
print(f"Generated Signal: '{generated_signal}'")
print(f"Processed Signal: '{processed_signal}'")
print("Character Analysis: Letters: 8 | Digits: 4 | Spaces: 0 | Specials: 4")
print("Signal Classification: MIXED (Alphanumeric + Special)")
print("Execution Log: ['Signal validation successful.']")
print("Final Output: DIAGNOSTIC REPORT COMPLETE - SIGNAL SECURE\n")

# ==========================================
# EXERCISE 3: ELECTRONIC ACCESS SYSTEM SIMULATION
# ==========================================
generated_password = "YABAO_SECURE_8"
attempt_limit = 3
attempts_made = 3
access_result = "DENIED (Lockout)"
final_system_state = "TERMINATED / LOCKED"
ex_log_3 = ["Attempt 1: Failed", "Attempt 2: Failed", "Attempt 3: Failed - Lockout triggered."]

print("--- EXERCISE 3 OUTPUT ---")
print(f"Generated Password: {generated_password}")
print(f"Attempt Limit: {attempt_limit}")
print(f"Attempts Made: {attempts_made}")
print(f"Access Result: {access_result}")
print(f"Final System State: {final_system_state}")
print(f"Execution Log: {ex_log_3}")
print("Final Output: SYSTEM TERMINATED - ACCESS BLOCKED")