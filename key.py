class Key:
    def key(self):
        global keyturned  # Global variable
        onoff = input('Is the key turned on or off (yes/no): ').lower()  # Ask input
        if onoff == 'yes':  # Key is turned on
            keyturned = True  # Set keyturned True
            return keyturned  # Return keyturned
        elif onoff == 'no':  # Key is not turned on
            keyturned = False  # Set keyturned False
            return keyturned  # Return keyturned
        else:
            print('Please make a choice between on or off')   # Let user make a valid choice