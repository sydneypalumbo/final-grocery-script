import csv

with open('../goodImages4.csv', 'r') as inputFile, open('../goodNutrition4.csv', 'a') as outputFile:
    csvReader = csv.reader(inputFile, delimiter='\t')
    csvWriter = csv.writer(outputFile, delimiter='\t')
    for row in csvReader:

        try:
            nutritionString = row[4]
        except IndexError:
            nutritionString = ''

        try:
            row5 = row[5]
        except IndexError:
            row5 = None

        try:
            row6 = row[6]
        except IndexError:
            row6 = None

        servingSize = None
        servingCount = None
        calories = None
        fatCalories = None
        totalFat = None
        satFat = None
        transFat = None
        polyFat = None
        monoFat = None
        cholesterol = None
        sodium = None
        potassium = None
        carbs = None
        fiber = None
        sugar = None
        protein = None
        vitamins = None

        if len(nutritionString) > 0:

            currentIndex = nutritionString.find('Size')
            if currentIndex == -1:
                currentIndex = nutritionString.find('Serving size') + 11
                servingsStart = currentIndex + 2
                currentIndex = nutritionString.find('Amount')
                servingsEnd = currentIndex - 1
                servingSize = nutritionString[(servingsStart - 1):servingsEnd]
            else:
                while nutritionString[currentIndex] != ' ':
                    currentIndex += 1
                servingsStart = currentIndex + 1
                currentIndex = nutritionString.find('Servings')
                if currentIndex == -1:
                    currentIndex = nutritionString.find('Amount')
                servingsEnd = currentIndex - 1
                servingSize = nutritionString[(servingsStart - 1):servingsEnd]

            currentIndex = nutritionString.find('Container') + 8
            if currentIndex == 7:
                currentIndex = nutritionString.find('Nutrition Facts') + 14
                countStart = currentIndex + 2
                countEnd = nutritionString.find('servings per container') - 1
                if countEnd == -2:
                    servingCount = None
                else:
                    servingCount = nutritionString[(countStart - 1):countEnd]
            else:
                countStart = currentIndex + 2
                currentIndex = nutritionString.find('Amount')
                countEnd = currentIndex - 1
                servingCount = nutritionString[(countStart - 1):countEnd]

            currentIndex = nutritionString.find('Calories from Fat') + 16
            if currentIndex != 15:
                currentIndex += 2
                fatCalStart = currentIndex
                while nutritionString[currentIndex] != ' ':
                    currentIndex += 1
                fatCalEnd = currentIndex
                fatCalories = nutritionString[(fatCalStart - 1):fatCalEnd]

            if fatCalories is not None:
                currentIndex += 1
                while nutritionString[currentIndex] != ' ':
                    currentIndex += 1
                currentIndex += 1
                calStart = currentIndex
                while nutritionString[currentIndex] != ' ':
                    currentIndex += 1
                calEnd = currentIndex
                calories = nutritionString[(calStart - 1):calEnd]
            else:
                currentIndex = nutritionString.find('Calories') + 7
                currentIndex += 2
                calStart = currentIndex
                while nutritionString[currentIndex] != ' ':
                    currentIndex += 1
                calEnd = currentIndex
                calories = nutritionString[(calStart - 1):calEnd]

            currentIndex = nutritionString.find('Total Fat') + 8
            if currentIndex != 7:
                currentIndex += 2
                totalFatStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                totalFatEnd = currentIndex
                totalFat = nutritionString[(totalFatStart - 1):totalFatEnd]

            currentIndex = nutritionString.find('Saturated Fat') + 12
            if currentIndex != 11:
                currentIndex += 2
                satFatStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                satFatEnd = currentIndex
                satFat = nutritionString[(satFatStart - 1):satFatEnd]

            currentIndex = nutritionString.find('Trans Fat') + 8
            if currentIndex != 7:
                currentIndex += 2
                transFatStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                transFatEnd = currentIndex
                transFat = nutritionString[(transFatStart - 1):transFatEnd]

            currentIndex = nutritionString.find('Polyunsaturated Fat') + 18
            if currentIndex != 17:
                currentIndex += 2
                polyFatStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                polyFatEnd = currentIndex
                polyFat = nutritionString[(polyFatStart - 1):polyFatEnd]

            currentIndex = nutritionString.find('Monounsaturated Fat') + 18
            if currentIndex != 17:
                currentIndex += 2
                monoFatStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                monoFatEnd = currentIndex
                monoFat = nutritionString[(monoFatStart - 1):monoFatEnd]

            currentIndex = nutritionString.find('Cholesterol') + 10
            if currentIndex != 9:
                currentIndex += 2
                cholesterolStart = currentIndex
                while nutritionString[currentIndex] != 'm':
                    currentIndex += 1
                cholesterolEnd = currentIndex
                cholesterol = nutritionString[(cholesterolStart - 1):cholesterolEnd]
                percentPresent = cholesterol.find('%')
                if percentPresent != -1:
                    cholesterol = None

            currentIndex = nutritionString.find('Sodium') + 5
            if currentIndex != 4:
                currentIndex += 2
                sodiumStart = currentIndex
                while nutritionString[currentIndex] != 'm':
                    currentIndex += 1
                sodiumEnd = currentIndex
                sodium = nutritionString[(sodiumStart - 1):sodiumEnd]

            currentIndex = nutritionString.find('Potassium') + 8
            if currentIndex != 7:
                currentIndex += 2
                potassiumStart = currentIndex
                while nutritionString[currentIndex] != 'm':
                    currentIndex += 1
                potassiumEnd = currentIndex
                potassium = nutritionString[(potassiumStart - 1):potassiumEnd]
                wrongPotassium = potassium.find('3500')
                if wrongPotassium != -1:
                    potassium = None

            currentIndex = nutritionString.find('Carbohydrates') + 12
            if currentIndex != 11:
                currentIndex += 2
                carbsStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                carbsEnd = currentIndex
                carbs = nutritionString[(carbsStart - 1):carbsEnd]

            currentIndex = nutritionString.find('Fiber') + 4
            if currentIndex != 3:
                currentIndex += 2
                fiberStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                fiberEnd = currentIndex
                fiber = nutritionString[(fiberStart - 1):fiberEnd]
                wrongFiber = fiber.find('Su')
                if wrongFiber != -1:
                    fiber = None

            currentIndex = nutritionString.find('Sugars') + 5
            if currentIndex != 4:
                currentIndex += 2
                sugarStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                sugarEnd = currentIndex
                sugar = nutritionString[(sugarStart - 1):sugarEnd]

            currentIndex = nutritionString.find('Protein') + 6
            if currentIndex != 5:
                currentIndex += 2
                proteinStart = currentIndex
                while nutritionString[currentIndex] != 'g':
                    currentIndex += 1
                proteinEnd = currentIndex
                protein = nutritionString[(proteinStart - 1):proteinEnd]

            currentIndex += 3
            vitaminsStart = currentIndex
            while nutritionString[currentIndex] != '*':
                currentIndex += 1
            vitaminsEnd = currentIndex - 1
            vitamins = nutritionString[(vitaminsStart - 1):vitaminsEnd]

        try:
            noImage = row[3].find('NoImage')
        except IndexError:
            noImage = -1
            continue

        if noImage != -1:
            continue

        try:
            newRow = [row[0], row[1], row[2], row[3], servingSize, servingCount, fatCalories, calories,
                      totalFat, satFat, transFat, polyFat, monoFat, cholesterol, sodium, potassium, carbs, fiber, sugar,
                      protein, vitamins, row5, row6]
        except IndexError:
            continue

        csvWriter.writerow(newRow)
