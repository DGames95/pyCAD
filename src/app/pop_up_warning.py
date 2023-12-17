from ..config import CADConfig

class PopUpWarning:
    def __init__(self):
        self.interactive = CADConfig.interactive

    def get_input(self, message):
        if self.interactive:
            while True:
                response = input(f"Error: {message} Do you want to try again? (y/n): ").strip().lower()
                if response == 'y':
                    return True
                elif response == 'n':
                    return False
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")
        else:
            print(f"Error: {message}")
            return False
