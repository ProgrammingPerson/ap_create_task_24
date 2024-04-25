import turtle as trtl

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
writer = trtl.Turtle()
writer.penup()
writer.hideturtle()
writer.speed(0)
writer.pensize(2)

def search(matrix, size, word, start_y, start_x, output_matrix) -> tuple[bool, list]:

    # Downward Search
    if start_y + len(word) <= size:
        not_found = False
        y = start_y
        curr_letter = 0
        # This for loop is 1 less than the length of the word because the first letter has already been checked
        for _ in range(len(word) - 1):
            y += 1 
            curr_letter += 1
            if matrix[y][start_x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * start_x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * start_x, 265 - 40 * y)
                output_matrix[y][start_x] = matrix[y][start_x]
                y -= 1
            writer.penup()
            return True, output_matrix
            
    # Upward Search
    if start_y + 1 - len(word) >= 0:
        not_found = False
        y = start_y
        curr_letter = 0
        for _ in range(len(word) - 1):
            y -= 1 
            curr_letter += 1
            if matrix[y][start_x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * start_x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * start_x, 265 - 40 * y)
                output_matrix[y][start_x] = matrix[y][start_x]
                y += 1
            writer.penup()
            return True, output_matrix

    # Right Search
    if start_x + len(word) <= size:
        not_found = False
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            x += 1 
            curr_letter += 1
            if matrix[start_y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * start_y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * start_y)
                output_matrix[start_y][x] = matrix[start_y][x]
                x -= 1
            writer.penup()
            return True, output_matrix     

    # Left Search
    if start_x + 1 - len(word) >= 0:
        not_found = False
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            x -= 1 
            curr_letter += 1
            if matrix[start_y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * start_y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * start_y)
                output_matrix[start_y][x] = matrix[start_y][x]
                x += 1
            writer.penup()
            return True, output_matrix         

    # Top Right Search
    if start_y + 1 - len(word) >= 0 and start_x + len(word) <= size:
        not_found = False
        y = start_y
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            y -= 1
            x += 1 
            curr_letter += 1
            if matrix[y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * y)
                output_matrix[y][x] = matrix[y][x]
                y += 1
                x -= 1
            writer.penup()
            return True, output_matrix    

    # Top Left Search
    if start_y + 1 - len(word) >= 0 and start_x + 1 - len(word) >= 0:
        not_found = False
        y = start_y
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            y -= 1
            x -= 1 
            curr_letter += 1
            if matrix[y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * y)
                output_matrix[y][x] = matrix[y][x]
                y += 1
                x += 1
            writer.penup()
            return True, output_matrix       

    # Bottom Right Search
    if start_y + len(word) <= size and start_x + len(word) <= size:
        not_found = False
        y = start_y
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            y += 1
            x += 1 
            curr_letter += 1
            if matrix[y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * y)
                output_matrix[y][x] = matrix[y][x]
                y -= 1
                x -= 1
            writer.penup()
            return True, output_matrix        

    # Bottom Left Search
    if start_y + len(word) <= size and start_x + 1 - len(word) >= 0:
        not_found = False
        y = start_y
        x = start_x
        curr_letter = 0
        for _ in range(len(word) - 1):
            y += 1
            x -= 1 
            curr_letter += 1
            if matrix[y][x] != word[curr_letter]:
                not_found = True
                break
        if not not_found:
            writer.goto(-295 + 40 * x, 265 - 40 * y)
            writer.pendown()
            for i in range(len(word)):
                writer.goto(-295 + 40 * x, 265 - 40 * y)
                output_matrix[y][x] = matrix[y][x]
                y -= 1
                x += 1
            writer.penup()
            return True, output_matrix
    
    return False, output_matrix
    
def main():
    # Currently takes in standard input, image input will be added later
    while True:
        try:
            size = int(wn.textinput("Size", "Please input the size of the word search:"))
            break
        except:
            print("Please input an integer\n")

    word_search_matrix = []

    # For now, the program will take in input to generate the word search array, will be changed later too
    for i in range(size):
        while True:
            line = wn.textinput("Line", "Please input a line of characters: ")
            if (len(line) == size):
                for j in range(size):
                    writer.goto(-300 + 40 * j, 250 - 40 * i)
                    writer.write(line[j], font=("Times New Roman", 20, "normal"))
                break
            else:
                print("Please enter the correct number of characters\n")
        
        word_search_matrix.append(line)

    # This will generate the word bank through user input
    correct = False
    while True:  
        words = wn.textinput("Word Bank", "Please input the words of the word bank separated by spaces: ").split()
        for word in words:
            if len(word) > size:
                print("Error: one of the words are too large\n")
                break
            else:
                correct = True
        if correct:
            break
    
    answer = [["" for i in range(size)] for j in range(size)]

    for word in words:
        found = False
        for i in range(size):
            for j in range(size):
                if not found and word_search_matrix[i][j] == word[0]:
                    found, answer = search(word_search_matrix, size, word, i, j, answer)
                    if found:
                        break
                if found:
                    break
            if found:
                break
        if not found:
            print(f"ERROR: '{word}' NOT FOUND")
            break

    wn.exitonclick()

main()