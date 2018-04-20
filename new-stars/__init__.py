import csv

with open('../goodCategoriesNoPublix4.csv', 'r+') as csvfile:
    with open('../finalProducts4.csv', 'w') as csvOutput:
        reader = csv.reader(csvfile, delimiter='\t')
        csvWriter = csv.writer(csvOutput, delimiter='\t')
        all = []
        threestarcounter = 0
        zerostarcounter = 0
        onestarcounter = 0
        twostarcounter = 0

        rowNum = 0
        for row in reader:
            if rowNum == 0:
                rowNum+=1
                continue

            saveRow = []
            try:
                saveRow = row
            except:
                continue

            # print nutritionFactsRow
            name = saveRow[1]
            #print name
            calories = saveRow[8]
           # print calories
            sugar = saveRow[19]
           # print sugar
            sodium = saveRow[15]
           # print sodium
            transfat = saveRow[11]
           # print transfat
            satfat = saveRow[10]
           # print satfat
            fiber = saveRow[18]
          #  print fiber
            vitaminsDV = saveRow[21]
          #  print vitaminsDV
            category = saveRow[25]
         #   print category
            ingredientsList = saveRow[22]


            # formatting parsed numbers correctly
            if sugar != 0 and not (not sugar):
                sugar = float(sugar)
            else:
                sugar = 0
            if transfat != 0 and not (not transfat):
                transfat = float(transfat)
            else:
                transfat = 0
            if satfat != 0 and not (not satfat):
                satfat = float(satfat)
            else:
                satfat = 0
            if fiber != 0 and not (not fiber):
                fiber = float(fiber)
            else:
                fiber = 0
            vitaminsDVF = []
            for dv in vitaminsDV.split():
                if dv[-1] == "%":
                    vitaminsDVF.append((dv[:-1]))

            if calories != 0 and not (not calories):
                calories = float(calories)
            else:
                calories = 0
            if sodium != 0 and not (not sodium):
                sodium = float(sodium)
            else:
                sodium = 0
            if not (not category):
                category = int(category)

            ingredientCount = 0
            for i in ingredientsList.split(","):
                ingredientCount+=1
            print name
            print ingredientCount


            starpoints = 0

            # Trans/Sat Fats ALGO
            if (transfat + satfat) > 1 and (transfat + satfat) <= 2:
                starpoints = starpoints - 1
            if (transfat + satfat) > 2 and (transfat + satfat) <= 3:
                starpoints = starpoints - 2
            if (transfat + satfat) > 3:
                starpoints = starpoints - 3

            # Added Sugar ALGO
            addedsugarpercent = .1
            if (calories != 0):
                addedsugarpercent = sugar / calories * 100
            if addedsugarpercent <= .1 and addedsugarpercent != 0:
                starpoints = starpoints - 1
            if addedsugarpercent <= .25 and addedsugarpercent > .1:
                starpoints = starpoints - 2
            if addedsugarpercent <= .40 and addedsugarpercent > .25:
                starpoints = starpoints - 3
            if addedsugarpercent > .40:
                starpoints = starpoints - 11

            # Sodium ALGO
            if sodium <= 240 and sodium > 120:
                starpoints = starpoints - 1
            if sodium <= 360 and sodium > 240:
                starpoints = starpoints - 2
            if sodium > 360 and sodium <= 600:
                starpoints = starpoints - 3
            if sodium > 600:
                starpoints = starpoints - 11

            # Fiber ALGO
            if fiber >= 3.75:
                starpoints = starpoints + 3
            if fiber >= 2.5 and fiber < 3.75:
                starpoints = starpoints + 2
            if fiber >= 1.25 and fiber < 2.5:
                starpoints = starpoints + 1

                # Whole grain
            if fiber > 1.5:  # whole grains additional boost
                starpoints = starpoints + 1

                # vitamins and minerals
            greaterThan10Count = 0
            greaterThan5Count = 0
            for dv in vitaminsDVF:
                if (dv > 10):
                    greaterThan10Count += 1
                elif (dv > 5):
                    greaterThan5Count += 1
            if (greaterThan10Count >= 2):
                starpoints = starpoints + 3
            elif (greaterThan10Count >= 1 or greaterThan5Count >= 2):
                starpoints = starpoints + 2
            elif (greaterThan5Count >= 1):
                starpoints = starpoints + 1

            guidingStars = 0
            # row.append(starpoints)
       #     print starpoints

            # if it is not a beverage, correct for  "added sugar", "added sodium", "o-3 fatty", "epa/dha"
            print category
            if (category != 7):
                starpoints = starpoints + 1
            if (category == 1):
                starpoints = 10

            # add points for items that have less ingredients (more natural)
            if (ingredientCount < 4 & category!=7):
                starpoints +=2
            if (ingredientCount < 10 & category!=7):
                starpoints +=1
            if (ingredientCount > 20):
                starpoints -=1
            elif (ingredientCount > 40):
                 starpoints -= 2


            # cut off thresholds
            if starpoints < 0:
                guidingStars = 0
                zerostarcounter+=1
            if starpoints == 1 or starpoints == 2:
                guidingStars = 1
                onestarcounter+=1
            if starpoints == 3 or starpoints == 4:
                guidingStars = 2
                twostarcounter+=2
            if starpoints >= 5:
                guidingStars = 3
                threestarcounter+=1


            row.append(starpoints)
            # row.append(guidingStars)
            print guidingStars
            csvWriter.writerow(row)
            rowNum+=1

        print threestarcounter
        print twostarcounter
        print onestarcounter
        print zerostarcounter
