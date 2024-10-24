# filename: select_from_list_demo.py
import inquirer

questions = [
  inquirer.List('size',
                message="What size do you need?",
                choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
            )
]
answers = inquirer.prompt(questions)
print(answers["size"])
