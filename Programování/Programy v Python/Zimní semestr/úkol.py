# První úkol Marek Potůček 2.10. Zaklady programování Python 1

points = 10   #počet dosažených bodů, zadá uživatel
grade = 1
if points >= 2:
    if points >= 3:
        if points >= 5:
            if points >= 7:
                if points >= 9:
                    grade = 1
                grade = grade + 1
            grade = grade + 1
        grade = grade + 1
    grade = grade + 1

print(grade) #tisk výsledné známky