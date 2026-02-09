sample_bay = ["Basalt", "Silica", "Iron", "Dust"]

print(sample_bay[0])
print(sample_bay[-1])
print(len(sample_bay))

for sample in sample_bay:
    print(f"Transmitting data for {sample}")

new_findings = []

for i in range(3):
    user_input = input("Enter a rock type to add to the findings:")
    new_findings.append(user_input)
    print("Find added successfully. current_findings: ", new_findings)