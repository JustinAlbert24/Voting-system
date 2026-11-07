tinubu_votes = 0
obi_votes = 0

voted_names = []

while len(voted_names) < 3:
    name = input("Your name: ").strip().lower()

    if name in voted_names:
        print("You have already voted!")
        continue

    while True:
        vote = input("Vote for Tinubu or Obi: ").strip().lower()

        if vote == "tinubu":
            tinubu_votes += 1
            voted_names.append(name)
            break

        elif vote == "obi":
            obi_votes += 1
            voted_names.append(name)
            break

        else:
            print("Invalid vote! Try again.")

print("Results")
print("Tinubu:", tinubu_votes)
print("Obi:", obi_votes)

if tinubu_votes > obi_votes:
    print("Winner: Bola Ahmed Tinubu")
elif obi_votes > tinubu_votes:
    print("Winner: Peter Obi")
else:
    print("It's a tie!")