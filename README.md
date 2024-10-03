# Text Similarity and Plagiarism Detection Project

## Author
**Hritik Ranjan**

## Project Overview
The Text Similarity and Plagiarism Detection project is a Python-based tool that uses text preprocessing techniques and the Levenshtein distance algorithm to detect similarity between two texts. This tool can be used to identify potential plagiarism based on a similarity threshold.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Results](#results)
- [License](#license)
- [Contact](#contact)

## Introduction
This project processes two input texts, removes unnecessary symbols (such as punctuation), and compares their similarity using the Levenshtein distance algorithm. It returns a similarity score and flags potential plagiarism based on a configurable threshold.

## Features
- **Text Preprocessing**: Removes punctuation and converts text to lowercase for standardized comparison.
- **Similarity Calculation**: Compares two texts using the Levenshtein distance algorithm, a common method for measuring the difference between two sequences.
- **Plagiarism Check**: Flags texts as plagiarized if the similarity score exceeds a specified threshold (default: 80%).

## Installation
To run this project, ensure Python is installed on your system. Follow these steps to set up and run the project:

1. **Clone the repository** (if applicable):
   ```bash
   git clone https://github.com/hritikranjan1/text-similarity-plagiarism-detection.git
   cd text-similarity-plagiarism-detection
2.Install dependencies: The project uses the numpy library, which can be installed using:

    pip install numpy

3.Run the script: Use the command below to run the plagiarism detection script:

    python plagiarism_detection.py
    
## Usage

Once the script is running, you will be prompted to input two texts for comparison:

  -  Input Texts: Enter the first and second text strings to be compared.
  -  Plagiarism Check: The script will process the texts and display whether they are plagiarized based on the similarity threshold.

## Example Workflow:
     Enter the first text: This is a test sentence for plagiarism detection.
     Enter the second text: This is a test sentence for plagiarism detection.

    Texts are plagiarized.
## Results

The result of the program is a determination of whether the two input texts are plagiarized. For example:
## Example Output:
     Enter the first text: This is a simple text for comparison.
    Enter the second text: This is a similar text for comparison.
    Texts are not plagiarized.
If the texts are sufficiently similar, the output will be:
  
    Texts are plagiarized.
## License

This project is licensed under the MIT License - see the LICENSE file for details.
## Contact
- Name: Hritik ranjan
- GitHub: https://github.com/hritikranjan1
- LinkedIn: https://www.linkedin.com/in/hritik-ranjan-05a835230/
