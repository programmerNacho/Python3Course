import matplotlib.pyplot as plt
import numpy as np

col_count = 3
bar_width = .2

korea_scores = (554, 536, 538)
canada_scores = (518, 523, 525)
china_scores = (613, 570, 580)
france_scores = (495, 505, 499)

index = np.arange(col_count)

k1 = plt.bar(index, korea_scores, bar_width, alpha=.4, label="Korea")
c1 = plt.bar(index + bar_width, canada_scores, bar_width, alpha=.4, label="Canada")
ch1 = plt.bar(index + (bar_width * 2), china_scores, bar_width, alpha=.4, label="China")
f1 = plt.bar(index + (bar_width * 3), france_scores, bar_width, alpha=.4, label="France")

def create_labels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2., height,
                 "%d" % int(height),
                 ha='center', va='bottom')

create_labels(k1)
create_labels(c1)
create_labels(ch1)
create_labels(f1)

plt.ylabel("Mean score in PISA 2012")
plt.xlabel("Subjects")
plt.title("Test Scores by Country")

plt.xticks(index + (bar_width * col_count / 2), ("Mathematics", "Reading", "Science"))
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.tight_layout()
plt.show()