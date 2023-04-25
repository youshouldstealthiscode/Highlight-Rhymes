# Import the eng_to_ipa library as ipa for converting English text to IPA format
import eng_to_ipa as ipa
# Import the print function and Console class from the rich library for highlighted text output
from rich import print as rprint
from rich.console import Console

# Define the main function of the program
def main():
    # Get input from the user as a word or sentence
    user_input = input("Please enter a word or a sentence: ")
    # Convert the input text to IPA format using the convert function from the eng_to_ipa library
    ipa_result = ipa.convert(user_input)
    # Split the IPA result into unique distinct IPA letters/groupings using the custom function split_ipa_characters
    ipa_split = split_ipa_characters(ipa_result)
    # Print the complete IPA transcription
    print("IPA transcription: ", ipa_result)
    # Print the split IPA characters/groupings
    print("IPA characters/groupings: ", ipa_split)

    # Highlight the split IPA characters/groupings using the custom function highlight_ipa
    highlighted_ipa = highlight_ipa(ipa_split)
    # Print the highlighted IPA string using the rich library's print function
    rprint(highlighted_ipa)

# Define a function to split IPA transcription into unique distinct IPA letters/groupings
def split_ipa_characters(ipa_result):
    # Initialize an empty list to store the IPA characters/groupings
    ipa_chars = []
    # Initialize a flag for skipping the next character in the loop
    skip_next = False
    # Loop through the IPA result string, getting the index and the character
    for i, char in enumerate(ipa_result):
        # If skip_next flag is set to True, reset it to False and continue to the next iteration
        if skip_next:
            skip_next = False
            continue

        # Check if the current character and the next one form a diphthong (two-element vowel sound)
        if i < len(ipa_result) - 1 and (char + ipa_result[i + 1]) in ipa.diphthongs:
            # If so, append the diphthong to the ipa_chars list
            ipa_chars.append(char + ipa_result[i + 1])
            # Set skip_next flag to True to skip the next character in the loop
            skip_next = True
        # If the character is not a stress mark, append it to the ipa_chars list
        elif char not in ipa.stresses:
            ipa_chars.append(char)

    # Return the list of IPA characters/groupings
    return ipa_chars

# Define a function to highlight the split IPA characters/groupings
def highlight_ipa(ipa_split):
    # Instantiate a Console object from the rich library for handling the highlighted text
    console = Console()
    # Define a list of colors for highlighting the IPA characters/groupings
    colors = [
        "red",
        "green",
        "blue",
        "magenta",
        "cyan",
        "yellow",
        "bright_red",
        "bright_green",
        "bright_blue",
        "bright_magenta",
        "bright_cyan",
        "bright_yellow",
    ]

    # Initialize an empty string to store the highlighted IPA characters/groupings
    highlighted_ipa = ""
    # Loop through the split IPA characters/groupings, getting the index and the character/grouping
    for i, char in enumerate(ipa_split):
        # Choose a background color from the list of colors using the current index modulo the length of the colors list
        bg_color = colors[i % len(colors)]
        # Add the IPA character/grouping to the highlighted string, formatted with black text on the chosen background color
        highlighted_ipa += f"[black on {bg_color}]{char}[/]"

    # Return the highlighted IPA string
    return highlighted_ipa

# Execute the main function when the script is run
if __name__ == "__main__":
    main()


