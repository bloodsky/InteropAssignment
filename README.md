# InteropAssignment

Simple terminal application written in Python, with numbered menu for working with CSV files.<br />


## Usage

After cloning the repository just cd inside project directory and<br /> 

```bash
  python3 main.py
```

## Tests

To run tests suite just cd inside main project directory (not tests directory) and<br /> 

```bash
  python3 -m unittest discover
```

## Handling of missing values

The management of missing values takes place following the constraints indicated by the specification.<br /> 
An ID field must always be present, unique and not negative. On the contrary, since no constraint regarding<br /> 
the yearly-amount field is indicated in the specification, and having empty entries related to this, a yearly<br /> 
amount field is implemented as an ```Optional``` which when not present is assumed as zero. the same goes <br />
for monthly variation and currency (empty mean EUR).

## Input tests folder

The test files to perform the assignments are located in the folder: ```input-test-files``` <br />
The two files referred to as ```input_file_test1.csv``` ```input_file_test2.csv``` <br /> are example files<br />
with errors, as reported by the specification.<br /> 
```clean_input_test.csv``` is a clean file, meaning that is an error-free csv file.<br />
