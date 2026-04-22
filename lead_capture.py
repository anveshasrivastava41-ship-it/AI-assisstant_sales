import csv

def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

    with open("leads.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, platform])