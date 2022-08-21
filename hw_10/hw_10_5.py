plan = {i for i in range(1, 20)}
circ = {i for i in range(len(plan)+1, len(plan) + 6)}
stadium = {i for i in range(max(circ)+1, max(circ) + 3)}
activ_child = plan | circ | stadium
print("В класссе", len(activ_child)+3, "учеников")
